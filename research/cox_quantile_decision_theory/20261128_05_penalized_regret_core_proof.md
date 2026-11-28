# 两阶段分位数 ITR：惩罚价值、决策遗憾与核心收敛定理（2026-11-28）

## 0. 定位与与已有记录的关系

本文不改变原始两阶段 plug-in 决策，不限制为线性规则，不将 Cox 参数作为核心研究对象。不单设显然的等价性定理。此前 20261128_02_policy_optimality_theorem.md 的无惩罚价值曲线与双侧价值差仍然有效，但无惩罚价值差可能为负；本记录采用精确惩罚构造非负 regret。以下给出自洽的决策层证明，并明确 Cox 辅助条件。K 是理论常数，不是临床权重或新实验评价指标；QNB、R_Q 不承担证明任务。

## 1. 定义

令 A={0,1}，D 为全部可测规则 z→A，p0=0.50、p1=0.10、L=36、delta=3（一般理论只要求固定 0<delta<L）。F0=F_all，F1 为重点原因 CIF；q_j(z,a)=inf{t in [0,L]: F_j(t|z,a)>=p_j}，若集合为空则取 L。所有 q_j 及估计量取值于 [0,L]。M0(z)=max_a q0(z,a)，c(z,a)=M0(z)-q0(z,a)。真实、估计可行集合分别 A_delta(z)={a:c(z,a)<=delta}，hat A_delta(z)={a:hat c(z,a)<=delta}，二者非空。V(d)=E_Z q1(Z,d(Z))；以下 E_Z 和 P_Z 对独立目标患者、条件于训练样本。

取固定 K>L，定义
$$v_\delta(z,a)=q_1(z,a)-K I\{c(z,a)>\delta\},\quad V_\delta(d)=E_Z v_\delta(Z,d(Z)).$$
估计版本用 hat q、hat c 代入。可行治疗价值非负，不可行治疗价值至多 L-K<0，故逐点最大化 v_delta 等价于原两阶段规则。真实及估计规则分别为 d* 和 hat d，均为相应逐点最大化者（任意可测并列处理）。非负遗憾
$$\mathcal R_\delta(\hat d)=V_\delta(d^*)-V_\delta(\hat d)=E_Z\ell(Z),\quad \ell(z)=v_\delta(z,d^*(z))-v_\delta(z,\hat d(z))\ge 0.$$

令 b(z) 为总体分位数最大治疗（并列固定），w=1-b，D0=q0(z,b)-q0(z,w)=|q0(z,1)-q0(z,0)|，G=q1(z,w)-q1(z,b)，D1=q1(z,1)-q1(z,0)。可行时选 w iff G>0（并列可选 b）。精确个体价值差 H_delta(z)=G(z)-K I{D0(z)>delta}。对任意估计规则，
$$\mathcal R_\delta(\hat d)=E_Z[|H_\delta(Z)| I\{\hat d(Z)\ne d^*(Z)\}].$$
当真实规则并列时 H=0，等式仍成立。这说明非负遗憾是加权规则不一致概率，而 H 在活跃约束边界处可能跳跃；不同于普通零治疗效应边界。

## 2. 核心定理及确定性证明

A1: e_j=max_a sup_z |hat q_j(z,a)-q_j(z,a)|=O_p(r_j)，j=0,1，r_j→0。可先分别讨论 r0,r1，避免不必要地绑定两种分位数估计精度。
A2: P_Z(|D0-delta|<=t)<=C0 t^beta，beta>0，小 t。
A3: P_Z(0<|D1|<=t)<=C1 t^alpha，alpha>=0，小 t。允许重点分位数双侧截断造成 D1=0 的正概率。alpha=0 时取 C1=1 即可。A3 可进一步仅限制 D0<=delta 的双可行区域。

**核心定理：**
$$\mathcal R_\delta(\hat d)=O_p(r_0^\beta+r_1^{1+\alpha}).$$
若 r0=r1=n^{-1/2}，则为 O_p(n^{-beta/2}+n^{-(1+alpha)/2})。

证明：max 运算为 sup 范数下 1-Lipschitz，故 sup|hat c-c|<=2e0。若 2e0<delta 且真实与估计可行集合不同，则至少有一个真实治疗损失在 [delta-2e0,delta+2e0] 内。真实损失只能是 0 或 D0，因而该患者属于 B={|D0-delta|<=2e0}。这是可行集合变化的必要条件，并不意味着每个 B 中患者都会发生误判。A2 给出 P_Z(B)<=C0(2e0)^beta。由于所有真实价值位于 [-K,L]，0<=ell<=K+L，故 E[ell I(B)]<=(K+L)C0(2e0)^beta。

