#!/usr/bin/env python3
"""N2-H1 eight-covariate high-dimensional competing-risk Oracle, no Cox fitting."""
from __future__ import annotations
import argparse, hashlib, json, importlib.util
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import brentq

BASE_SEED=2026112371
MECHS=('hd_correct','hd_nonlinear','hd_crossing')
NTRAIN=(500,1000)
NREPS=4
NTEST=180
CENS=(20,45)
P={'q1':(.06,.12,.18,.24),'qall':(.15,.25,.35,.45)}
L=3.0; K=1.4; PROB_CAUSE1=.55

# Literal DGP reused from N1, unchanged by estimator results
N1_PATH=Path(__file__).resolve().parents[2]/'N1_oracle/src/n1_oracle_study.py'
spec=importlib.util.spec_from_file_location('n1_analytic',str(N1_PATH)); n1=importlib.util.module_from_spec(spec);spec.loader.exec_module(n1)

def dgp_rates(mech,z):
    z1,z2,z3,z4,z5,z6,z7,z8 = [z[:,j] for j in range(8)]
    if mech == 'hd_nonlinear':
        rates=n1.make_rates(z1,z2,'cause_tradeoff')
        h=np.sin(np.pi*z3*z5); u4=z4*z4-1/3
        rates[:,:,0,:] *= np.exp(.25*z3+.20*u4+.15*z7)[:,None,None]
        rates[:,:,1,:] *= np.exp(-.20*z3+.20*z6-.15*z8)[:,None,None]
        rates[:,1,0,0] *= np.exp(.75*h+.45*u4+.25*z6*z7)
        rates[:,1,0,1] *= np.exp(-.55*h+.35*z7*z8)
        rates[:,1,1,0] *= np.exp(-.60*h-.35*z3*z6)
        rates[:,1,1,1] *= np.exp(.45*h+.30*u4)
    elif mech == 'hd_crossing':
        rates=n1.make_rates(z1,z2,'time_varying')
        h=np.sin(np.pi*z3*z5)
        rates[:,:,0,:] *= np.exp(.22*z3+.15*z5*z6)[:,None,None]
        rates[:,:,1,:] *= np.exp(-.20*z4+.17*z7)[:,None,None]
        rates[:,1,0,0] *= np.exp(.80*h+.45*z4*z6)
        rates[:,1,0,1] *= np.exp(-.90*h+.45*z7*z8)
        rates[:,1,1,0] *= np.exp(-.65*h+.35*z6*z7)
        rates[:,1,1,1] *= np.exp(.80*h-.40*z5*z8)
    else:raise ValueError(mech)
    if not np.all(rates>0):raise ValueError('nonpositive DGP rate')
    return rates

def covariates(rng,n):
    z=np.empty((n,8),float)
    z[:,0]=rng.uniform(-1,1,n)
    z[:,1]=rng.binomial(1,.5,n)
    z[:,2:]=rng.uniform(-1,1,(n,6))
    return z

def scale(z,a):
    z1,z2,z3,z4,z5,z6,z7,z8=[z[...,j] for j in range(8)]
    return np.exp(-.5+.15*z1+.12*z2+.10*z3-.08*z4+.07*z5+.08*z6-.07*z7+.06*z8+
                  a*(-.25+.20*z1+.15*z3))

def oracle_q(mech,z,p,endpoint):
    n=len(z)
    if mech=='hd_correct':
        scales=scale(z[:,None,:],np.array([0,1])[None,:])
        pmax=PROB_CAUSE1 if endpoint=='q1' else 1.
        if p>=pmax:return np.full((n,2),np.nan)
        q=scales*(-np.log1p(-p/pmax))**(1/K)
        return np.where(q<L-1e-12,q,np.nan)
    rates=dgp_rates(mech,z)
    return n1.q_exact(rates,p,0 if endpoint=='q1' else 'all')

def oracle_f(mech,z,t):
    if mech=='hd_correct':
        scales=scale(z[:,None,:],np.array([0,1])[None,:])
        ff=-np.expm1(-(t/scales)**K)
        return np.stack((PROB_CAUSE1*ff,(1-PROB_CAUSE1)*ff),axis=2)
    return n1.cif_at(dgp_rates(mech,z),t)[0]

def sample_tj(rng,mech,z,a):
    n=len(z)
    if mech=='hd_correct':
        T=scale(z,a)*rng.weibull(K,n)
        J=np.where(rng.random(n)<PROB_CAUSE1,1,2)
        return T,J
    rates=dgp_rates(mech,z)[np.arange(n),a]
    h0=rates[:,:,0].sum(axis=1);h1=rates[:,:,1].sum(axis=1)
    e=rng.exponential(size=n)
    early=e<h0*1.2
    T=np.where(early,e/h0,1.2+(e-h0*1.2)/h1)
    pp=np.where(early,rates[:,0,0]/h0,rates[:,0,1]/h1)
    J=np.where(rng.random(n)<pp,1,2)
    return T,J

