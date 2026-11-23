#!/usr/bin/env python3
"""N2-3: reachability-gated NON-COX quantile decision pilot.

Reuse N2 pilot's exact DGP/seed streams. The endpoint model is an IPCW
multinomial logistic model at H; it learns cause-1 reachability from an
estimated CIF(H), not from any oracle label. Gate direct per-cause quantiles.
The model is not the Peng-Fine published method. Not a new treatment rule.
"""
from __future__ import annotations
import argparse, importlib.util, json, time
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from scipy.special import expit

HERE=Path(__file__).resolve().parent
SOURCE=Path('/mnt/data/N2_new_project_research/src/n2_pilot.py')
# In GitHub checkout use sibling N2_pilot, no model fitted from a previous project.
if not SOURCE.is_file():
    SOURCE=HERE.parents[1]/'N2_pilot'/'src'/'n2_pilot.py'
if not SOURCE.is_file():
    raise FileNotFoundError('Require sibling N2_pilot/src/n2_pilot.py')
spec=importlib.util.spec_from_file_location('n2pilot',SOURCE)
M=importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
METHODS=('direct','gated_direct','gated_projected','joint','joint_confirmed')


def endpoint_phi(z,a):
    z1,z2=z[:,0],z[:,1]
    return np.column_stack([z1,z1*z1,z2,z1*z2,a,a*z1,a*z2])


def endpoint_fit(obs):
    # Observe the 3-state outcome at H if a first event occurred before H or
    # the person was still followed to H. All other records are censored before H.
    event=np.asarray(obs['delta'])
    at_h=obs['x']>=M.H-1e-10
    keep=event | at_h
    y=np.where(event,obs['j'],0)[keep]
    w=np.where(event, np.exp(obs['lamhat']*obs['x']),
               np.exp(obs['lamhat']*M.H))[keep]
    x=endpoint_phi(obs['z'][keep],obs['a'][keep].astype(float))
    scale=StandardScaler();xs=scale.fit_transform(x)
    lr=LogisticRegression(C=1.,solver='lbfgs',max_iter=350,tol=1e-5)
    lr.fit(xs,y,sample_weight=w)
    return (scale,lr), bool(lr.n_iter_.max()<350),int(keep.sum()),float(w.max())


def endpoint_predict(fit, z):
    sc,model=fit
    n=len(z); f=np.zeros((n,2,2))
    for a in range(2):
        prob=model.predict_proba(sc.transform(endpoint_phi(z,np.full(n,a,float))))
        for k in (1,2):
            loc=np.where(model.classes_==k)[0]
            if loc.size:f[:,a,k-1]=prob[:,loc[0]]
    assert (f>=0).all() and (f.sum(axis=2)<1+1e-9).all()
    return f


def estimate_direct(obs,zte,p):
    preds={};residual=[];solverok=[]
    for cause in (1,'all'):
        pred=np.empty((len(zte),2))
        for a in range(2):
            select=(obs['a']==a)
            coef,norm,ok=M.direct_one(obs['x'][select],obs['delta'][select],
                  obs['j'][select],obs['z'][select],p,cause,obs['lamhat'])
            pred[:,a]=M.H*expit(M.phi_direct(zte)@coef)
            residual.append(norm);solverok.append(ok)
        preds[cause]=pred
    return preds[1],preds['all'],max(residual),all(solverok)


def build_methods(direct_q1,direct_all,joint_f,endpoint_f,p):
    joint_q1=M.interp_q(joint_f[:,:,0,:],p)
    joint_all=M.interp_q(joint_f.sum(axis=2),p)
    # These are estimated supports, NEVER true oracle reachability labels.
    endpoint_reach1=endpoint_f[:,:,0]>p+1e-10
    endpoint_reachall=endpoint_f.sum(axis=2)>p+1e-10
    gated1=np.where(endpoint_reach1,direct_q1,np.nan)
    gatedall=np.where(endpoint_reachall,direct_all,np.nan)
    # A necessary same-p coherence inequality, not full CIF consistency.
    repaired=np.where(np.isfinite(gated1)&np.isfinite(gatedall),
                      np.maximum(gated1,gatedall),gated1)
    jointconfirm1=np.where(endpoint_reach1,joint_q1,np.nan)
    jointconfirmall=np.where(endpoint_reachall,joint_all,np.nan)
    return {
      'direct':(direct_q1,direct_all),
      'gated_direct':(gated1,gatedall),
      'gated_projected':(repaired,gatedall),
      'joint':(joint_q1,joint_all),
      'joint_confirmed':(jointconfirm1,jointconfirmall),
    }


