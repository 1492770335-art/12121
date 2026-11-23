"""Common cause-1 CIF inverse and conditional quantile scoring."""
import numpy as np
import pandas as pd
P_VALUES=[.06,.12,.18,.24]
L=3.

def invert_grid(t,cif,p):
    t=np.asarray(t,float);cif=np.asarray(cif,float)
    if t.ndim!=1 or cif.ndim!=1 or len(t)!=len(cif):
        raise ValueError("time/cif dimension mismatch")
    ix=np.where((t<=L+1e-12)&(cif>=p))[0]
    if not len(ix):return float('nan')
    j=int(ix[0])
    if j==0:return float(t[0])
    if cif[j]==cif[j-1]:return float(t[j])
    return float(t[j-1]+(p-cif[j-1])/(cif[j]-cif[j-1])*(t[j]-t[j-1]))

def summarize(method,mechanism,censor_percent,truth,pred_cif,t,run_note=""):
    truth=truth.reset_index(drop=True)
    n=len(truth)
    pred_cif=np.asarray(pred_cif,float)
    assert pred_cif.shape==(n,len(t)),(pred_cif.shape,n,len(t))
    rows=[]
    for p in P_VALUES:
        true=truth[f'true_q1_p{p:.2f}'].to_numpy(float)
        pred=np.array([invert_grid(t,pred_cif[i],p) for i in range(n)])
        tr=np.isfinite(true);pr=np.isfinite(pred);both=tr&pr
        rows.append(dict(method=method,mechanism=mechanism,censor_target=censor_percent,
                         p=p,n_eval=n,n_true_reachable=int(tr.sum()),n_pred_reachable=int(pr.sum()),
                         n_both=int(both.sum()),mae=float(np.mean(np.abs(true[both]-pred[both]))) if both.any() else np.nan,
                         fp_unreachable=int((~tr&pr).sum()),fn_missing=int((tr&~pr).sum()),
                         predicted_reach_pct=float(100*pr.mean()),scorable_pct=float(100*both.mean()),
                         cdf_nonmonotone_pct=float(100*np.mean(np.any(np.diff(pred_cif,axis=1)<-1e-5,axis=1))),
                         notes=run_note))
    return pd.DataFrame(rows)
