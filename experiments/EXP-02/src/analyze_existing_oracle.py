"""EXP-02: exact, targeted replay of two frozen Oracle scenarios.

Only the two missing patient-level mechanisms are recomputed. The original
archive is hash-checked and extracted into a temporary directory; its source
code, configuration, and existing results are never edited.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile

import numpy as np
import pandas as pd


HERE = Path(__file__).resolve().parents[1]
REPO = HERE.parents[1]
ORIGINAL = REPO / "literature/quantile_treatment_rules/oracle_20261123/original"
ZIP = ORIGINAL / "Oracle_竞争风险决策_20261123_结果包.zip"
SHA256 = "4700ea52b9a50c0d96786965ad4fe13e30b0b40952292bc396700699c34a06b7"
SCENARIOS = ("PH_tradeoff", "time_cross")
METRICS = ("q1_month", "qall_month", "rmet_month", "f1_12_pp", "f2_12_pp", "f1_36_pp", "f2_36_pp")
TOL = 1e-12


def source_from_archive(temp: Path):
    assert ZIP.is_file(), f"Run original/restore.py first: {ZIP}"
    digest = hashlib.sha256(ZIP.read_bytes()).hexdigest()
    assert digest == SHA256, (digest, SHA256)
    with ZipFile(ZIP) as archive:
        assert archive.testzip() is None
        for member in archive.infolist():
            path = Path(member.filename)
            assert not path.is_absolute() and ".." not in path.parts
        archive.extractall(temp)
    roots = list(temp.glob("*/config.json"))
    assert len(roots) == 1
    root = roots[0].parent
    spec = importlib.util.spec_from_file_location("exp02_original_oracle", root / "src/oracle.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return root, module


def calibrate(o, scenario, ci):
    cfg = o.CFG
    rng = np.random.default_rng(np.random.SeedSequence([cfg["calibration_seed"], ci]))
    z = o.sample(scenario, rng, cfg["calibration_n"])
    v = o.truth(*o.hazards(scenario, z))
    delta_q = cfg["delta_months"] / 12
    count = int(o.candidate(v["qall"], delta_q).all(axis=1).sum())
    gap = np.abs(np.diff(v["rmet"], axis=1)[:, 0])
    budget = 0.0 if count == 0 else float(np.partition(gap, count - 1)[count - 1])
    return budget, count / len(z)


def values_for(v, s12, f12, d, o):
    return np.column_stack((
        12 * o.take(v["q1"], d), 12 * o.take(v["qall"], d),
        12 * o.take(v["rmet"], d),
        100 * o.take(f12[:, :, 0], d), 100 * o.take(f12[:, :, 1], d),
        100 * o.take(v["f1"], d), 100 * o.take(v["f2"], d),
    ))


def replay_one(o, scenario, ci, rep, budget):
    cfg = o.CFG
    rng = np.random.default_rng(np.random.SeedSequence([cfg["seed"], ci, rep]))
    n = cfg["test_n"]
    z = o.sample(scenario, rng, n)
    coin = rng.integers(0, 2, n)
    rates, breaks = o.hazards(scenario, z)
    v = o.truth(rates, breaks)
    s12, f12 = o.curve_at(rates, breaks, 1.0)
    aq = o.candidate(v["qall"], cfg["delta_months"] / 12)
    ar = o.candidate(v["rmet"], budget)
    # Reproduce the original implementation first, then enforce one common
    # secondary tie key for both rules. Original Q1 ties are audited below.
    legacy_q = o.choose(v["q1"], coin, aq, v["qall"])
    legacy_r = o.choose(v["q1"], coin, ar, v["rmet"])
    dq = o.choose(v["q1"], coin, aq)
    dr = o.choose(v["q1"], coin, ar)
    changed = dq != dr
    mismatch = np.any(aq != ar, axis=1)
    assert not np.any(changed & ~mismatch)
    assert np.isin(dq, (0, 1)).all() and np.isin(dr, (0, 1)).all()
    assert aq.any(axis=1).all() and ar.any(axis=1).all()
    assert np.max(v["qall"].max(axis=1) - o.take(v["qall"], dq)) <= cfg["delta_months"] / 12 + TOL
    assert np.max(v["rmet"].max(axis=1) - o.take(v["rmet"], dr)) <= budget + TOL
    np.testing.assert_allclose(v["f1"] + v["f2"], 1-v["s"], atol=2e-14, rtol=0)
    np.testing.assert_allclose(f12.sum(axis=2) + s12, 1, atol=2e-14, rtol=0)
    assert np.all(f12 >= -TOL) and np.all(f12 <= v["f1"].max()+v["f2"].max()+TOL)
    assert np.all(f12 <= np.stack((v["f1"], v["f2"]), axis=2)+TOL)
    for key in ("q1", "qall", "rmet"):
        assert np.all((v[key] >= 0) & (v[key] <= cfg["horizon_years"]+TOL))

    yq = values_for(v, s12, f12, dq, o)
    yr = values_for(v, s12, f12, dr, o)
    diff = yq-yr
    if np.any(~changed):
        assert np.max(np.abs(diff[~changed])) == 0
    dqgap = 12 * (v["qall"][:, 1] - v["qall"][:, 0])
    drgap = 12 * (v["rmet"][:, 1] - v["rmet"][:, 0])
    d1gap = 12 * (v["q1"][:, 1] - v["q1"][:, 0])
    bq, br = aq.all(axis=1), ar.all(axis=1)
    tie = np.abs(v["q1"][:, 1]-v["q1"][:, 0]) <= cfg["absolute_tie_tolerance_years"]
    interior = ((v["f1"] > cfg["p_priority"] + TOL).all(axis=1)
                & ((1-v["s"]) > cfg["p_all"] + TOL).all(axis=1))
    near = (np.any(np.abs(v["f1"]-cfg["p_priority"]) <= TOL, axis=1)
            | np.any(np.abs((1-v["s"])-cfg["p_all"]) <= TOL, axis=1))
    assert np.all(interior == ((v["q1"] < cfg["horizon_years"]-TOL).all(axis=1)
                               & (v["qall"] < cfg["horizon_years"]-TOL).all(axis=1)))
    q_loss = 12*(v["qall"].max(axis=1)-o.take(v["qall"], dr))
    r_loss = 12*(v["rmet"].max(axis=1)-o.take(v["rmet"], dq))
    q_violation = q_loss > cfg["delta_months"]+12*TOL
    r_violation = r_loss > 12*budget+12*TOL

    masks = {
        "all": np.ones(n, bool), "changed": changed,
        "strict_interior": interior, "changed_strict_interior": changed & interior,
        "Q_both_R_single": bq & ~br, "Q_single_R_both": ~bq & br,
        "both_single_different": ~bq & ~br & mismatch,
        "changed_Q0_R1": changed & (dq == 0),
        "changed_Q1_R0": changed & (dq == 1),
    }
    categories = {
        "both_both": bq & br, "Q_both_R_single": bq & ~br,
        "Q_single_R_both": ~bq & br,
        "both_single_same": ~bq & ~br & ~mismatch,
        "both_single_different": ~bq & ~br & mismatch,
    }
    assert sum(int(m.sum()) for m in categories.values()) == n
    arows = []
    for category, mask in {**categories, "Q_both": bq, "R_both": br,
                           "Q_both_R_single_changed": bq & ~br & changed,
                           "Q_single_R_both_changed": ~bq & br & changed,
                           "candidate_mismatch": mismatch,
                           "action_mismatch": changed, "Q1_tie": tie,
                           "legacy_action_mismatch": legacy_q != legacy_r,
                           "legacy_vs_unified_Q": legacy_q != dq,
                           "legacy_vs_unified_R": legacy_r != dr}.items():
        arows.append(dict(scenario=scenario, rep=rep, category=category,
                          count=int(mask.sum()), n=n))
    brows = []
    for subset, mask in masks.items():
        row = dict(scenario=scenario, rep=rep, subset=subset, count=int(mask.sum()), n=n)
        for j, name in enumerate(METRICS):
            row[name + "_sum"] = float(diff[mask, j].sum())
            row["Q_" + name + "_sum"] = float(yq[mask, j].sum())
            row["R_" + name + "_sum"] = float(yr[mask, j].sum())
        row.update(q_budget_violation_sum=int((q_violation & mask).sum()),
                   q_budget_excess_month_sum=float(np.maximum(q_loss[mask]-cfg["delta_months"], 0).sum()),
                   r_budget_violation_sum=int((r_violation & mask).sum()),
                   q_treat1_sum=int((dq[mask] == 1).sum()),
                   r_treat1_sum=int((dr[mask] == 1).sum()),
                   q_boundary_distance_month_sum=float(np.abs(np.abs(dqgap[mask])-cfg["delta_months"]).sum()),
                   r_boundary_distance_month_sum=float(np.abs(np.abs(drgap[mask])-12*budget).sum()))
        brows.append(row)

    # The neutral mechanisms have Z1 ~ Uniform(-1,1), so these are fixed
    # population quartiles, never fitted to the observed outcome.
    quartile = np.searchsorted(np.array([-.5, 0, .5]), z[:, 0], side="right")
    cgroups = {"strict_interior": interior, "not_strict_interior": ~interior,
               "priority_unreachable_any": np.any(v["f1"] < cfg["p_priority"]-TOL, axis=1),
               "priority_unreachable_both": np.all(v["f1"] < cfg["p_priority"]-TOL, axis=1),
               "all_unreachable_any": np.any(1-v["s"] < cfg["p_all"]-TOL, axis=1),
               "near_cap_boundary": near}
    for q in range(4):
        for z2 in (0, 1):
            cgroups[f"Z1_Q{q+1}_Z2_{z2}"] = (quartile == q) & (z[:, 1] == z2)
    crows=[]
    for group, mask in cgroups.items():
        row=dict(scenario=scenario, rep=rep, group=group, count=int(mask.sum()), n=n,
                 changed_sum=int((changed & mask).sum()),
                 candidate_mismatch_sum=int((mismatch & mask).sum()),
                 q_treat1_sum=int((dq[mask]==1).sum()), r_treat1_sum=int((dr[mask]==1).sum()))
        for j,name in enumerate(METRICS):
            row[name+"_sum"] = float(diff[mask,j].sum())
        crows.append(row)

    index=np.flatnonzero(changed)
    patients=[]
    for i in index:
        row=dict(scenario=scenario,rep=rep,patient_id=int(i),z1=float(z[i,0]),z2=int(z[i,1]),
                 d_Q=int(dq[i]),d_R=int(dr[i]),A_Q_0=int(aq[i,0]),A_Q_1=int(aq[i,1]),
                 A_R_0=int(ar[i,0]),A_R_1=int(ar[i,1]),
                 D_Q_month=float(dqgap[i]),D_R_month=float(drgap[i]),D_1_month=float(d1gap[i]),
                 Qall0_month=float(12*v["qall"][i,0]),Qall1_month=float(12*v["qall"][i,1]),
                 Q10_month=float(12*v["q1"][i,0]),Q11_month=float(12*v["q1"][i,1]),
                 R0_month=float(12*v["rmet"][i,0]),R1_month=float(12*v["rmet"][i,1]),
                 strict_interior=int(interior[i]),q_budget_violation_R=int(q_violation[i]))
        row.update({name:float(diff[i,j]) for j,name in enumerate(METRICS)})
        patients.append(row)
    # Prespecified evenly spaced positions in each replication for the
    # background of the candidate-boundary plot, independent of outcomes.
    visual=[]
    for i in np.linspace(0,n-1,30,dtype=int):
        visual.append(dict(scenario=scenario,rep=rep,patient_id=int(i),
                           D_Q_month=float(dqgap[i]),D_R_month=float(drgap[i]),
                           changed=int(changed[i]),candidate_mismatch=int(mismatch[i])))
    return arows,brows,crows,patients,visual


def summary_counts(frame, group_cols):
    rows=[]
    for key, g in frame.groupby(group_cols, sort=False):
        if not isinstance(key, tuple): key=(key,)
        rate=g["count"] / g["n"]
        rows.append(dict(zip(group_cols,key)) | dict(count=int(g["count"].sum()), n=int(g["n"].sum()),
            pct=100*rate.mean(), mcse_pp=100*rate.std(ddof=1)/np.sqrt(len(rate)), reps=len(rate)))
    return pd.DataFrame(rows)


def summary_ratios(frame, group_cols, numerator_cols):
    rows=[]
    for key,g in frame.groupby(group_cols,sort=False):
        if not isinstance(key,tuple): key=(key,)
        total=g["count"].sum()
        row=dict(zip(group_cols,key)) | dict(count=int(total), n=int(g["n"].sum()),
                subset_pct=100*total/g["n"].sum(),reps=len(g))
        for col in numerator_cols:
            theta=g[col].sum()/total if total else np.nan
            influence=(g[col]-theta*g["count"])/g["count"].mean() if total else np.full(len(g),np.nan)
            row[col.removesuffix("_sum")]=theta
            row[col.removesuffix("_sum")+"_mcse"]=influence.std(ddof=1)/np.sqrt(len(g)) if total else np.nan
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    out=HERE/"results"
    out.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="exp02_verified_oracle_") as d:
        root,o=source_from_archive(Path(d))
        cfg=o.CFG
        assert cfg["repetitions"]==200 and cfg["test_n"]==5000
        assert cfg["p_all"]==.5 and cfg["p_priority"]==.1
        assert cfg["horizon_years"]==3 and cfg["delta_months"]==3
        historical=pd.read_csv(root/"results/pairs_raw.csv")
        prior_cal=pd.read_csv(root/"results/calibration_raw.csv")
        all_a=[];all_b=[];all_c=[];all_pat=[];all_vis=[];cal_rows=[]
        for scenario in SCENARIOS:
            ci=o.SCENARIOS.index(scenario)
            budget,match=calibrate(o,scenario,ci)
            old=prior_cal.loc[prior_cal.scenario==scenario].iloc[0]
            assert abs(12*budget-old.delta_rmet_month)<1e-10
            assert abs(100*match-old.qq_candidates_pct)<1e-10
            cal_rows.append(dict(scenario=scenario,delta_R_month=12*budget,
                                 independent_calibration_n=cfg["calibration_n"],
                                 matched_both_candidates_pct=100*match))
            for rep in range(1,cfg["repetitions"]+1):
                a,b,c,p,v=replay_one(o,scenario,ci,rep,budget)
                all_a+=a;all_b+=b;all_c+=c;all_pat+=p;all_vis+=v
                old_count=int(historical.loc[(historical.scenario==scenario)&
                    (historical.method=="RMET-Q1")&(historical.subset=="changed")&
                    (historical.rep==rep),"count"].iloc[0])
                observed=next(x["count"] for x in a if x["category"]=="legacy_action_mismatch")
                assert observed==old_count, (scenario,rep,observed,old_count)
                for subset in ("all","changed"):
                    old_row=historical.loc[(historical.scenario==scenario)&
                        (historical.method=="RMET-Q1")&(historical.subset==subset)&
                        (historical.rep==rep)].iloc[0]
                    new_row=next(x for x in b if x["subset"]==subset)
                    for new_col,old_col in (("q1_month","q1_month"),
                                            ("qall_month","qall_month"),
                                            ("rmet_month","rmet_month"),
                                            ("f1_36_pp","f1_pct"),
                                            ("f2_36_pp","f2_pct")):
                        assert abs(new_row[new_col+"_sum"]/new_row["count"]-old_row[old_col])<1e-10, (scenario,rep,subset,new_col)
            print(f"{scenario}: 200 original patient streams exactly replayed",flush=True)
        a=pd.DataFrame(all_a); b=pd.DataFrame(all_b); c=pd.DataFrame(all_c)
        pd.DataFrame(cal_rows).to_csv(out/"calibration_audit.csv",index=False)
        a.to_csv(out/"replicate_candidate_counts.csv",index=False)
        b.to_csv(out/"replicate_outcome_sums.csv",index=False)
        c.to_csv(out/"replicate_heterogeneity_sums.csv",index=False)
        pd.DataFrame(all_pat).to_csv(out/"changed_patients.csv",index=False)
        pd.DataFrame(all_vis).to_csv(out/"boundary_plot_sample.csv",index=False)
        summary_counts(a,["scenario","category"]).to_csv(out/"table_A_candidate_sets.csv",index=False)
        summary_ratios(b,["scenario","subset"],
            [col for col in b.columns if col.endswith("_sum")]).to_csv(out/"table_B_counterfactual_outcomes.csv",index=False)
        summary_ratios(c,["scenario","group"],
            [col for col in c.columns if col.endswith("_sum")]).to_csv(out/"table_C_reachability_heterogeneity.csv",index=False)
        audit=dict(archive_sha256=SHA256,original_config=cfg,
            source_file_count=sum(path.is_file() for path in root.rglob("*")),
            historical_replicate_counts_matched=True,
            legacy_pooled_rates={s:100*int(a.loc[(a.scenario==s)&(a.category=="legacy_action_mismatch"),"count"].sum())/(200*5000) for s in SCENARIOS})
        (out/"audit.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding="utf-8")


if __name__=="__main__":
    main()
