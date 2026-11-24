"""Truth-only scoring of native R policies, exactly matching Q-Q pilot Oracle."""
import sys,runpy
from pathlib import Path
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parent
REPS=int(sys.argv[1]) if len(sys.argv)>1 else 2
sys.argv=[sys.argv[0],str(REPS)]
hazards=runpy.run_path(str(ROOT/"generate.py"),run_name="__hazard_import__")["hazards"]
OUT=ROOT/"results";OUT.mkdir(exist_ok=True)
L=3.;PALL=.50;P1=.10
def truth(h):
    n=h.shape[0];s=np.ones((n,2));cif=np.zeros((n,2,2))
    qa=np.full((n,2),L);q1=qa.copy();rmet=np.zeros((n,2))
    for k in range(2):
        lam=h[:,:,:,k];total=lam.sum(axis=2);width=1. if k==0 else 2.
        mass=-np.expm1(-total*width);ss=s*np.exp(-total*width)
        new=cif+(s*mass/total)[...,None]*lam
        for out,prev,after,frac,th in [
            (qa,1-s,1-ss,np.ones_like(s),PALL),
            (q1,cif[:,:,0],new[:,:,0],lam[:,:,0]/total,P1)
        ]:
            hit=(out==L)&(prev<th)&(after>=th)
            u=(th-prev[hit])/(s[hit]*frac[hit])
            out[hit]=k-np.log1p(-u)/total[hit]
        rmet+=s*mass/total;s=ss;cif=new
    if np.max(abs(s+cif.sum(axis=2)-1))>5e-14:raise ValueError("probability identity violation")
    return dict(qall=qa,q1=q1,rmet=rmet,f1=cif[:,:,0],f2=cif[:,:,1])
rows=[];miss=[]
for rep in range(1,REPS+1):
  for m in ("M1","M2"):
    test=pd.read_csv(ROOT/"data"/f"test_{m}_r{rep}.csv")
    z=test[["Z1","Z2"]].to_numpy()
    v=truth(hazards(z,m))
    for method in ("PMCR","DTR","RSF","ITR"):
        p=OUT/f"pred_{method}_{m}_r{rep}.csv"
        if not p.is_file():
            miss.append((m,rep,method));continue
        a=pd.read_csv(p)
        if len(a)!=len(test) or not np.array_equal(a["id"].to_numpy(),test["id"].to_numpy()):
            raise ValueError("prediction ID misalignment "+str(p))
        d=a["action"].to_numpy(dtype=int)
        if not np.all(np.isin(d,[0,1])):raise ValueError("nonbinary treatments "+str(p))
        ix=np.arange(len(d))
        row=dict(mechanism=m,rep=rep,method=method,treat1_pct=100*float(d.mean()))
        for name,factor,outname in (("qall",12,"qall_month"),("q1",12,"q1_month"),("rmet",12,"rmet_month"),("f1",100,"f1_pct"),("f2",100,"f2_pct")):
            row[outname]=factor*float(v[name][ix,d].mean())
        rows.append(row)
df=pd.DataFrame(rows)
if len(df):
    df.to_csv(OUT/"native_scored_replicates.csv",index=False)
    names=["treat1_pct","qall_month","q1_month","rmet_month","f1_pct","f2_pct"]
    summary=df.groupby(["mechanism","method"])[names].agg(["mean","std","count"]).reset_index()
    summary.columns=["_".join(i).strip("_") if isinstance(i,tuple) else i for i in summary.columns]
    summary.to_csv(OUT/"native_scored_summary.csv",index=False)
    print(summary.to_string(index=False))
(OUT/"missing_predictions.csv").write_text("mechanism,rep,method\n"+"".join(",".join(map(str,row))+"\n" for row in miss),encoding="utf8")
print("VALID REPS",len(df),"MISSING",len(miss))
