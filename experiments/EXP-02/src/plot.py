"""Prespecified EXP-02 figures from targeted patient records and frozen truth."""
from pathlib import Path
import sys
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0,str(Path(__file__).resolve().parent))
from analyze_existing_oracle import HERE, SCENARIOS, source_from_archive


def main():
    inp=HERE/"results"
    out=HERE/"figures"
    out.mkdir(exist_ok=True)
    changed=pd.read_csv(inp/"changed_patients.csv")
    background=pd.read_csv(inp/"boundary_plot_sample.csv")
    calibration=pd.read_csv(inp/"calibration_audit.csv").set_index("scenario")
    fig,axes=plt.subplots(1,2,figsize=(12,5),layout="constrained")
    for ax,scenario in zip(axes,SCENARIOS):
        bg=background[background.scenario==scenario]
        ch=changed[changed.scenario==scenario]
        ax.scatter(bg.D_Q_month,bg.D_R_month,s=3,alpha=.09,color="#4477aa",label="prespecified background")
        ax.scatter(ch.D_Q_month,ch.D_R_month,s=3,alpha=.15,color="#cc3311",label="changed recommendation")
        budget=calibration.loc[scenario,"delta_R_month"]
        for x in (-3,3): ax.axvline(x,color="black",lw=.8,ls="--")
        for y in (-budget,budget): ax.axhline(y,color="black",lw=.8,ls="--")
        ax.set(title=scenario,xlabel="Qall(1) - Qall(0), months",ylabel="RMET(1) - RMET(0), months")
        ax.legend(fontsize=8,loc="best",markerscale=3)
    fig.savefig(out/"candidate_boundaries.png",dpi=180)
    plt.close(fig)

    fig,axes=plt.subplots(1,2,figsize=(12,5),layout="constrained")
    for ax,scenario in zip(axes,SCENARIOS):
        ch=changed[changed.scenario==scenario]
        h=ax.hexbin(ch.q1_month,ch.f1_36_pp,gridsize=48,mincnt=1,cmap="viridis",bins="log")
        ax.axhline(0,color="black",lw=.8); ax.axvline(0,color="black",lw=.8)
        ax.set(title=f"{scenario}: n={len(ch):,}",xlabel="QQ - RMET-Q1: priority Q, months",
               ylabel="QQ - RMET-Q1: priority CIF at 36 months, pp")
        fig.colorbar(h,ax=ax,label="changed patients (log count)")
    fig.savefig(out/"changed_joint_outcomes.png",dpi=180)
    plt.close(fig)

    with tempfile.TemporaryDirectory(prefix="exp02_plot_oracle_") as d:
        _,o=source_from_archive(Path(d))
        z=np.array([[-.5,0],[0,0],[.5,0]],float)
        rates,breaks=o.hazards("time_cross",z)
        v=o.truth(rates,breaks)
        pgrid=np.round(np.arange(o.CFG["p_scan"]["start"],o.CFG["p_scan"]["stop"]+.0025,
                                 o.CFG["p_scan"]["step"]),10)
        fig,axes=plt.subplots(3,2,figsize=(12,12),layout="constrained")
        labels=("no Q1 ranking flip", "interior Q1 ranking flip", "ranking flip excluded by Qall protection")
        for i in range(3):
            ts=np.linspace(0,3,361)
            f=np.array([o.curve_at(rates[i:i+1],breaks,t)[1][0] for t in ts])
            for a,style in ((0,"-"),(1,"--")):
                axes[i,0].plot(12*ts,100*f[:,a,0],style,color="#bb3344",label=f"F1, treatment {a}")
                axes[i,0].plot(12*ts,100*f[:,a,1],style,color="#4477aa",label=f"F2, treatment {a}")
                axes[i,0].plot(12*ts,100*f[:,a,:].sum(axis=1),style,color="#228855",label=f"Fall, treatment {a}")
            axes[i,0].set(title=f"Z=({z[i,0]:g},{int(z[i,1])}): {labels[i]}",
                          xlabel="months",ylabel="cumulative incidence (%)",xlim=(0,36),ylim=(0,100))
            axes[i,0].legend(fontsize=7,ncol=2)
            q=np.array([o.truth(rates[i:i+1],breaks,float(p))["q1"][0] for p in pgrid])
            axes[i,1].plot(pgrid,12*q[:,0],color="#bb3344",label="treatment 0")
            axes[i,1].plot(pgrid,12*q[:,1],color="#4477aa",label="treatment 1")
            for p in (.1,.15): axes[i,1].axvline(p,color="black",lw=.7,ls="--")
            axes[i,1].set(title=f"Qall: {12*v['qall'][i,0]:.2f} / {12*v['qall'][i,1]:.2f} months",
                          xlabel="priority CIF threshold p",ylabel="truncated Q1 (months)",ylim=(0,36))
            axes[i,1].legend(fontsize=8)
        fig.savefig(out/"time_cross_fixed_profiles.png",dpi=180)
        plt.close(fig)


if __name__=="__main__":
    main()
