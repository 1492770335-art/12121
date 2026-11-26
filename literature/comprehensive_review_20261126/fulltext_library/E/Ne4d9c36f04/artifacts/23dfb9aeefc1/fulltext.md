# Constructing a T ‐Test for Value Function Comparison of Individualized Treatment Regimes in the Presence of Multiple Imputation for Missing Data

Original PDF: [original.pdf](original.pdf). SHA256: `23dfb9aeefc1d9a7a9b472b19b20de8cc3dde0454917aa5b2ce99a744f754f0f`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
CONSTRUCTING A T-TEST FOR VALUE FUNCTION COMPARISON
OF INDIVIDUALIZED TREATMENT REGIMES IN THE PRESENCE OF
MULTIPLE IMPUTATION FOR MISSING DATA
A PREPRINT
Minxin Lu
Department of Biostatistics
University of North Carolina at Chapel Hill
North Carolina, U.S.A.
minxin.lu@unc.edu
Annie Green Howard
Department of Biostatistics, Carolina Population Center
University of North Carolina at Chapel Hill
North Carolina, U.S.A.
aghoward@email.unc.edu
Penny Gordon-Larsen
Department of Nutrition, Carolina Population Center
University of North Carolina at Chapel Hill
North Carolina, U.S.A.
pglarsen@unc.edu
Katie A. Meyer
Department of Nutrition
University of North Carolina at Chapel Hill
North Carolina, U.S.A.
ktmeyer@email.unc.edu
Hsiao-Chuan Tien
Carolina Population Center
University of North Carolina at Chapel Hill
North Carolina, U.S.A.
htien@unc.edu
Shufa Du
Department of Nutrition, Carolina Population Center
University of North Carolina at Chapel Hill
North Carolina, U.S.A.
dushufa@email.unc.edu
Huijun Wang
National Institute for Nutrition and Health
Chinese Center for Disease Control and Prevention
Beijing, China
wanghj@ninh.chinacdc.cn
Bing Zhang
National Institute for Nutrition and Health
Chinese Center for Disease Control and Prevention
Beijing, China
zhangbing@chinacdc.cn
Michael R. Kosorok
Department of Biostatistics
University of North Carolina at Chapel Hill
North Carolina, U.S.A.
kosorok@bios.unc.edu
April 22, 2025
ABSTRACT
Optimal individualized treatment decision-making has improved health outcomes in recent years. The
value function is commonly used to evaluate the goodness of an individualized treatment decision
rule. Despite recent advances, comparing value functions between different treatment decision rules
or constructing confidence intervals around value functions remains difficult. We propose a t-test
based method applied to a test set that generates valid p-values to compare value functions between a
given pair of treatment decision rules when some of the data are missing. We demonstrate the ease
in use of this method and evaluate its performance via simulation studies and apply it to the China
Health and Nutrition Survey data.
arXiv:2312.15217v3  [stat.ME]  19 Apr 2025

````

