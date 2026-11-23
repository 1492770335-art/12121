#!/usr/bin/env Rscript
# Published cmprskQR and randomForestSRC, matching Q1 and Qall on identical Oracle patients.
# Uses corrected native Peng-Fine log(ftime) and prediction-matrix column semantics.
suppressPackageStartupMessages(library(survival))
options(digits=15)
argv<-commandArgs(trailingOnly=TRUE)
if(length(argv)!=2L)stop('Usage: Rscript run_r_estimators.R data_path output_path')
datadir<-argv[1];outdir<-argv[2];dir.create(outdir,recursive=TRUE,showWarnings=FALSE)
MECHS<-c('aligned','cause_tradeoff','time_varying')
P1<-c(.06,.12,.18,.24)
PALL<-c(.15,.25,.35,.45)
L<-3

new_row<-function(method,mech,rep,censor,truth,endpoint,p,pred){
  real<-truth[[sprintf('true_%s_p%.2f',endpoint,p)]]
  data.frame(method=method,mechanism=mech,replicate=rep,censor_target=censor,
    endpoint=endpoint,p=p,patient_id=truth$patient_id,a=truth$a,
    true_q=real,pred_q=pred,true_reachable=as.integer(is.finite(real)),
    pred_reachable=as.integer(is.finite(pred)))
}

inverse_cif<-function(times,values,p){
  if(any(!is.finite(values))||any(values< -1e-6)||any(values>1+1e-6))return(NA_real_)
  hit<-which(values >= p)
  if(!length(hit))return(NA_real_)
  k<-hit[1]
  if(k==1L)return(as.numeric(times[1]))
  if(values[k]<=values[k-1])return(as.numeric(times[k]))
  as.numeric(times[k-1]+(p-values[k-1])*(times[k]-times[k-1])/(values[k]-values[k-1]))
}

forest_inverse<-function(time,curves,p){
  valid<-is.finite(time) & time>0 & time<=L+1e-10
  times<-time[valid]
  mat<-curves[,valid,drop=FALSE]
  if(!length(times))return(rep(NA_real_,nrow(curves)))
  # CIF of forest is stepwise; use value at last event time <=L for L.
  if(tail(times,1)<L){times<-c(times,L);mat<-cbind(mat,mat[,ncol(mat)])}
  times<-c(0,times)
  mat<-cbind(rep(0,nrow(mat)),mat)
  vapply(seq_len(nrow(mat)),function(i)inverse_cif(times,mat[i,],p),numeric(1))
}

predict_direct<-function(tr,truth,failcode,endpoint,probs,taurange){
  x<-as.matrix(tr[,c('a','z1','z2','az1')]);newx<-as.matrix(truth[,c('a','z1','z2','az1')])
  if(any(tr$ftime<=0))stop('native Peng-Fine requires positive time')
  status<-if(endpoint=='qall')as.integer(tr$fstatus>0) else tr$fstatus
  fit<-cmprskQR::crrQR(ftime=log(tr$ftime),fstatus=status,X=x,
      failcode=1,cencode=0,tau.range=taurange,tau.step=.01,variance=FALSE)
  pred<-as.matrix(predict(fit,newx,rearrangement=TRUE))
  if(ncol(pred)!=nrow(truth)+1L)stop(paste('unrecognized native quantile prediction matrix',paste(dim(pred),collapse='x')))
  tau<-as.numeric(pred[,ncol(pred)])
  qq<-t(pred[,-ncol(pred),drop=FALSE])
  if(any(diff(tau)<=0)||nrow(qq)!=nrow(truth))stop('invalid tau or matrix dimensions')
  qhat<-matrix(NA_real_,nrow=nrow(qq),ncol=length(probs))
  for(k in seq_along(probs)){
    for(i in seq_len(nrow(qq))){
      v<-qq[i,]
      if(all(is.finite(v))){
        q<-as.numeric(approx(x=tau,y=v,xout=probs[k],rule=1,ties='ordered')$y)
        if(is.finite(q)&&q>0&&q<L-1e-12)qhat[i,k]<-q
      }
    }
  }
  list(q=qhat,nonmonotone=as.integer(sum(apply(qq,1,function(r)any(diff(r) < -1e-9)))))
}

