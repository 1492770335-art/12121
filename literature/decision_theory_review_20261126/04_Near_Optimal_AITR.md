# Meng et al.: Near-optimal Individualized Treatment Recommendations
[JMLR 原文](https://jmlr.org/papers/v21/20-334.html)，[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8324003/)，[作者预印本](https://arxiv.org/abs/2004.02772)。
状态：已核对正文 §2、§7、Theorems 12/15 及 Corollary 13；补充材料证明尚未取得，不标记为逐句证明完成。
## 理论目标
该文输出一个近最优治疗集合，不是单个治疗。作者使用角度分类、reject/refine 和 outcome weighted learning；单一临床结局、相对容忍常数 c。不能把它描述成双结局约束规则。
§7 定义加权凸代理风险 R_l(f)=E[Y/p(A|X) l(<W_A,f(X)>)]，excess risk 是 R_l(f)-R_l(f')；因此定理直接研究代理风险而非治疗标签不一致概率。
## Theorem 12
条件：Assumptions 1,8,10,11；Assumption 10 要求 Y/p(A|X) 有界；11 要求 X∈[0,1]^p。τ_n=sqrt(log(p_n)/n)→0。线性类以系数平方范数预算 s_n 控制复杂度。
结果：e_l(fhat,f^(p_n))=O(max{c sqrt(p_n s_n) τ_n log(1/τ_n), δ_n})，几乎处处；δ_n 是受限线性类与全线性类最优代理风险差。
解释：增加 s_n 可降低逼近误差，却提高估计误差。Corollary 13 另要求最优函数仅依赖有限协变量等原文条件，简化至 O(c sqrt(p_n) τ_n log(1/τ_n))。
独立数学检查：固定 p>1 且 s_n 有界时，速率为 O(n^{-1/2} log n)。p=1 时 log p=0 的边界需核对约定。
## Theorem 15
Assumptions 1,8,10,14；14 要求可分 RKHS、K(x,x')≤B。结果为 O(max{c B sqrt(s_n/n) log n, δ_n}) 几乎处处。
解释：核函数有界性是控制复杂度的前提；线性核上界会随 p 增长，不能简单断言 RKHS 速度必然更快。
## 待核查
补充证明、Theorems 及前置 Assumptions 1/8 的精确内容、代理风险如何关联推荐集合，以及两类集合错误（错误纳入和错误排除）。不应将上述 excess risk 当作集合一致性定理。
