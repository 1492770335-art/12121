"""Frozen N2 native pilot. Regenerate right-censored, competing-risk datasets.
Uses N1's analytical generator as mathematical truth, not a Cox estimator.
"""
from pathlib import Path
import importlib.util,json,hashlib
import numpy as np
import pandas as pd
from scipy.optimize import brentq
base=Path(__file__).resolve().parents[2]
p=base/'N1_oracle/src/n1_oracle_study.py'
spec=importlib.util.spec_from_file_location('n1',p)
n1=importlib.util.module_from_spec(spec);spec.loader.exec_module(n1)
SEED=20261123; MECHS=['aligned','cause_tradeoff','time_varying']; P=[.06,.12,.18,.24]
L=3.; SWITCH=1.2;N=400;NTEST=120

def drawz(rng,n):return rng.uniform(-1,1,n),rng.binomial(1,.5,n)
def laplace(c,r):
    a=r[:,:,0].sum(1);b=r[:,:,1].sum(1);z=np.exp(-(a+c)*SWITCH)
    return a/(a+c)*(1-z)+z*b/(b+c)
def simulate(rng,r,c):
    a=r[:,:,0].sum(1);b=r[:,:,1].sum(1);e=rng.exponential(size=len(a))
    early=e<a*SWITCH; T=np.where(early,e/a,SWITCH+(e-a*SWITCH)/b)
    p=np.where(early,r[:,0,0]/a,r[:,0,1]/b)
    J=np.where(rng.uniform(size=len(a))<p,1,2)
    C=rng.exponential(scale=1/c,size=len(a))
    return np.minimum(T,C),np.where(T<=C,J,0)
def digest(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def main(out):
    out.mkdir(parents=True,exist_ok=True)
    manifest={'seed':SEED,'ntrain':N,'ntest':NTEST,'L':L,'switch':SWITCH,'p_grid':P,'scenario':[]}
    for idx,m in enumerate(MECHS):
        rng=np.random.default_rng(SEED+1000+idx);z1,z2=drawz(rng,30000)
        a=rng.integers(0,2,size=len(z1));r=n1.make_rates(z1,z2,m)[np.arange(len(a)),a]
        rngt=np.random.default_rng(SEED+2000+idx);z1,z2=drawz(rngt,NTEST)
        rt=n1.make_rates(z1,z2,m);f,_=n1.cif_at(rt,L)
        t=pd.DataFrame({'patient_id':np.repeat(np.arange(NTEST),2),
          'a':np.tile([0,1],NTEST),'z1':np.repeat(z1,2),'z2':np.repeat(z2,2),
          'az1':np.tile([0,1],NTEST)*np.repeat(z1,2),
          'true_f1_L':f[:,:,0].reshape(-1),'true_f2_L':f[:,:,1].reshape(-1)})
        for p in P:
            t[f'true_q1_p{p:.2f}']=n1.q_exact(rt,p,0).reshape(-1)
            t[f'true_qall_p{p:.2f}']=n1.q_exact(rt,p,'all').reshape(-1)
        truth=out/f'{m}_oracle_test.csv';t.to_csv(truth,index=False,float_format='%.12g')
        for ci,target in enumerate((.20,.45)):
            cr=brentq(lambda x:np.mean(1-laplace(x,r))-target,1e-7,10)
            rng=np.random.default_rng(SEED+3000+100*idx+ci)
            z1,z2=drawz(rng,N);a=rng.integers(0,2,size=N)
            rr=n1.make_rates(z1,z2,m)[np.arange(N),a]
            duration,status=simulate(rng,rr,cr)
            df=pd.DataFrame({'patient_id':np.arange(N),'a':a,'z1':z1,'z2':z2,'az1':a*z1,
                             'ftime':duration,'fstatus':status})
            train=out/f'{m}_c{int(target*100)}_train.csv'
            df.to_csv(train,index=False,float_format='%.12g')
            manifest['scenario'].append({'mechanism':m,'censor_target':target,'realized_censor_pct':100*(status==0).mean(),
                                        'censor_rate':cr,'train':train.name,'test':truth.name,
                                        'sha256_train':digest(train),'sha256_test':digest(truth),
                                        'cause_counts':np.bincount(status,minlength=3).tolist()})
            print(m,target,'censor_pct=',round(100*(status==0).mean(),2),flush=True)
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    # Check inverse at distinct strictly reachable positions
    for m in MECHS:
        t=pd.read_csv(out/f'{m}_oracle_test.csv')
        for row in t.iloc[::20].itertuples(index=False):
            rr=n1.make_rates(np.array([row.z1]),np.array([row.z2]),m)
            for p in P:
                q=t.loc[(t.patient_id==row.patient_id)&(t.a==row.a),f'true_q1_p{p:.2f}'].iloc[0]
                if np.isfinite(q):assert abs(n1.cif_at(rr,float(q))[0][0,int(row.a),0]-p)<1e-9
    print('PASS oracle CIF inverse verification')
if __name__=='__main__':main(Path(__file__).resolve().parents[1]/'data')
