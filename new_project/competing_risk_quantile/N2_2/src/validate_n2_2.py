#!/usr/bin/env python3
"""Cross-check N2-2 raw rows against original N2 prefix and structural invariants."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

THIS=Path(__file__).resolve().parents[1]
RAW=THIS/'results'/'n2_2_replications.csv'
BASELINE=THIS.parents[0] / 'N2_pilot' / 'results' / 'n2_replicate_results.csv'
if not BASELINE.exists():
    BASELINE=Path('/mnt/data/N2_new_project_research/results/n2_replicate_results.csv')


def run():
    raw=pd.read_csv(RAW)
    old=pd.read_csv(BASELINE)
    keys=['scenario','rate_censor','rep','p_diagnostic','method']
    merged=raw.merge(old,on=keys,how='left',validate='one_to_one',suffixes=('_new','_old'))
    assert len(merged)==len(raw)==288
    assert merged['q1_below_qall_pct'].notna().all()
    diff_coherence=float(np.max(np.abs(merged['incoherent_q1_less_qall_pct']-merged['q1_below_qall_pct'])))
    diff_censor=float(np.max(np.abs(merged['realized_censor_pct_new']-merged['realized_censor_pct_old'])))
    assert diff_coherence<1e-8 and diff_censor<1e-7
    assert raw[raw.method=='joint']['incoherent_q1_less_qall_n'].sum()==0
    assert raw[raw.method=='direct']['fn_unreached_arm_n'].sum()==0
    assert raw[raw.method=='direct']['estimated_reach_arm_n'].eq(2000).all()
    assert raw['joint_converged'].all()
    assert (raw[['fp_finite_arm_n','fn_unreached_arm_n','incoherent_q1_less_qall_n']].values>=0).all()
    assert np.all(raw['oracle_two_arm_q1_strict_interior_n'] >= raw['true_comparison_resolved_n']+raw['true_comparison_unresolved_n'])
    assert np.all(raw['oracle_two_arm_q1_strict_interior_n'] == raw['true_comparison_resolved_n']+raw['true_comparison_unresolved_n'])
    assert np.all(raw['wrong_recommendation_n']<=raw['true_comparison_resolved_n'])
    q=dict(pass_=True,raw_diagnostic_rows=len(raw),n_fitted_sample_replays=48,
           total_patient_test_replays=48000,three_p_values_are_repeated_on_same_patients=True,
           max_abs_coherence_rate_difference_vs_original_n2=diff_coherence,
           max_abs_realized_censor_rate_difference_vs_original_n2=diff_censor,
           direct_incoherence_total=int(raw[raw.method=='direct']['incoherent_q1_less_qall_n'].sum()),
           direct_incoherence_arm_predict_count=int(raw[raw.method=='direct']['eval_arm_n'].sum()),
           joint_incoherence_total=int(raw[raw.method=='joint']['incoherent_q1_less_qall_n'].sum()),
           method='Replayed first eight frozen seed streams of the original N2 pilot; no new independent trial',
           note='The three p diagnostics are correlated repeated evaluations on the same test patients; do not treat 288 rows as independent model fits')
    (THIS/'results'/'n2_2_validation.json').write_text(json.dumps(q,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print('PASS N2-2 matched original N2 and structural checks; max differences',diff_coherence,diff_censor)

if __name__=='__main__':run()
