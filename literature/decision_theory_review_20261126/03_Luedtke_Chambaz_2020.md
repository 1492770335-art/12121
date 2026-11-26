# Luedtke & Chambaz (2020): Performance Guarantees for Policy Learning
[正文与附录](https://pmc.ncbi.nlm.nih.gov/articles/PMC8939837/)，DOI 10.1214/19-AIHP1034，Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 56(3), 2162–2188（不是 JMLR）。
状态：Theorem 1 与 A.1 主证明 (A.12)–(A.15) 已核对；辅助引理及局部统一结果未逐句完成。

## 定理对象
令策略类 Π 的最优价值为 V*，regret R(π)=V*-V(π)。Theorem 1 在固定 P、Donsker 策略类、原文 (5)(6) 的统一线性展开及近似最优经验搜索条件下，给出 R(πhat)≤ E_n+(2+o_P(1))Rem_n；若 Rem_n=o_P(n^{-1/2})，则 R(πhat)=o_P(n^{-1/2})。闭包最优集可以包含多个策略。

## A.1 主证明顺序
1. 采用闭包内任一最优 π*，在原候选类内取其近似 π*_s，因最优者不一定在原集合内。价值误差至多 s（需前置引理）。
2. (A.12) 把 V*-V(πhat) 分成 V(π*_s)-V(πhat) 和近似误差 V*-V(π*_s)。
3. 加减两个经验价值，得到两个估计误差之差、经验优化差及近似误差；利用 (6)，经验优化差由 o_P(Rem_n) 控制。
4. 用 (5) 的统一展开，将估计误差之差变为 n^{-1/2}(G_n f_{πhat}-G_n f_{π*_s}) 与两个 remainder；合并常数得到 2+o_P(1)。
5. (A.13) 用三角不等式把差分界为 2 sup_f |G_n f|。Donsker 与连续映射使这个 sup 为 O_P(1)。
6. 令 s↓0，得粗界 R(πhat)=O_P(n^{-1/2})。这只能证明不慢于根 n，尚不能说明严格更快。
7. (A.14) 回到差分本身，不再使用全类 sup 的粗界。利用已经得到的 regret 一致性，把 πhat 限制在 R(π)≤R(πhat)+t_n 的近最优集合；t_n↓0，正数用于兼顾闭包最优者是否属于原集合。
8. 乘以 sqrt(n)，得到 (A.15)：0≤sqrt(n) R(πhat)≤h(G_n,R(πhat)+t_n)+o_P(1)。h 由 A.6 和 Corollary A.7 的上包络构造，关键是近最优集合随 regret 阈值收缩。
9. G_n 弱收敛到高斯过程，第二个参数趋于0；极限过程几乎必然一致连续。由联合收敛及连续映射，右侧 h 趋于0，故 sqrt(n)R(πhat)→0。
10. PMC 文本末句把阶数写作 o_P(n^{1/2})，与 (A.15) 及正文明确结论不符；应以定理与推导为准，正式 PDF 仍需核验。

## 边界
这个结论是固定数据生成分布下的 regret 速度，不是统一 minimax 保证，不是策略参数估计误差。不能在没有统一渐近线性和随机等度连续性的情况下直接套用。正文 Section 4.3 还讨论分位数政策价值（Corollary 12）；附录 B.17 需要继续核读，不能当作已完成。
