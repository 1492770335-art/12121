#!/usr/bin/env python3
"""N2 preliminary comparison of two NON-COX competing-risk estimators.

DIRECT: exploratory smoothed IPCW quantile moment learner inspired by
Peng & Fine (2009), NOT an exact implementation of the published estimator.
JOINT: IPCW weighted multinomial classification at a time grid; isotonic
max-projection plus common normalization for valid competing-risk CIFs.

No p is chosen as clinical threshold. No full treatment policy optimization.
"""
from __future__ import annotations
import argparse, json, warnings, sys
from pathlib import Path
from scipy.optimize import least_squares
from scipy.special import expit
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

SEED = 2026112309
H=3.0; SWITCH=1.2
SCENARIOS=('aligned','cause_tradeoff','time_varying')
P_SCAN=(.12,.18,.24) # diagnostic p grid; no clinical optimization
CENSOR_RATES=(.15,.35) # stochastic exponential per abstract time unit; realized censor % reported
# Direct and joint estimators share fitted censor survival G(t).
TIMES=np.r_[0.,np.linspace(.125,H,24)]


def rates(z,scenario):
    z1,z2=z[:,0],z[:,1]
    b1=.20*np.exp(.15*z1+.15*z2)
    b2=.14*np.exp(-.12*z1+.20*z2)
    r=np.empty((len(z),2,2,2))
    r[:,0,0,:]=b1[:,None];r[:,0,1,:]=b2[:,None]
    if scenario=='aligned':
        e1a=e1b=e2a=e2b=-.30+.10*z1
    elif scenario=='cause_tradeoff':
        e1a=e1b=-.30+.30*z1
        e2a=e2b=.30-.20*z1
    elif scenario=='time_varying':
        e1a=-.50+.25*z1; e1b=.55+.25*z1
        e2a=.20-.25*z1; e2b=-.20-.25*z1
    else:raise ValueError(scenario)
    r[:,1,0,0]=b1*np.exp(e1a);r[:,1,0,1]=b1*np.exp(e1b)
    r[:,1,1,0]=b2*np.exp(e2a);r[:,1,1,1]=b2*np.exp(e2b)
    return r


def cif(r,t):
    """Exact analytic competing risk CIF at t. r is N x 2 x 2 x 2."""
    t0=min(t,SWITCH);t1=max(t-SWITCH,0.)
    r0=r[:,:,:,0];h0=r0.sum(axis=2)
    s0=np.exp(-h0*t0)
    f=r0/h0[:,:,None]*(-np.expm1(-h0*t0))[:,:,None]
    if t1>0:
        r1=r[:,:,:,1];h1=r1.sum(axis=2)
        f+=s0[:,:,None]*r1/h1[:,:,None]*(-np.expm1(-h1*t1))[:,:,None]
    return f


def exact_q(r,p,c):
    r0=r[:,:,:,0];r1=r[:,:,:,1]
    tot0=r0.sum(axis=2);tot1=r1.sum(axis=2)
    if c=='all':w0=tot0;w1=tot1
    else:w0=r0[:,:,c];w1=r1[:,:,c]
    sw=np.exp(-tot0*SWITCH)
    fs=w0/tot0*(-np.expm1(-tot0*SWITCH))
    fL=fs+sw*w1/tot1*(-np.expm1(-tot1*(H-SWITCH)))
    good=(fL>p+1e-12)
    q=np.full(fL.shape,np.nan)
    early=good & (p<=fs)
    late=good & (p>fs)
    a0=np.clip(p*tot0/w0,0,1-1e-14)
    a1=np.clip((p-fs)*tot1/(sw*w1),0,1-1e-14)
    earlyq=-np.log1p(-a0)/tot0
    lateq=SWITCH-np.log1p(-a1)/tot1
    q[early]=earlyq[early];q[late]=lateq[late]
    return q


