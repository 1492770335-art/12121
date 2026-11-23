#!/usr/bin/env python3
"""N2-S2 frozen data generator: analytical competing-risk Oracle, no Cox fitting."""
from __future__ import annotations
import argparse, hashlib, json, importlib.util
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import brentq

BASE_SEED=2026112322
MECHS=('time_varying','nonlinear_interaction','logquantile_correct')
NTRAIN=(1000,)
NREPS=12
NTEST=180
CENS=(20,45)
P={'q1':(.06,.12,.18,.24),'qall':(.15,.25,.35,.45)}
L=3.0; K=1.4; PROB_CAUSE1=.55

# Literal DGP reused from N1, unchanged by estimator results
N1_PATH=Path(__file__).resolve().parents[2]/'N1_oracle/src/n1_oracle_study.py'
spec=importlib.util.spec_from_file_location('n1_analytic',str(N1_PATH)); n1=importlib.util.module_from_spec(spec);spec.loader.exec_module(n1)

def dgp_rates(mech,z1,z2):
    if mech!='nonlinear_interaction':return n1.make_rates(z1,z2,mech)
    rate=n1.make_rates(z1,z2,'time_varying')
    # Predeclared nonlinear patient-specific treatment interactions; control is unchanged.
    rate[:,1,0,0]*=np.exp(.55*np.sin(np.pi*z1)+.35*(z1*z1-1/3))
    rate[:,1,0,1]*=np.exp(-.45*np.sin(np.pi*z1)+.55*(z1*z1-1/3))
    rate[:,1,1,0]*=np.exp(-.40*np.sin(np.pi*z1/2)-.30*z1*z1)
    rate[:,1,1,1]*=np.exp(+.40*np.sin(np.pi*z1/2)+.20*z1*z1)
    return rate


def covariates(rng,n):
    return rng.uniform(-1,1,n),rng.binomial(1,.5,n)

def scale(z1,z2,a):
    return np.exp(-.5+.15*z1+.12*z2+a*(-.25+.20*z1))

def oracle_q(mech,z1,z2,p,endpoint):
    n=len(z1)
    if mech=='logquantile_correct':
        aa=np.array([0,1])[None,:]
        scales=scale(z1[:,None],z2[:,None],aa)
        pmax=PROB_CAUSE1 if endpoint=='q1' else 1.
        if p>=pmax:
            return np.full((n,2),np.nan)
        q=scales*(-np.log1p(-p/pmax))**(1/K)
        return np.where(q<L-1e-12,q,np.nan)
    rs=dgp_rates(mech,z1,z2)
    return n1.q_exact(rs,p,0 if endpoint=='q1' else 'all')

def oracle_f(mech,z1,z2,t):
    if mech=='logquantile_correct':
        scales=scale(z1[:,None],z2[:,None],np.array([0,1])[None,:])
        f= -np.expm1(-(t/scales)**K)
        return np.stack((PROB_CAUSE1*f,(1-PROB_CAUSE1)*f),axis=2)
    return n1.cif_at(dgp_rates(mech,z1,z2),t)[0]

def sample_tj(rng,mech,z1,z2,a):
    n=len(z1)
    if mech=='logquantile_correct':
        T=scale(z1,z2,a)*rng.weibull(K,n)
        J=np.where(rng.random(n)<PROB_CAUSE1,1,2)
        return T,J
    rates=dgp_rates(mech,z1,z2)[np.arange(n),a]
    h0=rates[:,:,0].sum(axis=1);h1=rates[:,:,1].sum(axis=1)
    e=rng.exponential(size=n)
    early=e<h0*1.2
    T=np.where(early,e/h0,1.2+(e-h0*1.2)/h1)
    pp=np.where(early,rates[:,0,0]/h0,rates[:,0,1]/h1)
    J=np.where(rng.random(n)<pp,1,2)
    return T,J

