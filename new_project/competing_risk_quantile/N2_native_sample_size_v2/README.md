# N2-S2 原生分位数估计方法：三样本量＋模型正确性检验

**主题限定：竞争风险数据下的条件分位数估计方法选型。** 原生 Peng–Fine、CR-RSF、SurvivalBoost；终点为原因1 CIF 条件分位数 Q1 与总体首次事件 Qall，决策排序仅为次要诊断。

研究方案已在代码和数据生成前提交：[PROTOCOL.md](PROTOCOL.md)。

## 数据设计

- **n=500、1000、2000**；3 个训练重复；4 个机制（既有 N1 三机制和直接对数分位数线性正确设定机制）；删失目标 20%、45%；72 组训练数据、36 组独立测试数据。
- 重点风险概率网格 0.06、0.12、0.18、0.24；总体概率网格 0.15、0.25、0.35、0.45。全部为方法学诊断参数；没有旧论文的临床 50%/10%/3 月偏好设定。
- 本地在模型拟合之前计算并冻结 [FROZEN_SHA256.json](FROZEN_SHA256.json) 中 108 份 CSV 的 SHA-256；GitHub Actions 必须先核对哈希才拟合。
- 软件是原生 `cmprskQR::crrQR`、`randomForestSRC::rfsrc`、`hazardous.SurvivalBoost`。不是自写的替代分位数回归或 Cox 拟合。

## 复现流程


tools: Python 3.11 / R release；本地无 R 时使用 GitHub Actions [工作流](../../../.github/workflows/n2-native-samplesize-v2.yml)（实际路径为仓库根目录 `.github/workflows/n2-native-samplesize-v2.yml`）。

```bash
python src/generate.py --output data
python src/validate.py --data data --frozen FROZEN_SHA256.json
# 原生 R/Python 方法由工作流原生环境执行，记录原生失败及版本
# 工作流合并输出后运行：
python src/stitch.py --r-root stage/r --py-root stage/py --out stage/combined
python src/analyze.py --data data --r-pred stage/combined/r_predictions.csv \
  --py-pred stage/combined/python_predictions.csv --output results
```

## 已完成的原生模型运行与结果

**状态：2026-11-23 已实际运行、全任务 SUCCESS。** [GitHub Actions #45179269757](https://github.com/1492770335-art/12121/actions/runs/45179269757)。包含冻结数据 108 份 CSV、72 个训练设置、三种真实原生方法，实际原生拟合检查 0 次失败。结果由 Actions 合并程序独立写入仓库 `results/`，主研究问题始终是 Q1 / Qall 条件分位数估计方法的比较。

- [完整统计评审](STATISTICAL_REVIEW.md)：方法设计、三样本量逐终点 MAE、正确设定控制、局部分位点例外和限制。
- [逐人完整配对预测（gzip）](results/all_patient_predictions.csv.gz)：207,360 行患者—治疗—p 对照。
- [逐训练重复、逐方法 MAE](results/replicate_level_mae.csv)；[配对差异和 Monte Carlo 标准误](results/paired_mc_summary.csv)。
- [可达支持／错误质量审计](results/quality.json)；[次要治疗排序诊断](results/replicate_level_ranking.csv)。

**主要发现（仅在三种一般机制、三方法共同可评分的同一组患者上）：**
Q1 的 Peng–Fine MAE 按 n=500/1000/2000 分别是 0.21583、0.13716、0.09971，低于同组 CR-RSF 和 SurvivalBoost；Qall 同样呈现较低误差。新增正确设定控制另表报告。**但每格仅 3 次重复且缺公平调参，不作最终显著优效或临床阈值结论。**