## PDF page 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
Lu et al
A PREPRINT
Keywords Value Function, T-test, Precision Medicine, Individualized Treatment Regimes, Imputation
1
Introduction
The response to a particular treatment can vary among individuals due to the influence of their unique characteristics.
This variability in treatment effect is particularly relevant in healthcare, where individualized treatment regimes
(ITRs) are employed. ITRs tailor treatments and preventive approaches for individuals based on factors such as their
socioeconomic status, environment, lifestyle choices, and medical conditions. The application of ITRs extends beyond
healthcare and medical treatment assignments, encompassing precision nutrition and behavioral interventions as well.
In these applications, decision-makers may seek to compare the effectiveness of an ITR against, for example, the
observed treatment assignment, a one-size-fits-all treatment approach, or another ITR. This comparison is valuable for
both patients and healthcare providers in directing their efforts toward the most effective treatment option. For example,
individuals with or at risk for hypertension are generally advised to increase their physical activity. The American Heart
Association, based on the Physical Activity Guidelines for Americans1, recommends that adults engage in 2.5-5 hours
of moderate-intensity physical activity per week; although it is noted that additional health benefits can be achieved by
achieving beyond 5 hours per week2. Nevertheless, this physical activity recommendation can be challenging to meet
for many people. In addition, it is possible that this level of physical activity may not be beneficial for all individuals3.
Thus, it is important to examine whether physical activity, especially at high recommended levels, which might be
challenging to implement, uniformly benefits hypertension prevention and management across all demographic groups.
This may be particularly relevant in countries in which the prevalence of anti-hypertensive medications is low, such as
China. We aim to use ITRs to differentiate between subpopulations that experience incremental benefits from increasing
their weekly physical activity to more (versus less or equal) than 5 hours per week and directly compare the ITR
generated to population-level recommendations. For subpopulations who are unable to adhere to recommended activity
levels, there are potential significant benefits conferred by focusing on alternative behavior interventions, such as dietary
modification. Moreover, there are various methods for estimating the ITRs, such as Q-learning and D-learning4,5.
Direct comparisons of these ITRs are valuable for determining whether one ITR results in a superior population-level
improvement, as compared to another ITR, or to a non-individualized treatment.
Observational data is frequently encountered in research studies and serves as a vital data source for deriving ITRs.
Observational epidemiologic studies have several potential strengths, including increased representation of variability in
the target population, through large sample sizes and sampling strategies to increase population representation. However,
observational data generally lack balance in treatment assignments. To address this confounding, the average outcome
for the population, assuming adherence to a specific treatment regime, is weighted by inverse individual propensity
scores, and this weighted outcome is defined as the value function. Researchers have commonly employed the value
function to evaluate the performance of an ITR derived from observational cohort data. The presence of missing data
constitutes a common challenge encountered within randomized trial datasets as well as observational datasets. While
large observation data potentially provides more heterogeneity than smaller, more controlled studies, observational
studies are often more susceptible to missing data problems. One efficacious approach involves the application of
multiple imputation6 whereby multiple plausible imputed datasets are generated. Each imputed dataset entails the
substitution of missing values with imputed values derived from a predictive model. Subsequently, standard statistical
methods are applied to each of the imputed datasets separately. This process yields a collection of results, and the
observed variability among these results across the imputed datasets reflects the inherent uncertainty associated with
missing values. Multiple imputation allows comprehensive assessment of the robustness of the study findings in the
presence of missing data and has the potential to enhance reliability and generalizability of the research outcomes.
Various approaches have been employed to estimate the variance of a value function for ITRs, such as jackknife7,
cross-validation8,9, Q-function model-based approaches10, and bootstrapping11. Each is explained below. However,
these approaches tend to become intricate when using multiple imputation and are not intended for directly comparing
the value functions of a pair of ITRs, such as estimating the variance around the difference between two value functions.
Jiang et al7. employed the jackknife or leave-one-out cross-validation method to estimate the variance of the value
function and compared 24 individualized treatment regimes derived from 24 machine learning models. This jackknife
approach consistently estimates the variance around a value function estimate and requires only weak assumptions such
as requiring the samples to be independent and identically distributed, and that as the sample size becomes larger, the
decision rule estimated from n-1 individuals converges to the decision rule estimated from n individuals. However, it is
a time-consuming implementation and better suited for small datasets. Cross-validation provides an alternative means to
estimate variance. Cui et al.8 and Zhao et al.9 used cross-validation in their paper. The data is divided into K folds, and
the ITR was estimated based on the K −1 folds and the value function was evaluated based on the remaining fold. The
process is repeated K times to get K estimates of value functions and then the variance of value function is calculated.
2

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
Lu et al
A PREPRINT
A common choice of K is K = 10 which is called 10-fold cross-validation. This method is less time-consuming than
the jackknife, though it has a tendency to understate the actual variance. This is because each data point is utilized in
both the training and testing sets, leading to a correlation among the accuracy measures of each fold.12 Shi et al.10 have
developed a method for constructing the statistical inference of a policy’s value function for reinforcement learning
when either the number of decision points or the sample trajectories diverge to infinity. Their approach involves utilizing
the sieve method to approximate the Q- function and employs “SequentiAl Value Evaluation” to split data and iteratively
find the optimal policy and the value function estimate. Their method constructs a valid confidence interval around the
value function estimate that achieves the nominal coverage. However, it requires estimation of the Q-function and relies
on the correctness of the Q-function model. Bootstrapping provides an alternative approach to compute the variance of
the value function for an ITR. The standard n-out-of-n bootstrap method11 involves randomly selecting n observations
with replacements from the original data with n observations to create new datasets, which are then repeatedly generated
500 or 1000 times. Then, methods for finding the value function of the ITR are applied to each sequence, resulting in
slightly different value functions. Subsequently, the variance and confidence interval of the ITR’s value function are
developed. Variations of the standard n-out-of-n bootstrap method include double bootstrap13, adaptive bootstrap14,
and m-out-of-n bootstrap15. All bootstrapping methods require repeating operations on the data, usually 500 times or
more, making the approach computationally intensive.
In this paper, we present a new method that enables the direct comparison of any two ITRs via the value function
and also provides a t-test-based p-value for the significance of observed differences. Our approach addresses the
shortcomings described above in that: 1) it is less time-consuming to implement than the jackknife or bootstrapping; 2)
it circumvents the problem of correlation in each fold experienced by cross-validation; and 3) it does not rely on the
estimation of the Q-function. Our method is suitable for both observational studies and clinical trials. Moreover, our
method enables deriving variance estimates from multiple imputed datasets without the need for additional replication
or bootstrapping, making it particularly advantageous and efficient when dealing with missing data. Specifically, our
approach provides a valid estimate of the variability surrounding both the value function itself and the difference
between the two value functions. With our approach, it is possible to assess whether the optimal ITR significantly
outperforms the one-size-fits-all approach or another ITR estimated using a different method. Furthermore, our method
is characterized by its ease of understanding and implementation, while providing theoretical guarantees for estimator
consistency and inference validity, including variance and confidence interval calculations. For illustrative purposes, we
use two models, Q-learning4 and D-learning5 for ITR comparison, although more sophisticated models can also be
incorporated.
The following outlines the structure of this paper. Section 2 presents the introduction of our method. In section 3, we
showcase the application of our method through simulation studies. Section 4 delves into the implementation of our
method on a real-world dataset. Finally, in Section 5, we discuss the advantages and limitations of our approach.
2
Methods
In this section, we detail the methodology for calculating the t-test based p-value to assess the difference between
two individualized treatment rule (ITR) value functions. We initiate our discussion by defining the framework and
introducing relevant notations. Subsequently, we present Proposition 1, which outlines the limiting distribution of
the variance estimation for the estimated value function. We then proceed to establish the limiting distribution of the
difference between two value functions as delineated in Proposition 2, and describe the derivation of the corresponding
t-test statistics for pairwise value function comparisons in Equation 12. Lastly, we discuss the adaptation of this variance
estimation and t-test statistics to accommodate datasets with missing entries via multiple imputation in Equation 15.
We assume that the dataset is divided into a training set that estimates the decision rule and a test set that evaluates
this rule on new data, with n and m individuals respectively. The training data is independent of the test data. The
individual index is denoted by i, where Xi represents the covariate vector, Ai the binary treatment assignment, and
Yi the outcome. Let ˆd1,n and ˆd2,n be two decision rules we want to compare. Each ˆdn is a map from covariates to
treatments. The ˆd1,n and ˆd2,n can be zero-ordered decision rules (e.g. assign everyone the same treatment), or ITRs as
a function of the covariates based on models from the training set (e.g. assign everyone who is younger than 40 years
old one treatment, and assign placebo otherwise). The variable n indicates that the rules are estimated using training
data, and in case of missing data, decision rules are derived from single or multiple imputation of the training data. The
main contribution of our new method provide the estimates for the following:
• The value function of the decision rule dj,n on the test set Vm(dj,n) = E(Ym|A = ˆdj,n(x)), for j = 1, 2
• The variance (and 95% confidence interval) associated with the value function V ar(Vm(dj,n))
• The difference between value functions of two decision rules Vm(d1,n) −Vm(d2,n)
3

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Lu et al
A PREPRINT
• The variance (and 95% confidence interval) of the difference between the value functions of two decision rules
V ar(Vm(d1,n) −Vm(d2,n))
• The p-value of the t-test for the significance of the difference between the value functions of two decision rules
Vm(d1,n) −Vm(d2,n)
2.1
Propensity Score
Although randomized trial data are ideal for estimating the optimal ITR, many researchers only have access to
observational data. When using observational data, the confounding effect is a main concern and can be mitigated
by propensity score modeling16. The propensity score, denoted as π(A|X) = P(A|X), models the probability of
receiving treatment A given covariate vector X. By weighting each individual with the inverse propensity score, the
observational data can approximate the data from a randomized trial. Let ˆπn(a|x) = πn(a|x, ˆθn) be the estimated
propensity score from the training set, and π0(a|x) = πn(a|x, θ0) be the true propensity score, where ˆθn and θ0 denote
the estimated and the true parameters for the propensity score model.
Assumption 1. Let ϕ0(A, X) be a vector of functions of A and X, such that the following equation is satisfied:
√n(π(a|x, ˆθn) −π(a|x, θ0)) = √n(ˆθn −θ0)T ϕ0(a, x) + op(1).
(1)
Assumption 2.
√n(ˆθn −θ0) →N(0, Σ0),
(2)
and there exists a consistent estimate ˆΣn for Σ0.
Assumption 3. Let ˆϕn be an estimate of ϕ0, where ϕ0 satisfies
P|ˆϕn(A, X) −ϕ0(A, X)|2
P−→0,
(3)
where P means taking the expectation over (X, A, Y ) under the true model.
In general, most generalize linear models satisfy all assumptions under regularity conditions. The assumptions can
be verified using a Taylor expansion, the asymptotic normality of the maximum likelihood estimator, and standard
empirical process arguments. For illustration, detailed derivations for the logistic regression case are provided in
Appendix A. Note that in randomized trial data, the propensity score will be fixed for binary treatment π(a|x) = 0.5
and ˆθn = 0.
2.2
Value Function
We evaluate the goodness of a decision rule ˆdj,n by estimating the value function V ( ˆdj,n) = E(Y |A = ˆdj,n(X), X) =
E( Y 1{A= ˆdj,n(X)}
P (A|X)
)4. The value function can be interpreted as the inverse propensity score weighted average outcome
if the population were to follow the decision rule ˆdj,n. Specifically, we will calculate the value function based on the
test set data, represented by the subscript m:
ˆVm( ˆdj,n(Xi)) =
Pm
i=1
yi1{Ai= ˆdj,n(xi)}
ˆπn(Ai|Xi)
Pm
i=1
1{Ai= ˆdj,n(xi)}
ˆπn(Ai|Xi)
,
where the propensity score ˆπn and the ITR ˆdj,n are estimated from the training set and applied to the test set. The data
(Xi, Ai, Yi), i = 1, . . . , m come from the test set. It is crucial to ensure independence between training and test sets for
the test set results to effectively reflect the generalizability of the training set result.
2.3
Variance for the Value Function
Let Z = (X, A, Y ). For any measurable function of Z, let U = U(Z), Pm(U) = m−1 Pm
i=1 Ui be the empirical
measure, and P(U) = E(U) be the expectation taken over U. Then Gm(U) = √m[Pm(U)−P(U)] →N(0, V ar(U))
by standard empirical process arguments. Through some derivations we can derive the following equation (detailed
proofs are attached in Appendix A):
√m( ˆVm( ˆdj,n) −V0( ˆdj,n)) = Gm((Y −V0( ˆdj,n))1{A = ˆdj,n(X)}
π0(A|X)
)
−
p
m/n√n(ˆθn −θ0)T E(ϕ0(A, X)(Y −V0( ˆdj,n))1{A = ˆdj,n(X)}
π2
0(A|X)
) + oP (1),
(4)
4

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
Lu et al
A PREPRINT
where m denotes the empirical estimate based on the test set with m individuals.
Let U = U(Z) = (Y −V0( ˆdj,n))1{A= ˆdj,n(X)}
π0(A|X)
and W = W(Z) = E(ϕ0(A, X) (Y −V0( ˆdj,n))1{A= ˆdj,n(X)}
π2
0(A|X)
). We can
show that the following proposition holds.
Proposition 1.
√m( ˆVm( ˆdj,n) −V0( ˆdj,n)) →N(0, V ar(U) + m
n W T Σ0W),
(5)
provided that the quotient m/n asymptotically approaches a finite limit.
Standard empirical process arguments yield Gm(U) = √m[Pn(U)−P(U)] →N(0, V ar(U)). Since √n(ˆθn −θ0) →
N(0, Σ0), we can also show that the random variables √m( ˆVm( ˆdj,n)−V0( ˆdj,n)) converge in distribution to a mean zero
normal distribution. In this context, as the value of n approaches infinity, we assume the quotient m/n asymptotically
approaches a finite limit, rather than diverging towards infinity.
where the estimated influence function for U and W are as follows:
ˆUi,j = (Yi −ˆVn( ˆdj,n))1{Ai = ˆdj,n}
ˆπn(Ai|Xi) ,
(6)
¯Uj = m−1
m
X
i=1
ˆUi,j,
(7)
ˆWj = m−1
m
X
i=1
[
ˆϕ(Ai, Xi) ˆUi,j
ˆπn(Ai|Xi) ],
(8)
where i = 1, ..., n.
Thus, the variance σ2
0 for the value function Vm(dj) can be estimated consistently by:
ˆσ2
m,j = V ar( ˆVm( ˆdj)) ≈m−2
m
X
i=1
( ˆUi,j −¯Uj)2 + 1
n
ˆW T
j ˆΣn ˆWj.
(9)
Note that the two parts in the variance equation are dependent. When the number of individuals in the test set is
much less than that in the training set (m << n), then we can ignore the second term 1
n ˆW T
j ˆΣn ˆWj.1 When we use
randomized trial data, we don’t need to estimate the propensity score, and thus ˆΣn = 0 in this situation, and hence only
the first term remains.
2.4
Comparison Between Value Functions
The distribution of the random variable for the difference between the two value functions of two ITRs ˆd1,n and ˆd2,n
can be shown to converge to a normal distribution:
Proposition 2.
√m( ˆVm( ˆd1,n) −ˆVm( ˆd2,n) −V0( ˆd1,n) + V0( ˆd2,n)) →N(0, T 2
0 ),
(10)
where
T 2
0 = V ar(U1 −U2) + m
n (W1 −W2)T Σ0(W1 −W2).
Thus, the variance for the difference between the value function of two ITRs is approximately:
1When the number of individuals in the test set is much less than that in the training set, m << n. Thus m−1 >> n−1. Looking
at equation (9), m−2 Pm
i=1( ˆUi,j −¯Uj)2 >> 1
n ˆ
W T
j ˆΣn ˆ
Wj.
5

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
Lu et al
A PREPRINT
V ar( ˆVm( ˆd1,n) −ˆVm( ˆd2,n)) = m−2
m
X
i=1
( ˆUi,1 −ˆUi,2 −¯U1 + ¯U2)2 + 1
n( ˆW1 −ˆW2)T ˆΣn( ˆW1 −ˆW2).
(11)
Here, ˆΣn is estimated from the training set based on both variances due to multiple imputation and variance due to
modeling the sample data:
ˆΣn = nV ar(ˆθn) = nK−1
K
X
k=1
V ar(ˆθn,k) + n(1 + 1/K)(K −1)−1
K
X
k=1
(ˆθn,k −¯θn)2,
where ¯θn = 1/K PK
k=1 ˆθn,k. ˆΣn is the same across imputations, and it is positive definite because it is the sum of a
positive definite matrix and a positive semi-definite matrix. Under the null hypothesis, V0( ˆd1,n) −V0( ˆd2,n) = 0. The
t-test statistics t for this null hypothesis can then be constructed as follows:
t =
ˆVm( ˆd1,n) −ˆVm( ˆd2,n)
q
V ar( ˆVm( ˆd1,n) −ˆVm( ˆd2,n))
∼N(0, 1),
(12)
and this can be used to compute the p-value.
2.5
Multiple Imputation
In the presence of missing data, we extend our method to address the variance of the value function in the case of
multiple imputation. This extension is based on the ideas from Chapter 2.3.2 from Van Buuren (2018)17. Suppose we
have K imputations. Let k = 1, . . . , K be the index of the multiple-imputed data. The subscript m indicates that the
estimates are obtained for the test set.
For the single decision rule ˆdj, let ˆVm,k( ˆdj) denote the estimated value function for the kth imputed test set. Let
˜Vm( ˆdj) = K−1 PK
k=1 ˆVm,k( ˆdj), be value function estimate for decision rule ˆdj. Let ˆσm,j,k = V ar( ˆVm,k( ˆdj)) be
the estimator of the variance-covariance matrix for the estimated value function for the kth imputed test set. Let
σ2
0,K = V arK( ˆV ( ˆdj)) denote the variance associated with the estimate for a single value function. The empirical
estimate of σ2
0,K is:
ˆσ2
m,K = (1 + 1/K)(K −1)−1
K
X
k=1
( ˆVm,k( ˆdj) −˜Vm( ˆdj))2 + K−1
K
X
k=1
ˆσ2
m,j,k.
(13)
For the paired test between decision rules ˆd1 and ˆd2, let ˆT 2
m,k = V ar( ˆVm,k( ˆd1) −ˆVm,k( ˆd2)) denote the estimated
variance for the difference between two value functions for the kth imputed test set. Let T 2
0,K = V arK( ˆV ( ˆd1)−ˆV ( ˆd2))
denote the variance for the difference between value functions for decision rule ˆd1 and ˆd2. The empirical estimate of
T 2
0,K is:
ˆT 2
m,K = (1 + 1/K)(K −1)−1
K
X
k=1
( ˆVm,k( ˆd1) −ˆVm,k( ˆd2) −˜Vm( ˆd1) + ˜Vm( ˆd2))2 + K−1
K
X
k=1
ˆT 2
m,k.
(14)
Under the null hypothesis, H0 : V0,K( ˆd1,n) −V0,K( ˆd2,n) = 0. The t-test statistics tK for this null hypothesis can be
constructed as follows:
tK = K−1 PK
k=1( ˆVm,k( ˆd1,n) −ˆVm,k( ˆd2,n))
q
V arK( ˆVm,K( ˆd1,n) −ˆVm,K( ˆd2,n))
∼N(0, 1)
(15)
The p-value for this t-test can be obtained from the test statistic tK.
3
Simulation
We evaluate and compare the value functions obtained from applying each of the following treatment regimes to the
population under two scenarios: (1) the observed treatment, (2-3) the one-size-fits-all approach (one for each of the
6

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
Lu et al
A PREPRINT
Figure 1: The value function results of four simulation scenarios with δt = 1 and n = 5000: (a) with random treatment
assignment and complete data, (b) with random treatment assignment and data missing at random (c) with treatment
assignment depending on the covariates and complete data, (d) with treatment assignment depending on the covariates
and data missing at random. Within each scenario, we compare the value functions of eight different treatment regimes
which are indicated in the x-axis: observed treatment, treatment A = 0 for all individuals, treatment A = 1 for all
individuals, Q-learning optimal ITR, and D-learning optimal ITR, treatment rule d1, treatment rule d2, and the true
optimal ITR. The true value function is presented with the grey line. The estimated values and 95% confidence intervals
from our method, bootstrap estimates, and the true empirical 95% confidence intervals are depicted using varying
shades of gray.
binary treatments), (4) Q-learning ITR, (5) D-learning ITR. A convex penalty, elastic net penalization18, was used for
each of the ITR models for variable selection. We generate a total of 5000 observations for each simulated training set
and 1500 observations for each test set. The number of covariates included in the model is p = 20. We perform 1000
replicates for each of the simulations.
The following data generation process is modified from the first simulation scenario in Tian et al5. The covariates X are
generated from three different underlying distributions: X1, ..., X10 are uncorrelated and generated from a multivariate
normal distribution with mean zero and the covariance-variance matrix is a diagonal of 1s; X11, ..., X15 are generated
from a uniform distribution U(−0.5, 0.5); X16, ..., X20 are generated from a binary distribution with p = 0.5. Let A
denote the binary treatment. In the model implementation step, we will use A = {0, 1} for Q-learning and switch
to A = {−1, 1} for D-learning. ε ∼N(0, 1) is the random error2 for generating the outcome Y . Let β0 = (
√
6)−1,
β1 = β2 = 0, βj = (2
√
6)−1, j = 3, 4, . . . , 10, β11 = ... = βp = 0 be the coefficient for the main effect. Let
Y ∼binomial with probability equal to the expit of
(β0 +
p
X
j=1
βjXj)2 + (I(X1 > 0) + I(X2 > 0) −2I(X1 ≤0)I(X2 ≤0))Aδt + ε.
2The error term has been incorporated into the outcome data generation mechanism to better reflect potential real-world
inaccuracies.
7

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
Lu et al
A PREPRINT
Figure 2: The differences of value functions and the associate standard deviation between selected pairs of the following
treatments: observed treatment, universal treatment A = 0, universal treatment A = 1, Q-learning’s optimal ITR,
D-learning’s optimal ITR, treatment rule d1, treatment rule d2, and the true optimal ITR. The results are presented
under four simulation scenarios with δt = 1 and n = 5000, comparing our estimates, bootstrap estimates, and the true
values and 95% confidence intervals.
The generated data is designed to have main effects (β0, . . . , βp), and treatment interaction effect (I(X1 > 0)+I(X2 >
0) −2I(X1 ≤0)I(X2 ≤0))δt, where δt > 0 is a parameter that controls the magnitude of the treatment interaction
effect on the outcome. To align with the application example presented in section 4, we assume, without loss of
generality, that a smaller outcome Y and a smaller value function are preferable. Thus, the optimal treatment regime
is dopt = I(I(X1 > 0) + I(X2 > 0) −2I(X1 ≤0)I(X2 ≤0)) ≤0 = I(X1 ≤0 and X2 ≤0). We consider four
scenarios:
(a) Propensity score π = 0.5 (randomized trial data)
(b) Propensity score π = 0.5 (randomized trial data with data missing at random)
(c) Propensity score logit(π) = 0.75X1 −0.75X2 (observational data)
(d) Propensity score logit(π) = 0.75X1 −0.75X2 (observational data with data missing at random)
In scenarios where data are missing at random, the missingness mechanism is implemented by assigning a conditional
probability of missingness to the variables X2, . . . , Xp. This probability is contingent upon the value of X1: specifically,
there is a 15% probability of missingness when X1 > 0, and a lower probability of 10% in cases where this condition is
not met.
The true value function V∗( ˆdj) is obtained from applying each decision rule ˆdj on a simulated large test set comprising
100,000 individuals. The data generation process for this large test set mirrors that of the corresponding complete training
set. The true value function V∗( ˆdj) is calculated based on the true propensity score parameters and the decision rule ˆdj
derived from the training set. We define the true variance of the value function as ˆτ 2
j = 1
L
PL
l=1(Vl( ˆdj) −V∗( ˆdj))2,
where Vl( ˆdj) represents the estimated value function from test set l, utilizing the estimated decision rule ˆdj and the
8

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
Lu et al
A PREPRINT
Table 1: Estimated difference in value functions Mean (SD) and t-test rejection rate (RR) under four scenarios for
simulation data based on 1000 replications (δt = 1, n = 5000).
Scenario 1
Scenario 2
Scenario 3
Scenario 4
Method
Test
Mean(SD)
RR
Mean(SD)
RR
Mean(SD)
RR
Mean(SD)
RR
Est
d1 vs. d2
-0.001(0.018)
0.069
-0.004(0.018)
0.089
0.000(0.021)
0.039
-0.004(0.021)
0.055
Boot
d1 vs. d2
-0.001(0.018)
0.069
-0.004(0.018)
0.085
0.000(0.021)
0.041
-0.004(0.020)
0.062
True
d1 vs. d2
0.001(0.019)
0.000
0.001(0.021)
0.000
-0.002(0.020)
0.000
-0.002(0.022)
0.000
Est
d1 vs. dopt
0.046(0.013)
0.940
0.043(0.013)
0.896
0.046(0.015)
0.861
0.044(0.015)
0.808
Boot
d1 vs. dopt
0.046(0.013)
0.939
0.043(0.013)
0.900
0.045(0.015)
0.869
0.044(0.015)
0.822
True
d1 vs. dopt
0.047(0.013)
1.000
0.047(0.014)
1.000
0.047(0.015)
1.000
0.047(0.016)
1.000
propensity score model from the corresponding training set. The true variance for the difference between value functions
is constructed in a similar manner.
The point estimates for value functions are derived by averaging the value function estimates across 1000 replications
on the test set. The estimated variance for each value function is computed using Equation 9, while the variances for
differences between two value functions are calculated using Equations 11 (for scenarios 1 and 3) and 14 (for scenarios
2 and 4), also averaged over 1000 replications. For bootstrapping estimates, the point estimate of the value function is
the mean obtained from 1000 bootstrap samples (we have also obtained estimates from 100, 200, 500 bootstrapping
samples, the results are similar to 1000 bootstraping samples and are thus omited here), which is then further averaged
across 1000 replications. Similarly, the bootstrapping variance is determined by calculating the variance of the 1000
bootstrap samples and averaging this across 1000 replications.
Figure 1 shows the value functions and standard deviation in four scenarios (a)-(d). We observe that the point estimates
of value functions using our estimated method are close to that estimated from bootstrapping and the true value, across
all 4 scenarios and almost all methods. The variance estimates of a single value function using our estimated method
are close to that estimated from bootstrapping and the true value (except that our method gives a slightly larger variance
estimate for the observed treatment). Figure 2 shows that, for comparing pairwise value functions, the point estimate
and the variance estimated for the difference from our method are also close to the bootstrapping estimates and the truth.
As expected, the value function for ITRs from dopt is the lowest among all methods. Table 1 presents the difference,
standard deviation (SD), and t-test rejection rates for comparisons between d1 vs. d2 and d1 vs. dopt, under the setting
δt = 1 and n = 5000. The point estimates and SDs are consistent across our estimates, bootstrapped estimates, and the
true value differences. The t-test for the difference between d1 and d2 yields a rejection rate close to zero, whereas the
test for the difference between d1 and dopt results in a rejection rate close to one. For observational data, when treatment
assignments are nonrandom and probabilities need to be estimated by propensity scores, value function estimates have
slightly larger variances compared to the value function estimates for randomized trial data (Table 1). For datasets with
missing values, the performance remains comparable to that of complete datasets when the missing data is random and
is addressed through multiple imputation using missForest. The results shown here are the test set results. The training
set results are similar to the test set results but with a smaller variance. The simulation results illustrate the effectiveness
of our approach in discerning disparities between two ITRs while maintaining reasonable variance estimates in both
observational data and randomized trial data, with or without missing values.
For our power analysis, we define two regimes: d1 = I(X1 ≤0), d2 = I(X2 ≤0). By design, V0( ˆd1,n) = V0( ˆd2,n)
and V0( ˆd1,n)̸ = V0( ˆdopt,n). The power analysis includes different training sample sizes n ∈{1000, 2000, 3500, 5000}
and varying values of δt ∈{1, 2, 5, 10}, where treatment interaction hyperparameter δt controls the magnitude of
treatment heterogeneity. As δt increases, the difference between value functions of d1 and dopt also increases. Table
2 show the Type I Error rate by testing H0 : d1 = d2. Table 3 shows the power (or 1-Type II Error rate) by testing
H0 : d1 = dopt. These results show that both the Type I Errors and the power of our method are slightly lower or
similar to that of bootstrapping method across 4 scenarios, across different effect size and different sample sizes.3
3The results for δt ∈{5, 10} were similar, we only present the results for δt ∈{1, 2} for clarity.
9

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
Lu et al
A PREPRINT
Table 2: Type 1 Error by sample size and δt.
Scenario 1
Scenario 2
Scenario 3
Scenario 4
n
Method
δt = 1
δt = 2
δt = 1
δt = 2
δt = 1
δt = 2
δt = 1
δt = 2
1000
Est
0.041
0.054
0.061
0.070
0.038
0.037
0.052
0.041
1000
Boot
0.047
0.060
0.066
0.075
0.060
0.075
0.077
0.086
2000
Est
0.053
0.057
0.062
0.087
0.049
0.044
0.062
0.063
2000
Boot
0.058
0.063
0.069
0.090
0.059
0.066
0.079
0.084
3500
Est
0.059
0.064
0.086
0.085
0.049
0.051
0.057
0.067
3500
Boot
0.062
0.064
0.085
0.085
0.056
0.057
0.067
0.076
5000
Est
0.069
0.063
0.089
0.097
0.039
0.039
0.055
0.071
5000
Boot
0.069
0.065
0.085
0.097
0.041
0.047
0.062
0.076
Table 3: Power by sample size and δt.
Scenario 1
Scenario 2
Scenario 3
Scenario 4
n
Method
δt = 1
δt = 2
δt = 1
δt = 2
δt = 1
δt = 2
δt = 1
δt = 2
1000
Est
0.916
1.000
0.850
0.997
0.811
0.998
0.757
0.996
1000
Boot
0.925
1.000
0.860
0.998
0.879
0.999
0.838
0.999
2000
Est
0.925
0.999
0.870
0.999
0.876
1.000
0.833
1.000
2000
Boot
0.929
0.999
0.875
0.999
0.899
1.000
0.869
1.000
3500
Est
0.918
1.000
0.864
1.000
0.880
0.999
0.846
0.998
3500
Boot
0.917
1.000
0.866
1.000
0.892
0.999
0.866
0.999
5000
Est
0.940
1.000
0.896
1.000
0.861
1.000
0.808
1.000
5000
Boot
0.939
1.000
0.900
1.000
0.869
1.000
0.822
1.000
Since our method relies on the correct specification of the propensity model, we examine how propensity score
estimation influences the value function and standard deviation estimates (Figure S1) as well as the differences between
value functions and their associated standard deviation estimates (Figure S2). The sensitivity analysis indicates that
the results remain similar whether using the estimated propensity score or the true propensity score. However, our
method may exhibit bias when the propensity score is misspecified; however, the extent of this bias is comparable to
that observed in the bootstrap estimates. These findings highlight a limitation of our approach: the accuracy of variance
estimation depends on the precision of propensity score estimation. Additionally, they provide insights into how our
method performs under model misspecification in certain conditions (Figure S3 illustrates the distribution of selected
propensity score models in relation to the true propensity score across the these four models).
4
Application
4.1
CHNS: Data Analysis
Hypertension, also known as high blood pressure, is a chronic medical condition that affects over one billion adults
worldwide19. It is a major risk factor for cardiovascular disease, which is the leading cause of death globally20.
People with hypertension are more likely to develop kidney disease,21 vision problems,22 and cognitive impairment.23
Hypertension can also affect quality of life and increase annual medical costs24. Over the past two to three decades,
China has experienced a significant increase in the prevalence of hypertension (from 20.8% in 2004 to 29.6% in
2010 and 24.7% in 2018) due to increased life expectancy and lifestyle changes25,26. As hypertension has become a
significant burden on China’s population health, it is important to study this condition and develop effective prevention
and treatment strategies. While medication proves effective in managing hypertension, the general adherence to
anti-hypertensive medication remains low. This can be attributed to factors such as a low reimbursement ratio, high daily
medical costs, and access to healthcare27. In addition to taking medications, adopting non-pharmacologic interventions
such as engaging in regular physical activity, reducing salt intake, and following a balanced diet rich in fruits and
10

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
Lu et al
A PREPRINT
vegetables can help to reduce high blood pressure28. However, there is potential heterogeneity in which individuals
may see the most benefit from behavioral interventions.
Our overall objective is to identify the most effective non-pharmacologic treatments for subpopulations of individuals,
considering the challenges of adhering to a comprehensive healthy lifestyle based on public health recommendations.
As a first step, we examine the potential variability in the effectiveness of exceeding 5 hours of weekly moderate-
to-vigorous physical activity (MVPA) in reducing the risk of hypertension in the CHNS population. We seek to
distinguish between participants who benefit from engaging in MVPA for more than 5 hours per week and those who
do not. For participants who see no hypertension benefit from increasing their physical activity, it is possible to identify
other potential interventions to consider, such as diet modification. Understanding which interventions confer optimal
outcomes empowers individuals to identify the most effective and efficient behavioral treatments and their associated
benefits. This knowledge can be highly beneficial, as individuals are more motivated to engage in behaviors when they
are aware of their positive outcomes29. To address this research question, we tested whether a personalized physical
activity intervention strategy could achieve population-level health outcomes comparable to an intervention that assigns
high physical activity to everyone.
We used data from the China Health and Nutrition Survey (CHNS)30, a population-based, observational data set
consisting of high-quality data on diet (3-day repeated 24-hour recalls) and physical activity (detailed 7-day recall)
collected from individuals in China using detailed recall instruments. Our analysis focused on the study year 2009
with 8320 adults. Our outcome, hypertension, was defined 4 as a systolic blood pressure ≥130 mmHg or diastolic
blood pressure ≥80 mmHg. Individuals with missing systolic or diastolic blood pressure measurements or who were
missing more than 10% of their covariates were excluded from our study, resulting in a final analytic sample of 5241
individuals, 60% of whom had hypertension. In the CHNS dataset, physical activity encompassing leisure, occupational,
transportation, and domestic activities, were collected via a comprehensive survey recall instrument31. Our study
focused on weekly moderate-to-vigorous physical activity (MVPA), defined as activities with a minimum of 3 METS
(Metabolic equivalent of task)32 5. Our sample population has a high MVPA level, with a median of 15 hours per
week31. Targeting the 5-hour MVPA weekly guideline2,1,31, we dichotomized the treatment into a binary variable
A: over 5 hours (A = 1) and 5 or fewer hours (A = 0) of MVPA per week. In the CHNS data, 66% of the sample
population engaged in more than 5 hours of MVPA weekly. With insights from biological understanding and published
literature31, we identified twenty risk factors for hypertension. These factors also have the potential to influence the
relationship between physical activity and hypertension, including: age, gender, caloric intake, BMI, education, smoking
status, sodium intake, potassium intake, alcohol consumption, hypertension medication, household income, province,
and urbanization index. Less than 15% of our sample had missing covariates, handled using missForest package in R
for multiple imputation34,35. Table 4 provides further details about these factors based on one imputed dataset. The
other imputed datasets exhibit similar distributions. The data was split into a 70% training set and a 30% test set, with
missForest imputation performed 10 times on each set to avoid dependency. We obtained Q-learning optimal ITRs4 and
D-learnings optimal ITR5 for each of the training sets using a logistic regression model with elastic-net penalization.
We then compared the value function of each treatment rule on the test set, including the observed treatment, assigning
all individuals to treatment A = 1 or A = 0, optimal ITRs derived from Q-learning and D-learning.
The value functions of these treatment rules were estimated using the common estimator V and the differences between
value functions were directly obtained by subtracting the value functions and then averaged over 10 imputed data sets.
The variance of the value function and the variance of the difference between the value functions were estimated by our
method, which accounts for both modeling and multiple imputation variance.
Our goal is to compare personalized and uniform interventions in reducing hypertension risk by comparing the value
functions in test sets for (1) observed physical activity, under the assumption that individuals continue their existing
routines; (2) assigning all individuals to treatment A = 1, assuming all individuals are above the 5 hours weekly MVPA
recommendation; (3) assigning all individuals to treatment A = 0, assuming all individuals are at or below the 5 hours
weekly MVPA recommendation; and (4) optimal ITRs derived from various methods. Figure 3(a) shows the value
function and 95% confidence interval for those treatment regimes. The differences between the value functions for
different decision rules are small. Especially, the Q-learning value function is the lowest but the confidence interval
intersects with the that of other treatment regimes. This means that if the population follows the Q-learning ITR, the
expected risk of hypertension in the population is similar to when the population follows the other treatment assignment
4Anti-hypertensive medication is included in the model in our analysis, so blood pressure measurements here are not adjusted for
medication. Participants who were taking medication may exhibit varying responses to changes in physical activity. Consequently,
we have included medication as a covariate that has the potential to influence how individuals respond to engaging in more than 5
hours of physical activity per week.
5The METS, or Metabolic equivalent of task, is a unit of measurement for physical activity. One MET is equivalent to a person’s
oxygen consumption at a rate of 3.5 milliliters per kilogram per minute. 33
11

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
Lu et al
A PREPRINT
Table 4: Descriptive Table for CHNS Data.
Training Data
Test Data
Overall
(N=3667)
(N=1574)
(N=5241)
Age, mean (SD)
48.7 (10.4)
48.8 (10.2)
48.7 (10.3)
Gender, n (%)
Male
1695 (46.2%)
746 (47.4%)
2441 (46.6%)
Female
1972 (53.8%)
828 (52.6%)
2800 (53.4%)
Calorie Intake (kcal/kg), mean (SD)
36.7 (11.8)
36.7 (11.8)
36.7 (11.8)
BMI, mean (SD)
23.3 (3.18)
23.4 (3.31)
23.3 (3.22)
Education, mean (SD)
1.56 (0.710)
1.54 (0.723)
1.56 (0.714)
Log-transformed Household Income, mean (SD)
2.51 (0.853)
2.50 (0.849)
2.51 (0.852)
Current Smoking, n (%)
1234 (33.7%)
510 (32.4%)
1744 (33.3%)
Sodium (mg/day), mean (SD)
4560 (2270)
4600 (2250)
4570 (2260)
Potassium (mg/day), mean (SD)
1750 (673)
1720 (657)
1740 (668)
Alcohol, n (%)
1262 (34.4%)
572 (36.3%)
1834 (35.0%)
MVPA (hours/week) , mean (SD)
34.2 (42.0)
36.3 (43.3)
34.8 (42.4)
Anti-Hypertensive Medication, n (%)
291 (7.9%)
144 (9.1%)
435 (8.3%)
Hypertension, n (%)
2184 (59.6%)
940 (59.7%)
3124 (59.6%)
Province, n (%)
21 – Liaoning
400 (10.9%)
170 (10.8%)
570 (10.9%)
23 – Heilongjiang
464 (12.7%)
199 (12.6%)
663 (12.7%)
32 – Jiangsu
424 (11.6%)
159 (10.1%)
583 (11.1%)
37 – Shandong
422 (11.5%)
200 (12.7%)
622 (11.9%)
41 – Henan
335 (9.1%)
148 (9.4%)
483 (9.2%)
42 – Hubei
367 (10.0%)
172 (10.9%)
539 (10.3%)
43 – Hunan
444 (12.1%)
183 (11.6%)
627 (12.0%)
45 – Guangxi
415 (11.3%)
156 (9.9%)
571 (10.9%)
52 – Guizhou
396 (10.8%)
187 (11.9%)
583 (11.1%)
Urbanization Index, mean (SD)
66.1 (19.0)
65.3 (18.7)
65.9 (18.9)
Source: China Health and Nutrition Survey (CHNS).
MVPA includes occupational, domestic, transportation and leisure activity.
(e.g. high PA for everyone). Figure 4(a) shows the pairwise difference of the value functions between treatment regimes
that we are interested in. Our focus is on determining the necessity of recommending over 5 hours of weekly MVPA to
everyone or specific subgroups. Thus we compare the best ITR, Q-learning ITR, defined by the lowest value function
estimate in the training set (Table S1) with the one-size-fits-all treatment A = 1 for the test set. Based on the t-test result,
the value functions are not significantly different, with a p-value of 0.156 for the Q-learning personalized treatment
rule compared to assigning all individuals to treatment A = 1 (Table S2). This suggests that a personalized approach
can achieve a similar hypertension risk as the population-level physical activity recommendations for doing physical
activity for more than five hours per week.The results presented herein pertain to the test set, which is essential for
evaluating the model’s generalizability to new, unseen data. A comparison of model performance between the training
and test sets is provided in Appendix Figure S4 and Figure S5. The training set results closely mirror those of the test
set, underscoring the model’s stability; however, the test set results are emphasized as they more accurately reflect the
model’s anticipated performance in real-world applications.
Our findings indicate that applying a uniform high level of physical activity across the entire population does not
significantly reduce hypertension risk compared to tailoring activity levels to individual characteristics. Specifically, our
results suggest that increased physical activity may benefit certain subgroups, whereas others do not derive additional
benefits beyond 5 hours of weekly MVPA. For these subpopulations, alternative non-pharmacologic interventions may
be more effective in mitigating hypertension risk. For instance, individuals with high sodium consumption may not
benefit significantly from increased physical activity alone. In contrast, sodium intake reduction could potentially offer
a more effective strategy for lowering hypertension risk. Another possible explanation is that much physical activity in
the CHNS data comprised working, as opposed to leisure, activities. Published data suggest that occupational physical
12

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
Lu et al
A PREPRINT
Figure 3: The value function and 95% confidence interval estimates of six different treatment regimes: observed
treatment (Obs), lower physical activity hours (AllLowPA, A = 0) for all individuals, higher physical activity hours
(AllHighPA, A = 1) for all individuals, Q-learning optimal ITR (Q), and D-learning optimal ITR (D). For comparison
purposes, we include the average outcome as a benchmark. (a) shows the results on original data, and (b)(c)(d) shows
the three simulated data with three levels of treatment effect modification δ = 1, δ = 2, δ = 10, respectively.
activity may not be as protective against hypertension36. The complete pairwise comparison of all the comparisons is
depicted in the appendix Figure S5.
4.2
CHNS: Augmented Simulation Analysis
In Section 4.1, our method did not detect a significant difference between the two treatment rules under comparison.
This finding prompted the question of whether the null result was attributable to limitations of the method when applied
to real-world data, or if the true difference was indeed minimal. To address this issue, we conducted an augmented
analysis to evaluate our method’s performance in scenarios where a true difference between the treatment rules is
present. It is important to note that the models in Section 4.1 considered only a limited set of factors influencing
the effect of physical activity on hypertension. Given the complexity of hypertension—arising from the interplay of
individual behavior, environmental influences, and additional factors such as metabolism and genetics—incorporating
these variables could reveal important insights and better identify the underlying heterogeneity in the impact of physical
activity on hypertension. Consequently, we examined our method’s performance in the presence of prescriptive
treatment effect interactions that account for these additional factors, or their combinations with our existing factors,
which may explain more of the variation in individual hypertension risk. An additional analysis was therefore conducted
using simulated datasets with modified prescriptive treatment effect interaction terms.
The outcome variables in these data sets were generated by the fitted Q-learning outcome regression model with the
treatment effect interaction terms (excluding the treatment main effect term) multiplied by a factor of δ ≥1. We
investigate three options of δ for this analysis: δ = 1, δ = 2, and δ = 10, representing the estimated original, double,
and tenfold treatment effect, respectively. In each analysis, hypertension outcomes are replaced by generated outcomes
from the modified Q-learning outcome regression model. This augmented analysis examines our method’s performance
when the outcome generative process is known and how the performance varies as the true prescriptive treatment effect
13

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
Lu et al
A PREPRINT
Figure 4: The value function differences and 95% confidence interval among selected pairs of treatment regimes.
Specifically, the Q-learning optimal ITR comparison with the observed treatment, treatment A = 0 for all individuals,
treatment A = 1 for all individuals, and D-learning optimal ITR are shown. (a) shows the results on original data,
and (b)(c)(d) shows the three simulated data with three levels of treatment effect modification δ = 1, δ = 2, δ = 10,
respectively.
enlarges. As δ increases, from δ = 1, to δ = 2, to δ = 10 (Figure 3 (b)-(d)), the value function differences between the
Q-learning strategy and other treatment rules increase. Figure 4 shows the difference in magnitude between selected
pairwise differences in value function results between the Q-learning treatment rules, assigning all individuals to either
treatment A = 1, and treatment A = 0. 6. Across all instances, the Q-learning models produced the most effective
ITRs, with values decreasing significantly as δt increased. This trend indicates a reduced risk of hypertension in the
heterogeneous, treatment-effect-augmented population, especially compared to population-level interventions where
all individuals are assigned to high physical activity. When δ = 1, we observe that the pattern of value functions
bears resemblance to that of the original data across various methods. As the prescriptive treatment effect becomes
increasingly evident, both Q-learning and D-learning demonstrate progressively superior performance compared to the
’one-size-fits-all’ approaches. This underscores the importance of personalizing over population-level interventions
when certain factors significantly affect individual responses to treatment. Applying these methods to existing rich,
detailed observational data can provide an important insight into factors that might distinguish these subgroups of
responders. Future work will build on these existing models to better incorporate additional high-dimensional data.
However, these results suggest that if a large heterogeneous effect truly exists, our method can successfully capture it.
5
Discussion
In this paper, we propose an innovative t-test based approach that can directly compare the value functions of any
two treatment regimes. The validity of the approach follows from the asymptotic normality of the standard value
function for the estimated treatment regime and the asymptotic normality of the propensity score model parameters.
Our method provides valid estimates for (1) the variance and 95% confidence interval for a value function for a single
treatment regime, (2) the variance and 95% confidence interval for the difference between two value functions of two
6The complete pairwise comparison of all the comparisons is depicted in the appendix Figure S5
14

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
Lu et al
A PREPRINT
treatment regimes, (3) the p-value of the t-test for the significance of the difference between two value functions, and
(4) the application of these estimations in scenarios involving multiple imputations. Our method’s estimates exhibit
comparable Type I error and power performance to those obtained via bootstrap. Moreover, our approach simplifies
variance calculation and is computationally more efficient, especially when multiple imputation is used to handle
missing data. Through simulation studies and the data application example, we demonstrate the performance and the
ease of implementation of our method in different scenarios. Additionally, this method enables the evaluation and
comparison of ITR effectiveness using abundant observational cohort data when clinical trial data are not available.
This comparison is crucial as individuals seek behavioral modification guidance amidst numerous recommendations,
and emphasizing targeting strategies could increase the likelihood of effective changes.
Nevertheless, it is important to acknowledge a limitation inherent in our methodology – its reliance on the presupposition
that the propensity score model holds true. In observational data, extreme propensity scores can influence the estimates
of the value function as well as the variance estimates of the value function. For future work, it will be interesting to use
more robust estimators to alleviate the impact of potential misspecification of the propensity score model. Another
extension of this method is to multiple-stage ITR comparison. Extending our method to simultaneously compare more
than two ITRs presents an interesting avenue for future research, which would require establishing the asymptotic
normality of the joint propensity scores for multiple treatment assignments.
To conclude, our method offers a convenient approach to comparing two treatment regimes directly. Furthermore, it
is suitable for observational data and randomized trial data and has the ability to incorporate multiple imputation for
missing data.
Acknowledgments
This work was supported by the NIH, Eunice Kennedy Shriver National Institute of Child Health and Human Devel-
opment (R01 HD30880), and the National Institute on Aging (R01AG065357). This research uses data from China
Health and Nutrition Survey (CHNS). We are grateful to research grant funding from the National Institute for Health
(NIH), the Eunice Kennedy Shriver National Institute of Child Health and Human Development (NICHD) for R01
HD30880 and R01 HD38700, National Institute on Aging (NIA) for R01 AG065357, National Institute of Diabetes and
Digestive and Kidney Diseases (NIDDK) for R01 DK104371 and P30 DK056350, National Heart, Lung, and Blood
Institute (NHLBI) for R01 HL108427, the NIH Fogarty grant D43 TW009077, the Carolina Population Center for P2C
HD050924 and P30 AG066615 since 1989, and the China-Japan Friendship Hospital, Ministry of Health for support
for CHNS 2009, Chinese National Human Genome Center at Shanghai since 2009, and Beijing Municipal Center for
Disease Prevention and Control since 2011. We thank the National Institute for Nutrition and Health, China Center
for Disease Control and Prevention, Beijing Municipal Center for Disease Control and Prevention, and the Chinese
National Human Genome Center at Shanghai. In addition, Minxin Lu was supported by NC TraCS collaboration on
"Optimizing weight status based on potentially modifiable risk factors". Both Minxin Lu and Michael Kosorok were
funded in part by grant UM1 TR004406 from the National Center for Advancing Translational Sciences. We thank
Matthew Christopher Brown and Lina Maria Montoya for their help and support for the project. The content is solely
the responsibility of the authors and does not necessarily represent the official views of the NIH.
Author contributions
Minxin Lu, Annie Green Howard, Penny Gordon-Larsen, Katie A. Meyer, Shufa Du, and Michael R. Kosorok
contributed to the study conception and design. Data preparation was performed by Annie Green Howard and Hsiao-
Chuan Tien. Data collection was performed by Huijin Wang and Bing Zhang. Statistical analysis was performed
by Minxin Lu and Michael R. Kosorok. The first draft of the manuscript was written by Minxin Lu and all authors
commented on previous versions of the manuscript. All authors read and approved the final manuscript.
Financial disclosure
None reported.
Conflict of interest
The authors declare no potential conflict of interests.
15

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
Lu et al
A PREPRINT
References
[1] Katrina L Piercy, Richard P Troiano, Rachel M Ballard, Susan A Carlson, Janet E Fulton, Deborah A Galuska,
Stephanie M George, and Richard D Olson. The physical activity guidelines for americans. Jama, 320(19):
2020–2028, 2018.
[2] Richard D Olson, Katrina L Piercy, Richard P Troiano, Rachel M Ballard, Janet E Fulton, Deborah A Galuska,
Shellie Y Pfohl, Alison Vaux-Bjerke, Julia B Quam, Stephanie M George, Kyle Sprow, Susan A Carlson,
Eric T Hyde, and Kate Olscamp. Physical Activity Guidelines for Americans 2nd edition. The U.S. Depart-
ment of Health and Human Services, https://health.gov/sites/default/files/2019-09/Physical_
Activity_Guidelines_2nd_edition.pdf, 2019.
[3] Claude Bouchard and Tuomo Rankinen. Individual differences in response to regular physical activity. Medicine
& Science in Sports & Exercise, 33(6):S446–S451, 2001.
[4] Min Qian and Susan A Murphy. Performance guarantees for individualized treatment rules. Annals of statistics,
39(2):1180, 2011.
[5] Lu Tian, Ash A Alizadeh, Andrew J Gentles, and Robert Tibshirani. A simple method for estimating interactions
between a treatment and a large number of covariates. Journal of the American Statistical Association, 109(508):
1517–1532, 2014.
[6] Jonathan AC Sterne, Ian R White, John B Carlin, Michael Spratt, Patrick Royston, Michael G Kenward, Angela M
Wood, and James R Carpenter. Multiple imputation for missing data in epidemiological and clinical research:
potential and pitfalls. Bmj, 338, 2009.
[7] Xiaotong Jiang, Amanda E Nelson, Rebecca J Cleveland, Daniel P Beavers, Todd A Schwartz, Liubov Arbeeva,
Carolina Alvarez, Leigh F Callahan, Stephen Messier, Richard Loeser, et al. Precision medicine approach to
develop and internally validate optimal exercise and weight-loss treatments for overweight and obese adults with
knee osteoarthritis: data from a single-center randomized trial. Arthritis care & research, 73(5):693–701, 2021.
[8] Yifan Cui, Ruoqing Zhu, and Michael Kosorok. Tree based weighted learning for estimating individualized
treatment rules with censored data. Electronic journal of statistics, 11(2):3927, 2017.
[9] Yingqi Zhao, Donglin Zeng, A John Rush, and Michael R Kosorok. Estimating individualized treatment rules
using outcome weighted learning. Journal of the American Statistical Association, 107(499):1106–1118, 2012.
[10] Chengchun Shi, Sheng Zhang, Wenbin Lu, and Rui Song. Statistical inference of the value function for re-
inforcement learning in infinite-horizon settings. Journal of the Royal Statistical Society Series B: Statistical
Methodology, 84(3):765–793, 2022.
[11] Bradley Efron. Bootstrap methods: another look at the jackknife. In Breakthroughs in statistics: Methodology
and distribution, pages 569–593. Springer, 1992.
[12] Stephen Bates, Trevor Hastie, and Robert Tibshirani. Cross-validation: what does it estimate and how well does it
do it? arXiv preprint arXiv:2104.00673, 2021.
[13] Bibhas Chakraborty, Susan Murphy, and Victor Strecher. Inference for non-regular parameters in optimal dynamic
treatment regimes. Statistical methods in medical research, 19(3):317–343, 2010.
[14] Eric B Laber and Susan A Murphy. Adaptive confidence intervals for the test error in classification. Journal of the
American Statistical Association, 106(495):904–913, 2011.
[15] Bibhas Chakraborty, Eric B Laber, and Yingqi Zhao. Inference for optimal dynamic treatment regimes using an
adaptive m-out-of-n bootstrap scheme. Biometrics, 69(3):714–723, 2013.
[16] Peter C Austin. An introduction to propensity score methods for reducing the effects of confounding in observa-
tional studies. Multivariate behavioral research, 46(3):399–424, 2011.
[17] Stef Van Buuren. Flexible imputation of missing data. CRC press, Boca Raton, 2nd edition, 2018.
[18] Hui Zou and Trevor Hastie. Regularization and variable selection via the elastic net. Journal of the royal statistical
society: series B (statistical methodology), 67(2):301–320, 2005.
[19] Michael J Bloch. Worldwide prevalence of hypertension exceeds 1.3 billion. Journal of the American Society of
Hypertension: JASH, 10(10):753–754, 2016.
[20] Samantha Bromfield and Paul Muntner. High blood pressure: the leading global burden of disease risk factor and
the need for worldwide prevention programs. Current hypertension reports, 15:134–136, 2013.
[21] Misghina Weldegiorgis and Mark Woodward. The impact of hypertension on chronic kidney disease and end-stage
renal disease is greater in men than women: a systematic review and meta-analysis. BMC nephrology, 21(1):1–9,
2020.
16

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
Lu et al
A PREPRINT
[22] M Bhargava, MK Ikram, and Tien Yin Wong. How does hypertension affect your eyes? Journal of human
hypertension, 26(2):71–83, 2012.
[23] Lena Kilander, Hakan Nyman, Merike Boberg, Lennart Hansson, and Hans Lithell. Hypertension is related to
cognitive impairment: a 20-year follow-up of 999 men. Hypertension, 31(3):780–786, 1998.
[24] Guijing Wang, Xilin Zhou, Xiaohui Zhuo, and Ping Zhang. Annual total medical expenditures associated with
hypertension by diabetes status in us adults. American journal of preventive medicine, 53(6):S182–S189, 2017.
[25] Mei Zhang, Yu Shi, Bin Zhou, Zhengjing Huang, Zhenping Zhao, Chun Li, Xiao Zhang, Guiyuan Han, Ke Peng,
Xinhua Li, et al. Prevalence, awareness, treatment, and control of hypertension in china, 2004-18: findings from
six rounds of a national survey. bmj, 380, 2023.
[26] Ji-Guang Wang, Wei Zhang, Yan Li, and Lisheng Liu. Hypertension in china: epidemiology and treatment
initiatives. Nature Reviews Cardiology, pages 1–15, 2023.
[27] Bin Cui, Zhaohui Dong, Mengmeng Zhao, Shanshan Li, Hua Xiao, Zhitao Liu, and Xiaowei Yan. Analysis of
adherence to antihypertensive drugs in chinese patients with hypertension: a retrospective analysis using the china
health insurance association database. Patient preference and adherence, pages 1195–1204, 2020.
[28] Lawrence J Appel. Lifestyle modification as a means to prevent and treat high blood pressure. Journal of the
American Society of Nephrology, 14(suppl 2):S99–S102, 2003.
[29] James Cane, Denise O’Connor, and Susan Michie. Validation of the theoretical domains framework for use in
behaviour change and implementation research. Implementation science, 7:1–17, 2012.
[30] Bing Zhang, FY Zhai, SF Du, and Barry M Popkin. The c hina h ealth and n utrition s urvey, 1989–2011. Obesity
reviews, 15:2–7, 2014.
[31] Shu Wen Ng, A-G Howard, HJ Wang, Chang Su, and Bing Zhang. The physical activity transition among adults
in c hina: 1991–2011. Obesity Reviews, 15:27–36, 2014.
[32] Barbara E Ainsworth, William L Haskell, Stephen D Herrmann, Nathanael Meckes, David R Bassett Jr, Catrine
Tudor-Locke, Jennifer L Greer, Jesse Vezina, Melicia C Whitt-Glover, and Arthur S Leon. 2011 compendium of
physical activities: a second update of codes and met values. Medicine & science in sports & exercise, 43(8):
1575–1581, 2011.
[33] Louisa G Sylvia, Emily E Bernstein, Jane L Hubbard, Leigh Keating, and Ellen J Anderson. A practical guide to
measuring physical activity. Journal of the Academy of Nutrition and Dietetics, 114(2):199, 2014.
[34] Daniel J. Stekhoven. missForest: Nonparametric Missing Value Imputation using Random Forest. CRAN,
https://cran.r-project.org/package=missForest, 2022. R package version 1.5.
[35] Daniel J. Stekhoven and Peter Buehlmann. Missforest - non-parametric missing value imputation for mixed-type
data. Bioinformatics, 28(1):112–118, 2012.
[36] Pengcheng Huai, Huanmiao Xun, Kathleen Heather Reilly, Yiguan Wang, Wei Ma, and Bo Xi. Physical activity
and risk of hypertension: a meta-analysis of prospective cohort studies. Hypertension, 62(6):1021–1026, 2013.
17

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
Lu et al
A PREPRINT
A
Proofs
Proof of Equation (4)
Proof. √m( ˆVm( ˆdj,n) −V0( ˆdj,n)) =
√m(
Pm
i=1
yi1{ai= ˆdj,n(xi)}
ˆπn(ai|xi)
−mE( Y 1{A= ˆdj,n(X)}
ˆπn(A|X)
)
Pm
i=1
1{ai= ˆdj,n(xi)}
ˆπn(ai|xi)
)
−√m(
E[ Y 1{A= ˆdj,n(X)}
ˆπn(A|X))
][Pn
i=1
1{ai= ˆdj,n(xi)}
ˆπn(ai|xi)
−mE( 1{A= ˆdj,n(X)}
ˆπn(A|X)
)]
E[ 1{A= ˆdj,n(X)}
ˆπn(A|X))
][Pn
i=1
1{ai= ˆdj,n(xi)}
ˆπn(ai|xi)
]
)
+√m