def sample(r,z,rng,c_rate):
    """Randomized baseline treatment, continuous piecewise-exp failure, independent censor."""
    n=len(z);a=rng.integers(0,2,n)
    rsel=r[np.arange(n),a]
    h0=rsel[:,:,0].sum(axis=1);h1=rsel[:,:,1].sum(axis=1)
    eh=rng.exponential(size=n)
    first=(eh<=h0*SWITCH)
    t=np.where(first,eh/h0,SWITCH+(eh-h0*SWITCH)/h1)
    cause_prob=np.where(first,rsel[:,0,0]/h0,rsel[:,0,1]/h1)
    j=np.where(rng.random(n)<cause_prob,1,2)
    cens=rng.exponential(1/c_rate,n)
    x=np.minimum(np.minimum(t,cens),H)
    event=(t<=cens)&(t<=H)
    stochastic_censor=(cens<t)&(cens<H)
    j=np.where(event,j,0)
    # Censoring rate MLE with time at risk until any failure, censor or admin H.
    lambda_hat=max(1e-5,stochastic_censor.sum()/x.sum())
    return dict(x=x,delta=event,j=j,a=a,z=z,lamhat=float(lambda_hat),
                stochastic_censor_pct=float(100*stochastic_censor.mean()),
                event_pct=float(100*event.mean()),admin_pct=float(100*(~(stochastic_censor|event)).mean()))


def phi_direct(z):
    return np.c_[np.ones(len(z)),z[:,0],z[:,1],z[:,0]*z[:,1]]


def direct_one(x,delta,j,z,p,c,lambda_hat):
    """Finite-dimensional smoothed cause-CIF moment estimator.

    Moment E[phi * (Delta 1{J=c, X<=q(z)}/G_C(X) - p)]=0.
    q(z)=H expit(phi@beta) is bounded to [0,H], so the estimator cannot
    distinguish q near H from truly unreached target; disclose this limitation.
    """
    v=phi_direct(z)
    event=(delta if c=='all' else (delta & (j==c)))
    weight=np.where(event,np.exp(lambda_hat*x),0.)
    bandwidth=.075 # numerical smoothing for preliminary method, not bandwidth optimized
    def resid(b):
        q=H*expit(v@b)
        s=expit((q-x)/bandwidth)
        return np.mean(v*((weight*s-p)[:,None]),axis=0)
    q_guess=np.clip(np.quantile(x[delta],min(.4,p+.15)) if np.any(delta) else .6, .1,2.)
    b0=np.array([np.log(q_guess/(H-q_guess)),0,0,0])
    fit=least_squares(resid,b0,bounds=(-6*np.ones(4),6*np.ones(4)),
                      ftol=1e-7,xtol=1e-7,gtol=1e-7,max_nfev=95)
    return fit.x,float(np.linalg.norm(resid(fit.x))),bool(fit.success)


def features(z,a,t):
    z1=z[:,0];z2=z[:,1]
    return np.c_[t,t*t,t*t*t,np.log1p(t),z1,z1*z1,z2,a,a*z1,a*z2,
                 a*t,a*t*t,a*z1*t,a*z2*t,t*z1,t*z2]


def long_data(obs):
    x=obs['x'];delta=obs['delta'];j=obs['j'];z=obs['z'];a=obs['a']
    Xs=[];ys=[];ws=[]
    for t in TIMES[1:]:
        # Event by t -> inverse G at event time, no first event by t -> inverse G(t).
        fail=delta & (x<=t)
        no=(x>t)
        keep=fail|no
        if not np.any(keep):continue
        label=np.zeros(len(x),dtype=np.int8)
        label[fail]=j[fail]
        weights=np.zeros(len(x))
        weights[fail]=np.exp(obs['lamhat']*x[fail])
        weights[no]=np.exp(obs['lamhat']*t)
        Xs.append(features(z[keep],a[keep].astype(float),np.full(keep.sum(),t)))
        ys.append(label[keep]);ws.append(weights[keep])
    return np.concatenate(Xs),np.concatenate(ys),np.concatenate(ws)


def joint_fit(obs):
    X,y,w=long_data(obs)
    scaler=StandardScaler()
    Xs=scaler.fit_transform(X)
    fit=LogisticRegression(C=1.0,max_iter=450,solver='lbfgs',tol=1e-4)
    fit.fit(Xs,y,sample_weight=w)
    return (scaler,fit),len(y),bool(fit.n_iter_.max()<450)


def joint_predict(fit,z):
    scaler, classifier = fit
    n=len(z);k=len(TIMES)
    out=np.zeros((n,2,2,k),float)
    for ai in range(2):
        for ti,t in enumerate(TIMES[1:],start=1):
            prob=classifier.predict_proba(scaler.transform(features(z,np.full(n,float(ai)),np.full(n,t))))
            for jj in (1,2):
                loc=np.where(classifier.classes_==jj)[0]
                out[:,ai,jj-1,ti]=prob[:,loc[0]] if len(loc) else 0.
    # Isotonic max projection (monotone CIF); multiply both by a shared constant
    # if needed, retaining 0<=F1+F2<=1 and time monotonicity.
    out=np.maximum.accumulate(out,axis=-1)
    m=np.maximum(1.,out.sum(axis=2).max(axis=-1))
    out/=m[:,:,None,None]
    assert out.min()>=-1e-11 and out.sum(axis=2).max()<=1+1e-11
    assert np.diff(out,axis=-1).min()>=-1e-11
    return out


