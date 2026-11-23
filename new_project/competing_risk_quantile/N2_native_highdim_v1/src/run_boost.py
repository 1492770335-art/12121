#!/usr/bin/env python3
"""Native hazardous SurvivalBoost: two train-only candidate models and final refit."""
from __future__ import annotations
import argparse, importlib.metadata, json, time, traceback
from pathlib import Path
import numpy as np
import pandas as pd
from validation_score import score, P, L

MECHS=('hd_correct','hd_nonlinear','hd_crossing')
NTRAIN=(500,1000)
NREPS=4
TIME=np.linspace(0,L,301)
SEED=2026112371


def inverse(cifs:np.ndarray,p:float)->np.ndarray:
    """Inverse on fixed t-grid. Unknown/out-of-window gets NaN, no cap as true Q."""
    if cifs.ndim!=2 or cifs.shape[1]!=len(TIME):raise ValueError('bad CIF shape')
    out=np.full(len(cifs),np.nan)
    for i,row in enumerate(cifs):
        if not np.isfinite(row).all() or row.min() < -1e-6 or row.max()>1+1e-6:continue
        indices=np.flatnonzero(row>=p)
        if not len(indices):continue
        k=int(indices[0])
        if k==0:q=0.
        else:
            ylo,yhi=row[k-1],row[k]
            q=float(TIME[k] if yhi<=ylo else TIME[k-1]+(p-ylo)*(TIME[k]-TIME[k-1])/(yhi-ylo))
        if np.isfinite(q) and 0<=q<L-1e-12:out[i]=q
    return out


def extract(cifs:np.ndarray)->dict:
    if cifs.ndim!=3 or cifs.shape[1:]!=(3,len(TIME)):
        raise ValueError(f'incorrect predicted survival states shape {cifs.shape}')
    if not np.isfinite(cifs).all() or np.abs(cifs.sum(axis=1)-1).max()>.002:
        raise ValueError('invalid CIF normalization')
    if (cifs<-0.002).any() or (cifs>1.002).any():raise ValueError('invalid probabilities')
    return {'q1':cifs[:,1,:],'qall':cifs[:,1,:]+cifs[:,2,:]}


def predict_rows(model,feature_frame,identifiers):
    cifs=extract(model.predict_cumulative_incidence(feature_frame,times=TIME))
    rows=[]
    for endpoint,probs in P.items():
        curves=cifs[endpoint]
        for p in probs:
            rows.append(pd.DataFrame({'patient_id':identifiers.to_numpy(int),
                'endpoint':endpoint,'p':p,'pred_q':inverse(curves,p)}))
    return pd.concat(rows,ignore_index=True),cifs


def make_model(niter,seed):
    from hazardous import SurvivalBoost
    return SurvivalBoost(n_iter=niter,learning_rate=.05,max_leaf_nodes=7,
        min_samples_leaf=20,show_progressbar=False,
        ipcw_strategy='kaplan-meier',random_state=seed)