E[ Y 1{A= ˆdj,n(X)}
ˆπn(A|X))
] −E[ Y 1{A= ˆdj,n(X)}
π0(A|X))
]
E[ 1{A= ˆdj,n(X)}
ˆπn(A|X))
]


−√m(
E[ Y 1{A= ˆdj,n(X)}
π0(A|X))
][E[ 1{A= ˆdj,n(X}
ˆπn(A|X)
−E( 1{A= ˆdj,n(X)}
π0(A|X)
)]
E[ 1{A= ˆdj,n(X)}
ˆπn(A|X))
]E[ 1{A= ˆdj,n(X)}
π0(A|X)
]
)
= B1,m −B2,m + B3,m −B4,m,
where
B1,m = √m(
Pm
i=1
yi1{ai= ˆdj,n(xi)}
ˆπn(ai|xi)
−mE( Y 1{A= ˆdj,n(X)}
ˆπn(A|X)
)
Pm
i=1
1{ai= ˆdj,n(xi)}
ˆπn(ai|xi)
)
=
Gn( Y 1{A= ˆdj,n(X)}
ˆπn(A|X)
)
Pn[ 1{A= ˆdj,n(X)}
ˆπn(A|X)
]
= Gn[Y 1{A = ˆdj,n(X)}
π0(A|X)
] + oP (1),
where Gn((f(U)) = √n[Pn(f(U)) −P(f(U))], Pnf(U) = n−1 Pn
i=1 f(ui) is the empirical measure, Pf(U) =
E(f(U)) is the expectation taken over U. By empirical process methods, Pn[ 1{A= ˆdj,n(X)}
ˆπn(A|X)
] →E[ 1{A= ˆdj,n(X)}
π0(A|X)
] = 1,
in probability. Using Slutsky’s theorem, and the empirical average converges to its limiting value.
Next,
B2,m =
E[ Y 1{A= ˆdj,n(X)}
ˆπn(A|X)
]Gn[ 1{A= ˆdj,n(X)}
ˆπn(A|X)
]
E[ 1{A= ˆdj,n(X)}
ˆπn(A|X)
]Pn[ 1{A= ˆdj,n(X)}
ˆπn(A|X)
]
= V0( ˆdj,n)Gn(1{A = ˆdj,n(X)}
π0(A|X)
) + oP (1),
by the following steps based on empirical process methods and Slutsky’s theorem:
E[ Y 1{A= ˆdj,n(X)}
ˆπn(A|X)
]
E[ 1{A= ˆdj,n(X)}
ˆπn(A|X)
]
=
E[ Y 1{A= ˆdj,n(X)}
π0(A|X)
]
E[ 1{A= ˆdj,n(X)}
π0(A|X)
]
+ oP (1) = V0( ˆdj,n) + oP (1),
Pn[1{A = ˆdj,n(X)}
ˆπn(A|X)
] = 1 + oP (1),
Gn[1{A = ˆdj,n(X)}
ˆπn(A|X)
] = Gn[1{A = ˆdj,n(X)}
π0(A|X)
] + oP (1).
Next,
18

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
Lu et al
A PREPRINT
B3,m = √m

E[ Y 1{A= ˆdj,n(X)}
ˆπn(A|X))
] −E[ Y 1{A= ˆdj,n(X)}
π0(A|X))
]
E[ 1{A= ˆdj,n(X)}
ˆπn(A|X))
]


