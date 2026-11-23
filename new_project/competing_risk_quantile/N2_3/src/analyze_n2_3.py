#!/usr/bin/env python3
"""Recompute N2-3 combined reports and paired 32-replicate differences."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
root=Path(__file__).resolve().parents[1]
indir=root/'results'
x=pd.read_csv(indir/'n2_3_replications.csv.gz', compression='gzip')
rows=[]
for (sc,p,m),g in x.groupby(['scenario','p_diagnostic','method'],sort=False):
    d={'scenario':sc,'p_diagnostic':p,'method':m,'reps':len(g),
       'true_unreachable_arm_n':int(g.true_unreachable_arm_n.sum()),
       'false_finite_arm_n':int(g.fp_finite_arm_n.sum()),
       'false_unreachable_arm_n':int(g.fn_unreachable_arm_n.sum()),
       'true_twoarm_comparable_n':int(g.true_twoarm_comparable_n.sum()),
       'unresolved_true_twoarm_n':int(g.true_twoarm_unresolved_n.sum()),
       'wrong_deployed_n':int(g.deployed_wrong_n.sum()),
       'false_finite_twoarm_comparison_n':int(g.false_twoarm_finite_n.sum()),
       'q1_below_qall_samep_n':int(g.q1_below_qall_same_p_n.sum())}
    d['false_finite_pct_given_unreachable']=100*d['false_finite_arm_n']/d['true_unreachable_arm_n'] if d['true_unreachable_arm_n'] else None
    d['wrong_deployed_pct_given_true_comparable']=100*d['wrong_deployed_n']/d['true_twoarm_comparable_n'] if d['true_twoarm_comparable_n'] else None
    d['unresolved_pct_given_true_comparable']=100*d['unresolved_true_twoarm_n']/d['true_twoarm_comparable_n'] if d['true_twoarm_comparable_n'] else None
    d['mean_q1_regret_abstract_time']=float(g.mean_oracle_q1_regret_all_comparable.mean())
    rows.append(d)
pd.DataFrame(rows).to_csv(indir/'n2_3_compact.csv',index=False)
# Sensitivity: when abstaining on a truly comparable patient, the treatment
# policy is undefined. Illustrate three EXTERNAL fallback conventions.
fb=[]
for (sc,p,m),g in x.groupby(['scenario','p_diagnostic','method'],sort=False):
    n=float(g.true_twoarm_comparable_n.sum())
    resolved_wrong=float(g.wrong_on_resolved_n.sum())
    unresolved=float(g.true_twoarm_unresolved_n.sum())
    default0_wrong=float(g.deployed_wrong_n.sum())
    default1_wrong=resolved_wrong+unresolved-(default0_wrong-resolved_wrong)
    random_expected=resolved_wrong+0.5*unresolved
    fb.append(dict(scenario=sc,p_diagnostic=p,method=m,true_comparable=int(n),
                   abstained=int(unresolved),
                   wrong_pct_fallback0=100*default0_wrong/n if n else None,
                   wrong_pct_fallback1=100*default1_wrong/n if n else None,
                   expected_wrong_pct_random50=100*random_expected/n if n else None,
                   wrong_on_resolved_pct=100*resolved_wrong/(n-unresolved) if n>unresolved else None))
pd.DataFrame(fb).to_csv(indir/'n2_3_fallback_sensitivity.csv',index=False)
# 32 MC replication paired method comparisons. Both dropout and outcome
# evaluated on identical rep and patients. Report approximate t_{31} CI.
tcrit=2.039513446
res=[]
for (sc,rate,p),g in x.groupby(['scenario','rate_censor','p_diagnostic'],sort=False):
    pivot=g.pivot(index='rep',columns='method',values=[
        'deployed_wrong_pct_true_comparable','mean_oracle_q1_regret_all_comparable',
        'fp_finite_arm_n','fn_unreachable_arm_n','true_twoarm_unresolved_n'])
    assert pivot.shape[0]==32
    for method in ['gated_direct','gated_projected','joint','joint_confirmed']:
        for field in ['deployed_wrong_pct_true_comparable','mean_oracle_q1_regret_all_comparable','fp_finite_arm_n','fn_unreachable_arm_n','true_twoarm_unresolved_n']:
            diff=(pivot[(field,method)]-pivot[(field,'direct')]).astype(float)
            diff=diff[np.isfinite(diff)]
            if not len(diff):continue
            m=float(diff.mean()); se=float(diff.std(ddof=1)/np.sqrt(len(diff)))
            res.append({'scenario':sc,'rate_censor':rate,'p_diagnostic':p,'method':method,'contrast':'method-minus-direct',
                        'metric':field,'n_replicates':len(diff),'mean_paired_difference':m,
                        'mcse':se,'ci95_mc_lower':m-tcrit*se,'ci95_mc_upper':m+tcrit*se})
pd.DataFrame(res).to_csv(indir/'n2_3_paired_mc.csv',index=False)
print('PASS N2-3 summary and paired MC statistics')