def run_one(train,truth,mech,n,rep,censor):
    feature=['a']+[f'z{j}' for j in range(1,9)]+['az1','az3']
    fit=train[train.is_validation==0]
    val=train[train.is_validation==1]
    seeds=SEED+MECHS.index(mech)*10000+n*7+rep*10+censor
    status=[]
    for k,niter in enumerate((40,100)):
        start=time.monotonic()
        try:
            model=make_model(niter,seeds+k)
            model.fit(fit[feature],{'event':fit.fstatus.to_numpy(int), 'duration':fit.ftime.to_numpy(float)})
            preds,_=predict_rows(model,val[feature],val.patient_id)
            loss,segments=score(train,preds)
            status.append({'candidate':niter,'validation_loss':loss,'seconds':time.monotonic()-start,'error':''})
        except Exception as exc:
            status.append({'candidate':niter,'validation_loss':None,'seconds':time.monotonic()-start,
                           'error':f'{type(exc).__name__}: {exc}'})
    finite=[q for q in status if q['validation_loss'] is not None and np.isfinite(q['validation_loss'])]
    if not finite:raise RuntimeError('Both native SurvivalBoost candidates failed: '+str(status))
    best=min(finite,key=lambda q:(q['validation_loss'],q['candidate']))
    t0=time.monotonic()
    m=make_model(best['candidate'],seeds+100)
    m.fit(train[feature],{'event':train.fstatus.to_numpy(int),'duration':train.ftime.to_numpy(float)})
    _,curves=predict_rows(m,truth[feature],truth.patient_id)
    # Two treatment rows per patient; preserve row order when attaching (patient_id,a).
    pred_by=[]
    for endpoint,probs in P.items():
        curve=curves[endpoint]
        for p in probs:
            qq=inverse(curve,p)
            pred_by.append(pd.DataFrame({'method':'SurvivalBoost','mechanism':mech,'n_train':n,'replicate':rep,
                'censor_target':censor,'endpoint':endpoint,'p':p,
                'patient_id':truth.patient_id.to_numpy(int),'a':truth.a.to_numpy(int),
                'true_q':truth[f'true_{endpoint}_p{p:.2f}'].to_numpy(float),'pred_q':qq}))
    output=pd.concat(pred_by,ignore_index=True)
    audit={'method':'SurvivalBoost','mechanism':mech,'n_train':n,'replicate':rep,'censor_target':censor,
          'selected_candidate':best['candidate'],'selected_val_loss':best['validation_loss'],
          'candidates':status,'seconds_full_fit':time.monotonic()-t0,
          'n_nonmonotone_cif1':int((np.diff(curves['q1'],axis=1)<-1e-5).any(axis=1).sum()),
          'n_nonmonotone_cifall':int((np.diff(curves['qall'],axis=1)<-1e-5).any(axis=1).sum()),
          'status':'ok'}
    return output,audit


def main():
    a=argparse.ArgumentParser()
    a.add_argument('--data',type=Path,required=True)
    a.add_argument('--output',type=Path,required=True)
    a.add_argument('--mechanism',choices=MECHS,required=True)
    a.add_argument('--ntrain',type=int,choices=NTRAIN,required=True)
    opt=a.parse_args();opt.output.mkdir(parents=True,exist_ok=True)
    print('HAZARDOUS',importlib.metadata.version('hazardous'),flush=True)
    results=[];audit=[]
    for rep in range(NREPS):
        truth=pd.read_csv(opt.data/f'{opt.mechanism}_n{opt.ntrain}_r{rep:02d}_oracle_test.csv')
        for cen in (20,45):
            train=pd.read_csv(opt.data/f'{opt.mechanism}_n{opt.ntrain}_r{rep:02d}_c{cen}_train.csv')
            try:
                pred,rec=run_one(train,truth,opt.mechanism,opt.ntrain,rep,cen)
                results.append(pred);audit.append(rec)
                print('PASS',opt.mechanism,opt.ntrain,rep,cen,'n_iter',rec['selected_candidate'],
                      'val',round(rec['selected_val_loss'],6),flush=True)
            except Exception as exc:
                msg=f'{type(exc).__name__}: {exc}'
                audit.append({'method':'SurvivalBoost','mechanism':opt.mechanism,'n_train':opt.ntrain,
                    'replicate':rep,'censor_target':cen,'status':'failed','error':msg,'trace':traceback.format_exc()})
                print('FAILED',opt.mechanism,opt.ntrain,rep,cen,msg,flush=True)
    if results:pd.concat(results,ignore_index=True).to_csv(opt.output/'native_python_predictions.csv',index=False)
    (opt.output/'native_python_fit_status.json').write_text(json.dumps(audit,indent=2,allow_nan=False)+'\n')
    (opt.output/'native_python_versions.json').write_text(json.dumps({x:importlib.metadata.version(x) for x in
            ['numpy','pandas','scipy','scikit-learn','hazardous']},indent=2)+'\n')
    if len(results)!=NREPS*2:raise SystemExit(f'Incomplete Python native fits {len(results)}/{NREPS*2}')

if __name__=='__main__':main()
