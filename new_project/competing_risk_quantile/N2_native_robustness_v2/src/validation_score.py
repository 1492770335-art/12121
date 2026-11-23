#!/usr/bin/env python3
"""Train-only censored proper check-score for cause-CIF hitting times.

Loss is IPCW pinball for Y_j=min(T if J=j else infinity,L).
Censor survival G is KM estimated using 75% fitting subset only.
Absolutely no oracle test information is used in parameter selection.
"""
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd

P={'q1':(.06,.12,.18,.24),'qall':(.15,.25,.35,.45)}
L=3.

def km_censor(fit):
    obs=fit[['ftime','fstatus']].sort_values('ftime')
    times=obs.ftime.to_numpy(float)
    cens=(obs.fstatus.to_numpy(int)==0)
    uniq, idx, counts=np.unique(times, return_index=True,return_counts=True)
    nrisk=len(times)-idx
    dcens=np.add.reduceat(cens.astype(int),idx)
    surv=np.cumprod(1.-dcens/nrisk)
    def get(t):
        t=np.asarray(t,dtype=float)
        ind=np.searchsorted(uniq,t,side='right')-1
        return np.where(ind>=0,surv[np.clip(ind,0,len(surv)-1)],1.)
    return get

def score(frame,pred):
    if 'is_validation' not in frame.columns:raise ValueError('No train-only split')
    fit=frame.loc[frame.is_validation==0]
    valid=frame.loc[frame.is_validation==1]
    if len(fit)==0 or len(valid)==0:raise ValueError('Empty split')
    get_g=km_censor(fit)
    val=valid[['patient_id','ftime','fstatus']]
    if pred.duplicated(['patient_id','endpoint','p']).any():raise ValueError('duplicate predictions')
    if not pred[['endpoint','p']].drop_duplicates().shape[0]==8:raise ValueError('Incomplete endpoint p grid')
    merged=pred.merge(val,on='patient_id',validate='many_to_one')
    if len(merged)!=len(valid)*8:raise ValueError('missing patient p predictions')
    X=merged.ftime.to_numpy(float)
    J=merged.fstatus.to_numpy(int)
    p=merged.p.to_numpy(float)
    y=np.full(len(merged),L)
    target=merged.endpoint.to_numpy(str)
    event_before=(X<L)&(J!=0)
    target_event=(J==1)&(target=='q1') | (J!=0)&(target=='qall')
    y[event_before&target_event]=X[event_before&target_event]
    known=(X>=L)|event_before
    w=1./np.maximum(get_g(np.minimum(X,L)),1e-7)
    predtime=merged.pred_q.to_numpy(float)
    predtime=np.where(np.isfinite(predtime),np.clip(predtime,0,L),L)
    u=y-predtime
    loss=w * np.where(u>=0,p*u,(p-1)*u)
    loss[~known]=0.
    values=[]
    for end,plist in P.items():
        for pp in plist:
            sel=(target==end)&(np.abs(p-pp)<1e-8)
            denom=np.sum(w[sel&known])
            if denom<=0:raise ValueError('no identifiable validation pseudo-time labels')
            values.append(float(loss[sel].sum()/denom/L))
    return float(np.mean(values)),values


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--train',type=Path,required=True)
    ap.add_argument('--pred',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    val,values=score(pd.read_csv(a.train),pd.read_csv(a.pred))
    a.out.write_text(json.dumps({'validation_loss':val,'per_endpoint_p':values},indent=2)+'\n')
    print('VALIDATION',val)

if __name__=='__main__':main()
