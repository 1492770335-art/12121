#!/usr/bin/env python3
"""N2-2: reachability, coherence and decision-error audit for two non-Cox N2 estimators.

Replays the original N2 pilot's frozen seed streams for a specified prefix of
replicates. No p, followup window or clinical utility parameter is optimized.
Direct estimator is a *prototype inspired by* Peng & Fine, not the paper's method.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.special import expit


def load_pilot():
    here = Path(__file__).resolve()
    repos = [here.parents[2] / "N2_pilot" / "src" / "n2_pilot.py",
             Path("/mnt/data/N2_new_project_research/src/n2_pilot.py")]
    for path in repos:
        if path.is_file():
            spec = importlib.util.spec_from_file_location("n2_source", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod, path
    raise FileNotFoundError("Original N2 pilot source missing: " + str(repos))

M, SOURCE = load_pilot()
TOL = 1e-10


def diagnostic_row(sc, rate, rep, p, method, trueq, tqa, true_f1_L,
                   fhat, predq, predall, direct_norm, direct_fail, joint_conv,
                   realized_censor):
    n = len(trueq)
    true_reach = true_f1_L > p + TOL
    if method == "direct":
        est_reach = np.isfinite(predq)
    else:
        est_reach = fhat[:, :, 0, -1] > p + TOL
    if method == "joint":
        assert np.array_equal(est_reach, np.isfinite(predq)), (sc, rate, rep, p)

    true_unreach = ~true_reach
    est_unreach = ~est_reach
    tp = np.sum(true_reach & est_reach)
    tn = np.sum(true_unreach & est_unreach)
    fp = np.sum(true_unreach & est_reach)
    fn = np.sum(true_reach & est_unreach)
    assert tp + tn + fp + fn == n * 2

    # Same probability p for priority vs all, necessary Q_1(p) >= Q_all(p).
    pq = np.where(np.isfinite(predq), predq, M.H)
    pa = np.where(np.isfinite(predall), predall, M.H)
    incoherent = pq + 1e-6 < pa

    strict_true_pair = true_reach.all(axis=1) & (abs(trueq[:, 1]-trueq[:, 0]) > 1e-6)
    strict_pred_pair = est_reach.all(axis=1) & (abs(pq[:, 1]-pq[:, 0]) > 1e-6)
    resolved = strict_true_pair & strict_pred_pair
    unresolved = strict_true_pair & ~strict_pred_pair
    wrong = resolved & (np.sign(trueq[:, 1]-trueq[:, 0]) != np.sign(pq[:, 1]-pq[:, 0]))
    assert int(wrong.sum() + (resolved & ~wrong).sum() + unresolved.sum()) == int(strict_true_pair.sum())

    # A falsely finite comparison is not called a wrong recommendation: the
    # *ground truth has no finite, comparable two-arm Q(p) within the horizon*.
    false_comparable = ~true_reach.all(axis=1) & est_reach.all(axis=1)
    missed_comparable = true_reach.all(axis=1) & ~est_reach.all(axis=1)
    
    # On the oracle jointly strict-interior set, quantify regret only for
    # resolved decisions. Unresolved patients are not assigned artificial Q=L.
    oracle_joint = strict_true_pair & np.isfinite(tqa).all(axis=1)
    cnd = oracle_joint & strict_pred_pair
    if cnd.any():
        chosen = np.where(pq[:, 1] > pq[:, 0], 1, 0)
        other = 1 - chosen
        qi = np.take_along_axis(trueq, chosen[:,None],axis=1)[:,0]
        qi_other = np.take_along_axis(trueq, other[:,None],axis=1)[:,0]
        qa = np.take_along_axis(tqa, chosen[:,None],axis=1)[:,0]
        qa_other = np.take_along_axis(tqa, other[:,None],axis=1)[:,0]
        regret = np.maximum(0., np.nanmax(trueq, axis=1) - qi)
        dominated = cnd & (qi_other > qi + 1e-6) & (qa_other > qa + 1e-6)
        mean_regret = np.mean(regret[cnd]); dominated_n = int(dominated.sum())
    else:
        mean_regret = float('nan'); dominated_n = 0

    # Near endpoint, the true classification is especially sensitive.
    near_end = abs(true_f1_L-p) <= .03
    near_denom = int(near_end.sum())
    near_miss = int((near_end & (true_reach != est_reach)).sum())

    def safe(a,b): return float(100*a/b) if b else float('nan')
    return dict(
        scenario=sc,rate_censor=rate,rep=rep,p_diagnostic=p,method=method,
        realized_censor_pct=float(realized_censor),
        ntest=n,arms=2,eval_arm_n=n*2,
        true_reach_arm_n=int(true_reach.sum()),true_unreachable_arm_n=int(true_unreach.sum()),
        estimated_reach_arm_n=int(est_reach.sum()),
        true_unreachable_arm_pct=safe(true_unreach.sum(),n*2),
        fp_finite_arm_n=int(fp),fn_unreached_arm_n=int(fn),
        false_finite_pct_of_true_unreachable=safe(fp,true_unreach.sum()),
        false_unreachable_pct_of_true_reachable=safe(fn,true_reach.sum()),
        reachability_accuracy_pct=safe(tp+tn,2*n),
        endpoint_near_p_arm_n=near_denom,
        endpoint_near_p_misclass_pct=safe(near_miss,near_denom),
        incoherent_q1_less_qall_n=int(incoherent.sum()),
        incoherent_q1_less_qall_pct=safe(incoherent.sum(),2*n),
        oracle_two_arm_q1_strict_interior_n=int(strict_true_pair.sum()),
        predicted_two_arm_finite_n=int(est_reach.all(axis=1).sum()),
        false_finite_comparison_n=int(false_comparable.sum()),
        missed_finite_comparison_n=int(missed_comparable.sum()),
        true_comparison_resolved_n=int(resolved.sum()),
        true_comparison_unresolved_n=int(unresolved.sum()),
        wrong_recommendation_n=int(wrong.sum()),
        wrong_recommendation_pct_of_oracle_comparable=safe(wrong.sum(),strict_true_pair.sum()),
        unresolved_pct_of_oracle_comparable=safe(unresolved.sum(),strict_true_pair.sum()),
        true_joint_all_priority_interior_n=int(oracle_joint.sum()),
        true_joint_value_resolved_n=int(cnd.sum()),
        mean_q1_regret_only_resolved=float(mean_regret),
        dominated_choice_n=dominated_n,
        dominated_choice_pct_of_joint_resolved=safe(dominated_n,cnd.sum()),
        direct_max_moment_residual=float(direct_norm),
        direct_fail_count=int(direct_fail),joint_converged=bool(joint_conv)
    )


def replay(sc: str, rate: float, rep: int, ntrain: int, ntest: int):
    seed = np.random.SeedSequence([M.SEED,M.SCENARIOS.index(sc),int(rate*1000),rep,ntrain])
    rng = np.random.default_rng(seed)
    ztr=np.c_[rng.uniform(-1,1,ntrain),rng.binomial(1,.5,ntrain)]
    zte=np.c_[rng.uniform(-1,1,ntest),rng.binomial(1,.5,ntest)]
    rtr=M.rates(ztr,sc);rte=M.rates(zte,sc)
    obs=M.sample(rtr,ztr,rng,rate)
    fitted,fit_n,converged=M.joint_fit(obs)
    joint_f=M.joint_predict(fitted,zte)
    assert np.all(np.diff(joint_f,axis=-1)>=-1e-10)
    assert joint_f.sum(axis=2).max()<1+1e-10
    true_final=M.cif(rte,M.H)[:,:,0]
    rows=[]
    for p in M.P_SCAN:
        direct={}; detail=[]
        for cause in ('all',1):
            pred=np.full((ntest,2),np.nan)
            for a in (0,1):
                mask=obs['a']==a
                theta,norm,success=M.direct_one(obs['x'][mask],obs['delta'][mask],obs['j'][mask],obs['z'][mask],p,cause,obs['lamhat'])
                pred[:,a]=M.H*expit(M.phi_direct(zte)@theta)
                detail.append((norm,success))
            direct[cause]=pred
        t1=M.exact_q(rte,p,0)
        ta=M.exact_q(rte,p,'all')
        for method in ('direct','joint'):
            pq = direct[1] if method=='direct' else M.interp_q(joint_f[:,:,0,:],p)
            pa = direct['all'] if method=='direct' else M.interp_q(joint_f.sum(axis=2),p)
            rows.append(diagnostic_row(sc,rate,rep,p,method,t1,ta,true_final,joint_f,pq,pa,
                    max(x[0] for x in detail),sum(not x[1] for x in detail),converged,
                    obs['stochastic_censor_pct']))
    return rows


def aggregate(raw:pd.DataFrame):
    # Each replication is the unit of MC uncertainty, not each correlated arm.
    keys=['scenario','rate_censor','p_diagnostic','method']
    count_cols=['true_unreachable_arm_n','fp_finite_arm_n','fn_unreached_arm_n',
                'incoherent_q1_less_qall_n','oracle_two_arm_q1_strict_interior_n',
                'false_finite_comparison_n','wrong_recommendation_n',
                'true_comparison_unresolved_n','true_comparison_resolved_n',
                'dominated_choice_n']
    metric_cols=['true_unreachable_arm_pct','false_finite_pct_of_true_unreachable',
                 'false_unreachable_pct_of_true_reachable','reachability_accuracy_pct',
                 'endpoint_near_p_misclass_pct','incoherent_q1_less_qall_pct',
                 'wrong_recommendation_pct_of_oracle_comparable',
                 'unresolved_pct_of_oracle_comparable',
                 'mean_q1_regret_only_resolved',
                 'dominated_choice_pct_of_joint_resolved']
    rec=[]
    for key,group in raw.groupby(keys,sort=False):
        d=dict(zip(keys,key));d['reps']=len(group)
        for c in count_cols: d[c+'_total']=int(group[c].sum())
        for c in metric_cols:
            v=group[c].to_numpy(dtype=float)
            v=v[np.isfinite(v)]
            d[c+'_mean']=float(np.mean(v)) if len(v) else None
            d[c+'_mcse']=float(np.std(v,ddof=1)/np.sqrt(len(v))) if len(v)>1 else None
            d[c+'_available_reps']=int(len(v))
        rec.append(d)
    return pd.DataFrame(rec)


def selftest():
    # One unreachable arm, one reachable; learner always predicts finite for both.
    p=.2
    q=np.array([[1.,np.nan],[1.1,1.3]])
    qa=np.array([[.7,.8],[.6,.8]])
    truth=np.array([[.25,.15],[.3,.27]])
    joint=np.zeros((2,2,2,3));joint[:,:,0,-1]=truth
    ffinite=np.array([[1.,2.],[1.1,1.4]])
    fqa=np.array([[.8,1.],[.7,.8]])
    row=diagnostic_row('self',0,1,p,'direct',q,qa,truth,joint,ffinite,fqa,0,0,True,25)
    assert row['true_unreachable_arm_n']==1
    assert row['fp_finite_arm_n']==1
    assert row['false_finite_comparison_n']==1
    assert row['oracle_two_arm_q1_strict_interior_n']==1
    assert row['wrong_recommendation_n']==0
    assert row['true_comparison_resolved_n']==1
    # Coherence violation check, if Q1 artificially before Qall.
    fqa[0,0]=1.2
    row2=diagnostic_row('self',0,1,p,'direct',q,qa,truth,joint,ffinite,fqa,0,0,True,25)
    assert row2['incoherent_q1_less_qall_n']==1
    print('PASS N2-2 unit tests: reachability confusion, unresolved, structural violation')


def main():
    arg=argparse.ArgumentParser()
    arg.add_argument('--self-test',action='store_true')
    arg.add_argument('--reps',type=int,default=8)
    arg.add_argument('--ntrain',type=int,default=900)
    arg.add_argument('--ntest',type=int,default=1000)
    arg.add_argument('--out',type=Path,default=Path(__file__).resolve().parents[1]/'results')
    args=arg.parse_args()
    selftest()
    if args.self_test:return
    rows=[]
    for sc in M.SCENARIOS:
        for rate in M.CENSOR_RATES:
            for rep in range(1,args.reps+1):
                data=replay(sc,rate,rep,args.ntrain,args.ntest)
                rows.extend(data)
                if rep%4==0:print('complete',sc,rate,rep,'/',args.reps,flush=True)
    args.out.mkdir(parents=True,exist_ok=True)
    df=pd.DataFrame(rows)
    assert len(df)==len(M.SCENARIOS)*len(M.CENSOR_RATES)*args.reps*len(M.P_SCAN)*2
    assert df.loc[df.method=='joint','incoherent_q1_less_qall_n'].sum()==0
    assert df.loc[df.method=='direct','fn_unreached_arm_n'].sum()==0
    assert df.loc[df.method=='direct','predicted_two_arm_finite_n'].eq(args.ntest).all()
    assert df.loc[df.method=='joint','joint_converged'].all()
    df.to_csv(args.out/'n2_2_replications.csv',index=False,float_format='%.9f')
    summ=aggregate(df)
    summ.to_csv(args.out/'n2_2_summary.csv',index=False,float_format='%.9f')
    # Compact summary aggregated over p/repeats/rates; diagnosis only.
    compact=[]
    for (sc,p,method),part in df.groupby(['scenario','p_diagnostic','method']):
        u=part.true_unreachable_arm_n.sum();fp=part.fp_finite_arm_n.sum();tpair=part.oracle_two_arm_q1_strict_interior_n.sum()
        compact.append(dict(scenario=sc,p_diagnostic=p,method=method,training_replications=len(part),
            true_unreachable_arm_n=int(u),false_finite_arm_n=int(fp),
            false_finite_rate_among_true_unreachable_pct=100*fp/u if u else None,
            true_comparable_patient_n=int(tpair),wrong_recommendation_n=int(part.wrong_recommendation_n.sum()),
            unresolved_recommendation_n=int(part.true_comparison_unresolved_n.sum()),
            coherence_violation_n=int(part.incoherent_q1_less_qall_n.sum()),
            false_finite_comparison_n=int(part.false_finite_comparison_n.sum())))
    pd.DataFrame(compact).to_csv(args.out/'n2_2_compact.csv',index=False)
    config=dict(seed=int(M.SEED),mechanisms=list(M.SCENARIOS),reps=args.reps,ntrain=args.ntrain,ntest=args.ntest,
        censor_rates=list(M.CENSOR_RATES),p_diagnostic=list(M.P_SCAN),horizon=M.H,
        base_N2_source=str(SOURCE),strict_interior_rule='F1^a(H)>p+1e-10',
        no_final_risk_threshold_selected=True,no_first_stage_delta_selected=True,
        truth_unreachable_decision='not ranked; flag as undefined not worse or better',
        direct='bounded quantile estimating equation ALWAYS finite, thus structurally incapable of detecting unattainability',
        joint='IPCW multinomial CIF, monotonic normalization, window-end reachability indicator',
        note='Pilot and structural audit, not exact Peng-Fine method or clinical result; same frozen original N2 seed streams')
    (args.out/'n2_2_config.json').write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('DONE N2-2',len(df),'diagnostic rows',flush=True)


if __name__=='__main__':main()
