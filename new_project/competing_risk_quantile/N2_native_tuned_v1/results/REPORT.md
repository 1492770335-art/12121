# N2-T1 原生估计器样本量与正确设定机制试验：自动汇总报告

**性质：**独立新课题，主要比较 Q1 与 Qall 的分位数估计；本轮 4 次训练重复为方法验证，不支持临床优效/最终模型选择。

- Oracle 逐患者—治疗—p 记录：230400。
- 真实严格内点记录：229512；三方法共同可评分：223333。

|方法|有限预测数|真实可达漏报|真实不可达误报|预测时间恰为0|
|---|---:|---:|---:|---:|
|PengFine|225824|4011|323|0|
|CRRSF|227897|1997|382|0|
|SurvivalBoost|228262|1649|399|52|

具体数值详见 replicate_level_mae.csv、replicate_level_pairwise.csv、paired_mc_summary.csv、replicate_level_ranking.csv。

**限制**：只有 4 个重复；原生算法函数类和超参不同；仅能在共同可评分人群上严格配对，必须同时报告各方法的可达率与漏报。

此文由 analyze.py 从实际预测表生成，不是预先猜测的赢家报告。

**本轮额外事实：** Peng–Fine 在 `cause_tradeoff,n=500,replicate=1,censor_target=45` 出现一次原生全样本重拟合维度错误；`native_fit_audit.json` 记录了完整错误。该样本对应的 2,833 条真实有限分位数均缺少 Peng–Fine 预测，三方法共同评分数因此为零；原始结果没有被重填。请同时参阅正式 [STATISTICAL_REVIEW.md](../STATISTICAL_REVIEW.md)。
