from pathlib import Path
import numpy as np, pandas as pd, json
D=Path(__file__).parent/'results'
f=pd.read_csv(D/'n2_replicate_results.csv')
ids=['scenario','rate_censor','p_diagnostic','rep']
cols=['q1_mae_cap','qall_mae_cap','q1_rank_wrong_pct','q1_rank_unresolved_pct','q1_est_unreachable_pct','qall_est_unreachable_pct','q1_below_qall_pct']
wide=f.pivot(index=ids,columns='method',values=cols)
flat=pd.DataFrame(index=wide.index)
for metric in cols:flat[metric+'_joint_minus_direct']=wide[(metric,'joint')]-wide[(metric,'direct')]
flat=flat.reset_index()
rows=[]
for keys,g in flat.groupby(ids[:-1]):
 row=dict(zip(ids[:-1],keys)); row['reps']=len(g)
 for c in cols:
  x=g[c+'_joint_minus_direct'].dropna();
  row[c+'_difference_mean']=x.mean()
  row[c+'_difference_mcse']=x.std(ddof=1)/np.sqrt(len(x)) if len(x)>1 else np.nan
  row[c+'_difference_ci_low']=x.mean()-1.96*x.std(ddof=1)/np.sqrt(len(x)) if len(x)>1 else np.nan
  row[c+'_difference_ci_high']=x.mean()+1.96*x.std(ddof=1)/np.sqrt(len(x)) if len(x)>1 else np.nan
 rows.append(row)
pd.DataFrame(rows).sort_values(ids[:-1]).to_csv(D/'n2_paired_differences.csv',index=False)
q={
 'total_training_replications':int(len(f)/(2*3)),
 'rows_expected':int(3*2*32*3*2),
 'rows_found':int(len(f)),
 'all_joint_models_converged':bool(f.joint_converged.all()),
 'all_direct_solvers_success_status':bool((f.direct_fail_count==0).all()),
 'direct_moment_norm_max':float(f.direct_max_moment_residual.max()),
 'direct_moment_norm_over_0p01_fraction':float((f[f.method=='direct'].direct_max_moment_residual>.01).mean()),
 'no_invalid_class_probabilities_by_projection':True,
 'true_joint_strict_interior_min_pct':float(f.oracle_joint_interior_pct.min()),
 'true_joint_strict_interior_mean_pct':float(f.oracle_joint_interior_pct.mean()),
 'all_comparison_pairs_matched':bool(len(flat)==3*2*32*3),
 'mean_direct_incoherent_q1_below_qall_pct':float(f[f.method=='direct'].q1_below_qall_pct.mean()),
 'mean_joint_incoherent_q1_below_qall_pct':float(f[f.method=='joint'].q1_below_qall_pct.mean()),
 'note':'Direct moment solver success is not proof moment root was found: non-zero moments remain and are audited; global model cannot detect true unreachable p.'
}
(D/'n2_quality_report.json').write_text(json.dumps(q,ensure_ascii=False,indent=2))
print(json.dumps(q,indent=2))
r=pd.DataFrame(rows)
print('\nMain checkpoint: p=.18, paired JOINT minus DIRECT:')
for _,row in r[r.p_diagnostic==.18].iterrows():
 print(row['scenario'],row['rate_censor'], 'Q1 MAE diff', round(row['q1_mae_cap_difference_mean'],4),'95CI', [round(row['q1_mae_cap_difference_ci_low'],4),round(row['q1_mae_cap_difference_ci_high'],4)], 'rank wrong diff (pp)',round(row['q1_rank_wrong_pct_difference_mean'],2))