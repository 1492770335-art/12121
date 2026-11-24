#!/usr/bin/env Rscript
# Native author/package estimators ONLY; do not substitute any Cox baselines.
suppressPackageStartupMessages(library(survival))
argv <- commandArgs(trailingOnly=TRUE)
method <- if(length(argv)>=1) argv[1] else Sys.getenv("PILOT_METHOD","DTR")
reps <- if(length(argv)>=2) as.integer(argv[2]) else 1L
root <- getwd()
out <- file.path(root,"pilot/v8_native_five/results")
dir.create(out,showWarnings=FALSE,recursive=TRUE)
datadir <- file.path(root,"pilot/v8_native_five/data")
set.seed(20261124)
cat("METHOD:",method," REPS:",reps,"\n",flush=TRUE)

extract_tx <- function(pred,levels,n) {
    if(is.list(pred) && !is.null(pred$optimal)) pred <- pred$optimal
    if(isS4(pred)) val <- slot(pred,"optimalTx") else val <- pred
    val <- as.numeric(val)
    if(length(val)!=n || anyNA(val)) stop("bad predicted treatment length or NA")
    if(all(val %in% seq_along(levels))) return(as.integer(as.numeric(levels[val])))
    if(all(val %in% c(0,1))) return(as.integer(val))
    stop(paste("unknown policy labels:",paste(unique(val),collapse=","), "levels:",paste(levels,collapse=",")))
}
run_method <- function(method,train,test,seed) {
    set.seed(seed)
    if(method=="PMCR") {
        source(file.path(root,"pilot/v8_native_five/PMCRfun.R"),local=FALSE)
        # Original author function and its original policy family. Disable rgenoud
        # for smoke; final run must record this explicit optimizer choice.
        fit <- PMCR(Time="obs_time",Event="status",formula=Trt~Z1+Z2,
                   data=train,rgenoud=FALSE,Restrict=TRUE,
                   propscore="true",t0=3,alp=.35,M=1000)
        if(is.null(fit$beta3) || anyNA(fit$beta3)) stop("PMCR returned invalid beta3")
        if(is.null(fit$Fbeta3)||length(fit$Fbeta3)<2) stop("PMCR missing native CIF diagnostics")
        x <- model.matrix(~Z1+Z2,data=test)
        b <- as.numeric(x %*% fit$beta3)
        return(list(d=as.integer(b>0),detail=sprintf("PMCR F1=%.6f F2=%.6f beta=(%s)",fit$Fbeta3[1],fit$Fbeta3[2],paste(round(fit$beta3,4),collapse=";"))))
    }
    if(method=="DTR") {
        suppressPackageStartupMessages(library(dtrSurv))
        # Original Cho dynamic survival forest, first-event status = D.0.
        fit <- dtrSurv::dtrSurv(data=train,txName="Trt",
           models=list(Surv(obs_time,D.0)~Z1+Z2),
           usePrevTime=TRUE,tau=3,timePoints="uni",nTimes=100,
           criticalValue="mean",splitRule="mean",ERT=TRUE,uniformSplit=TRUE,
           replace=FALSE,randomSplit=.2,nTree=300,mTry=1,
           pooled=FALSE,stratifiedSplit=.1,nodeSize=5,minEvent=2)
        pred <- predict(fit,newdata=test,stage=1,findOptimal=TRUE)
        levels <- fit@stageResults[[1]]@txLevels
        d <- extract_tx(pred,levels,nrow(test))
        return(list(d=d,detail="dtrSurv 1-stage native forest RMET"))
    }
    if(method=="RSF") {
        suppressPackageStartupMessages(library(randomForestSRC))
        dcf <- matrix(NA_real_,nrow(test),2)
        for(a in 0:1) {
           sub <- train[train$Trt==a,,drop=FALSE]
           sub$status <- as.integer(sub$status)
           fit <- randomForestSRC::rfsrc(Surv(obs_time,status)~Z1+Z2,
               data=sub,ntree=500,nodesize=15,mtry=2,nsplit=10,
               splitrule="logrankCR",cause=1,importance=FALSE,block.size=1)
           pred <- predict(fit,newdata=test[,c("Z1","Z2")])
           if(length(dim(pred$cif))!=3) stop(paste("RSF CIF wrong dims",paste(dim(pred$cif),collapse="x")))
           k <- max(which(pred$time.interest<=3))
           if(!is.finite(k)) stop("RSF time grid no t<=3")
           dcf[,a+1] <- pred$cif[,k,1]
        }
        if(any(!is.finite(dcf))) stop("RSF nonfinite CIF predictions")
        return(list(d=as.integer(dcf[,2]<dcf[,1]-1e-12),detail="randomForestSRC competing-risk CIF at 3y"))
    }
    if(method=="ITR") {
       suppressPackageStartupMessages(library(dplyr))
       suppressPackageStartupMessages(library(itrSurv))
       times <- sort(unique(train$obs_time[train$D.0==1]))
       fit <- itrSurv::itrSurv(
          data=train[order(train$obs_time),],endPoint="CR",
          yName="obs_time",txName="Trt",epName="status",
          models=list(Surv(obs_time,D.0)~Z1+Z2,Surv(obs_time,D.1)~Z1+Z2),
          timePointsSurvival=times,timePointsEndpoint=times,tau=3,
          criticalValue1="mean",criticalValue2="mean",tol1=c(.07,0),
          splitRule1="mean_surv",splitRule2="gray_cr",
          ERT=TRUE,uniformSplit=TRUE,replace=FALSE,randomSplit=.2,
          nTree=300,mTry=1,pooled=FALSE,stratifiedSplit=.1,
          nodeSizeSurv=5,nodeSizeEnd=5,minEventSurv=2,minEventEnd=2)
       p1<-predict(fit,newdata=test,Phase=1,endPoint="CR",epName1="status",findOptimal=TRUE)
       p2<-predict(fit,newdata=test,Phase=2,endPoint="CR",epName1="status",findOptimal=TRUE)
       if(is.null(p1$optimal) || is.null(p2$optimal)) stop("itrSurv native prediction missing optimal")
       stopind <- p1$optimal@Ratio_Stopping_Ind
       lev <- fit@phaseResults[[1]]@txLevels
       a1 <- extract_tx(p1,lev,nrow(test))
       a2 <- extract_tx(p2,lev,nrow(test))
       if(length(stopind)!=nrow(test) || anyNA(stopind)) stop("itrSurv invalid stopping indicators")
       d <- ifelse(stopind==1,a1,a2)
       return(list(d=as.integer(d),detail=sprintf("itrSurv ratio stop phase1=%g",mean(stopind==1))))
    }
    stop("Unknown method")
}
status <- data.frame(mechanism=character(),rep=integer(),method=character(),status=character(),detail=character(),elapsed_s=double(),stringsAsFactors=FALSE)
for(r in seq_len(reps)) for(m in c("M1","M2")) {
    stem <- paste0(m,"_r",r)
    train <- read.csv(file.path(datadir,paste0("train_",stem,".csv")),check.names=FALSE)
    test <- read.csv(file.path(datadir,paste0("test_",stem,".csv")),check.names=FALSE)
    names(train) <- make.names(names(train))
    # R make.names maps D.0 to D.0 unchanged.
    set.seed(100000+100*r+ifelse(m=="M1",1,2))
    tick <- proc.time()[["elapsed"]]
    ans <- tryCatch(run_method(method,train,test,100000+100*r+ifelse(m=="M1",1,2)), error=function(e) e)
    dt <- proc.time()[["elapsed"]]-tick
    if(inherits(ans,"error")) {
       detail <- conditionMessage(ans)
       status <- rbind(status,data.frame(mechanism=m,rep=r,method=method,status="FAIL",detail=detail,elapsed_s=dt))
       cat("FAILED",method,stem,detail,"seconds",round(dt,1),"\n")
    } else {
       d <- as.integer(ans$d)
       if(length(d)!=nrow(test) || anyNA(d) || !all(d %in% 0:1)) stop("invalid d")
       write.csv(data.frame(id=as.integer(test$id),action=d),file.path(out,paste0("pred_",method,"_",stem,".csv")),row.names=FALSE)
       status <- rbind(status,data.frame(mechanism=m,rep=r,method=method,status="OK",detail=ans$detail,elapsed_s=dt))
       cat("SUCCESS",method,stem,"n1",sum(d),"seconds",round(dt,1),ans$detail,"\n")
    }
    write.csv(status,file.path(out,paste0("status_",method,".csv")),row.names=FALSE)
    flush.console()
}
cat("DONE",method,"\n")