=
E[Y 1{A = ˆdj,n(X)}]E[√m(
1
ˆπn(A|X) −
1
π0(A|X))]
E[ 1{A= ˆdj,n(X)}
ˆπn(A|X)
]
= −E[Y 1{A = ˆdj,n(X)}√m(ˆπn(A|X) −π0(A|X))
π2
0(A|X)
] + oP (1).
Since √n(π(a|x, ˆθn) −π(a|x, θ0)) = √n(ˆθn −θ0)T ϕ0(a, x) + op(1), we now have that
B3,m = −
p
m/n ∗√n(ˆθn −θ0)T E[ϕ0(A, X)Y 1{A = ˆdj,n(X)}
π2
0(A|X)
] + oP (1).
Finally,
B4,m = −√m
E( Y 1{A= ˆdj,n(X)}
π0(A|X)
)E[1{A = ˆdj,n(X)}(
1
ˆπn(A|X) −
1
π0(A|X))]
E( 1{A= ˆdj,n(X)}
π0(A|X)
)E( 1{A= ˆdj,n(X)}
ˆπn(A|X)
)
= −V0( ˆdj,n)E[1{A = ˆdj,n(X)}√m(
1
ˆπn(A|X) −
1
π0(A|X))] + oP (1)
= V0( ˆdj,n)E[1{A = ˆdj,n(X)}
π2
0(A|X)
√m(ˆπn(A|X) −π0(A|X))] + oP (1)
=
p
m/n√n(ˆθn −θ0)T E[ϕ0(A, X)1{A = ˆdj,n(X)}
π2
0(A|X)
]V0( ˆdj,n) + oP (1).
Thus:
√m( ˆVm( ˆdj,n) −V0( ˆdj,n)) = Gm(Y 1{A = ˆdj,n(X)}
π0(A|X)
)
−V0( ˆdj,n)Gm(1{A = ˆdj,n(X)}
π0(A|X)
)
−
p
m/n√n(ˆθn −θ0)T E[ϕ0(A|X)Y 1{A = ˆdj,n(X)}
π2
0(A|X)
]
+
p
m/n√n(ˆθn −θ0)T E[ϕ0(A|X)1{A = ˆdj,n(X)}
π2
0(A|X)
]V0( ˆdj,n) + oP (1)
= Gm((Y −V0( ˆdj,n))1{A = ˆdj,n(X)}
π0(A|X)
)
−
p
m/n√n(ˆθn −θ0)T E(ϕ0(A, X)(Y −V0( ˆdj,n))1{A = ˆdj,n(X)}
π2
0(A|X)
) + oP (1),
and the desired results follow.
Proof of Proposition 2
Proof.
√m( ˆVm( ˆd1,n) −ˆVm( ˆd2,n) −V0( ˆd1,n) + V0( ˆd2,n))
= Gm[(Y −V0( ˆd1,n))1{A = ˆd1,n(X)} −(Y −V0( ˆd2,n))1{A = ˆd2,n(X)}
π0(A|X)
]
19

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
Lu et al
A PREPRINT
−
p
m/n√n(ˆθn −θ0)T E(ϕ0(A, X)(Y −V0( ˆd1,n))1{A = ˆd1,n(X)} −(Y −V0( ˆd2,n))1{A = ˆd2,n(X)}
π2
0(A|X)
) + oP (1)
→N(0, T 2
0 ),
in distribution, where
T 2
0 = V ar(U1 −U2) + m
n (W1 −W2)T Σ0(W1 −W2),
and standard arguments can now be used to show that ˆT 2
m →T 2
0 as m →∞, where
ˆT 2
m = m−1
m
X
i=1
( ˆUi,1 −ˆUi,2 −¯U1 + ¯U2)2 + m
n ( ˆW1 −ˆW2)T ˆΣn( ˆW1 −ˆW2).
Proof of Assumptions: logistic regression as an example
Proof. In general, most generalized linear models satisfy all assumptions under standard regularity conditions. Here,
we illustrate this using logistic regression as an example. The first assumption is automatically satisfied for logistic
regression. Suppose the propensity score model is specified as π(a|x, θ0) =
eaθT
0 x
1+eθT
0 x , for a ∈{0, 1}.
The left-hand side of Equation (1) becomes
√n
 
