# N2-H1｜模型拟合前独立生成数据与 Oracle 核验

预先冻结方案 commit: `9de4c9e620083b3ebcc952244b6f8c62c563d438`。在方案提交后才生成本轮输入。

- 基础维度 8，其中 Z1、Z3..Z8 连续，Z2 为 Bernoulli；新高维错设机制和正向 log-linear 控制均为解析竞争风险真值。
- 研究窗口 L=3，原因别风险分段切换 1.2；风险模型仅是 DGP，不是 Cox 估计器。
- 按新种子 `2026112371` 生成 48 个训练 CSV + 24 个独立 Oracle CSV，共 72 个文件；全部 SHA256 由 `FROZEN_SHA256.json` 锁定。
- `python src/validate.py --data data --frozen FROZEN_SHA256.json` 检查 72 个哈希并通过。
- 生成器逐患者抽检 `F_j(Q_j(p))=p`，并使用 N1 解析 CIF 函数计算每个独立样本真值。

| 机制 | 删失目标 | 实际删失均值 | 最小 | 最大 |
|---|---:|---:|---:|---:|
|hd_correct|20%|20.07%|18.40%|21.20%|
|hd_correct|45%|45.15%|42.50%|47.60%|
|hd_crossing|20%|20.65%|18.50%|22.00%|
|hd_crossing|45%|46.09%|43.20%|49.70%|
|hd_nonlinear|20%|20.29%|18.60%|21.80%|
|hd_nonlinear|45%|46.48%|45.50%|47.40%|

## 独立 Oracle 支持诊断（并非临床选取）

|机制|终点|p|真值有限比例|
|---|---|---:|---:|
|hd_correct|q1|0.06|100.00%|
|hd_correct|q1|0.12|100.00%|
|hd_correct|q1|0.18|100.00%|
|hd_correct|q1|0.24|100.00%|
|hd_correct|qall|0.15|100.00%|
|hd_correct|qall|0.25|100.00%|
|hd_correct|qall|0.35|100.00%|
|hd_correct|qall|0.45|100.00%|
|hd_crossing|q1|0.06|100.00%|
|hd_crossing|q1|0.12|100.00%|
|hd_crossing|q1|0.18|99.97%|
|hd_crossing|q1|0.24|99.38%|
|hd_crossing|qall|0.15|100.00%|
|hd_crossing|qall|0.25|100.00%|
|hd_crossing|qall|0.35|100.00%|
|hd_crossing|qall|0.45|100.00%|
|hd_nonlinear|q1|0.06|100.00%|
|hd_nonlinear|q1|0.12|99.65%|
|hd_nonlinear|q1|0.18|95.69%|
|hd_nonlinear|q1|0.24|85.90%|
|hd_nonlinear|qall|0.15|100.00%|
|hd_nonlinear|qall|0.25|100.00%|
|hd_nonlinear|qall|0.35|100.00%|
|hd_nonlinear|qall|0.45|100.00%|

这些风险水平来自前轮统一诊断网格；不可达比例是估计质量评价条件，不开发拒绝治疗策略。

**拟合结果尚未包含在本审计中**；必须以 GitHub Actions 原生 R/Python 产物为准。

## 运行环境哈希审计补充

本地 72 份CSV的SHA256已按 `FROZEN_SHA256.json` 验证，但 GitHub CI 重新生成时浮点文本可能不完全同字节；首次 CI 在拟合前的比对关口**失败停止**。修订后CI**只生成一次**，在任何估计器拟合前冻结 `data/CI_FROZEN_SHA256.json`，然后由R与Python三个方法任务共享同一文件artifact，并逐文件核对CI哈希。最终 CI 哈希须随真实结果归档；不能声称本地与CI文件逐字节相同。生成机制、种子、研究目标和评价 p 网格均未改动。
