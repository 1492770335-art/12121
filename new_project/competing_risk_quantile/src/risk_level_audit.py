#!/usr/bin/env python3
"""N1 competing-risk threshold feasibility audit, independent of any estimator.

Input npz:
    time: (K,), strictly increasing, starting at 0
    f1, f2: (N, 2, K), treatment-specific cause CIFs
Output:
    risk_level_support.csv and summary.json

The p-grid is for numerical diagnosis, NOT a selected clinical risk threshold.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import numpy as np

PROB_TOL = 1e-10


def validate(time: np.ndarray, f1: np.ndarray, f2: np.ndarray) -> None:
    if time.ndim != 1 or len(time) < 3:
        raise ValueError("time must be a 1-D array with >=3 points")
    if not np.isfinite(time).all() or abs(time[0]) > PROB_TOL or not np.all(np.diff(time) > 0):
        raise ValueError("time must start at 0, be finite and strictly increasing")
    if f1.ndim != 3 or f1.shape != f2.shape:
        raise ValueError("f1 and f2 must have identical 3-D shapes")
    if f1.shape[0] == 0 or f1.shape[1:] != (2, len(time)):
        raise ValueError("expected cause CIF arrays (N,2,K) and N>0")
    if not np.isfinite(f1).all() or not np.isfinite(f2).all():
        raise ValueError("CIF contains non-finite values")
    if np.min(f1) < -PROB_TOL or np.min(f2) < -PROB_TOL:
        raise ValueError("CIF contains negative probabilities")
    if np.max(f1 + f2) > 1.0 + PROB_TOL:
        raise ValueError("two competing CIFs sum to more than 1")
    if np.any(np.diff(f1, axis=-1) < -PROB_TOL) or np.any(np.diff(f2, axis=-1) < -PROB_TOL):
        raise ValueError("CIF must be nondecreasing in time")
    if np.max(np.abs(f1[..., 0])) > PROB_TOL or np.max(np.abs(f2[..., 0])) > PROB_TOL:
        raise ValueError("this prototype requires zero incidence at t=0")


def interior_quantile(time: np.ndarray, cif: np.ndarray, p: float) -> np.ndarray:
    """Piecewise-linear inverse on a supplied time grid; NaN if no strict interior.

    This is a grid-based numerical approximation to the inverse of continuous
    CIFs. It is not an estimator and must not be represented as exact inversion.
    """
    n, a, k = cif.shape
    reached_inside = (cif[..., -1] > p + PROB_TOL)
    idx = np.sum(cif < p, axis=-1)
    upper = np.minimum(idx, k - 1)
    lower = np.maximum(upper - 1, 0)
    yhi = np.take_along_axis(cif, upper[..., None], axis=-1)[..., 0]
    ylo = np.take_along_axis(cif, lower[..., None], axis=-1)[..., 0]
    q = np.full((n, a), np.nan, dtype=float)
    at_zero = (upper == 0) & reached_inside
    q[at_zero] = time[0]
    regular = (upper > 0) & reached_inside
    frac = np.zeros_like(q)
    np.divide(p - ylo, yhi - ylo, out=frac, where=regular & (yhi > ylo))
    interpolated = time[lower] + np.clip(frac, 0, 1) * (time[upper] - time[lower])
    q[regular] = interpolated[regular]
    return q


def audit(time: np.ndarray, f1: np.ndarray, f2: np.ndarray, grid_size: int = 199):
    validate(time, f1, f2)
    if not 9 <= grid_size <= 9999:
        raise ValueError("grid_size must be 9..9999")
    pall = f1 + f2
    n = len(f1)
    # Scan all of (0,1). This is a numeric mesh, not an optimized/chosen p.
    levels = np.arange(1, grid_size + 1, dtype=float) / (grid_size + 1)
    last = np.zeros(n, dtype=np.int8)
    flipped = np.zeros(n, dtype=bool)
    had_a_sign = np.zeros(n, dtype=bool)
    rows = []
    qtol = 1e-9 * max(1., time[-1])

    for p in levels:
        r1 = np.all(f1[..., -1] > p + PROB_TOL, axis=1)
        ra = np.all(pall[..., -1] > p + PROB_TOL, axis=1)
        q1 = interior_quantile(time, f1, float(p))
        delta = q1[:, 1] - q1[:, 0]
        pos = r1 & (delta > qtol)
        neg = r1 & (delta < -qtol)
        ties = r1 & ~pos & ~neg
        sign = np.zeros(n, dtype=np.int8)
        sign[pos] = 1
        sign[neg] = -1
        flipped |= (last != 0) & (sign != 0) & (sign != last)
        last = np.where(sign != 0, sign, last)
        had_a_sign |= sign != 0
        denom = int((pos | neg).sum())
        rows.append({
            "p_diagnostic_only": float(p),
            "priority_both_treatments_strict_interior_pct": float(100 * r1.mean()),
            "overall_both_treatments_strict_interior_pct": float(100 * ra.mean()),
            "joint_at_same_p_strict_interior_pct": float(100 * (r1 & ra).mean()),
            "priority_treatment1_better_pct_among_nonties":
                float(100 * pos.sum() / denom) if denom else None,
            "priority_ties_pct_among_strict_interior":
                float(100 * ties.sum() / r1.sum()) if r1.any() else None,
            "priority_nontie_patients": denom,
        })

    summary = {
        "n_patients": int(n),
        "n_treatments": 2,
        "n_time_points": int(time.size),
        "time_horizon_in_input_units": float(time[-1]),
        "diagnostic_grid_points": int(grid_size),
        "strict_interior_flip_ever_pct_all_patients": float(100 * flipped.mean()),
        "has_non_tied_reachable_point_pct": float(100 * had_a_sign.mean()),
        "note": (
            "Diagnostic p scan only. No p, delta, clinical utility or estimator was "
            "selected. Piecewise-linear interpolation of supplied CIF time grid."
        ),
    }
    return rows, summary


def self_test() -> None:
    time = np.array([0., 1., 2.])
    # Person 0 has strictly interior quantile ordering reversal near p=.2.
    # Person 1 remains ordered and does not cross.
    f1 = np.array([
        [[0., .20, .30], [0., .15, .45]],
        [[0., .10, .20], [0., .08, .18]],
    ], dtype=float)
    f2 = np.array([
        [[0., .02, .04], [0., .03, .06]],
        [[0., .04, .08], [0., .02, .04]],
    ], dtype=float)
    rows, summary = audit(time, f1, f2, 99)
    assert len(rows) == 99
    assert abs(summary["strict_interior_flip_ever_pct_all_patients"] - 50) < 1e-10
    at_p10 = next(x for x in rows if abs(x["p_diagnostic_only"] - .1) < 1e-9)
    assert at_p10["priority_both_treatments_strict_interior_pct"] == 100.
    at_p35 = next(x for x in rows if abs(x["p_diagnostic_only"] - .35) < 1e-9)
    assert at_p35["priority_both_treatments_strict_interior_pct"] == 0.
    try:
        broken = f1.copy()
        broken[0, 0, 2] = .01
        validate(time, broken, f2)
        raise AssertionError("incorrectly accepted decreasing CIF")
    except ValueError:
        pass
    print("PASS N1 self-test: support, strict interior, rank flip and invalid CIF")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--input", type=Path, help="NPZ with time, f1, f2")
    parser.add_argument("--output", type=Path, help="new output directory")
    parser.add_argument("--grid-size", type=int, default=199,
                        help="numerical resolution; NOT a scientific risk threshold")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.input or not args.output:
        parser.error("both --input and --output are required")
    with np.load(args.input, allow_pickle=False) as arrays:
        time, f1, f2 = (np.asarray(arrays[k], float) for k in ("time", "f1", "f2"))
    rows, summary = audit(time, f1, f2, args.grid_size)
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "risk_level_support.csv").open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (args.output / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("PASS N1 risk-level audit; no scientific risk threshold selected")


if __name__ == "__main__":
    main()