eaˆθT
n x
1 + eˆθT
n x −
eaθT
0 x
1 + eθT
0 x
!
.
Using a Taylor expansion of ˆθn around θ0 for both a = 1 and a = 0, we obtain:
√n(ˆθn −θ0)T (2a −1)x ·
eaθT
0 x
(1 + eθT
0 x)2 + oP (1).
Therefore, we define
ϕ0(a, x) = x(2a −1) ·
eaθT
0 x
(1 + eθT
0 x)2 ,
and
ˆϕn(a, x) = x(2a −1) ·
eaˆθT
n x
(1 + eˆθT
n x)2 .
This confirms that Assumption 1 is satisfied.
Assumption 2 holds by the asymptotic normality of the maximum likelihood estimator (MLE) for logistic regression,
provided the standard covariance estimator from the MLE is used. An implication of this assumption is that the
propensity score model must be correctly specified.
We can also verify that the third assumption holds. From Assumption 2, we have that ˆθn →θ0 in probability as n →∞.
By the continuous mapping theorem, it follows that ˆϕn(A, X) →ϕ0(A, X) in probability as n →∞.
Moreover, since ∥ˆϕn(A, X)−ϕ0(A, X)∥≤∥X∥and E∥X∥2 < ∞, we can apply the dominated convergence theorem
to conclude that
P∥ˆϕn(A, X) −ϕ0(A, X)∥2 →0,
in probability as n →∞.
20

