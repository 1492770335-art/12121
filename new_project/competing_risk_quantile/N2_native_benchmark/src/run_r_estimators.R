#!/usr/bin/env Rscript
# Native cmprskQR and randomForestSRC on the same censoring data and Oracle truth.
# No Cox fit and no imputed replacement after a model failure.
suppressPackageStartupMessages(library(survival))
args <- commandArgs(trailingOnly=TRUE)
if (length(args)!=2L) stop('Usage: Rscript run_r_estimators.R data_dir result_dir')
datadir <- args[1]; resultdir <- args[2]
dir.create(resultdir,recursive=TRUE,showWarnings=FALSE)
mechs <- c('aligned','cause_tradeoff','time_varying')
probs <- c(.06,.12,.18,.24)
get_quantile <- function(times,values,p,L=3){
  good <- which(is.finite(times)&is.finite(values)&times<=L+1e-12&values>=p)
  if(!length(good)) return(NA_real_)
  k<-good[1]
  if(k==1) return(as.numeric(times[k]))
  if(values[k]<=values[k-1]) return(as.numeric(times[k]))
  as.numeric(times[k-1]+(p-values[k-1])/(values[k]-values[k-1])*(times[k]-times[k-1]))
}
results<-list(); failures<-list(); cursor<-0; icur<-0
record_fail<-function(method,mechanism,censor,msg){
  icur<<-icur+1
  failures[[icur]]<<-data.frame(method=method,mechanism=mechanism,censor_target=censor,error=msg)
  cat('FAIL',method,mechanism,censor,substr(msg,1,200),'\n')
}
score<-function(method,mech,censor,truth,time,cf,version){
  if(!is.matrix(cf)||nrow(cf)!=nrow(truth)||ncol(cf)!=length(time)) stop('invalid cause1 CIF dimensions')
  valid_row<-apply(cf,1,function(x)all(is.finite(x)&x>=-1e-6&x<=1+1e-6))
  n_invalid<-sum(!valid_row)
  cat('CIF_AUDIT',method,mech,censor,'invalid_rows',n_invalid,
      'nonfinite_cells',sum(!is.finite(cf)),
      'negative_cells',sum(cf< -1e-6,na.rm=TRUE),
      'above_one_cells',sum(cf>1+1e-6,na.rm=TRUE),
      'min',suppressWarnings(min(cf,na.rm=TRUE)),
      'max',suppressWarnings(max(cf,na.rm=TRUE)),'\n')
  n<-nrow(truth)
  out<-lapply(probs,function(p){
    truth_col<-sprintf('true_q1_p%.2f',p)
    q0<-truth[[truth_col]]
    qhat<-vapply(seq_len(n),function(i)if(valid_row[i])get_quantile(time,cf[i,],p) else NA_real_,numeric(1))
    tgood<-is.finite(q0);pgood<-is.finite(qhat);both<-tgood&pgood
    data.frame(method=method,mechanism=mech,censor_target=censor,p=p,n_eval=n,
     n_true_reachable=sum(tgood),n_pred_reachable=sum(pgood),n_both=sum(both),
     mae=if(any(both))mean(abs(q0[both]-qhat[both]))else NA_real_,
     fp_unreachable=sum(!tgood&pgood),fn_missing=sum(tgood&!pgood),
     predicted_reach_pct=100*mean(pgood),scorable_pct=100*mean(both),
     cdf_nonmonotone_pct=100*mean(apply(cf,1,function(x)if(all(is.finite(x)))any(diff(x)< -1e-5)else NA),na.rm=TRUE),n_invalid_curve=n_invalid,notes=version)
  })
  do.call(rbind,out)
}
score_direct <- function(method,mech,censor,truth,tau,qmat,version){
  if(!is.matrix(qmat)||nrow(qmat)!=nrow(truth)||ncol(qmat)!=length(tau))stop('invalid direct Q dimensions')
  if(any(!is.finite(tau))||any(diff(tau)<=0)||min(tau)<=0||max(tau)>=1)stop('invalid tau grid')
  rows<-lapply(probs,function(p){
    true<-truth[[sprintf('true_q1_p%.2f',p)]]
    # The native crrQR prediction is a row of time quantiles per test record, not a CIF.
    pred<-vapply(seq_len(nrow(qmat)),function(i){
      v<-qmat[i,]
      if(any(!is.finite(v))) return(NA_real_)
      as.numeric(approx(x=tau,y=v,xout=p,rule=1,ties='ordered')$y)
    },numeric(1))
    invalid<-!is.finite(pred)|pred<=0
    reached<-!invalid & pred < 3-1e-12
    actual<-is.finite(true)
    both<-actual&reached
    data.frame(method=method,mechanism=mech,censor_target=censor,p=p,n_eval=nrow(qmat),
      n_true_reachable=sum(actual),n_pred_reachable=sum(reached),n_both=sum(both),
      mae=if(any(both))mean(abs(true[both]-pred[both]))else NA_real_,
      fp_unreachable=sum(!actual&reached),fn_missing=sum(actual&!reached),
      predicted_reach_pct=100*mean(reached),scorable_pct=100*mean(both),
      cdf_nonmonotone_pct=NA_real_,n_invalid_curve=sum(invalid),
      notes=paste0('native direct quantile time; version=',version))
  })
  cat('PENGFINE_Q_AUDIT',mech,censor,'tau_length',length(tau),
      'Q_min',suppressWarnings(min(qmat,na.rm=TRUE)),
      'Q_max',suppressWarnings(max(qmat,na.rm=TRUE)),
      'nonfinite',sum(!is.finite(qmat)),'\n')
  do.call(rbind,rows)
}
for(mech in mechs){
  truth<-read.csv(file.path(datadir,paste0(mech,'_oracle_test.csv')),check.names=FALSE)
  newdata<-truth[,c('a','z1','z2','az1')]
  for(censor in c(20,45)){
    train<-read.csv(file.path(datadir,sprintf('%s_c%d_train.csv',mech,censor)),check.names=FALSE)
    x<-as.matrix(train[,c('a','z1','z2','az1')])
    newx<-as.matrix(newdata)
    if(requireNamespace('cmprskQR',quietly=TRUE)){
      tryCatch({
        fit<-cmprskQR::crrQR(ftime=train$ftime,fstatus=train$fstatus,X=x,failcode=1,cencode=0,
                          tau.range=c(.02,.26),tau.step=.02,variance=FALSE)
        predicted<-predict(fit,newx,rearrangement=TRUE)
        predicted<-as.matrix(predicted)
        if(ncol(predicted)!=nrow(truth)+1L)stop(sprintf('unexpected crrQR prediction matrix %s',paste(dim(predicted),collapse='x')))
        # Official source cbind(exp(x beta(tau)), tau.seq): last column is tau.
        tau<-as.numeric(predicted[,ncol(predicted)])
        qmat<-t(predicted[,-ncol(predicted),drop=FALSE])
        if(any(diff(tau)<=0))stop('non-increasing quantile probability grid')
        cursor<-cursor+1;results[[cursor]]<-score_direct('PengFine-cmprskQR-native',mech,censor,truth,tau,qmat,as.character(packageVersion('cmprskQR')))
        cat('PASS PengFine',mech,censor,'\n')
      },error=function(e)record_fail('PengFine-cmprskQR-native',mech,censor,conditionMessage(e)))
    }else record_fail('PengFine-cmprskQR-native',mech,censor,'R package cmprskQR not installed')
    if(requireNamespace('randomForestSRC',quietly=TRUE)){
      tryCatch({
        f<-randomForestSRC::rfsrc(Surv(ftime,fstatus)~a+z1+z2+az1,data=train,
                                  ntree=100,nsplit=5,nodesize=15,seed=-20261123)
        pred<-predict(f,newdata=newdata)
        cif<-pred$cif
        if(length(dim(cif))!=3L) stop(sprintf('unexpected forest cif dims %s',paste(dim(cif),collapse='x')))
        if(dim(cif)[1]!=nrow(truth)||dim(cif)[3]<2)stop('forest output missing cause dimensions')
        tm<-as.numeric(pred$time.interest)
        cf<-as.matrix(cif[,,1])
        if(any(diff(tm)<0))stop('unsorted forest times')
        cursor<-cursor+1;results[[cursor]]<-score('CRRSF-randomForestSRC-native',mech,censor,truth,tm,cf,as.character(packageVersion('randomForestSRC')))
        cat('PASS CR-RSF',mech,censor,'\n')
      },error=function(e)record_fail('CRRSF-randomForestSRC-native',mech,censor,conditionMessage(e)))
    }else record_fail('CRRSF-randomForestSRC-native',mech,censor,'R package randomForestSRC not installed')
  }
}
if(length(results))write.csv(do.call(rbind,results),file.path(resultdir,'r_native_metrics.csv'),row.names=FALSE)
if(length(failures))write.csv(do.call(rbind,failures),file.path(resultdir,'r_native_failures.csv'),row.names=FALSE)
writeLines(capture.output(sessionInfo()),file.path(resultdir,'r_session_info.txt'))
if(!length(results))stop('Neither R native estimator was successfully run')