def metrics(true_q1,true_qa,true_f1L,estimated,p,group):
    q1,qa=estimated
    n=len(q1)
    true_reach=true_f1L>p+1e-10
    predicted_reach=np.isfinite(q1)
    tn=np.sum((~true_reach)&(~predicted_reach));fp=np.sum((~true_reach)&predicted_reach)
    fn=np.sum(true_reach&(~predicted_reach));tp=np.sum(true_reach&predicted_reach)
    assert tp+tn+fp+fn==2*n
    valid=true_reach.all(axis=1)&np.isfinite(true_q1).all(axis=1) & (abs(true_q1[:,1]-true_q1[:,0])>1e-6)
    predvalid=predicted_reach.all(axis=1) & (abs(np.nan_to_num(q1[:,1],nan=0)-np.nan_to_num(q1[:,0],nan=0))>1e-6)
    resolved=valid&predvalid
    unresolved=valid&(~predvalid)
    true_opt=true_q1[:,1]>true_q1[:,0]
    pred_opt=q1[:,1]>q1[:,0]
    wrong=resolved&(true_opt!=pred_opt)
    # For genuine two-arm oracle comparability, inability to decide is costly:
    # fallback to treatment 0; never silently drop patients with no decision.
    deployed=np.where(predvalid,pred_opt,False)
    deploy_wrong=valid & (deployed != true_opt)
    q_choice=np.where(deployed,true_q1[:,1],true_q1[:,0])
    oraclemax=np.fmax(true_q1[:,0],true_q1[:,1])
    regret=np.maximum(oraclemax-q_choice,0.)
    false_comparable=np.sum(~true_reach.all(axis=1)&predicted_reach.all(axis=1))
    qq_consistency=np.sum(np.isfinite(q1)&np.isfinite(qa)&(q1+1e-6<qa))
    only_both_reach=np.isfinite(true_q1).all(axis=1)
    all_both_reach=only_both_reach & np.isfinite(true_qa).all(axis=1)
    # report accuracy among comparable, accuracy conditional on resolved,
    # and deployed wrong with fallback; using pre-defined denominators.
    def rate(num,den):return float(100*num/den) if den else None
    nonfinite=~np.isfinite(q1)
    return dict(scenario=group[0],rate_censor=group[1],rep=group[2],p_diagnostic=p,
        method=group[3],n_patient=n,arm_count=2*n,
        true_unreachable_arm_n=int((~true_reach).sum()),
        fp_finite_arm_n=int(fp),fn_unreachable_arm_n=int(fn),
        false_finite_pct_of_true_unreachable=rate(fp,(~true_reach).sum()),
        false_unreachable_pct_of_true_reachable=rate(fn,true_reach.sum()),
        predicted_unreachable_arm_pct=rate(nonfinite.sum(),2*n),
        reachability_acc_pct=rate(tp+tn,2*n),
        true_twoarm_comparable_n=int(valid.sum()),
        true_twoarm_allpriority_interior_n=int(all_both_reach.sum()),
        true_twoarm_resolved_n=int(resolved.sum()),
        true_twoarm_unresolved_n=int(unresolved.sum()),
        unresolved_pct_true_comparable=rate(unresolved.sum(),valid.sum()),
        wrong_on_resolved_n=int(wrong.sum()),
        wrong_on_resolved_pct=rate(wrong.sum(),resolved.sum()),
        deployed_wrong_n=int(deploy_wrong.sum()),
        deployed_wrong_pct_true_comparable=rate(deploy_wrong.sum(),valid.sum()),
        mean_oracle_q1_regret_all_comparable=float(regret[valid].mean()) if valid.any() else None,
        false_twoarm_finite_n=int(false_comparable),
        q1_below_qall_same_p_n=int(qq_consistency))


def run_one(sc,rate,rep,ntrain,ntest):
    ss=np.random.SeedSequence([M.SEED,M.SCENARIOS.index(sc),int(rate*1000),rep,ntrain])
    rng=np.random.default_rng(ss)
    ztr=np.c_[rng.uniform(-1,1,ntrain),rng.binomial(1,.5,ntrain)]
    zte=np.c_[rng.uniform(-1,1,ntest),rng.binomial(1,.5,ntest)]
    rtr=M.rates(ztr,sc); rte=M.rates(zte,sc)
    obs=M.sample(rtr,ztr,rng,rate)
    jfit,fitrows,jconv=M.joint_fit(obs)
    joint_f=M.joint_predict(jfit,zte)
    efit,econv,weighted_rows,maxweight=endpoint_fit(obs)
    end_f=endpoint_predict(efit,zte)
    # same true CIF for all estimators; no oracle labels used for gating.
    true_final=M.cif(rte,M.H)[:,:,0]
    out=[]
    for p in M.P_SCAN:
        d1,da,res,ok=estimate_direct(obs,zte,p)
        qtrue=M.exact_q(rte,p,0)
        atru=M.exact_q(rte,p,'all')
        methods=build_methods(d1,da,joint_f,end_f,p)
        for method,est in methods.items():
            row=metrics(qtrue,atru,true_final,est,p,(sc,rate,rep,method))
            row.update(ntrain=ntrain,ntest=ntest,realized_censor_pct=obs['stochastic_censor_pct'],
                       joint_converged=jconv,endpoint_converged=econv,
                       endpoint_fit_rows=weighted_rows,endpoint_max_weight=maxweight,
                       direct_max_residual=res,direct_all_solvers_succeeded=ok)
            out.append(row)
    return out