````

## PDF page 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
Lu et al
A PREPRINT
B
Additional Tables and Figures
Table S1: Estimated value functions of different treatment regimes for CHNS data.
Training Set
Test Set
Mean
SD
Mean
SD
Obs
0.602
0.021
0.595
0.031
AllLowPA
0.603
0.018
0.591
0.026
AllHighPA
0.600
0.011
0.598
0.017
Q-Learning
0.574
0.013
0.573
0.017
D-Learning
0.576
0.016
0.598
0.023
Table S2: Estimated value differences and p-values of selected comparisons between treatment regimes for CHNS data.
Training Set
Test Set
Difference
Mean
SD
P-Value
Mean
SD
P-Value
AllLowPA vs. Obs
0.001
0.011
0.924
-0.004
0.017
0.827
AllHighPA vs. Obs
-0.001
0.018
0.953
0.003
0.026
0.897
AllHighPA vs. AllLowPA
-0.002
0.021
0.921
0.007
0.032
0.821
Q vs. Obs
-0.028
0.017
0.096
-0.022
0.026
0.407
Q vs. AllLowPA
-0.029
0.017
0.086
-0.018
0.026
0.497
Q vs. AllHighPA
-0.027
0.013
0.043
-0.025
0.018
0.156
Q vs. D
-0.002
0.013
0.871
-0.024
0.020
0.223
21

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
Lu et al
A PREPRINT
Figure S1: Value functions and 95% confidence interval estimates obtained using propensity scores obtained from
different propensity score models: (a) a logistic regression model including all covariates ˆπ = ˆθX, (b) a correctly
specified model containing only truly relevant covariates with estimated parameters ˆπ = ˆθ⊤[1, X1, X2], (c) the true
propensity score model with known parameters π0 = θ⊤
0 [1, X1, X2], and (d) an incorrectly specified model including
only non-relevant covariates with estimated parameters ˆπ = ˆθ⊤[1, X3, X10, X15, X20]. Results shown here are for
scenario 4 (observational data with data missing at random) with n = 5000 training samples, and δt = 1. Scenario 3
shows similar results and is thus omitted. When the propensity score is incorrect, the true value function remains the
same for d1 d2 dopt, the estimates have larger bias, and thus the true variance becomes larger. The true variance for
value difference equals the average of the squared difference between the estimated value difference and the true value
difference.
22

