# N2-T1：训练内调参和非线性竞争风险条件分位数实验

**状态：执行中，协议先于数据生成；未完成原生拟合前不宣布模型赢家。**

- [冻结协议](PROTOCOL.md)，2026-11-23，先于本轮生成／拟合提交
- [数据 SHA-256 冻结表](FROZEN_SHA256.json)：80 份训练 + 40 份独立 Oracle 测试 CSV
- [解析生成器](src/generate.py)；[哈希校验](src/validate.py)
- [训练内 IPCW 分位数 check loss](src/validation_score.py)
- [原生 Peng–Fine / CR-RSF](src/run_native_r.R)；[原生 SurvivalBoost](src/run_boost.py)
- [统一逐患者评分](src/analyze.py)，以及 [分片数据合并](src/stitch.py)

## 目标

**选择条件原因别 CIF 分位数估计方法**，而不是研究拒绝推荐或将某个治疗规则预设为最优。两个独立估计目标：

\[
Q_{1}^{a}(p\mid z)=\inf\{t\le L:F_1^a(t\mid z)\ge p\},\quad
Q_{all}^{a}(p\mid z)=\inf\{t\le L:(F_1^a+F_2^a)(t\mid z)\ge p\}.
\]

主结果同一患者—治疗—p 的共同可评分 MAE，辅以各方法漏报、误报、失败率、train-only 选参频率和计算耗时。**正确设定的 log-quantile 机制独立报告，不加入一般机制的总体比较。**

## 数据机制

前三个一般机制 `aligned, cause_tradeoff, time_varying` 直接调用 N1 的解析分段风险生成器；`logquantile_correct` 沿用 N2-S2 的 Weibull scale 模型，用于检查 Peng–Fine 的 log-quantile 结构正确设定控制。`nonlinear_interaction` 按 N1 `time_varying` 分段原因风险为基础，只对治疗 1 的原因风险乘以预先指定的非线性因子：

- 原因 1、早期：`exp(.55 sin(pi z1) + .35 (z1² - 1/3))`
- 原因 1、晚期：`exp(-.45 sin(pi z1) + .55 (z1² - 1/3))`
- 原因 2、早期：`exp(-.40 sin(pi z1/2) - .30 z1²)`
- 原因 2、晚期：`exp(+.40 sin(pi z1/2) + .20 z1²)`

固定生成种子 `2026112351`，`L=3` 抽象时间单位，训练 n=500/1000，重复 4 次，两档目标删失 20%/45%，测试 180 人且每人评价两治疗。模型同时估计原因1 `p={.06,.12,.18,.24}` 与总体 `p={.15,.25,.35,.45}`。这些是诊断网格，**不是临床阈值**。

## 训练内超参数选择

同一训练样本先以固定随机数、与观测结局无关的方式拆分 **75% 拟合、25% 验证**，两档删失使用相同验证病人 ID。对候选模型，在验证样本上针对被删失校正的目标时间 pseudo-outcome 计算 IPCW 加权 pinball loss，**G_C 仅通过拟合子集的 KM 估计**。所有方法在同样 p 网格、Q1/Qall 上等权评分；风险在窗口内不可达时，**仅验证分位数损失的截断目标**将预测值取 L，正式 Oracle MAE 仍将无有限根者记 NA。

- Peng–Fine：线性矩阵 `(a,z1,z2,a z1)` vs 再加 `(z1²,a z1²)`；原生 `cmprskQR::crrQR` 拟合 2 类目标并按同一验证损失选设计。
- CR-RSF：固定 `ntree=160, nsplit=5`，选择 `nodesize=5` 或 `20`。
- SurvivalBoost：固定 `learning_rate=.05,max_leaf_nodes=7,min_samples_leaf=20`，选择 `n_iter=40` 或 `100`。

对有效候选选择验证分数较低者后，在**全部训练样本**重新拟合，预测完全独立的测试数据。若候选程序失败，保留错误和所剩候选；不能将自写简化估计器当作文献方法。

## 可复现执行命令

```bash
python src/generate.py --output data
python src/validate.py --data data --frozen FROZEN_SHA256.json
# 原生 R 环境：
Rscript src/run_native_r.R data results_r/aligned_n500 aligned 500 src/validation_score.py
# 官方 hazardous 环境：
python src/run_boost.py --data data --output results_py/aligned_n500 --mechanism aligned --ntrain 500
# GitHub Actions 汇总原生分片结果后调用：
python src/analyze.py --data data --r-pred combined/r_predictions.csv --py-pred combined/python_predictions.csv --output results
```

实际运行均在 GitHub Actions 的 R/Python 环境中完成并上传 artifact。上述相对路径命令需在本文件所在目录执行。

**判定纪律**：四个重复不足以得出可靠显著性结论；强非线性机制与正确设定机制结果须单列，不靠人为挑有利的 DGP、p 或超参下最终赢家结论。
