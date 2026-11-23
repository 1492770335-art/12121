#!/usr/bin/env python3
"""N1 independent, non-Cox Oracle mechanism study.

Uses piecewise-constant cause-specific *data generating hazards*, never Cox
estimation. Direct analytic integration and inversion of competing-risk CIF.
The p grid is descriptive, not optimized to select a clinical cutoff.
"""
from pathlib import Path
import argparse, json
import numpy as np
import pandas as pd

SEED=2026112417
N=4000
HORIZON=3.0
SWITCH=1.2
GRID=np.arange(1,200,dtype=float)/200  # 0.005 to 0.995, no chosen focal p
MECHANISMS=('aligned','cause_tradeoff','time_varying')


def make_rates(z1,z2,mechanism):
    b1=0.20*np.exp(0.15*z1+0.15*z2)
    b2=0.14*np.exp(-0.12*z1+0.20*z2)
    zeros=np.zeros_like(z1)
    if mechanism=='aligned':
        e1a=e1b=-0.30+0.10*z1
        e2a=e2b=e1a
    elif mechanism=='cause_tradeoff':
        e1a=e1b=-0.30+0.30*z1
        e2a=e2b=+0.30-0.20*z1
    elif mechanism=='time_varying':
        e1a=-0.50+0.25*z1
        e1b=+0.55+0.25*z1
        e2a=+0.20-0.25*z1
        e2b=-0.20-0.25*z1
    else: raise ValueError(mechanism)
    # N x treatment x cause x segment
    rates=np.empty((len(z1),2,2,2))
    rates[:,0,0,:]=b1[:,None]
    rates[:,0,1,:]=b2[:,None]
    rates[:,1,0,0]=b1*np.exp(e1a)
    rates[:,1,0,1]=b1*np.exp(e1b)
    rates[:,1,1,0]=b2*np.exp(e2a)
    rates[:,1,1,1]=b2*np.exp(e2b)
    assert np.all(rates>0)
    return rates


def cif_at(rates,t):
    """Exact piecewise exponential competing-risk CIF, shape N x 2 x 2."""
    end1=min(t,SWITCH)
    end2=max(t-SWITCH,0)
    r0=rates[:,:,:,0]
    tot0=r0.sum(axis=2)
    surv0=np.exp(-tot0*end1)
    f=r0/tot0[:,:,None]*(-np.expm1(-tot0*end1))[:,:,None]
    if end2>0:
        r1=rates[:,:,:,1]
        tot1=r1.sum(axis=2)
        f+=surv0[:,:,None]*r1/tot1[:,:,None]*(-np.expm1(-tot1*end2))[:,:,None]
        s=surv0*np.exp(-tot1*end2)
    else: s=surv0
    np.testing.assert_allclose(f.sum(axis=2)+s, 1, atol=5e-14,rtol=0)
    return f,s


def q_exact(rates,p,cause):
    """Exact inverse to both-treatment strict-interior cause/all CIF.
    Returns NaN when p not strictly below CIF(L), rather than cap=L.
    """
    if cause=='all':
        r0=rates[:,:,:,0].sum(axis=2)
        r1=rates[:,:,:,1].sum(axis=2)
    else:
        r0=rates[:,:,cause,0]
        r1=rates[:,:,cause,1]
    tot0=rates[:,:,:,0].sum(axis=2)
    tot1=rates[:,:,:,1].sum(axis=2)
    s_switch=np.exp(-tot0*SWITCH)
    f_switch=(r0/tot0)*(-np.expm1(-tot0*SWITCH))
    f_final=f_switch+s_switch*(r1/tot1)*(-np.expm1(-tot1*(HORIZON-SWITCH)))
    out=np.full(f_final.shape,np.nan)
    strictly=(p < f_final - 1e-12)
    early=strictly & (p <= f_switch)
    late=strictly & (p > f_switch)
    arg0=np.clip(p*tot0/r0,0,1-1e-15)
    arg1=np.clip((p-f_switch)*tot1/(s_switch*r1),0,1-1e-15)
    q0=-np.log1p(-arg0)/tot0
    q1=SWITCH-np.log1p(-arg1)/tot1
    out[early]=q0[early]
    out[late]=q1[late]
    assert np.all((out[np.isfinite(out)]>=-1e-10)&(out[np.isfinite(out)]<HORIZON+1e-10))
    return out


