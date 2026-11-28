# 13 — 补充最优决策价值估计量的收敛速度：直接对应 Zhou (2023 JASA) Theorem 2

## 1. 原先理论框架遗漏的对象

Yu Zhou, Lan Wang, Rui Song, Tuoyi Zhao (2023), Transformation-Invariant Learning of Optimal Individualized Decision Rules with Time-to-Event Outcomes, JASA 118(544), 2632–2644, DOI https://doi.org/10.1080/01621459.2022.2068420 。核验公开作者稿 https://arxiv.org/pdf/2204.04052 的第3.2节、式(7)–(10)、Theorem 2及Remark 5（作者稿第12–13页）、第4节Theorem 3。Theorem 1讨论规则索引参数的cube-root极限；Theorem 2讨论最优价值估计量 hat V_n-V_opt=o_p(n^(-1/2+gamma0)), 任意gamma0>0，无需最优规则唯一；Remark 5说明唯一性条件下可加强到根n。Theorem 3为动态情形的近参数速率。该文价值为规则诱导潜在生存时间分布的边际分位数，本文是平均条件竞争风险分位数，不能视为相同泛函。

05–12的主要结论关于 V_delta(d*)-V_delta(hat d) 的真实人口惩罚遗憾、真实无惩罚价值差及R_Q，不等于可计算的最优价值估计量与真实最优价值之差。12的理论定稿方案因此必须修正。本文件补上这一缺口，不改现有规则，不把n^(-1/3)索引参数速率照搬到Cox plug-in规则。

## 2. 定义

A={0,1}，D为全体可测规则，q_j与hat q_j均在[0,L]，固定0<delta<L。c(z,a)=max_b q0(z,b)-q0(z,a)，A_delta(z)={a:c<=delta}，估计版本由hat q0代入。d*与hat d逐点最大化各自候选集内重点分位数。假定可测并列处理。V(d)=E_Z q1(Z,d(Z))。
$$m_\delta(z)=\max_{a\in A_\delta(z)}q_1(z,a),\qquad V_{\mathrm{opt},\delta}=E_Z m_\delta(Z)=\sup_{d\in D_\delta}V(d).$$
定义
$$\widehat m_{\delta,n}(z)=\max_{a\in\widehat A_{\delta,n}(z)}\hat q_1(z,a),\quad
\widehat V_{\mathrm{opt},\delta,n}=P_n\widehat m_{\delta,n}=\frac1n\sum_i\hat q_1(Z_i,\hat d_n(Z_i)).$$
P_n使用同一训练样本的经验协变量分布（iid目标抽样）；不要求与Cox训练独立。若另有m个独立目标协变量，经验抽样项改为O_p(m^-1/2)。真实与估计最优值均不含K；精确惩罚的最优值数值相同，因为各自优化选择各自可行治疗。

## 3. 核心定理（对应 Zhou 2023 Theorem 2）

假设iid样本，e_j=max_a sup_z |hat q_j-q_j|=O_p(r_j), r_j→0；D(z)=|q0(z,1)-q0(z,0)|满足P_Z(|D-delta|<=t)<=C0 t^beta，beta>0，充分小t。则
$$\widehat V_{\mathrm{opt},\delta,n}-V_{\mathrm{opt},\delta}=O_p(n^{-1/2}+r_1+r_0^\beta).$$
若正确Cox及05的统一截断反演等正则条件给r0=r1=n^-1/2，则O_p(n^-1/2+n^-beta/2)。beta>=1时为O_p(n^-1/2)，从而对于任意gamma0>0亦为o_p(n^-1/2+gamma0)。无需最优规则唯一，无需重点排序margin A3，允许两个重点分位数同时截断为L。不要据此声称无条件快于Zhou，目标、模型、正则条件不同。若beta<1，仅保证更慢的上界；若仅边界无原子可得一致性但无幂速率。

证明：写P=E_Z，P_n经验测度。
$$\hat V_{\mathrm{opt}}-V_{\mathrm{opt}}=(P_n-P)m_\delta+P_n(\hat m_\delta-m_\delta).$$
固定m_delta有界，第一项O_p(n^-1/2)。在高概率事件2e0<delta上，候选集不一致只能发生于B_n={|D-delta|<=2e0}，因为sup_{z,a}|hat c-c|<=2e0且真实c为0或D。B_n^c上取最大值的Lipschitz性给|hat m-m|<=e1；B_n内有界于L。故
$$|P_n(\hat m-m)|\le e_1+LP_n(B_n).$$
注意B_n依赖训练数据，不能直接条件化成独立经验比例。令固定标量U(z)=|D(z)-delta|，由DKW不等式（或一维经验CDF统一根n界）
$$\sup_t|P_n(U\le t)-P(U\le t)|=O_p(n^{-1/2}).$$
可代入随机阈值2e0，结合margin得到P_n(B_n)=O_p(r0^beta+n^-1/2)。合并即证。等价地可用确定性高概率包络宽度和Markov界，不需学习规则类的经验过程复杂度。证明针对最优值估计量，不是oracle评价指标。

若要研究更精细的最优值极限分布，需要同时处理P_n-P、Cox影响函数和估计约束的移动边界；即便已有R_Q的正态极限也不能直接推出hat V_opt的正态极限。在正质量重点并列时，最大值映射仅方向可微；不能以根n速度代替正态性或置信区间证明。此次未建立该极限、未运行hat V_opt的统计估计误差模拟。

## 4. 理论与模拟调整

将最优值估计速度作为首个核心定理（与Zhou 2023直接对照），规则遗憾速度作为第二个；双尺度极限与R_Q理论可作后续定理/推论或附录，不以增加定理数为目的。区别三类量：
- hat V_opt - V_opt：最优价值估计误差，可能正负，新增明确理论对象；
- V_delta(d*) - V_delta(hat d)：学习规则的非负惩罚遗憾；
- R_Q：两个真实平均条件分位数价值的联合距离。
后两者不等价于第一项。原模拟已有oracle R/RQ不能验证本定理的可计算估计量；后续单独计算每次训练样本hat V_opt、oracle人口最优值、二者偏差/RMSE与sqrt(n)误差分布。保持原有跨方法QNB/RQ，不强制新增跨方法指标。此文件修正12的章节建议，历史推导不覆盖。