def selftest():
    # Direct: unreachable/finite, coherence violation; endpoint gate and
    # necessary coherence projection are independently checkable.
    d1=np.array([[1.,1.5],[.8,1.3]])
    da=np.array([[1.1,1.2],[.5,.6]])
    jf=np.zeros((2,2,2,len(M.TIMES)))
    jf[:,:,0,-1]=np.array([[.3,.1],[.3,.3]])
    jf[:,:,1,-1]=.1
    # interpolating only a terminal jump yields finite values for reachable arm
    end=np.array([[[.3,.1],[.1,.1]],[[.3,.1],[.3,.1]]])
    pred=build_methods(d1,da,jf,end,.2)
    assert np.isfinite(pred['direct'][0]).all()
    assert np.isnan(pred['gated_direct'][0][0,1])
    gp=pred['gated_projected'][0]
    assert gp[0,0]>=pred['gated_projected'][1][0,0]
    assert np.isfinite(gp[1]).all()
    t1=np.array([[1.,np.nan],[1.5,1.]])
    ta=np.array([[.5,.5],[.5,.5]])
    truth=np.array([[.3,.1],[.3,.3]])
    m=metrics(t1,ta,truth,pred['gated_direct'],.2,('self',.15,1,'gated_direct'))
    assert m['true_unreachable_arm_n']==1 and m['fp_finite_arm_n']==0
    assert m['true_twoarm_comparable_n']==1
    assert m['deployed_wrong_n']==1  # A1 predicted, but A0 is oracle best
    print('PASS N2-3 selftest: endpoint gate, projection, true support, fallback denominator')


def summarize(df):
    cols=['fp_finite_arm_n','fn_unreachable_arm_n','false_finite_pct_of_true_unreachable',
          'false_unreachable_pct_of_true_reachable','reachability_acc_pct',
          'true_twoarm_comparable_n','true_twoarm_resolved_n','true_twoarm_unresolved_n',
          'unresolved_pct_true_comparable','wrong_on_resolved_n','wrong_on_resolved_pct',
          'deployed_wrong_n','deployed_wrong_pct_true_comparable',
          'mean_oracle_q1_regret_all_comparable','false_twoarm_finite_n','q1_below_qall_same_p_n']
    out=[]
    for key,g in df.groupby(['scenario','rate_censor','p_diagnostic','method'],sort=False):
        r=dict(zip(['scenario','rate_censor','p_diagnostic','method'],key))
        r['reps']=len(g)
        for col in cols:
            values=pd.to_numeric(g[col],errors='coerce').to_numpy(float)
            finite=values[np.isfinite(values)]
            r[col+'_mean']=float(np.mean(finite)) if len(finite) else None
            r[col+'_mcse']=float(np.std(finite,ddof=1)/np.sqrt(len(finite))) if len(finite)>1 else None
            r[col+'_sum']=float(np.nansum(values)) if col.endswith('_n') else None
        out.append(r)
    return pd.DataFrame(out)


def main():
    p=argparse.ArgumentParser();p.add_argument('--self-test',action='store_true')
    p.add_argument('--reps',type=int,default=8)
    p.add_argument('--ntrain',type=int,default=900)
    p.add_argument('--ntest',type=int,default=1000)
    p.add_argument('--out',type=Path,default=HERE.parents[0]/'results');args=p.parse_args()
    selftest()
    if args.self_test:return
    t0=time.time();rows=[]
    for sc in M.SCENARIOS:
        for rate in M.CENSOR_RATES:
            for rep in range(1,args.reps+1):
                rows.extend(run_one(sc,rate,rep,args.ntrain,args.ntest))
                if rep%2==0: print(f'{sc} censor_rate={rate} rep {rep}/{args.reps} elapsed={time.time()-t0:.1f}s',flush=True)
    args.out.mkdir(parents=True,exist_ok=True)
    df=pd.DataFrame(rows)
    df.to_csv(args.out/'n2_3_replications.csv',index=False)
    summary=summarize(df)
    summary.to_csv(args.out/'n2_3_summary.csv',index=False)
    cfg=dict(source=str(SOURCE),seed=M.SEED,reps=args.reps,ntrain=args.ntrain,ntest=args.ntest,
             scenarios=M.SCENARIOS,censor_rates=M.CENSOR_RATES,diagnostic_p=M.P_SCAN,
             actual_model_classes=list(METHODS),horizon=M.H,
             note='Finite p only a diagnostic. Never chosen to maximize performance; abstain uses fixed A=0 in deploy metric.')
    (args.out/'config.json').write_text(json.dumps(cfg,indent=2),encoding='utf-8')
    assert df.groupby(['scenario','rate_censor','rep','p_diagnostic']).size().eq(5).all()
    assert df.joint_converged.all() and df.endpoint_converged.all()
    print('PASS N2-3 all paired rows and both classifier convergence; elapsed',round(time.time()-t0,2))

if __name__=='__main__':main()