def analyze(rates,mechanism):
    fL,sL=cif_at(rates,HORIZON)
    fs,ss=cif_at(rates,SWITCH)
    rows=[]
    prev=np.zeros(len(rates),dtype=np.int8)
    ever=np.zeros(len(rates),bool)
    ever_valid=np.zeros(len(rates),bool)
    first_p=np.full(len(rates),np.nan)
    last_p=np.full(len(rates),np.nan)
    for p in GRID:
        qi=q_exact(rates,p,0)
        qa=q_exact(rates,p,'all')
        good1=np.isfinite(qi).all(axis=1)
        goodall=np.isfinite(qa).all(axis=1)
        # Sign strictly from interior quantiles: 1 benefits treatment 1.
        difference=qi[:,1]-qi[:,0]
        sign=np.where(good1 & (difference>1e-9),1,np.where(good1&(difference<-1e-9),-1,0))
        ever_valid |= sign != 0
        flip=(prev!=0)&(sign!=0)&(prev!=sign)
        newly=flip & ~ever
        first_p[newly]=p
        ever |= flip
        prev=np.where(sign!=0,sign,prev)
        last_p=np.where(sign!=0,p,last_p)
        denom=np.count_nonzero(sign)
        rows.append(dict(mechanism=mechanism,p_diagnostic=round(float(p),5),
                         priority_both_interior_pct=100*good1.mean(),
                         overall_both_interior_pct=100*goodall.mean(),
                         joint_same_p_interior_pct=100*np.mean(good1 & goodall),
                         priority1_better_pct_given_strict_order=(100*np.mean(sign[sign!=0]>0) if denom else np.nan),
                         priority_ordered_n=int(denom),
                         priority_exact_tie_n=int(np.count_nonzero(good1 & (sign==0)))))
    # Any flip as p changes, requires strict interior and strict treatment preference.
    groups=np.where(ever,'flip','no_flip')
    group_rows=[]
    for grp in ('flip','no_flip'):
        sel=(groups==grp)
        group_rows.append(dict(mechanism=mechanism,group=grp,n=int(sel.sum()),pct=100*sel.mean(),
                               z1_mean=float(z1_glob[sel].mean()) if sel.any() else None,
                               z2_1_pct=100*float(z2_glob[sel].mean()) if sel.any() else None,
                               f1_at_L_mean=float(fL[sel,:,0].mean()) if sel.any() else None,
                               f2_at_L_mean=float(fL[sel,:,1].mean()) if sel.any() else None,
                               first_flip_p_median=float(np.nanmedian(first_p[sel])) if grp=='flip' and sel.any() else None))
    summary=dict(mechanism=mechanism,n=len(rates),seed=SEED,horizon=HORIZON,switch_time=SWITCH,
                 n_grid=int(len(GRID)),p_grid_min=float(GRID[0]),p_grid_max=float(GRID[-1]),
                 patients_ever_strict_interior_q1_flip_pct=100*ever.mean(),
                 patients_with_any_two_treatment_strict_priority_comparison_pct=100*ever_valid.mean(),
                 mean_cif1_at_L_treat0=float(fL[:,0,0].mean()),mean_cif1_at_L_treat1=float(fL[:,1,0].mean()),
                 mean_cif2_at_L_treat0=float(fL[:,0,1].mean()),mean_cif2_at_L_treat1=float(fL[:,1,1].mean()),
                 mean_overall_failure_at_L_treat0=float((1-sL[:,0]).mean()),mean_overall_failure_at_L_treat1=float((1-sL[:,1]).mean()),
                 note='Oracle only; no censoring, no estimation and no clinical p selected')
    return rows,group_rows,summary


def selftest():
    z1=np.array([-.7,0.,+.8])
    z2=np.array([0.,1.,1.])
    for sc in MECHANISMS:
        rate=make_rates(z1,z2,sc)
        f0,s0=cif_at(rate,0)
        assert np.max(abs(f0))<1e-14
        assert np.max(abs(s0-1))<1e-14
        f3,s3=cif_at(rate,HORIZON)
        f15,s15=cif_at(rate,1.5)
        assert np.all(f15<=f3)
        assert np.all(s15>=s3)
        for c in (0,1,'all'):
            for p in (.01,.05,.1):
                q=q_exact(rate,p,c)
                for i in range(len(z1)):
                    for a in (0,1):
                        if np.isfinite(q[i,a]):
                            f,_=cif_at(rate,float(q[i,a]))
                            actual=f[i,a].sum() if c=='all' else f[i,a,c]
                            assert abs(actual-p)<1e-12,(sc,c,p,actual)
    print('PASS analytic CIF normalization, monotonicity, invertibility')


def main():
    global z1_glob,z2_glob
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args()
    selftest()
    rng=np.random.default_rng(SEED)
    z1_glob=rng.uniform(-1,1,N)
    z2_glob=rng.binomial(1,0.5,N)
    all_rows=[]; all_groups=[]; all_summary=[]
    for sc in MECHANISMS:
        rs=make_rates(z1_glob,z2_glob,sc)
        rows,groups,summary=analyze(rs,sc)
        all_rows+=rows;all_groups+=groups;all_summary.append(summary)
        print(f'{sc}: strict-interior p flip in {summary["patients_ever_strict_interior_q1_flip_pct"]:.3f}% of patients')
    args.out.mkdir(parents=True,exist_ok=True)
    pd.DataFrame(all_rows).to_csv(args.out/'n1_risk_grid.csv',index=False,float_format='%.10f')
    pd.DataFrame(all_groups).to_csv(args.out/'n1_subgroups.csv',index=False,float_format='%.10f')
    (args.out/'n1_summary.json').write_text(json.dumps(all_summary,ensure_ascii=False,indent=2),encoding='utf8')
    # A compact, predeclared regular sampling of the full p grid for public table.
    sampled=pd.DataFrame(all_rows)
    sampled=sampled[np.isclose((sampled.p_diagnostic*100)%5,0,atol=1e-8)]
    sampled.to_csv(args.out/'n1_20grid_summary.csv',index=False,float_format='%.6f')
    # Sensible additional independent validation of direction in aligned mechanism.
    aligned=np.array([r['priority1_better_pct_given_strict_order'] for r in all_rows if r['mechanism']=='aligned'])
    assert np.nanmax(aligned)==100.,'aligned should have no preference reversal'
    assert np.all(np.diff([r['priority_both_interior_pct'] for r in all_rows if r['mechanism']=='time_varying']) <= 1e-10)
    print('PASS N1 predeclared mechanism invariants and monotone support')

if __name__=='__main__':main()
