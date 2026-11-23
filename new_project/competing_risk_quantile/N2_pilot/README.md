# N2 Pilot | Right-censored competing-risk conditional quantiles

**Independent research branch of `new_project/competing_risk_quantile/`.**

This is an executed pilot comparing two *non-Cox*, *non-identical* outcome
learning strategies on one common conditional competing-risk quantile estimand.
It does **not** inherit old thesis risk thresholds, tolerance budgets, or
clinical data. All numbers are diagnostic and in abstract time units.

- [Full statistical report (Chinese)](REPORT.md)
- [Main experiment source](src/n2_pilot.py)
- [Paired summary and validation](src/analyze_results.py)
- [Replicate-level data](results/n2_replicate_results.csv)
- [Paired MC differences](results/n2_paired_differences.csv)
- [Quality audit](results/n2_quality_report.json)

Commands:

```bash
python src/n2_pilot.py --self-test
python src/n2_pilot.py --reps 32 --ntrain 900 --ntest 1000 --out results
python src/analyze_results.py
```

Dependencies: Python 3.11+, numpy, scipy, pandas, scikit-learn.
Direct estimator is a *smoothed IPCW GMM prototype inspired by* Peng–Fine,
**not** their published estimator. The joint estimator is a simple IPCW
multinomial baseline; Alberge et al. (2025) already studied proper IPCW
competing-risk classification losses. See report for limitations and diagnostics.