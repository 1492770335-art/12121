#!/usr/bin/env python3
"""Audit every native model fit from GitHub Actions shard artifacts."""
import argparse,json
from pathlib import Path
import pandas as pd

p=argparse.ArgumentParser()
p.add_argument('--r-root',type=Path,required=True)
p.add_argument('--py-root',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
rows=[]
for file in a.r_root.rglob('native_r_fit_status.csv'):
    df=pd.read_csv(file)
    for row in df.to_dict('records'):
        rows.append({'source_file':str(file),'method':row['method'],'mechanism':row['mechanism'],
            'n_train':row['n_train'],'replicate':row['replicate'],
            'censor_target':row['censor_target'],'status':row['status'],
            'selected_candidate':row.get('selected_candidate'),
            'validation_loss':row.get('selected_validation_loss'),
            'seconds':row.get('elapsed_seconds'),'error':row.get('error'),
            'candidate_details':row.get('candidate_details')})
for file in a.py_root.rglob('native_python_fit_status.json'):
    for row in json.loads(file.read_text()):
        rows.append({'source_file':str(file),'method':row['method'],'mechanism':row['mechanism'],
            'n_train':row['n_train'],'replicate':row['replicate'],
            'censor_target':row['censor_target'],'status':row['status'],
            'selected_candidate':row.get('selected_candidate'),
            'validation_loss':row.get('selected_val_loss'),
            'seconds':row.get('seconds_full_fit'),
            'error':row.get('error',''),
            'candidate_details':json.dumps(row.get('candidates',[]),ensure_ascii=False)})
frame=pd.DataFrame(rows)
key=['mechanism','n_train','replicate','censor_target','method']
if frame.duplicated(key).any():raise ValueError('duplicate fit')
if len(frame)!=5*2*4*2*3:raise ValueError(f'wrong native fit count {len(frame)} expected 240')
frame=frame.sort_values(key)
frame.to_csv(a.output/'native_fit_selection.csv',index=False)
count=frame.groupby(['method','status'],dropna=False).size().rename('n').reset_index().to_dict('records')
selection=frame.groupby(['method','selected_candidate'],dropna=False).size().rename('n').reset_index().to_dict('records')
report={'n_total_native_full_training_fits':len(frame),'counts_by_status':count,
        'train_only_candidate_selection_counts':selection,
        'failed':frame[frame.status!='ok'][key+['error']].fillna('').to_dict('records'),
        'explanation':'Native-model failures are retained, never imputed; these are final full-training fits after train-only validation.'}
(a.output/'native_fit_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print('NATIVE AUDIT',len(frame),'failed',len(report['failed']))
