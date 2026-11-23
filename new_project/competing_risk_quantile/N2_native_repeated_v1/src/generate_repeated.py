#!/usr/bin/env python3
"""Frozen multi-replicate native estimator data generator (no Cox model fit)."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import json
import hashlib
import numpy as np
import pandas as pd

# Import the EXACT existing N2 analytical DGP; do not modify old files.
BASE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE / 'N2_native_benchmark' / 'src'))
from generate import rates, scalar_f, invert, sample_covariates, simulate_one, censor_rate_for_target

BASE_SEED = 2026112304
MECHS = ('aligned', 'cause_tradeoff', 'time_varying')
CENS = (.20, .45)
N_REPS = 4
N_TRAIN = 500
N_TEST = 180
L = 3.
P1 = (.06,.12,.18,.24)
PALL = (.15,.25,.35,.45)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    a = argparse.ArgumentParser()
    a.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'data')
    args=a.parse_args()
    dest = args.output
    dest.mkdir(exist_ok=True, parents=True)
    record = {'seed':BASE_SEED,'nreps':N_REPS,'ntrain':N_TRAIN,'ntest':N_TEST,
              'horizon':L,'cut_time':1.2,'p1':P1,'pall':PALL,
              'mechanisms':MECHS,'censor_targets':CENS,
              'data_generation_source':'N2_native_benchmark/src/generate.py (unchanged)',
              'files':{},'scenarios':[]}
    for mi, mechanism in enumerate(MECHS):
        calib_rng=np.random.default_rng(BASE_SEED + 700000 + 20*mi)
        zcal1,zcal2=sample_covariates(calib_rng,30000)
        acal=calib_rng.integers(0,2,size=zcal1.size)
        rcal=rates(zcal1,zcal2,mechanism)[np.arange(zcal1.size),acal]
        cs={int(c*100):censor_rate_for_target(c,rcal) for c in CENS}
        for rep in range(N_REPS):
            # Same held-out patients for both censoring strengths within replicate.
            test_rng=np.random.default_rng(BASE_SEED + 400000 + mi*1000+rep)
            z1,z2=sample_covariates(test_rng,N_TEST)
            ar=np.tile(np.array([0,1]),N_TEST)
            rtest=rates(z1,z2,mechanism)
            fL=scalar_f(L,rtest)
            df=pd.DataFrame({'patient_id':np.repeat(np.arange(N_TEST),2),
                             'a':ar,'z1':np.repeat(z1,2),'z2':np.repeat(z2,2),
                             'az1':ar*np.repeat(z1,2),
                             'true_f1_L':fL[:,:,0].reshape(-1),
                             'true_f2_L':fL[:,:,1].reshape(-1)})
            for endpoint,probabilities,cause in [('q1',P1,0),('qall',PALL,'all')]:
                for p in probabilities:
                    df[f'true_{endpoint}_p{p:.2f}']=invert(rtest,p,cause).reshape(-1)
            test_fn=f'{mechanism}_r{rep:02d}_oracle_test.csv'
            test_fp=dest/test_fn
            df.to_csv(test_fp,index=False,float_format='%.12g')
            record['files'][test_fn]=digest(test_fp)
            # Independent training dataset at each censoring target.
            for ci,c in enumerate(CENS):
                rng=np.random.default_rng(BASE_SEED + 600000 + mi*10000 + rep*100 + ci)
                tz1,tz2=sample_covariates(rng,N_TRAIN)
                a_train=rng.integers(0,2,size=N_TRAIN)
                trates=rates(tz1,tz2,mechanism)[np.arange(N_TRAIN),a_train]
                ftime,fstatus,T,J=simulate_one(rng,trates,cs[int(c*100)])
                assert np.all(ftime>0)
                train=pd.DataFrame({'patient_id':np.arange(N_TRAIN),'a':a_train,
                                    'z1':tz1,'z2':tz2,'az1':a_train*tz1,
                                    'ftime':ftime,'fstatus':fstatus})
                train_fn=f'{mechanism}_r{rep:02d}_c{int(c*100)}_train.csv'
                train_fp=dest/train_fn
                train.to_csv(train_fp,index=False,float_format='%.12g')
                record['files'][train_fn]=digest(train_fp)
                record['scenarios'].append({'mechanism':mechanism,'replicate':rep,
                  'censor_target':c,'train':train_fn,'test':test_fn,
                  'censor_rate':cs[int(c*100)],'realized_censoring':float((fstatus==0).mean()),
                  'counts':[int((fstatus==j).sum()) for j in (0,1,2)]})
                print(f'{mechanism} rep{rep:02d} censor{int(c*100)}: observed={np.mean(fstatus==0):.3f}',flush=True)
    (dest/'manifest.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    # Independent exact-CIF inversion spot check for both endpoints.
    from generate import scalar_f as observed_true_cif
    for mech in MECHS:
        for rep in range(N_REPS):
            truth=pd.read_csv(dest/f'{mech}_r{rep:02d}_oracle_test.csv')
            for endpoint,probs,cause in [('q1',P1,0),('qall',PALL,'all')]:
                for p in probs:
                    col=f'true_{endpoint}_p{p:.2f}'
                    valid=truth[np.isfinite(truth[col])]
                    for _,row in valid.iloc[::max(1,len(valid)//12)].iterrows():
                        rr=rates(np.array([row["z1"]]),np.array([row["z2"]]),mech)
                        val=observed_true_cif(float(row[col]),rr)[0,int(row["a"]),:]
                        ev=float(val[0] if endpoint=='q1' else val.sum())
                        if abs(ev-p)>3e-10:raise ValueError((mech,endpoint,p,ev))
    print('PASS frozen data generation and cause + overall analytic inverse')

if __name__=='__main__':main()