````

## PDF page 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
Lu et al
A PREPRINT
Figure S2: Differences between the two value functions and their corresponding 95% confidence interval estimates,
obtained using propensity scores derived from different models: (a) a logistic regression model including all covariates
ˆπ = ˆθX, (b) a correctly specified model containing only truly relevant covariates with estimated parameters ˆπ =
ˆθ⊤[1, X1, X2], (c) the true propensity score model with known parameters π0 = θ⊤
0 [1, X1, X2], and (d) an incorrectly
specified model including only non-relevant covariates with estimated parameters ˆπ = ˆθ⊤[1, X3, X10, X15, X20].
Results shown here are for scenario 4 with n=5000 training samples and δt = 1. Scenario 3 shows similar results and is
thus omitted.
23

````

## PDF page 24

Technical extraction; compare with original PDF page 24.

````text
Lu et al
A PREPRINT
Figure S3: A demonstration of one estimated propensity score compared to the true propensity score in propensity score
model misspecification sensitivity analysis in one replication.
24

````

## PDF page 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
Lu et al
A PREPRINT
Figure S4: The value function results for both training and test sets for five different treatment regimes: observed
treatment, treatment A = 0 for all individuals, treatment A = 1 for all individuals, Q-learning optimal ITR, and
D-learning optimal ITR. For comparison purposes, we include the average outcome as a benchmark. The results on
original data (a) and three simulated data sets with three levels of treatment effect modification are shown (b) δ = 1, (c)
δ = 2, (d) δ = 10.
25

````

## PDF page 26

FORMULA CHECK REQUIRED: original PDF page 26.

````text
Lu et al
A PREPRINT
Figure S5: The differences of value functions between the pairs of the following treatments for both training and test
sets: treatment A = 0 for all individuals, treatment A = 1 for all individuals, Q-learning optimal ITR, and D-learning
optimal ITR. The results on original data (a) and three simulated data with three levels of treatment effect modification
are shown (b) δ = 1, (c) δ = 2, (d) δ = 10.
26

````

