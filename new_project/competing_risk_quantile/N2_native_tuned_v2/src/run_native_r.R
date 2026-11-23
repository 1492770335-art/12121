#!/usr/bin/env Rscript
# Native Peng-Fine crrQR and randomForestSRC; train-only IPCW quantile check loss selection.
suppressPackageStartupMessages(library(survival))
options(digits=15)
argv <- commandArgs(trailingOnly=TRUE)
if(length(argv)!=5L) stop('Rscript run_native_r.R data_dir output_dir mechanism ntrain validation_script')
datadir<-argv[1];outdir<-argv[2];MECH<-argv[3];NTRAIN<-as.integer(argv[4]);scorer<-argv[5]
dir.create(outdir,recursive=TRUE,showWarnings=FALSE)
MECHS<-c('aligned','cause_tradeoff','time_varying','logquantile_correct','nonlinear_interaction')
P1<-c(.06,.12,.18,.24);PALL<-c(.15,.25,.35,.45);L<-3
if(!(MECH %in% MECHS)||!(NTRAIN %in% c(500,1000)))stop('bad shard selectors')

make_x<-function(frame,basis){
  x<-as.matrix(frame[,c('a','z1','z2','az1')]);storage.mode(x)<-'double'
  if(basis=='quad')x<-cbind(x,z1_sq=frame$z1^2,az1_sq=frame$a*frame$z1^2)
  x
}

predict_peng<-function(tr,other,endpoint,basis){
  status<-if(endpoint=='qall')as.integer(tr$fstatus>0) else as.integer(tr$fstatus)
  rng<-if(endpoint=='q1')c(.02,.30) else c(.10,.49)
  probs<-if(endpoint=='q1')P1 else PALL
  fit<-cmprskQR::crrQR(ftime=log(tr$ftime),fstatus=status,
                       X=make_x(tr,basis),failcode=1,cencode=0,
                       tau.range=rng,tau.step=.01,variance=FALSE)
  pred<-as.matrix(predict(fit,make_x(other,basis),rearrangement=TRUE))
  if(ncol(pred)!=nrow(other)+1L)stop('unexpected PengFine predict dimensions')
  tau<-as.numeric(pred[,ncol(pred)])
  qq<-t(pred[,-ncol(pred),drop=FALSE])
  if(any(diff(tau)<=0)||length(tau)!=ncol(qq))stop('invalid tau or prediction layout')
  out<-matrix(NA_real_,nrow(other),length(probs))
  for(i in seq_len(nrow(other))){
    v<-qq[i,];if(!all(is.finite(v)))next
    predq<-approx(x=tau,y=v,xout=probs,rule=1,ties='ordered')$y
    out[i,]<-ifelse(is.finite(predq)&predq>0&predq<L-1e-12,predq,NA_real_)
  }
  out
}

inverse_cif<-function(times,values,p){
  if(any(!is.finite(values)) || any(values< -1e-6) || any(values>1+1e-6))return(NA_real_)
  hit<-which(values>=p)
  if(!length(hit))return(NA_real_)
  k<-hit[1]
  if(k==1L) q<-times[k]
  else q<-if(values[k]<=values[k-1])times[k] else
    times[k-1]+(p-values[k-1])*(times[k]-times[k-1])/(values[k]-values[k-1])
  if(!is.finite(q) || q < 0 || q>=L-1e-12)return(NA_real_)
  as.numeric(q)
}

q_from_forest<-function(model,other){
  pred<-predict(model,newdata=other)
  ff<-pred$cif; times<-as.numeric(pred$time.interest)
  if(length(dim(ff))!=3L||dim(ff)[1]!=nrow(other)||dim(ff)[3]<2L)stop('invalid forest CIF shape')
  if(any(diff(times)<0))stop('forest time not sorted')
  valid<-is.finite(times) & times > 0 & times <= L+1e-10
  t<-times[valid]
  if(!length(t))stop('no forest event times within L')
  c1<-as.matrix(ff[,valid,1]);c2<-as.matrix(ff[,valid,2]);call<-c1+c2
  if(any(call>1.002,na.rm=TRUE)||any(call< -0.002,na.rm=TRUE))stop('invalid CIF sum')
  if(tail(t,1)<L){t<-c(t,L);c1<-cbind(c1,c1[,ncol(c1)]);call<-cbind(call,call[,ncol(call)])}
  t<-c(0,t);c1<-cbind(rep(0,nrow(other)),c1);call<-cbind(rep(0,nrow(other)),call)
  out<-list()
  for(e in c('q1','qall')){
    probs<-if(e=='q1')P1 else PALL
    curve<-if(e=='q1')c1 else call
    q<-matrix(NA_real_,nrow(other),length(probs))
    for(k in seq_along(probs))q[,k]<-vapply(seq_len(nrow(other)),function(i)inverse_cif(t,curve[i,],probs[k]),numeric(1))
    out[[e]]<-q
  }
  out
}

as_validation_predictions<-function(other,quantiles){
  res<-list();idx<-0L
  for(e in c('q1','qall')){
    ps<-if(e=='q1')P1 else PALL
    for(k in seq_along(ps)){
      idx<-idx+1L
      res[[idx]]<-data.frame(patient_id=other$patient_id,endpoint=e,p=ps[k],pred_q=quantiles[[e]][,k])
    }
  }
  do.call(rbind,res)
}

