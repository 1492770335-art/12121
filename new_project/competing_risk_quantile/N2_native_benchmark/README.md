# N2 Native Benchmark / 首轮原生分位数估计试跑

本次研究**先提交 PROTOCOL.md（91abab07），再生成训练数据与 Oracle 真值，并冻结 9 个 CSV 的 SHA-256**。不使用 Cox 估计、不继承旧课题临床阈值。

- [预先提交的方案](PROTOCOL.md)
- [可执行数据生成器](src/generate.py)
- [数据冻结哈希](FROZEN_SHA256.json)
- [Peng–Fine 与 CR-RSF 的 R 原生调用](src/run_r_estimators.R)
- [SurvivalBoost 的 Python 原生调用](src/run_survivalboost.py)

三机制（同向、原因取舍、时变）×两档目标删失（20%/45%）；训练每格 400 名患者、独立测试每机制 120 名患者，每人预测两治疗。首次试跑只有每格**一次重复**，不能据此给出方法优劣结论。诊断 p 为 0.06、0.12、0.18、0.24；尚无最终临床阈值。

数据生成采用相同新课题 N1 已归档的解析 competing-risk CIF 模型与固定种子 20261123。训练数据含观测首次失效/删失时间、原因状态及随机治疗；对每名独立测试对象输出两个治疗的真实原因 CIF 和可达的原因分位数。

## 原生环境依赖

- R: cmprskQR::crrQR（Peng–Fine 2009）；randomForestSRC::rfsrc competing-risk CIF
- Python: hazardous.SurvivalBoost（Alberge 等 2025）
- GitHub Actions 的工作流使用固定模拟数据进行原生软件安装、拟合与结果保存。运行状态必须根据实际 workflow jobs/logs 核验，不能把“已提交工作流”误写成“三种方法已成功运行”。

## 统计评价

统一比较原因1患者条件分位数在 [0,3] 的严格内点 MAE、真实/预测可达率、不可达误报、可达漏报、有效评分数量、拟合失败，以及 CIF 单调性。**不能只报告成功预测者的 MAE，也不能通过拒绝预测让误差虚假改善**。

首轮仅验证原生调用和量级；后续有了充分配对重复、共同调参协议及有效样本支持，才可研究哪个估计方法在不同机制更合适。