def interp_q(f,p):
    """Inverse of piecewise-linear CIF on TIMES; nan if not attained by horizon."""
    n,arms,k=f.shape
    good=f[:,:,-1]>p+1e-10
    upper=np.minimum(np.sum(f<p,axis=-1),k-1)
    lower=np.maximum(upper-1,0)
    fhi=np.take_along_axis(f,upper[...,None],axis=-1)[...,0]
    flo=np.take_along_axis(f,lower[...,None],axis=-1)[...,0]
    v=np.divide(p-flo,fhi-flo,out=np.zeros_like(fhi),where=(fhi>flo))
    q=TIMES[lower]+np.clip(v,0,1)*(TIMES[upper]-TIMES[lower])
    return np.where(good,q,np.nan)


def score(trueq,predq,good,goal):
    """Common fixed oracle support denominator; unreachable preds capped L and flagged."""
    tq=np.where(np.isfinite(trueq),trueq,H)
    pq=np.where(np.isfinite(predq),predq,H)
    valid=good
    if not np.any(valid):return dict(mae=np.nan,pred_unreachable_pct=np.nan,rank_error_pct=np.nan,rank_unresolved_pct=np.nan,n=0)
    mae=np.abs(tq-pq)[valid].mean()
    unreached=(~np.isfinite(predq)).any(axis=1)
    # Truth strictly different; near-zero (<1e-5) excludes nearly tied comparator patients.
    ordered=valid & (np.abs(tq[:,1]-tq[:,0])>1e-5)
    resolved=ordered & (~unreached)
    wrong=resolved & (np.sign(tq[:,1]-tq[:,0])!=np.sign(pq[:,1]-pq[:,0]))
    return dict(mae=float(mae),pred_unreachable_pct=float(100*unreached[valid].mean()),
                rank_error_pct=float(100*wrong.sum()/ordered.sum()) if ordered.any() else np.nan,
                rank_unresolved_pct=float(100*(ordered&unreached).sum()/ordered.sum()) if ordered.any() else np.nan,
                n=int(valid.sum()))


def one_rep(scenario,rate_c,rep,ntrain,ntest):
    seedseq=np.random.SeedSequence([SEED,SCENARIOS.index(scenario),int(rate_c*1000),rep,ntrain])
    rng=np.random.default_rng(seedseq)
    ztr=np.c_[rng.uniform(-1,1,ntrain),rng.binomial(1,.5,ntrain)]
    zte=np.c_[rng.uniform(-1,1,ntest),rng.binomial(1,.5,ntest)]
    rtr=rates(ztr,scenario);rte=rates(zte,scenario)
    obs=sample(rtr,ztr,rng,rate_c)
    joint,fit_n,conv=joint_fit(obs)
    fhat=joint_predict(joint,zte)
    direct={};direct_details=[]
    for c in ('all',1):
        for p in P_SCAN:
            pred=np.full((ntest,2),np.nan)
            for a in (0,1):
                mask=obs['a']==a
                th,norm,ok=direct_one(obs['x'][mask],obs['delta'][mask],obs['j'][mask],obs['z'][mask],p,c,obs['lamhat'])
                pred[:,a]=H*expit(phi_direct(zte)@th)
                direct_details.append(dict(goal=str(c),p=p,arm=a,moment_residual=norm,solver_success=ok))
            direct[(c,p)]=pred
    rows=[]
    for p in P_SCAN:
        tq1=exact_q(rte,p,0); tqa=exact_q(rte,p,'all')
        goalgood=np.isfinite(tq1).all(axis=1) & np.isfinite(tqa).all(axis=1)
        for method in ('direct','joint'):
            q1=direct[(1,p)] if method=='direct' else interp_q(fhat[:,:,0,:],p)
            qa=direct[('all',p)] if method=='direct' else interp_q(fhat.sum(axis=2),p)
            m1=score(tq1,q1,goalgood,'priority')
            ma=score(tqa,qa,goalgood,'overall')
            cq1=np.where(np.isfinite(q1),q1,H)
            cqa=np.where(np.isfinite(qa),qa,H)
            incoherent=np.mean(cq1+1e-6 < cqa)
            rows.append(dict(scenario=scenario,rate_censor=rate_c,rep=rep,ntrain=ntrain,ntest=ntest,
                p_diagnostic=p,method=method,realized_censor_pct=obs['stochastic_censor_pct'],
                lambda_c_hat=obs['lamhat'],joint_fit_rows=fit_n,joint_converged=conv,
                oracle_joint_interior_pct=100*goalgood.mean(),oracle_joint_interior_n=int(goalgood.sum()),
                q1_mae_cap=m1['mae'],qall_mae_cap=ma['mae'],
                q1_est_unreachable_pct=m1['pred_unreachable_pct'],
                qall_est_unreachable_pct=ma['pred_unreachable_pct'],
                q1_rank_wrong_pct=m1['rank_error_pct'],q1_rank_unresolved_pct=m1['rank_unresolved_pct'],
                q1_below_qall_pct=100*incoherent,
                direct_max_moment_residual=max(v['moment_residual'] for v in direct_details),
                direct_fail_count=sum(not v['solver_success'] for v in direct_details),
            ))
    return rows,obs