score_via_python<-function(trainpath,other,quantiles){
  prediction_file<-tempfile(fileext='.csv');out<-tempfile(fileext='.json')
  on.exit(unlink(c(prediction_file,out)))
  write.csv(as_validation_predictions(other,quantiles),prediction_file,row.names=FALSE,na='')
  cmd<-c(scorer,'--train',trainpath,'--pred',prediction_file,'--out',out)
  log<-suppressWarnings(system2('python',shQuote(cmd),stdout=TRUE,stderr=TRUE))
  if(!file.exists(out))stop(paste('validation scorer did not create output',paste(log,collapse=' | ')))
  lines<-readLines(out,warn=FALSE)
  matched<-grep('"validation_loss"',lines,value=TRUE)
  if(length(matched)!=1L)stop('missing validation_loss')
  val<-as.numeric(sub('.*"validation_loss"[[:space:]]*:[[:space:]]*([-0-9eE+.]+).*','\\1',matched))
  if(!is.finite(val))stop('invalid train-only validation loss')
  val
}

add_rows<-function(method,mech,n,rep,censor,truth,quants){
  ans<-list();j<-0L
  for(e in c('q1','qall')){
    ps<-if(e=='q1')P1 else PALL
    for(k in seq_along(ps)){
      j<-j+1L
      ans[[j]]<-data.frame(method=method,mechanism=mech,n_train=n,replicate=rep,
        censor_target=censor,endpoint=e,p=ps[k],patient_id=truth$patient_id,a=truth$a,
        true_q=truth[[sprintf('true_%s_p%.2f',e,ps[k])]],pred_q=quants[[e]][,k])
    }
  }
  do.call(rbind,ans)
}

outputs<-list();fits<-list();k<-0L;h<-0L
for(rep in 0:7){
 truth<-read.csv(file.path(datadir,sprintf('%s_n%d_r%02d_oracle_test.csv',MECH,NTRAIN,rep)))
 for(censor in c(20,45)){
  trainpath<-file.path(datadir,sprintf('%s_n%d_r%02d_c%d_train.csv',MECH,NTRAIN,rep,censor))
  train<-read.csv(trainpath)
  fit<-train[train$is_validation==0,];valid<-train[train$is_validation==1,]
  for(method in c('PengFine','CRRSF')){
   started<-proc.time()[3];best<-NA_character_;best_loss<-Inf;trials<-list()
   tryCatch({
    cand<-if(method=='PengFine')c('linear','quad') else c('5','20')
    for(j in seq_along(cand)){
      key<-cand[j]
      val_loss<-Inf;error<-''
      tryCatch({
        if(method=='PengFine'){
          q<-list(q1=predict_peng(fit,valid,'q1',key),qall=predict_peng(fit,valid,'qall',key))
        } else {
          forest<-randomForestSRC::rfsrc(Surv(ftime,fstatus)~a+z1+z2+az1,
             data=fit,ntree=160,nsplit=5,nodesize=as.integer(key),
             seed=as.integer(-(2026112351+NTRAIN+rep*100+censor)))
          q<-q_from_forest(forest,valid)
        }
        val_loss<-score_via_python(trainpath,valid,q)
      },error=function(err){error<<-conditionMessage(err)})
      trials[[length(trials)+1L]]<-data.frame(candidate=key,loss=val_loss,error=substr(error,1,400))
      if(is.finite(val_loss) && val_loss<best_loss){best<-key;best_loss<-val_loss}
    }
    if(!is.finite(best_loss))stop('all candidates failed validation')
    if(method=='PengFine'){
      q<-list(q1=predict_peng(train,truth,'q1',best),qall=predict_peng(train,truth,'qall',best))
    }else{
      forest<-randomForestSRC::rfsrc(Surv(ftime,fstatus)~a+z1+z2+az1,
         data=train,ntree=160,nsplit=5,nodesize=as.integer(best),
         seed=as.integer(-(2026112351+NTRAIN+rep*100+censor+10000)))
      q<-q_from_forest(forest,truth)
    }
    k<-k+1L;outputs[[k]]<-add_rows(method,MECH,NTRAIN,rep,censor,truth,q)
    status<-'ok';msg<-''
   },error=function(e){status<<-'failed';msg<<-conditionMessage(e)})
   h<-h+1L
   fits[[h]]<-data.frame(method=method,mechanism=MECH,n_train=NTRAIN,
      replicate=rep,censor_target=censor,status=status,
      selected_candidate=ifelse(is.na(best),'',best),selected_validation_loss=ifelse(is.finite(best_loss),best_loss,NA_real_),
      candidate_details=paste(vapply(trials,function(x)paste0(x$candidate,':',format(x$loss,digits=5),':',x$error),character(1)),collapse=';'),
      elapsed_seconds=as.numeric(proc.time()[3]-started),error=substr(msg,1,500))
   cat('FIT',method,MECH,NTRAIN,rep,censor,status,best,round(best_loss,5),substr(msg,1,140),'\n');flush.console()
  }
 }
}
if(length(outputs))write.csv(do.call(rbind,outputs),file.path(outdir,'native_r_predictions.csv'),row.names=FALSE,na='')
write.csv(do.call(rbind,fits),file.path(outdir,'native_r_fit_status.csv'),row.names=FALSE)
writeLines(capture.output(sessionInfo()),file.path(outdir,'native_r_session.txt'))
if(sum(vapply(fits,function(f)f$status=='ok',logical(1)))!=16)stop('Incomplete R native model fits')
