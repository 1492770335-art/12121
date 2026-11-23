# N2-T2 | 独立重复下的原生竞争风险条件分位数估计

**状态**：冻结协议及 SHA256 已提交；生成器、原生方法适配、统一训练内评分和聚合程序已提交，待 GitHub Actions 运行本轮新数据。

本实验的独立研究对象是 **条件竞争风险 CIF 分位数**，不是旧论文 Cox 模型或其两阶段治疗决策规则。

- [预先冻结方案](PROTOCOL.md)（commit `b906c4c7`）：12 次独立训练重复、两档删失、n=1000，三种机制。
- [108 份 CSV 的 SHA-256 及场景说明](FROZEN_SHA256.json)：包含 72 份训练样本和 36 份独立 Oracle 测试集；生成后在本地已经校验，原生拟合前在 Actions 再核验。
- [生成器](src/generate.py)、[哈希核验](src/validate.py)。
- [原生 Peng–Fine/CR-RSF](src/run_native_r.R)、[原生 SurvivalBoost](src/run_boost.py)、[共同训练内 IPCW 分位数评分](src/validation_score.py)。
- [逐患者汇总](src/analyze.py)、[分片核验](src/stitch.py)、[原生拟合状态审计](src/collect_fits.py)。

**前人工作限制**：N2-T1 四次重复的优劣不直接带入新表；n=1000、12 次重复仍然只是更可靠的**配对稳健性试验**，不是 100 重复的论文终局实证。正确设定控制 `logquantile_correct` 不参与两个主机制均值。

**预定结果文件**：`results/all_patient_predictions.csv.gz`、`results/replicate_level_mae.csv`、`results/replicate_level_pairwise.csv`、`results/paired_mc_summary.csv`、`results/replicate_level_ranking.csv`、`results/quality.json`；另保留实际运行的原生失败数和参数选择。

**诚信规则**：尚未运行的结果一律不填，运行失败的模型保持 missing；不得用旧 N2-T1 结果替代本轮预测。
