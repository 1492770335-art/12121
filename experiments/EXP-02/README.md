# EXP-02：总体分位数保护与 RMET 保护

本目录按 `research/2026-11-23/04_EXP02_总体Q保护与RMET保护_定向分析任务.md` 执行。比较的两条 Oracle 规则共用真实重点分位数目标，仅第一层的总体保护量不同。固定 `p_all=0.50`、`p_1=0.10`、`L=36` 月、`δ_Q=3` 月；原机制、种子和 200 次各 5,000 人的测试流未改动。仅重建 `PH_tradeoff` 与 `time_cross`。

## 输入与数据可用性

原始输入位于 `literature/quantile_treatment_rules/oracle_20261123/original/`。运行 `restore.py` 后得到原 ZIP，SHA-256 必须为 `4700ea52b9a50c0d96786965ad4fe13e30b0b40952292bc396700699c34a06b7`，长度 3,875,284 字节。分析脚本再次核验 SHA-256，再把 ZIP 只读解压到临时目录并导入其中的 `src/oracle.py`。

归档有 `config.json`、原生源码和测试、`results/calibration_raw.csv`、逐次的 `pairs_raw.csv`、`policies_raw.csv`、`subgroups_raw.csv`，以及相应汇总；**没有逐患者协变量、两治疗真值、候选集合和推荐记录**。因此本目录的逐患者结果是按原 `SeedSequence([seed, scenario_index, rep])` 精确重建的定向 Oracle 补充。脚本逐重复逐指标与原 `pairs_raw.csv` 交叉核对，不从汇总表反推个体值。归档中的五机制主实验未重跑。`δ_R` 从独立原校准流精确复算，并与原 `calibration_raw.csv` 比对；最终测试患者没有参与校准。

## 运行

Python 3.13.5，使用归档 `requirements.txt` 中的 NumPy 2.5.5、pandas 3.1.1、SciPy 1.18.1、Matplotlib 3.11.2。仓库根目录运行：

```powershell
python literature/quantile_treatment_rules/oracle_20261123/original/restore.py
python experiments/EXP-02/src/analyze_existing_oracle.py
python experiments/EXP-02/src/plot.py
python experiments/EXP-02/tests/test_consistency.py
```

原始 `tests/test_oracle.py` 也通过 3 项测试；EXP-02 通过 4 项测试。主结果见 [REPORT.md](REPORT.md)。

## 输出说明

- `results/table_A_candidate_sets.csv`：第一层候选集合分解、最终处方及 Monte Carlo 标准误。
- `results/table_B_counterfactual_outcomes.csv`：全体、改判、方向与严格内点人群的真实配对结局；含 Q 和 R 各自的绝对均值及差值。
- `results/table_C_reachability_heterogeneity.csv`：可达性、固定总体四分位 `Z1` 与 `Z2` 二分组。
- `results/replicate_*.csv`：按 200 次重复保留计数与和，可重算上述 MCSE。
- `results/changed_patients.csv`：两机制所有改判患者的协变量、候选、处方、两治疗分位数/RMET 与配对结局差。没有保存未改判者的全量微观 CSV；可由冻结种子与脚本精确重建。
- `results/boundary_plot_sample.csv`：按患者序号预设的背景散点抽样，仅供绘图。`results/audit.json` 记录配置与重放结论。
- `figures/`：候选边界、改判结局联合分布与固定 3 位代表患者的曲线。

CSV 中 `*_month` 为月，`*_pp` 为百分点；`Q_`、`R_` 前缀表示两条规则下的绝对真值，未加前缀是 Q–Q 减 RMET–Q1。`*_mcse` 以重复为单元计算模拟积分误差，并非临床推断区间。分位数是条件 CIF 达到指定概率的时间；政策平均条件分位数不是政策诱导总体的边际分位数。
