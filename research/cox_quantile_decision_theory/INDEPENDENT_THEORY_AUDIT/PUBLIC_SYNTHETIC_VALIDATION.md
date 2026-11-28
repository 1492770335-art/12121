# Synthetic Cox validation of joint quantile value

A randomized competing-risks experiment used two exponential causes, independent exponential censoring, and the same 36-unit analysis window throughout. The two conditional quantile levels were .50 and .10. The closed absolute budget was 3. A separate train/test calculation used the analytic population contrasts to evaluate each learned rule. The numbers below contain only simulated records' aggregate values.

For a homogeneous budget equality case with arm medians 12 and 9, and cause-1 shares .60 and .18, the exclusion error in 96 repetitions at n = 5120 was 0.5521 (Monte Carlo standard error 0.0510). The true budget violation rate was zero in every repetition. In a homogeneous priority tie, the priority quantile loss was zero, and the mean joint value distance was 0.9375 (0.1024).

The following diagnostic uses 24 new replications per cell. Each displayed pair gives n = 20480 and n = 81920, in that order.

| Synthetic mechanism | Mean joint value distance | Scaled priority shortfall |
|---|---:|---:|
| One regular budget boundary | 0.7709, 0.4375 | sqrt(n) times shortfall: 51.30, 43.56 |
| One interior ranking boundary with nonzero overall contrast at its root | 0.2675, 0.1069 | n times shortfall: 434.32, 212.03 |
| One interior ranking boundary with zero overall contrast at its root | 0.02601, 0.00401 | n times shortfall: 494.20, 304.11 |

The scaled averages vary at these sample sizes. They are Monte Carlo diagnostics, whereas the mathematical rates concern conditional population losses given a training sample. The fixed settings and runs were kept when the empirical slopes differed from the theoretical exponents.
