# Two-stage binary quantile decisions: a joint value calculation

Consider two bounded conditional quantile endpoints. Write $u=q_0(1)-q_0(0)$ and $v=q_1(1)-q_1(0)$. A rule first retains both arms when $|u|\le\delta$ and otherwise retains the arm with the higher $q_0$. It then maximizes $q_1$, with a fixed lexicographic tie-break. The signed difference between two rule values is $E[(u,v)^\top(\hat d-d^*)]$. The norm of this mean is at most $E[\|(u,v)\|_2 1_{\hat d\ne d^*}]$.

Suppose a scalar covariate has a continuous density at finitely many separated interior switching points, each with nonzero slope. On fixed neighborhoods the relevant estimated contrasts have a joint continuous root-$n$ process limit $(G_u,G_v)$, and the comparison is uniformly stable outside them. At an active budget point $c$, $w=-\operatorname{sgn}(v)u-\delta$ crosses zero with $v(c)\ne0$. Set $J_c=f(c)/|w'(c)|$. At an interior ranking point $s$, $|u(s)|<\delta$ and $v$ crosses zero. Set $J_s=f(s)/|v'(s)|$. The leading signed vector is
\[
 \sum_c J_c(u(c),v(c))^\top G_u(c)+\sum_s J_s(u(s),0)^\top G_v(s).
\]
The corresponding nonnegative individual loss has a sum of absolute contributions. At an interior ranking point, the leading priority loss instead has scale $n^{-1}$ and limit $J_sG_v(s)^2/2$. These conclusions are conditional population losses given training, with weak convergence over training samples.

To verify the constants, rescale the covariate locally by $n^{-1/2}$. A sign comparison moves from $a y>0$ to $a y+G>0$. The signed indicator difference integrates to $G/|a|$. The integral of the absolute true contrast on the disagreement strip is $G^2/(2|a|)$. In the budget comparison the preferred arm is used when $w\le0$. Reversing the indicator sign and multiplying by the coding direction of the preferred arm gives $G_u$. At coincident switching points, integrate the intersection of the two linearized half-line conditions. Separate contributions cannot be summed there.

A synthetic exponential competing-risks example uses arm medians 12 and 9, cause-1 shares .60 and .18, a 36-unit window, levels .50 and .10, and budget 3. Both arms meet the true budget, and the cause-1 quantile gap is about 7.373. Under a centered nondegenerate continuous limit for the fitted overall contrast, the better cause-1 arm is excluded about half the time although the true budget has no violations. The example uses no empirical records.