def calibration_censor_rates(mech,mi):
    rng=np.random.default_rng(BASE_SEED+800000+mi)
    z=covariates(rng,60000);a=rng.integers(0,2,len(z))
    t,_=sample_tj(rng,mech,z,a)
    return {c:float(brentq(lambda rate: float((-np.expm1(-rate*t)).mean())-c/100, 1e-8,20)) for c in CENS}

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def generate(output):
    output.mkdir(parents=True,exist_ok=True)
    meta={'seed':BASE_SEED,'nreps':NREPS,'ntrains':list(NTRAIN),'ntest':NTEST,'mechanisms':MECHS,
         'censor_targets':CENS,'p_grid':P,'horizon':L,'correct_k':K,'correct_cause1_prob':PROB_CAUSE1,
         'dgp':'eight covariates: positive-control log-time model, hd nonlinear and hd time-crossing; PRE-REGISTERED formulas in PROTOCOL.md',
         'files':{},'scenarios':[]}
    for mi,mech in enumerate(MECHS):
        cens_rates=calibration_censor_rates(mech,mi)
        for ni,n in enumerate(NTRAIN):
            for rep in range(NREPS):
                trng=np.random.default_rng(BASE_SEED+100000+mi*30000+ni*1000+rep)
                z=covariates(trng,NTEST)
                aa=np.tile([0,1],NTEST)
                FF=oracle_f(mech,z,L)
                test=pd.DataFrame({'patient_id':np.repeat(np.arange(NTEST),2),
                    'a':aa,**{f'z{j+1}':np.repeat(z[:,j],2) for j in range(8)},
                    'az1':aa*np.repeat(z[:,0],2),'az3':aa*np.repeat(z[:,2],2),
                    'true_f1_L':FF[:,:,0].reshape(-1),'true_f2_L':FF[:,:,1].reshape(-1)})
                for endpoint,plist in P.items():
                    for p in plist:
                        test[f'true_{endpoint}_p{p:.2f}']=oracle_q(mech,z,p,endpoint).reshape(-1)
                name=f'{mech}_n{n}_r{rep:02d}_oracle_test.csv'
                test.to_csv(output/name,index=False,float_format='%.12g');meta['files'][name]=digest(output/name)
                rng=np.random.default_rng(BASE_SEED+400000+mi*30000+ni*1000+rep)
                zt=covariates(rng,n);a=rng.integers(0,2,n)
                splitrng=np.random.default_rng(BASE_SEED+900000+mi*30000+ni*1000+rep)
                heldout=splitrng.permutation(n)[:int(np.ceil(.25*n))]
                T,J=sample_tj(rng,mech,zt,a)
                u=np.clip(rng.random(n),1e-12,1-1e-12)
                for c in CENS:
                    Ct=-np.log(u)/cens_rates[c]
                    observed=np.minimum(T,Ct); status=np.where(T<=Ct,J,0)
                    train=pd.DataFrame({'patient_id':np.arange(n),'a':a,
                        **{f'z{j+1}':zt[:,j] for j in range(8)},
                        'az1':a*zt[:,0],'az3':a*zt[:,2],
                        'ftime':observed,'fstatus':status,
                        'is_validation':np.isin(np.arange(n),heldout).astype(int)})
                    assert np.isfinite(observed).all() and (observed>0).all()
                    fname=f'{mech}_n{n}_r{rep:02d}_c{c}_train.csv'
                    train.to_csv(output/fname,index=False,float_format='%.12g');meta['files'][fname]=digest(output/fname)
                    meta['scenarios'].append({'mechanism':mech,'n_train':n,'replicate':rep,'censor_target':c,
                        'censor_rate':cens_rates[c],'realized_censor_pct':100*float((status==0).mean()),
                        'counts':{str(j):int((status==j).sum()) for j in (0,1,2)}})
                # Analytic CIF inversion and probability conservation spot checks, both treatments.
                for endpoint,plist in P.items():
                    for p in plist:
                        col=f'true_{endpoint}_p{p:.2f}'
                        good=test[np.isfinite(test[col])]
                        for _,row in good.iloc[::max(1,len(good)//12)].iterrows():
                            zz=np.array([[row[f'z{j+1}'] for j in range(8)]])
                            f=oracle_f(mech,zz,float(row[col]))
                            actual=float(f[0,int(row.a),0] if endpoint=='q1' else f[0,int(row.a),:].sum())
                            if abs(actual-p)>3e-9:raise ValueError((mech,endpoint,p,actual))
            print('DATA VERIFIED',mech,n,flush=True)
    (output/'manifest.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    print('PASS',len(meta['files']),'frozen CSV files, exact competing-risk CIF quantile inverses',flush=True)
    return meta

def main():
    a=argparse.ArgumentParser();a.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'data')
    v=a.parse_args();generate(v.output)
if __name__=='__main__':main()
