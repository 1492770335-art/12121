# 原因别 Cox 子模型中的遗憾紧致性与局部 minimax 下界

日期：2026-11-28。承接 20261128_05_penalized_regret_core_proof.md。目标：证明第一阶段 n^{-1/2} 项并非纯粹由粗糙证明造成。以下构造是理论反例，不是实际数据或模拟结果；固定 K>L。仅对正则子模型建立精确阶与局部 minimax 下界，不宣称一般 DGP 的精确阶。

## 1. 正确设定的 PH 子模型

Z~Unif(zc-h,zc+h)，zc=log(4/3)，h>0 足够小；A~Bernoulli(1/2) 独立于 Z。设 lambda=log(2)/12。治疗0两原因危险率分别为 0.6 lambda、0.4 lambda；治疗1分别为 0.2 lambda exp(z+theta)、0.8 lambda exp(z+theta)。均为指数基线、包含 A、AZ 交互的原因别 Cox 模型：
lambda_k(t|z,a)=lambda_{k0} exp(a eta_k+az+a theta)，eta_1=log(1/3)，eta_2=log(2)。
可取行政删失 C=L=36，满足独立删失且末端前风险概率有正下界。训练样本 iid。theta 在 0 的小邻域内，其余参数在本子模型视为已知。该子模型的 q0,q1 都在 (0,L) 内，且一致正斜率，满足反演条件。

p0=.5,p1=.1,delta=3,L=36：
q0(z,0)=12, q0(z,1)=12 exp(-(z+theta))；
F1(t|z,0)=.6(1-exp(-lambda t)), F1(t|z,1)=.2(1-exp(-lambda exp(z+theta)t))；
q1(z,0)=log(6/5)/lambda, q1(z,1)=12 exp(-(z+theta))。
取 h 和 theta 邻域足够小使 z+theta>0，G(z;theta)=q1(z,1)-q1(z,0) 一致大于正数 g_min，并且 G<=L。D0=12(1-exp(-(z+theta)))。边界 z+theta=zc 上 q0(1)=q1(1)=9，G_c=9-log(6/5)/lambda>0（约5.84月）。D0 在边界的导数为9，故 beta=1；D1 远离0，A3 对任意 alpha>=0 成立。所有分位数非截断；反例属于允许截断的模型类。

真实 oracle d_theta*(z)=I(z<=zc-theta)，取等号时治疗1；该点 P_Z 概率为0。估计 theta 后的原始两阶段 plug-in 规则 hat d=I(z<=zc-hat theta)，不是另行设计的规则。在 theta=0 附近，训练得到的正则非退化估计满足 sqrt(n)(hat theta-theta)⇒W~N(0,sigma^2)，例如该已知其余参数的指数模型极大似然估计：治疗1的 score 为 Delta-lambda exp(z+theta)X，方差/信息严格正，治疗0贡献0；行政删失下每个 score 有界、常规 iid MLE 理论适用。若使用完整 Cox 拟合且全部 nuisance 未知，需要另外证明其边界位移的非退化极限；本子模型证明不能一般提高上界，不直接声称完整实现的极限分布。

## 2. 精确阶及极限分布

固定 theta=0，边界位移 u=hat theta-theta。在 |u|<h 时，规则不一致区间的 P_Z 质量恰为 |u|/(2h)。
u>0: 错误排除可行且有益的治疗1，R=(1/(2h)) int_{zc-u}^{zc} G(z;0) dz。
u<0: 错误纳入不可行治疗1，R=(1/(2h)) int_{zc}^{zc-u} [K-G(z;0)] dz。
u=0: R=0。
G 连续且局部 Lipschitz，因此
$$R=\frac{G_c u_+ + (K-G_c)(-u)_+}{2h}+O(u^2).$$
连续映射定理给出
$$\sqrt n R\Rightarrow [G_c W_+ +(K-G_c)(-W)_+]/(2h).$$
右侧非退化且几乎处处正，故 R=O_p(n^-1/2) 但 R 不为 o_p(n^-1/2)。这表明在 beta=1 的正则 PH 情形，前一文件的根 n 上界可达。若 G_c=0，左侧错误排除的非惩罚损失可消失，但错误纳入仍有理论惩罚；本例取 G_c>0，使两方向均有正损失。此分布为子模型示例，不能直接用于一般 Cox 规则置信区间。

