#!/usr/bin/env python3
"""Predeclared N2-T2 analysis: p-macro error, independent-training-replicate MCSE.

Not a test of universal superiority. One training repetition is the MC unit;
patient-treatment-p records are used to form a within-fit MAE, never treated
as independent Monte Carlo replicates.
"""
from __future__ import annotations
from pathlib import Path
import argparse, json
import numpy as np
import pandas as pd
from scipy.stats import t as student_t

P_PER_ENDPOINT=4
METHODS=('PengFine','CRRSF','SurvivalBoost')

def collapse_p(df, keys, value):
    rows=[]
    for key,g in df.groupby(keys,dropna=False,sort=True):
        vals=g[value].to_numpy(float)
        good=len(g)==P_PER_ENDPOINT and g.p.nunique()==P_PER_ENDPOINT and np.isfinite(vals).all()
        rows.append(dict(zip(keys,key), valid_complete_p=bool(good), p_count=int(g.p.nunique()),
                         macro_value=float(vals.mean()) if good else np.nan,
                         total_common=int(g.n_common.min()) if 'n_common' in g else 0))
    return pd.DataFrame(rows)

def t_summary(df, keys):
    rows=[]
    for key,g in df.groupby(keys,dropna=False,sort=True):
        d=g.macro_value.dropna().to_numpy(float)
        n=len(d)
        center=float(d.mean()) if n else np.nan
        sd=float(d.std(ddof=1)) if n>1 else np.nan
        se=float(sd/np.sqrt(n)) if n>1 else np.nan
        crit=float(student_t.ppf(.975,n-1)) if n>1 else np.nan
        rows.append(dict(zip(keys,key),reps_scored=n,reps_missing=int(len(g)-n),
                         mean=center,sd=sd,mcse=se,
                         ci95_low=center-crit*se if n>1 else np.nan,
                         ci95_high=center+crit*se if n>1 else np.nan,
                         note='Exploratory MC t interval, independent training repeats'))
    return pd.DataFrame(rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--results',type=Path,required=True)
    a=ap.parse_args();d=a.results
    pair=pd.read_csv(d/'replicate_level_pairwise.csv')
    maes=pd.read_csv(d/'replicate_level_mae.csv')
    pairkeys=['mechanism','n_train','censor_target','replicate','endpoint','method_a','method_b']
    maekeys=['mechanism','n_train','censor_target','replicate','endpoint','method']
    pm=collapse_p(pair,pairkeys,'delta_mae_common')
    mm=collapse_p(maes,maekeys,'mae_common')
    pairs=t_summary(pm,[x for x in pairkeys if x!='replicate'])
    methods=t_summary(mm,[x for x in maekeys if x!='replicate'])
    pm.to_csv(d/'macro_replicate_pairwise.csv',index=False,float_format='%.9f')
    mm.to_csv(d/'macro_replicate_mae.csv',index=False,float_format='%.9f')
    pairs.to_csv(d/'paired_t_intervals.csv',index=False,float_format='%.9f')
    methods.to_csv(d/'method_mc_intervals.csv',index=False,float_format='%.9f')
    if len(pm)==0 or len(mm)==0:raise ValueError('no native methods available to compare')
    if (pm.groupby([x for x in pairkeys if x!='replicate']).size()>12).any():raise ValueError('more than 12 MC repeats')
    cfg={'n_paired_repetition_cells':int(len(pm)),'n_method_repetition_cells':int(len(mm)),
         'n_missing_macro_pairwise':int(pm.macro_value.isna().sum()),
         'n_missing_macro_mae':int(mm.macro_value.isna().sum()),
         'primary_mechanisms':['time_varying','nonlinear_interaction'],
         'correct_spec_control':'logquantile_correct',
         'summary':'All four diagnostic p weights equal; repeats are MC units; paired t intervals exploratory.'}
    (d/'aggregate_mc_audit.json').write_text(json.dumps(cfg,indent=2)+'\n')
    print('PASS 12-replicate p-macro intervals',cfg)
if __name__=='__main__':main()