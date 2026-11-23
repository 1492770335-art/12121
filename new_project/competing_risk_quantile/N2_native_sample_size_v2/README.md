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

## 结果状态

本目录上传时**仅完成方案冻结、数据生成及哈希/解析反演核验**。执行 GitHub Actions 后才能产生真实原生拟合指标。`results/` 目录若无文件，表示估计/汇总尚未完成，而非“零误差”。

本实验只含每格 3 次训练重复，是**样本量趋势及软件稳健性扩展性研究**，不是最终显著性比较；目前三方法配置未实现同等强度交叉验证调参，不可声称全体参数空间的最佳方法。
