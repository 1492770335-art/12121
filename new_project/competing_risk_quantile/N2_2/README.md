# N2-2｜非 Cox 竞争风险条件分位数的可达性、联合相容性与治疗排序审计

**独立新课题**：`new_project/competing_risk_quantile/`。**状态**：已运行定向先导审计，尚不是正式方法学优效研究，也未决定临床概率阈值或完整治疗规则。

本研究对 [N2_pilot](../N2_pilot/README.md) 的**前 8 次冻结随机数流**进行逐患者重放，而不是重新设计有利于某种估计器的数据或重复原完整 32 次试验。N2 使用的已知竞争风险 Oracle 分布，非 Cox 直接分位数原型（受 Peng–Fine 启发）和非 Cox IPCW 联合 CIF 基线全部不变。

### 主要文件

- [统计研究报告](REPORT.md)
- [`src/n2_2_reachability.py`](src/n2_2_reachability.py)：逐患者预测状态和决策审计
- [`src/validate_n2_2.py`](src/validate_n2_2.py)：与已提交 N2 结果逐次一致性核验
- [`results/n2_2_replications.csv`](results/n2_2_replications.csv)：全部 288 个诊断输出行
- [`results/n2_2_summary.csv`](results/n2_2_summary.csv)：重复级均值和 Monte Carlo 标准误
- [`results/n2_2_compact.csv`](results/n2_2_compact.csv)：跨两档删失的机制 × p × 方法汇总
- [`results/n2_2_validation.json`](results/n2_2_validation.json)：源结果重放核验
- [`results/n2_2_config.json`](results/n2_2_config.json)：完整冻结配置与限制说明

### 运行

在仓库根目录执行（依赖已安装 `numpy scipy pandas scikit-learn`）：

```bash
python new_project/competing_risk_quantile/N2_2/src/n2_2_reachability.py --self-test
python new_project/competing_risk_quantile/N2_2/src/n2_2_reachability.py \
  --reps 8 --ntrain 900 --ntest 1000 \
  --out new_project/competing_risk_quantile/N2_2/results
python new_project/competing_risk_quantile/N2_2/src/validate_n2_2.py
```

**重要**：审计程序动态导入原来的 `N2_pilot/src/n2_pilot.py`，不能单独将 N2_2 文件夹拷贝到其他目录运行；仓库版无需 `/mnt/data`。初始 p 列表 `.12,.18,.24` 是已冻结**诊断网格**，不是新课题最终风险水平；整体时间 `H=3` 是抽象时间单位，不是 3 个月安全预算，也没有第一层容忍量。

### 研究边界

1. **直接原型的有限分位数是结构强制的**：`q=H*sigmoid(...)`，不可能识别不可达的 `F_1(H)<p`。本研究检验的是这个*原型*，不能将这一缺陷归于 Peng–Fine 原论文的任何具体实现。
2. **联合 CIF 的概率合法性不代表可达性校准良好**。它能满足 `F_1+F_2<=1` 且随时间单调，但样本较小时仍可能错判 `F_1(H)>p`。
3. **如果真实两治疗任一分位数不可达，则不把它的“治疗偏好”评为对错**；单列为“虚假的有限两药比较”。真实两药均有内点且估计也可比较时，才评价重点事件分位数排序错误。
4. **没有第一层总体保护 δ、临床效用与最终 p**。所报告的是输入完整受约束政策前的*必要诊断*，不是完整治疗策略的疗效或临床处方结论。
5. **仅 8 次/机制×删失**的配对先导重放；采用重复为 Monte Carlo 不确定性单位，不能将数百万重复 p/患者当成独立模型样本。
