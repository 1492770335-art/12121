#!/usr/bin/env python3
"""Native SurvivalBoost; per-patient quantile predictions for two endpoints."""
from __future__ import annotations
from pathlib import Path
import argparse, json, importlib.metadata, traceback, time
import numpy as np
import pandas as pd

MECHS=('aligned','cause_tradeoff','time_varying')
P1=(.06,.12,.18,.24)
PALL=(.15,.25,.35,.45)
TIME=np.linspace(0,3,301)


def first_hitting(values:np.ndarray,p:float)->float:
    if not np.isfinite(values).all() or np.min(values)<-1e-6 or np.max(values)>1+1e-6:
        return np.nan
    indices=np.flatnonzero(values >= p)
    if not len(indices):return np.nan
    k=int(indices[0])
    if k==0:return 0.
    lo,hi=float(values[k-1]),float(values[k])
    if hi<=lo:return float(TIME[k])
    return float(TIME[k-1]+(p-lo)*(TIME[k]-TIME[k-1])/(hi-lo))


def as_rows(mech,rep,cens,truth,endpoint,p,estimated):
    true=truth[f'true_{endpoint}_p{p:.2f}'].to_numpy(dtype=float)
    return pd.DataFrame({
        'method':'SurvivalBoost','mechanism':mech,'replicate':rep,
        'censor_target':cens,'endpoint':endpoint,'p':p,
        'patient_id':truth['patient_id'].to_numpy(int),'a':truth['a'].to_numpy(int),
        'true_q':true,'pred_q':estimated,
        'true_reachable':np.isfinite(true).astype(int),
        'pred_reachable':np.isfinite(estimated).astype(int)})


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--data',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    from hazardous import SurvivalBoost
    print('hazardous version',importlib.metadata.version('hazardous'),flush=True)
    rs=[];fits=[]
    for mi,mech in enumerate(MECHS):
        for rep in range(4):
            truth=pd.read_csv(a.data/f'{mech}_r{rep:02d}_oracle_test.csv')
            Xtest=truth[['a','z1','z2','az1']]
            for ci,cens in enumerate((20,45)):
                train=pd.read_csv(a.data/f'{mech}_r{rep:02d}_c{cens}_train.csv')
                X=train[['a','z1','z2','az1']]
                y={'event':train['fstatus'].to_numpy(int),
                   'duration':train['ftime'].to_numpy(float)}
                start=time.monotonic()
                entry={'method':'SurvivalBoost','mechanism':mech,'replicate':rep,
                       'censor_target':cens,'status':'failed','error':''}
                try:
                    model=SurvivalBoost(n_iter=55,learning_rate=.05,max_leaf_nodes=7,
                        min_samples_leaf=20,show_progressbar=False,
                        ipcw_strategy='kaplan-meier',random_state=2026112304+mi*100+rep*2+ci)
                    model.fit(X,y)
                    pred=model.predict_cumulative_incidence(Xtest,times=TIME)
                    if pred.shape!=(len(truth),3,len(TIME)):
                        raise ValueError(f'wrong predicted CIF shape={pred.shape}')
                    if not np.isfinite(pred).all():
                        raise ValueError('nonfinite predictions')
                    if np.max(abs(pred.sum(axis=1)-1))>2e-3:
                        raise ValueError('CIF does not normalize to 1')
                    cif1=pred[:,1,:]
                    cifall=pred[:,1,:]+pred[:,2,:]
                    if cifall.max()>1.002 or cifall.min()<-0.002:
                        raise ValueError('invalid overall CIF bounds')
                    for endpoint,probs,curve in [('q1',P1,cif1),('qall',PALL,cifall)]:
                        for p in probs:
                            q=np.array([first_hitting(row,p) for row in curve])
                            rs.append(as_rows(mech,rep,cens,truth,endpoint,p,q))
                    entry.update(status='ok',seconds=round(time.monotonic()-start,3),
                         cause1_nonmonotone_rows=int((np.diff(cif1,axis=1)<-1e-5).any(axis=1).sum()),
                         overall_nonmonotone_rows=int((np.diff(cifall,axis=1)<-1e-5).any(axis=1).sum()))
                except Exception as e:
                    entry['error']=repr(e)
                    entry['traceback']=traceback.format_exc()
                fits.append(entry)
                print('FIT',entry['method'],mech,rep,cens,entry['status'],entry.get('seconds',''),entry['error'][:200],flush=True)
    if rs:
        pd.concat(rs,ignore_index=True).to_csv(a.output/'native_python_predictions.csv',index=False,float_format='%.10f')
    (a.output/'native_python_fit_status.json').write_text(json.dumps(fits,indent=2)+'\n')
    (a.output/'native_python_versions.json').write_text(json.dumps({
        m:importlib.metadata.version(m) for m in ['hazardous','numpy','pandas','scipy','scikit-learn']},indent=2)+'\n')
    print('SUCCESSFUL FITS:',sum(x['status']=='ok' for x in fits),'/',len(fits),flush=True)
    if not rs:raise SystemExit('no successful SurvivalBoost fit')

if __name__=='__main__':main()