在 B^c 上，两可行集合一致。若为单例则治疗必然相同；若为双例，利用估计重点分位数的最优性，
q1(z,d*)-q1(z,hat d)<=2e1。
如果存在正遗憾，则两种治疗的真实重点分位数不同且推荐不同，故 0<|D1|<=2e1。于是
$$E_Z[\ell I(B^c)]\le 2e_1 P_Z(0<|D_1|\le 2e_1)\le C_1(2e_1)^{1+\alpha}.$$
相加得到高概率事件上的确定性不等式
$$\boxed{\mathcal R_\delta(\hat d)\le (K+L)C_0(2e_0)^\beta+C_1(2e_1)^{1+\alpha}.}$$
A1 保证 e_j 足够小的事件概率趋于 1，且各随机幂次满足相应 O_p 速度。证毕。

## 3. 推论（不单设额外主定理）

(1) 渐近最优性 V_delta(hat d)→p V_delta(d*)。

(2) 真实约束违反概率 P_v=P_Z(c(Z,hat d)>delta)。每个违规患者 ell>=K-L，故 P_v<=R/(K-L)。更精确地，违规必有 |D0-delta|<=2e0（真实不可行但估计可行），P_v=O_p(r0^beta)。确定性逐点保护为 [c(z,hat d)-delta]_+<=2e0，但这不是严格可行性；不要将概率趋零解读为有限样本全体患者均可行。

(3) V(d*)=V_delta(d*)，V(hat d)=V_delta(hat d)+K P_v。故 |V(hat d)-V(d*)|<=R+K P_v=O_p(r0^beta+r1^(1+alpha))。此无惩罚价值差可能正也可能负。进一步逐点 |q1(z,hat d)-q1(z,d*)|<=ell(z)+K I(违规)，同样可积分。

(4) 若真实最优规则几乎处处唯一，即 P_Z(D0<=delta,D1=0)=0，则
$$P_Z(\hat d(Z)\ne d^*(Z))\le P_Z(B)+P_Z(D_0\le\delta,0<|D_1|\le2e_1)=O_p(r_0^\beta+r_1^\alpha).$$
alpha>0 保证该界趋零；若 alpha=0 仍可借助 P(0<|D1|<=t)→0 和 e1→p0 获得一致性，但无指定幂速率。允许并列时，宜研究 P_Z(hat d 不属于真实最优治疗集合)，同一上界仍成立，不需要排除 D1=0。不能将任意指定代表规则的一致性作为无条件结果。

(5) 如果定义联合价值向量 V_Q(d)=(E_Z q0(Z,d(Z)),E_Z q1(Z,d(Z)))，则唯一性和规则一致性给出 ||V_Q(hat d)-V_Q(d*)||_2<=sqrt(2)L P_Z(hat d≠d*)。这是 R_Q 的一个条件性结果；若最优重点价值并列但总体价值不同，单凭非负 regret 一致性不足以推出联合价值一致性。若实际 R_Q 使用其他定义（如边际分位数），不可直接套用。

## 4. 更精细的活跃边界控制

上述 A2 是充分而非必要条件。设 e0<delta/4。对 B 中患者，D0>=delta-2e0>2e0，因此总体最优治疗 b 与估计总体最优治疗相同。若真实与估计可行状态均为双例，或者真实/估计单例相同，仍由第二阶段小差异界控制。若可行状态变化且产生正遗憾，则必须 G>=-2e1：当 G<-2e1 时真实和估计重点排序均严格偏好 b，且 b 在两个集合均可行，故不会产生遗憾。因此
$$\mathcal R_\delta(\hat d)\le (K+L)P_Z(|D_0-\delta|\le2e_0,G\ge-2e_1)+2e_1P_Z(0<|D_1|\le2e_1).$$
该界更精确：只有可能受重点事件收益驱动而选 w 的患者才形成活跃约束边界。等号 G=-2e1 保留以覆盖任意估计并列。若在阈值邻域 G<=-g0<0，则对足够小 e1 第一项为零，恢复单阶段快速度。若边界上存在正收益患者，则即使 D0 接近 delta，错误排除 w 的损失 G 可以为正的常数；错误纳入 w 的损失 K-G>=K-L。不能一般性地给第一项再乘 e0。即便 G=0，估计误纳且选 w 仍会造成 K 的理论惩罚，故无惩罚价值曲线的加权原子条件 E[G_+ I(D0=delta)]=0 不足以单独保证此惩罚 regret 的一致性。

