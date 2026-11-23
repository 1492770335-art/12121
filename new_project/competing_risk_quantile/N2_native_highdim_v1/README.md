# N2-H1｜八维非线性和时变竞争风险的原生分位数估计器压力试验

**课题主线**：固定治疗、给定协变量时估计原因1/全部首次事件的条件 CIF 分位数 Q1 与 Qall，并比较 Peng–Fine、CR-RSF、SurvivalBoost 原生方法。

- [先提交的冻结实验方案](PROTOCOL.md)
- [数据与解析 Oracle 核验](ORACLE_AUDIT.md) · [真实可达水平表](ORACLE_SUPPORT.csv) · [72份数据哈希清单](FROZEN_SHA256.json)
- [代码与复现](src/) · [运行记录（触发后更新）](https://github.com/1492770335-art/12121/actions/workflows/n2-native-highdim-v1.yml)
- 预设 8 基线协变量，三个机制（两个强错设，一项 log-linear 控制），n=500/1000、两删失、4 配对重复；先完成原生适配与 Oracle 验证，不用原论文 Cox 模型。
- 预定主要结果 Q1 与 Qall 的 **同患者共同可评分 MAE**；同时报告成功率、可达误报/漏报、训练内选参及运行耗时。若原生任务尚未实际完成，任何旧阶段的 MAE 均不能冒充本轮结论。
- `hd_correct` 仅作为正向模型结构控制，在主分析中只宏平均两个复杂机制。

历史：N2-T2 八重复在低维机制下 Peng–Fine 误差较低，但存在两次原生拟合失败。N2-H1 **单独测试高维/复杂相互作用的适用边界**，不是改动旧数据追求某法胜出。