def test():
    rng=np.random.default_rng(452)
    z=np.c_[rng.uniform(-1,1,4),rng.binomial(1,.5,4)]
    for sc in SCENARIOS:
        r=rates(z,sc)
        assert np.max(abs(cif(r,0.)))<1e-12
        for p in (.05,.10,.15):
            for c in ('all',0,1):
                q=exact_q(r,p,c)
                for i in range(len(z)):
                    for a in (0,1):
                        if np.isfinite(q[i,a]):
                            got=cif(r[i:i+1],q[i,a])[0,a]
                            val=got.sum() if c=='all' else got[c]
                            assert abs(val-p)<1e-10,(sc,c,p,val)
        obs=sample(r,z,rng,.23)
        assert np.all(obs['x']<=H) and np.all(obs['x']>=0)
    raw=np.zeros((2,2,2,len(TIMES)))
    raw[...,0]=0
    print('PASS: analytic CIF, inverse and censoring simulation')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parents[1]/'results')
    parser.add_argument('--reps',type=int,default=12)
    parser.add_argument('--ntrain',type=int,default=900)
    parser.add_argument('--ntest',type=int,default=1000)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    test()
    if args.self_test:return
    rows=[]
    for sc in SCENARIOS:
        for rate in CENSOR_RATES:
            for rep in range(1,args.reps+1):
                rr,obs=one_rep(sc,rate,rep,args.ntrain,args.ntest)
                rows.extend(rr)
                if rep%4==0:print('completed',sc,rate,rep,'/',args.reps,flush=True)
    args.out.mkdir(parents=True,exist_ok=True)
    raw=pd.DataFrame(rows)
    raw.to_csv(args.out/'n2_replicate_results.csv',index=False)
    grouping=['scenario','rate_censor','p_diagnostic','method']
    cols=['realized_censor_pct','oracle_joint_interior_pct','q1_mae_cap','qall_mae_cap',
          'q1_est_unreachable_pct','qall_est_unreachable_pct','q1_rank_wrong_pct',
          'q1_rank_unresolved_pct','q1_below_qall_pct','direct_max_moment_residual','direct_fail_count']
    summarized=raw.groupby(grouping,as_index=False)[cols].agg(['mean','std'])
    summarized.columns=['_'.join(x).strip('_') if isinstance(x,tuple) else x for x in summarized.columns]
    summarized.to_csv(args.out/'n2_summary.csv',index=False)
    cfg=dict(seed=SEED,reps=args.reps,ntrain=args.ntrain,ntest=args.ntest,horizon=H,
             mechanism=list(SCENARIOS),p_diagnostic=list(P_SCAN),stochastic_censor_rates=list(CENSOR_RATES),
             direct='smoothed IPCW moment equation, q=H*sigmoid(phi beta), bandwidth=0.075, linear 4 features; prototype not Peng-Fine exact',
             joint='weighted multinomial classification of three observable time-status classes + monotone normalization',
             nuisance='single estimated exp censor rate from counting process; G_c(t)=exp(-lambda_hat*t)',
             grid_time=list(map(float,TIMES)),estimated_interior='direct learner by construction always returns interior; cannot detect nonattainable p',
             disclaimer='Pilot only; p is diagnostic not chosen clinical threshold. No stage-1 constraint, no policy clinical gains. No Cox estimation.' )
    (args.out/'config.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2),encoding='utf-8')
    print('DONE',len(raw),'result rows',flush=True)

if __name__=='__main__':main()