## 5. Cox 与截断分位数辅助引理（条件性）

原因 k 的模型 lambda_k(t|z,a)=lambda_{k0}(t) exp(theta_k^T x(z,a))。假定独立个体、正确设定、固定维有界协变量及目标协变量紧集、条件独立删失与治疗正值性（因果解释另需一致性和可交换性）、非退化 Cox 信息矩阵、[0,L] 风险集正下界、连续有界累计基线危险。使用标准 Cox/Breslow 渐近结论 ||hat theta-theta||=O_p(n^-1/2)、sup_t|hat Lambda-Lambda|=O_p(n^-1/2)。此处需在论文中引用并逐项核对适用条件（尤其实际中心相关性与随访终点）。由指数函数在有界集上的 Lipschitz 性，sup_{t,z,a}|hat H_k-H_k|=O_p(n^-1/2)。

令 S=exp(-sum H_k)，F0=1-S，Fk=int S dH_k（真实 H 连续）。hat S=exp(-sum hat H_k)。sup|hat S-S|=O_p(n^-1/2)。设中间 CIF 为 tilde Fk=int hat S(u-) d hat H_k。分解
tilde Fk-Fk=int (hat S_- - S)d hat H_k + int S d(hat H_k-H_k)。
第一项由 sup 差乘 hat H_k(L)=O_p(1) 控制，第二项 Stieltjes 分部积分由 sup|hat H_k-H_k| 乘 (sup|S|+TV(S)) 控制；真实 S 连续单调，TV<=1。均为 O_p(n^-1/2)，统一于 t,z,a。

实际指数增量递推：跳点 u，h=sum_k Delta hat H_k(u)，Delta hat F_k=hat S(u-) (1-exp(-h)) Delta hat H_k/h（h=0 时定义为 0）。与左端点积分增量差的绝对值 <= h Delta hat H_k/2，因为 0<=h-(1-exp(-h))<=h^2/2。累加差 <= max_u h * hat H_k(L)/2。真实 H 连续意味着 max_u Delta hat H_all<=2 sup|hat H_all-H_all|，于是实际递推与中间估计差 O_p(n^-1/2)。总 CIF 同理或直接用 1-hat S。故 sup_{j,t,z,a}|hat F_j-F_j|=O_p(n^-1/2)。递推保持 S+sum F=1。

**截断反演引理：** 设真实 F 连续非降，hat F 非降。q=inf{t in [0,L]:F(t)>=p}，空集取 L。假设存在 m>0、h0>0，统一于 j,z,a，对于 0<h<=h0：
- 若 q-h>=0，p-F(q-h)>=m h；
- 若 q+h<L，F(q+h)-p>=m h。
该条件允许 F(L)<p、F(L)=p 和内点反演。令 epsilon=sup|hat F-F|，取 h=2epsilon/m（epsilon=0 时两反演相等）。若 q-h>=0，则 hat F(q-h)<p，非降性给 hat q>=q-h；否则由 hat q>=0 自动成立。若 q+h<L，则 hat F(q+h)>p，故 hat q<=q+h；否则由 hat q<=L 自动成立。于是 sup|hat q-q|<=2epsilon/m（epsilon 足够小时），包括 q=L。得到 A1，r0=r1=n^-1/2。若改用统一幂穿越 m h^kappa_j，则 r_j=n^-1/(2 kappa_j)，决策核心定理不变。若 CIF 在目标分位点处有平台、缺乏统一穿越，不能直接断言根 n 反演。

标准 Cox/Breslow 理论不是本文创新；对实际 Cox 实现、协变量支持、中心依赖、删失与反演正则性的核验仍需完成。非 PH 错设场景不受本定理自动覆盖；收敛到伪真模型规则不等于收敛到真实 oracle。

## 6. 当前结论与论文组织

第四章保留必要假设、一个核心定理及自然推论，所有证明与 Cox 辅助引理放附录。双边界上界是严格条件性证明，不是精确阶、渐近分布或一般 minimax 结论。下一份记录构造原因别 PH 子模型，在该模型证明根 n 约束边界项可达，并给出局部 minimax 下界，说明为何不能一般改进。不要因为惩罚价值的理论便利将其替换为临床净收益指标；固定 K>L，改变 K 只改变理论 regret 的常数与尺度，不改变规则。