def calibration_censor_rates(mech,mi):
    rng=np.random.default_rng(BASE_SEED+800000+mi)
    z1,z2=covariates(rng,80000);a=rng.integers(0,2,len(z1))
    t,_=sample_tj(rng,mech,z1,z2,a)
    return {c:float(brentq(lambda rate: float((-np.expm1(-rate*t)).mean())-c/100, 1e-8,20)) for c in CENS}

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def generate(output):
    output.mkdir(parents=True,exist_ok=True)
    meta={'seed':BASE_SEED,'nreps':NREPS,'ntrains':list(NTRAIN),'ntest':NTEST,'mechanisms':MECHS,
         'censor_targets':CENS,'p_grid':P,'horizon':L,'correct_k':K,'correct_cause1_prob':PROB_CAUSE1,
         'dgp':'Original N2-T1 time varying and nonlinear interactions plus correct-structure control, no DGP coefficient changes',
         'files':{},'scenarios':[]}
    for mi,mech in enumerate(MECHS):
        cens_rates=calibration_censor_rates(mech,mi)
        for ni,n in enumerate(NTRAIN):
            for rep in range(NREPS):
                trng=np.random.default_rng(BASE_SEED+100000+mi*30000+ni*1000+rep)
                z1,z2=covariates(trng,NTEST)
                aa=np.tile([0,1],NTEST)
                F=oracle_f(mech,z1,z2,L)
                test=pd.DataFrame({'patient_id':np.repeat(np.arange(NTEST),2),
                    'a':aa,'z1':np.repeat(z1,2),'z2':np.repeat(z2,2),
                    'az1':aa*np.repeat(z1,2),
                    'true_f1_L':F[:,:,0].reshape(-1),'true_f2_L':F[:,:,1].reshape(-1)})
                for endpoint,plist in P.items():
                    for p in plist:
                        test[f'true_{endpoint}_p{p:.2f}']=oracle_q(mech,z1,z2,p,endpoint).reshape(-1)
                name=f'{mech}_n{n}_r{rep:02d}_oracle_test.csv'
                test.to_csv(output/name,index=False,float_format='%.12g');meta['files'][name]=digest(output/name)
                rng=np.random.default_rng(BASE_SEED+400000+mi*30000+ni*1000+rep)
                z1t,z2t=covariates(rng,n);a=rng.integers(0,2,n)
                # Split by fixed RNG independent of outcomes, reused across both censoring arms.
                splitrng=np.random.default_rng(BASE_SEED+900000+mi*30000+ni*1000+rep)
                heldout=splitrng.permutation(n)[:int(np.ceil(.25*n))]
                T,J=sample_tj(rng,mech,z1t,z2t,a)
                u=np.clip(rng.random(n),1e-12,1-1e-12)
                for c in CENS:
                    Ct=-np.log(u)/cens_rates[c]
                    observed=np.minimum(T,Ct); status=np.where(T<=Ct,J,0)
                    train=pd.DataFrame({'patient_id':np.arange(n),'a':a,'z1':z1t,'z2':z2t,
                        'az1':a*z1t,'ftime':observed,'fstatus':status,
                        'is_validation':np.isin(np.arange(n),heldout).astype(int)})
                    assert np.isfinite(observed).all() and (observed>0).all()
                    fname=f'{mech}_n{n}_r{rep:02d}_c{c}_train.csv'
                    train.to_csv(output/fname,index=False,float_format='%.12g');meta['files'][fname]=digest(output/fname)
                    meta['scenarios'].append({'mechanism':mech,'n_train':n,'replicate':rep,'censor_target':c,
                        'censor_rate':cens_rates[c],'realized_censor_pct':100*float((status==0).mean()),
                        'counts':{str(j):int((status==j).sum()) for j in (0,1,2)}})
                # Verify true CIF analytical at the finite inversions (spot check)
                for endpoint,plist in P.items():
                    for p in plist:
                        col=f'true_{endpoint}_p{p:.2f}'
                        good=test[np.isfinite(test[col])]
                        for _,row in good.iloc[::max(1,len(good)//8)].iterrows():
                            f=oracle_f(mech,np.array([row.z1]),np.array([row.z2]),float(row[col]))
                            actual=float(f[0,int(row.a),0] if endpoint=='q1' else f[0,int(row.a),:].sum())
                            if abs(actual-p)>3e-9:raise ValueError((mech,endpoint,p,actual))
            print('DATA VERIFIED',mech,n,flush=True)
    (output/'manifest.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    print('PASS',len(meta['files']),'frozen CSV files, N1 and exact log-linear Oracle inverse',flush=True)
    return meta

def main():
    a=argparse.ArgumentParser();a.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'data')
    v=a.parse_args();generate(v.output)
if __name__=='__main__':main()
