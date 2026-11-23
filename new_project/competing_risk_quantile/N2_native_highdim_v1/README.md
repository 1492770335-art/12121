# N2-H1｜八维非线性和时变竞争风险的原生分位数估计器压力试验

**课题主线**：固定治疗、给定协变量时估计原因1/全部首次事件的条件 CIF 分位数 Q1 与 Qall，并比较 Peng–Fine、CR-RSF、SurvivalBoost 原生方法。

- [先提交的冻结实验方案](PROTOCOL.md)
- [数据与解析 Oracle 核验](ORACLE_AUDIT.md) · [真实可达水平表](ORACLE_SUPPORT.csv) · [72份数据哈希清单](FROZEN_SHA256.json)
- [代码与复现](src/) · [运行记录（触发后更新）](https://github.com/1492770335-art/12121/actions/workflows/n2-native-highdim-v1.yml)
- 预设 8 基线协变量，三个机制（两个强错设，一项 log-linear 控制），n=500/1000、两删失、4 配对重复；先完成原生适配与 Oracle 验证，不用原论文 Cox 模型。
- 预定主要结果 Q1 与 Qall 的 **同患者共同可评分 MAE**；同时报告成功率、可达误报/漏报、训练内选参及运行耗时。若原生任务尚未实际完成，任何旧阶段的 MAE 均不能冒充本轮结论。
- `hd_correct` 仅作为正向模型结构控制，在主分析中只宏平均两个复杂机制。

历史：N2-T2 八重复在低维机制下 Peng–Fine 误差较低，但存在两次原生拟合失败。N2-H1 **单独测试高维/复杂相互作用的适用边界**，不是改动旧数据追求某法胜出。

**复现口径说明**：`FROZEN_SHA256.json` 是本地生成的72份 CSV 的参考哈希。首次 GitHub Actions 生成器运行通过了解析反演，但与本地的CSV字节哈希不完全相同，因此**没有进入拟合**。修订后的 GitHub Actions 在唯一的 `frozen-data` job 中生成数据并立即复制 `manifest.json` 为 `CI_FROZEN_SHA256.json`，在每个原生方法任务中核对同一份不可变数据 artifact，且在最终结果中保留 CI 的真实哈希清单。这比假称跨运行环境位级一致更准确；本轮数值以实际 CI 同批数据为准。原始本地哈希不删除或改写。

## 已完成：原生三方法估计及独立统计评审（2026-11-23）

- [完整独立统计评审](STATISTICAL_REVIEW.md)（含高维分机制比较、训练重复配对差、四重复 MCSE、正向控制与研究限制）。
- [真实 GitHub Actions #45213043665](https://github.com/1492770335-art/12121/actions/runs/45213043665)：frozen-data、6 R、6 Python、combine 共 **14 jobs SUCCESS**。已独立从全部 12 份原生分片 artifact 验证 **144/144 次全训练集模型拟合成功**。
- [逐患者与重复级数值](results/) · [四个主宏平均结果 CSV](results/MAE_MACRO_TWO_HIGH_DIMENSIONAL_MECHANISMS.csv) · [原生拟合审计](results/native_fit_audit.json) · [实际训练内选参记录](results/native_fit_selection.csv)。
- 完整 138,240 条患者—治疗—p Oracle 记录；严格可达 137,122；三法共同可评分 134,557（真实可达的 98.13%）。对真实不可达的风险水平不以 L 冒充有限 Q。

| 目标 | n | Peng–Fine | CR-RSF | SurvivalBoost |
|---|---:|---:|---:|---:|
| Q1 | 500 | 0.3781 | **0.3144** | 0.3626 |
| Q1 | 1000 | 0.2987 | **0.2924** | 0.3006 |
| Qall | 500 | 0.2531 | **0.1798** | 0.2125 |
| Qall | 1000 | 0.1943 | 0.1688 | **0.1584** |

**统计意义**：仅对两个复杂机制做等权主平均；`hd_correct` 正向模型结构控制单列。高维下原生 CIF 反演路线取得明显竞争力，反驳“Peng–Fine 在所有数据结构中必然最好”，但四次独立训练重复尚不足以最终选定赢家。不同模型训练内搜索空间仍有限，计算预算也不是严格匹配。

**哈希说明**：本地的 `FROZEN_SHA256.json` 与 CI 重新生成的 CSV 在字节上不完全一致。首次 CI 在拟合前停止；有效第二次 CI 在同一数据 job 内只生成一次并保存 `data/CI_FROZEN_SHA256.json`，所有模型共享不可变 artifact，最终的 CI 真哈希另外归档在 `results/CI_FROZEN_SHA256.json`。
