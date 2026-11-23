#!/usr/bin/env python3
"""Combine per-shard native artifacts; enforce exact expected sharded coverage."""
import argparse,json
from pathlib import Path
import pandas as pd

p=argparse.ArgumentParser();p.add_argument('--r-root',type=Path,required=True);p.add_argument('--py-root',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
expected={(m,n) for m in ('aligned','cause_tradeoff','time_varying','logquantile_correct') for n in (500,1000,2000)}
for root,method,filename in [(a.r_root,'r','native_r_predictions.csv'),(a.py_root,'python','native_python_predictions.csv')]:
    paths=list(root.rglob(filename));seen=set();frames=[]
    for file in paths:
        frame=pd.read_csv(file)
        sh=set(zip(frame.mechanism,frame.n_train))
        if len(sh)!=1:raise ValueError(f'inconsistent shard in {file} {sh}')
        if seen.intersection(sh):raise ValueError(f'duplicate shard {sh}')
        seen|=sh;frames.append(frame)
    if seen!=expected:raise ValueError(f'{method} missing or extra shards: missing={expected-seen}, extra={seen-expected}')
    combined=pd.concat(frames,ignore_index=True)
    if method=='r':
        m=set(combined.method.unique())
        if m!={'PengFine','CRRSF'}:raise ValueError(f'R native methods missing: {m}')
    else:
        if set(combined.method.unique())!={'SurvivalBoost'}:raise ValueError('boost missing')
    combined.to_csv(a.out/f'{method}_predictions.csv',index=False,float_format='%.10f')
    print('PASS native',method,'shards',len(paths),'prediction rows',len(combined),flush=True)
