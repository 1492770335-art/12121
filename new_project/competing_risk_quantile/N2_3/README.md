# N2-3 | 非 Cox 竞争风险分位数：可达性门控与实际推荐代价

**研究日期**：2026-11-23。**状态**：已执行的探索性 Monte Carlo 试验（32 次/格）；不是最终发表级算法，不是旧论文 Cox 方案，也不是临床试验。  
**项目目录**：`new_project/competing_risk_quantile/N2_3/`；需要同级既有 `N2_pilot/src/n2_pilot.py`。原 `N2_pilot` 与 `N2_2` 只读保留。

## 本轮问题

在统一的原因别 CIF 分位数目标下，**增加一个 IPCW 终点状态概率模型，先判断 p 是否可达，再输出直接估计的分位数**，能否减少“不可能达到的风险水平仍返回有限分位数”错误？是否同时降低治疗决策错误，还是仅把错误转成“错误拒绝”和“未决处置”？

## 完整研究结果

- [`REPORT.md`](REPORT.md)：正式中文统计研究解读，包括负面结果、分母、潜在失败原因与后续方案。
- [`src/n2_3_gate.py`](src/n2_3_gate.py)：独立新增的 IPCW 三状态期末分类器、门控、结构投影与相同患者评价。
- [`src/analyze_n2_3.py`](src/analyze_n2_3.py)：对重复级原始输出计算配对 Monte Carlo 差异及不同未决回退行为。
- [`src/validate_n2_3.py`](src/validate_n2_3.py)：原 N2-2 前 8 次重放、概率/行数和分类不变量核验。
- [`results/n2_3_compact.csv`](results/n2_3_compact.csv)：三机制、三个 p、五方法的 45 行可读汇总。
- [`results/n2_3_paired_mc.csv`](results/n2_3_paired_mc.csv)：32 次重复配对差值/MCSE/探索性区间。
- [`results/n2_3_fallback_sensitivity.csv`](results/n2_3_fallback_sensitivity.csv)：未决时处置为治疗0、治疗1、均匀随机时的差异。
- [`results/n2_3_replications.csv.gz`](results/n2_3_replications.csv.gz)：**2,880 条完整重复级结果，gzip 压缩**；解压后文件名 `n2_3_replications.csv`。
- [`results/n2_3_summary.csv`](results/n2_3_summary.csv)：90 组统计量及 MCSE。
- [`results/validation.json`](results/validation.json)：原 N2-2 完全一致性检验结果。
- [`results/config.json`](results/config.json)：冻结配置与来源。

## 复现命令

在仓库根目录：

```bash
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
python new_project/competing_risk_quantile/N2_3/src/n2_3_gate.py --self-test
python new_project/competing_risk_quantile/N2_3/src/n2_3_gate.py --reps 32 --ntrain 900 --ntest 1000 \
  --out new_project/competing_risk_quantile/N2_3/results
python new_project/competing_risk_quantile/N2_3/src/analyze_n2_3.py 
python new_project/competing_risk_quantile/N2_3/src/validate_n2_3.py
```

`analyze_n2_3.py`、`validate_n2_3.py` 可直接读取 `results/n2_3_replications.csv.gz`，无需先解压；如再次运行主实验，请将新输出指定为 `results/`。

依赖：Python 3.11+、numpy、pandas、scipy、scikit-learn。研究只对模拟真 CIF 做评价，没有使用真值作为训练门控标签。

**重要限制**：所谓直接方法是 Peng–Fine 思路启发的平滑 IPCW 原型，而非作者原生算法；终点分类器与联合 CIF 分类器均为简单非 Cox 基线。不能据此宣称“可达性分类具有有限样本安全保证”或“提出全新受约束治疗学习方法”。
