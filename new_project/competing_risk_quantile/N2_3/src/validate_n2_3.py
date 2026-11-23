#!/usr/bin/env python3
"""Independent repeat-level N2-2 and N2-3 baseline audit."""
from pathlib import Path
import json,sys
import pandas as pd
import numpy as np

base=Path(__file__).resolve().parents[1]
new=pd.read_csv(base/'results32'/'n2_3_replications.csv')
oldpath=Path('/mnt/data/n2_2_study/results/n2_2_replications.csv')
if not oldpath.is_file():
    oldpath=Path(__file__).resolve().parents[1]/'N2_2'/'results'/'n2_2_replications.csv'
if not oldpath.is_file():
    raise FileNotFoundError('need frozen N2-2 replicate CSV to certify same initial 8 seeds')
old=pd.read_csv(oldpath)
compare=new[(new.rep<=8)&new.method.isin(['direct','joint'])]
keys=['scenario','rate_censor','rep','p_diagnostic','method']
merged=compare.merge(old,on=keys,suffixes=('','_old'),validate='one_to_one')
assert len(merged)==len(compare)==len(old)==288
comparisons={
    'fp_finite_arm_n':'fp_finite_arm_n_old',
    'fn_unreachable_arm_n':'fn_unreached_arm_n',
    'q1_below_qall_same_p_n':'incoherent_q1_less_qall_n',
    'true_twoarm_comparable_n':'oracle_two_arm_q1_strict_interior_n',
    'true_twoarm_unresolved_n':'true_comparison_unresolved_n',
    'wrong_on_resolved_n':'wrong_recommendation_n',
}
max_diff={}
for a,b in comparisons.items():
    diff=np.max(np.abs(merged[a].astype(float)-merged[b].astype(float)))
    assert diff==0,(a,b,diff)
    max_diff[a]=float(diff)
assert new.shape[0]==32*3*2*3*5
assert new.groupby(keys[:-1]).size().eq(5).all()
assert new.joint_converged.all() and new.endpoint_converged.all()
for g in new.groupby(['scenario','rate_censor','rep','p_diagnostic']):
    subgroup=g[1]
    assert subgroup.true_unreachable_arm_n.nunique()==1
    assert subgroup.true_twoarm_comparable_n.nunique()==1
    assert (subgroup.fp_finite_arm_n>=0).all()
    assert (subgroup.fn_unreachable_arm_n>=0).all()
    assert (subgroup.true_twoarm_unresolved_n<=subgroup.true_twoarm_comparable_n).all()
    assert (subgroup.deployed_wrong_n<=subgroup.true_twoarm_comparable_n).all()
    assert (subgroup[subgroup.method=='gated_projected'].q1_below_qall_same_p_n==0).all()
    assert (subgroup[subgroup.method=='joint'].q1_below_qall_same_p_n==0).all()
results={'pass':True,'n2_3_rows':len(new),'paired_group_count':int(len(new)/5),
         'replayed_n2_2_rows_exact':int(len(merged)), 'metrics_max_abs_diff':max_diff,
         'joint_convergence_all':True,'endpoint_convergence_all':True,
         'warning':'All observations are simulation replicates, not patient clinical evidence.'}
(base/'results32'/'validation.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print('PASS N2-3 row integrity, convergence, exact replay of 288 N2-2 baseline rows')