predictions<-list();fits<-list();nrows<-0;nf<-0
addstatus<-function(method,mech,rep,censor,endpoint,status,error='',nmono=NA_integer_){
  nf<<-nf+1
  fits[[nf]]<<-data.frame(method=method,mechanism=mech,replicate=rep,
      censor_target=censor,endpoint=endpoint,status=status,error=substr(error,1,800),
      nonmonotone=nmono,stringsAsFactors=FALSE)
  cat('FIT',method,mech,rep,censor,endpoint,status,substr(error,1,140),'\n'); flush.console()
}
for(mech in MECHS){
  for(rep in 0:3){
    truth<-read.csv(file.path(datadir,sprintf('%s_r%02d_oracle_test.csv',mech,rep)),check.names=FALSE)
    newdata<-truth[,c('a','z1','z2','az1')]
    for(censor in c(20,45)){
      train<-read.csv(file.path(datadir,sprintf('%s_r%02d_c%d_train.csv',mech,rep,censor)),check.names=FALSE)
      if(requireNamespace('cmprskQR',quietly=TRUE)){
        for(endpoint in c('q1','qall')){
          probs<-if(endpoint=='q1')P1 else PALL
          rng<-if(endpoint=='q1')c(.02,.30) else c(.10,.49)
          tryCatch({
            pr<-predict_direct(train,truth,1,endpoint,probs,rng)
            for(k in seq_along(probs)){
              nrows<-nrows+1
              predictions[[nrows]]<-new_row('PengFine',mech,rep,censor,truth,endpoint,probs[k],pr$q[,k])
            }
            addstatus('PengFine',mech,rep,censor,endpoint,'ok',nmono=pr$nonmonotone)
          },error=function(e)addstatus('PengFine',mech,rep,censor,endpoint,'failed',conditionMessage(e)))
        }
      }else for(endpoint in c('q1','qall'))addstatus('PengFine',mech,rep,censor,endpoint,'failed','cmprskQR missing')
      if(requireNamespace('randomForestSRC',quietly=TRUE)){
        tryCatch({
          f<-randomForestSRC::rfsrc(Surv(ftime,fstatus)~a+z1+z2+az1,
                          data=train,ntree=160,nodesize=15,nsplit=5,
                          seed=as.integer(-(2026112304+rep+100*which(MECHS==mech)+censor)))
          pred<-predict(f,newdata=newdata)
          cif<-pred$cif;times<-as.numeric(pred$time.interest)
          if(length(dim(cif))!=3L||dim(cif)[1]!=nrow(truth)||dim(cif)[3]<2L)stop('invalid forest cause CIF layout')
          cc1<-as.matrix(cif[,,1]);cc2<-as.matrix(cif[,,2]);ccall<-cc1+cc2
          if(max(ccall,na.rm=TRUE)>1.002||min(ccall,na.rm=TRUE) < -0.002)stop('invalid joint CIF probabilities')
          for(endpoint in c('q1','qall')){
            probs<-if(endpoint=='q1')P1 else PALL
            curves<-if(endpoint=='q1')cc1 else ccall
            for(p in probs){
              qhat<-forest_inverse(times,curves,p)
              nrows<-nrows+1
              predictions[[nrows]]<-new_row('CRRSF',mech,rep,censor,truth,endpoint,p,qhat)
            }
            nmono<-sum(apply(curves,1,function(z)any(diff(z) < -1e-5)))
            addstatus('CRRSF',mech,rep,censor,endpoint,'ok',nmono=nmono)
          }
        },error=function(e){
          for(endpoint in c('q1','qall'))addstatus('CRRSF',mech,rep,censor,endpoint,'failed',conditionMessage(e))
        })
      }else for(endpoint in c('q1','qall'))addstatus('CRRSF',mech,rep,censor,endpoint,'failed','randomForestSRC missing')
    }
  }
}
if(length(predictions))write.csv(do.call(rbind,predictions),file.path(outdir,'native_r_predictions.csv'),row.names=FALSE,na='')
write.csv(do.call(rbind,fits),file.path(outdir,'native_r_fit_status.csv'),row.names=FALSE)
writeLines(capture.output(sessionInfo()),file.path(outdir,'native_r_session.txt'))
if(!length(predictions))stop('R fit failure: no successful PengFine/CRRSF model')