## 3. 更强结论：任意规则学习器的局部 minimax 下界

令 theta_-=-b/sqrt(n), theta_+=b/sqrt(n)，b>0 固定且足够小；两最优规则在区间 J_n=(zc-b/sqrt(n),zc+b/sqrt(n)] 取相反治疗（端点忽略）。P_Z(J_n)=b/(h sqrt(n))。

令 P_-^n,P_+^n 表示训练样本分布。为控制 KL，可先考虑无删失完整数据 (Z,A,T,J)。治疗1的事件时间指数率 mu_theta=lambda exp(z+theta)，事件类型概率 (.2,.8) 不依赖 theta，治疗0分布不变；指数率 mu_-,mu_+ 的 KL 为 log(mu_-/mu_+)+mu_+/mu_- -1 = exp(2b/sqrt(n))-1-2b/sqrt(n)=O(b^2/n)。乘随机治疗概率1/2，再乘 n 得 KL(P_-^n||P_+^n)<=C b^2；行政删失为确定性映射，数据处理不等式保证同样上界。Pinsker 给 TV<=sqrt(C b^2/2)，选 b 使 TV<=1/2。

令任意可测数据驱动规则 tilde d_n（允许独立随机化）。对 z∈J_n，一个模型的 oracle 为1，另一个为0。选择错误的个体惩罚遗憾至少 m=min(g_min,K-L)>0。对固定 z，二点检验不等式给
P_-^n(tilde d_n(z)≠d_-*(z))+P_+^n(tilde d_n(z)≠d_+*(z))>=1-TV(P_-^n,P_+^n)>=1/2。
由 Tonelli 积分，
E_- R_-(tilde d_n)+E_+ R_+(tilde d_n)>=m P_Z(J_n)/2=m b/(2h sqrt(n)).
故
$$\inf_{\tilde d_n}\max_{\theta\in\{\theta_-,\theta_+\}} E_\theta R_\theta(\tilde d_n)\ge m b/(4h\sqrt n).$$
这是局部二点 minimax **期望**遗憾下界；它不等同于逐点概率下界。还可直接得到概率版本：令 X_\pm=积分_{J_n} I(推荐错误)dP_Z，0<=X_\pm<=P_Z(J_n)=s_n；上式给至少一个模型 E X>=s_n/4，故 P(X>=s_n/8)>=1/8（由 E X<=s_n/8+s_n P(X>=s_n/8)），而 R>=m X。于是任意学习器至少在一个局部模型满足 P(R>=m b/(8h sqrt(n)))>=1/8。故无法在包含此子模型的模型类上统一取得 o_p(n^-1/2)。

## 4. 论文使用与限制

- 主定理仍为双 margin 决策遗憾上界。紧致性例子与局部二点下界可作为附录命题或讨论，不必强行新增正文主定理。
- 下界是对 beta=1、重点收益远离零的子类成立；不覆盖所有 beta，也不证明整个模型类的全局 minimax 等价阶。
- 本例采用简化已知 nuisance 的正则估计来展示非退化极限；任意学习器下界不依赖该估计形式。
- 固定 K 的非负 regret 刻画硬约束目标，不能作为 QNB 临床权重。惩罚值不连续是目标本身的性质；若改成连续超预算惩罚，一般不能保持原始规则的精确等价性。
- 尚需核查正式 Cox 拟合的设计矩阵是否允许交互、实际 DGP 的 margin 与反演条件；若实际模型不同，不应把子模型极限分布当作实证推断结果。
