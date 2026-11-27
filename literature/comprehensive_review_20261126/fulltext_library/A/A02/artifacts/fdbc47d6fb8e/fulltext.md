# Optimal individualized treatment regimes for survival data with competing risks

Original PDF: [original.pdf](original.pdf). SHA256: `fdbc47d6fb8ed52aa8e948fe4aca85d8738c63f4b947b9ee4d1793ad218dfb62`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
Optimal individualized treatment regimes for
survival data with competing risks
Christina W. Zhou
Department of Biostatistics, University of North Carolina at Chapel Hill
Nikki L. B. Freeman,
Department of Biostatistics and Bioinformatics, Duke University
Katharine L. McGinigle,
Division of Vascular Surgery, UNC-CH
and
Michael R. Kosorok
Department of Biostatistics, UNC-CH
November 5, 2024
Abstract
Precision medicine leverages patient heterogeneity to estimate individualized treat-
ment regimens—formalized, data-driven approaches designed to match patients with
optimal treatments. In the presence of competing events, where multiple causes of
failure can occur and one cause precludes others, it is crucial to assess the risk of
the specific outcome of interest, such as one type of failure over another. This helps
clinicians tailor interventions based on the factors driving that particular cause, lead-
ing to more precise treatment strategies. Currently, no precision medicine methods
simultaneously account for both survival and competing risk endpoints. To address
this gap, we develop a nonparametric individualized treatment regime estimator. Our
two-phase method accounts for both overall survival from all events as well as the
cumulative incidence of a main event of interest. Additionally, we introduce a multi-
utility value function that incorporates both outcomes. We develop random survival
and random cumulative incidence forests to construct individual survival and cumu-
lative incidence curves. Simulation studies demonstrated that our proposed method
performs well, which we applied to a cohort of peripheral artery disease patients at
high risk for limb loss and mortality.
Some keywords: multi-utility optimization; precision medicine; random forests; cumulative
incidence function
1
arXiv:2411.08315v1  [stat.ME]  13 Nov 2024

````

## PDF page 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
1
Introduction
Precision medicine (PM) aims to improve healthcare decision-making by tailoring medical
treatments to individual characteristics (Kosorok and Moodie, 2015; Jiang et al., 2017;
Moodie and Krakow, 2020; Kosorok et al., 2021). One way to formalize this goal is through
individualized treatment regimes (ITRs), maps from patient characteristics to treatment
recommendations (Kosorok and Laber, 2019). Ideally, we would like to identify optimal
ITRs, the treatment regimes that, if followed, would yield the best outcome on average in
the targeted population (Kosorok and Laber, 2019; Kosorok and Moodie, 2015). One way
to evaluate this is through the value function, the expected clinical outcome based on a
specified treatment regime.
In healthcare settings, identifying the best outcome can be challenging, especially when
managing complex health conditions.
For example, chronic limb threatening ischemia
(CLTI), the most severe form of peripheral artery disease (PAD), is a disease characterized
by abnormal narrowing and occlusion of the arteries in the lower extremities. CLTI is a
marker for severe, poorly controlled cardiovascular disease and diabetes. Even with medi-
cal and surgical treatment, patients with CLTI are at high risk for devastating outcomes,
including limb loss, cardiac events (e.g., heart attack and stroke), and death (Criqui et al.,
2021). From a statistical perspective, CLTI and CLTI outcomes demonstrate an example of
competing risks (CR). Competing risks arise when individuals are at risk for multiple types
of events, and the occurrence of one event precludes or alters the probability of other events
occurring. For example, if a patient with CLTI dies, they are no longer at risk for limb loss.
Standard survival analyses ignore CR by including patients experiencing the competing risk
as part of the risk set, despite that they can no longer experience the main event of interest.
Thus, methods estimating the cumulative incidence function (CIF), or subdistribution, is
often of interest when analyzing CR data (Kalbfleisch and Prentice, 1980; Fine and Gray,
1999; Austin et al., 2016). By accounting for competing risks, estimation methods avoid
inflation or bias in event probabilities or survival estimates.
Patients with CLTI are highly heterogeneous, and evidence suggests that precision
medicine strategies may improve treatment recommendations and, ultimately, patient out-
comes (McGinigle et al., 2021; Chung et al., 2022). Current ITR estimation methods for
handling the competing risk setting, like that posed by CLTI, focus on either optimizing the
survival curve or minimizing risks of individual events, i.e., minimizing the CIF. However,
none of the existing methods simultaneously optimize the survival function and the CIF.
We address this gap by proposing a nonparametric two-phase optimal ITR estimator
that leverages multi-utility optimization. To do this, we construct a novel multi-utility value
(objective) function that maximizes overall survival (OS) from all causes while minimizing
the CIF of a priority cause (PC), the main event of interest over any other cause of failure.
The first phase of our estimation strategy constructs individual OS curves by adapting the
generalized random survival forests from Cho et al. (2023) to the single stage treatment set-
ting. We develop random cumulative incidence forests (RCIFs) to construct individualized
CIF curves for the PC in the second phase. To select an optimal ITR, we use a flexible, user-
specified criterion (i.e., a tolerance level) to balance treatments so that they appropriately
weigh survival and risks. Unlike most existing methods restricted to binary treatments,
our method considers a flexible finite number of treatment arms. Because our forests are
nonparametric, we can capture complex decision rules. The software package implementing
2

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
our proposed method is made freely available at https://github.com/cwzhou/itrSurv.
The rest of this paper is organized as follows: Section 2 reviews existing literature for
precision medicine and the competing risk setting. Section 3 details our analytic framework
and introduces our proposed method.
Section 4 presents the theoretical properties of
our ITR estimator and forests. Section 5 describes the finite sample performance of our
proposed estimator through simulation studies. We demonstrate our proposed method’s
application to the CLTI setting in Section 6 and follow with a discussion in Section 7.
2
Background
In this section, we briefly review precision analytic survival and CR methods. We conclude
this section with foundational survival and CR ideas that we will use through the remainder
of the manuscript.
2.1
PM methods for survival and CR outcomes
Our work uses tree-based estimators to construct ITRs that simultaneously account for
survival outcomes and CRs. Although a variety of innovative methods have been developed
for estimating ITRs with survival outcomes (Zhao et al., 2015; Hager et al., 2018; Wu et al.,
2020; Zhong et al., 2021; Schrod et al., 2022; Choi et al., 2023; Bakoyannis, 2023), only a
few have employed tree-based methods or accounted for multiple outcomes. Forest-based
methods include Cui et al. (2017); Zhu et al. (2018); Doubleday et al. (2022); Devaux et al.
(2023). Recently, Cho et al. (2023) introduced the generalized random survival forest, a
tree-based approach to predict individualized survival curves. The predicted survival curves
are then used to estimate optimal multi-stage ITRs that maximize the survival curve. Our
proposed method extends the work of Cho et al. (2023) by incorporating multiple outcomes,
i.e., OS and PC cumulative incidence.
Current precision medicine methods for CR is limited. Yavuz et al. (2018) proposed a
nonparametric CIF estimator that was then used to construct optimal ITRs that minimize
the CIF using SMART data. Zhou et al. (2021) focused on minimizing side effects in a CR
setting by estimating the optimal ITR at a specific time point, with side effects constrained
below a set threshold. In He et al. (2021), the authors minimize the CIF to identify the
optimal ITR using a doubly robust method to guard against model misspecification, which
ensures consistency if either model component is correctly specified.
In terms of multiple outcomes, Liu et al. (2023) introduced a multi-stage cumulative
benefit-risk framework for sequential multiple assignment randomized trials (SMARTs). By
incorporating a trade-off framework, Liu et al. (2023) maximized the expected benefit while
simultaneously keeping the expected cumulative risk below a pre-defined threshold. This
framework is not designed to address the complexities of the CR setting, where multiple
failure types may occur.
Standard practices for multiple endpoints include developing composite outcomes
(Neuhauser, 2006; Jetsupphasuk et al., 2023) or using multivariate models (Teixeira-Pinto
et al., 2009; Wu et al., 2024). However, composite outcomes can be difficult to interpret,
especially if one component drives the overall result. An alternative approach is maximizing
an utility function, a fixed summary measure of outcomes (Hayes et al., 2022). Utility
functions for multiple outcomes, which we call multi-utility, have been used for developing
3

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
PM algorithms (Butler et al., 2018; Jiang et al., 2021; Zitovsky et al., 2023). However,
existing methods are not designed for survival data, where censoring may occur. To our
knowledge, there are no existing precision medicine methods for survival outcomes with
CRs that simultaneously account for both outcomes, and there are no existing precision
medicine methods for survival data that utilize a multi-utility value function.
2.2
Foundational Survival and CR ideas
We briefly review key concepts for survival analysis and CRs. Let T represent failure time
and Z represent the associated covariates. The survival function is the probability of not
experiencing an event over time, while the hazard rate is the instantaneous risk of an event
occurring at a specific time, given that the event has not occurred up to that point. The
OS function is S(t; Z) = Pr(T > t|Z) = exp

−
R t
0 λ(u; Z)du

, where λ(t; Z) is the hazard
function at time t.
The CIF, or subdistribution, is the probability that a specific event has occurred by a
certain time, while considering the overall risk set of individuals, including the potential
occurrence of other competing events. The CIF differs from the traditional survival func-
tion, which focuses on time to first event regardless of type. Let fj(t) be the (sub)density
function for the time to a cause j failure, then the cause-j specific hazard is defined as
λj(t; Z) = dΛj(t; Z) = fj(t;Z)
S(t;Z) (Kalbfleisch and Prentice, 1980). A jump point exists when
an individual experiences an event of interest, and the probability of this event occurring
at the jump point is dΛj(t; Z) = Pr(T = t, ϵ = j|T ≥t; Z). If t is a continuity point of
Λj(t; Z), then dΛj(t; Z) = λj(t; Z)dt, indicating a smooth and consistent risk over a very
small time interval around t. The CIF for cause j corresponding to the external covariate
as Fj(t; Z) = Pr(T ≤t, J = j|Z) =
R t
0 S(u −|Z)dΛj(u; Z), where S(t−) is the left-hand
limit of the OS function at time t and Λj(t) is the (left continuous) cumulative cause j
specific hazard function (Kalbfleisch and Prentice, 1980).
3
Proposed Methods
3.1
Framework and Notation
Let ϵi be the cause indicator such that ϵi = j means individual i experienced failure from
cause j, where j = 1, . . . , J. Our focus is on a priority cause of interest. In cases with more
than two causes, we collapse the causes into two such that Pr(ϵ = 1) + Pr(ϵ = 2) = 1:
the PC (cause 1) and all others (cause 2). Let T1i and T2i denote the failure times for
causes 1 and 2, respectively, for patient i, and Ti = min(T1i, T2i) be the overall survival
time, representing time to the first failure. Right-censoring due to study end (τ) or loss
to follow-up is denoted Ci, with censoring time distribution Gi(t) = Pr(Ci ≥t|Zi). The
observed time is Xi = min(Ti, Ci). The OS event indicator is δi = I(Ti ≤Ci). We define
δ1i = I(T1i ≤Ci ∧T2i) and δ2i = I(T2i ≤Ci ∧T1i).
We assume a finite treatment space A.
Let Zi = (Zi1, . . . , ZiP)T represent the P
covariates. For each z ∈Z, let ψ(z) ⊆A to be the set of allowable treatments for a patient
with Z = z. We observe data composed of n i.i.d replicates Dn = {Zi, Xi, δi, δ1i}n
i=1. When
unambiguous, we drop the index i for simplicity.
4

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
Let d represent an ITR, which maps patient covariate information (zi ∈Z) to the
treatment assignment (ai ∈A), d(zi) : zi →ai for each patient i, which satisfies d(z) ∈ψ(z)
for all z ∈Z. Let ϕ(·) be an optimization criteria for OS and CI. In this manuscript,
we focus on the truncated (at τ) area under the curves, ϕ(S) =
R τ
0 S(t) dt and ϕ(Fj) =
R τ
0 Fj(t) dt, the restricted mean survival time at time τ and integrated CIF truncated at τ
respectively. The latter quantity measures the accumulation of the probability of having
the primary event of interest during the follow-up period.
For any treatment a ∈A and covariates vector Z, let S(a)(· | Z) and F (a)
j
(· | Z)
be the potential survival and cumulative incidence curves for patients with covariates Z
and treatment a, respectively. Let ϕ(a)
1 (Z) = ϕ(S(a)(· | Z)) and ϕ(a)
2 (Z) = ϕ(F (a)
j
(· | Z))
denote the potential outcomes of interest. Under regime d, define the potential outcomes
as ϕ(d)
1 (Z) = P
a∈A ϕ(a)
1 (Z)1{d(Z) = a} and ϕ(d)
2 (Z) = P
a∈A ϕ(a)
2 (Z)1{d(Z) = a}, where
1{B} is the indicator of B. We assume that a prolonged time to failure is optimal, so we
optimize a criterion (ϕ1) to maximize OS. Additionally, we want to minimize the CIF of
the PC via ϕ2 due to its inherent importance over all other causes. We aim to estimate the
optimal ITR dopt that optimizes a joint criterion ϕ(d)(Z) =
 
ϕ(d)
1 (Z)
ϕ(d)
2 (Z)
!
= P
a∈A
 
ϕ(a)
1 (Z)
ϕ(a)
2 (Z)
!
·
1{d(Z) = a}.
For any treatment regime d(Z), we define the joint value function of the
ITR estimator as
V(d) =
X
a∈A
E
h
ϕ(a)(Z) · 1{d(Z) = a}
i
.
Define a∗
1 = arg maxa∈A ϕ(a)
1 (Z) with V ∗
1 (Z) = ϕ
(a∗
1)
1
(Z). If OS across treatments are suffi-
ciently close (i.e., within a tolerance level αϕ), then for a treatment a,
1 −ϕ(a)
1 (Z)
V ∗
1 (Z) ≤αϕ.
(1)
This condition assesses if the treatment a performs nearly as well as the best available treat-
ment within the acceptable margin. Equation (1) implies ϕ(a)
1 (Z) ≥(1 −αϕ)V ∗
1 (Z). Thus,
the optimal ITR is defined as dopt(Z) =
(
arg mina∈A ϕ(a)
2 (Z)
if ϕ(a)
1 (Z) ≥(1 −αϕ)V ∗
1 (Z),
arg maxa∈A ϕ(a)
1 (Z)
otherwise.
3.2
Proposed Estimators
To identify the potential outcomes, we assume Assumptions 1-3 (Kidwell, 2016; Kosorok
and Laber, 2019). Then, using identified data, the value function can be written as
V(d) = P
a∈A E [ϕ(a, Z) · 1{d(Z) = a}], and we want to estimate the conditional probabil-
ities ϕ1(a, Z) =
R τ
0 S(t|Z, A = a) dt and ϕ2(a, Z) =
R τ
0 Fj(t|Z, A = a) dt.
Assumption 1 (Stable Unit Treatment Value Assumption (SUTVA)). Each individual’s
counterfactual outcomes, such as cause-specific failure time or overall failure time, are
not affected by the treatment assignments or histories of other individuals in the study.
Additionally, the process of censoring is assumed to be independent of other individuals’
treatments and histories.
5

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
Assumption 2 (Strong ignorability). The treatment assignment is conditionally indepen-
dent of future potential outcomes (such as ϕ(a)
1
or ϕ(a)
2 ), given the individual’s covariates Z.
This can be expressed as ϕ(a) ⊥A | Z, for all a ∈A.
Assumption 3 (Positivity). Given covariate information, the probability of having each
treatment a ∈A is greater than a constant L > 0, or Pr(A = a|Z = z) > L for all a ∈A,
z such that Pr(Z = z) > 0.
3.2.1
Random Forests
To estimate individualized curves for OS and PC cumulative incidence, we develop a ran-
dom survival forest (RSF) and random cumulative incidence forest (RCIF), respectively.
We adapt the generalized random survival forest in Cho et al. (2023) to the single stage
treatment setting. We provide details on the construction of the proposed RSF in the
Supplementary Material.
Following the construction of the RSF, we develop RCIFs to obtain individual CIF
curves for optimization (see Algorithm 1). The Aalen-Johanson (AJ) estimator bFj is used
to estimate the cumulative incidence function, as well as for node splitting.
Letting k
represent the node, the AJ estimator for the CIF for cause j failure (i.e., ϵ = j) in group
k is given by:
bFjk(t) =
Z t
0
bSk(u−)Y −1
k (u)dNjk(u)
(2)
where bSk(t−) is the left-hand limit of the Kaplan-Meier estimate bSk(t) for OS (see Equation
(S1) in Supplementary Material), Njk(t) is the number of failures of cause j by t, Yk(t) is
the number of subjects still at risk just prior to t in group k (Gray, 1988). In building
the trees for the RCIF, k denotes the two groups that are being compared; however, for
prediction, k = 1, . . . , K indexes the terminal node, where K is the number of terminal
nodes. Whenever Fjk(t) refers to the CIF within terminal nodes, we omit the index k such
that Fjk(t) ≡Fj, since there is no risk of ambiguity.
In order to partition a node into two potential daughter nodes (L1, L2), we use Gray’s
two-sample test (Gray, 1988) to compare the priority cause CIF between groups:
Gray(L1, L2) =
Z τ
0
K(t){[1 −bF11(t−)]−1d bF11(t) −[1 −bF12(t−)]−1d bF12(t)},
(3)
where bF1k is an estimate of F1k based on the AJ estimator for CIF of failure cause 1 in
group k and K(t) is some weight function. In this paper, we define K(t) = 1. The splitting
rule chooses (L1, L2) = arg maxL1,L2 Gray(L1, L2) as the best partition.
The recursive
partitioning continues with a minimum of nminevent events (from any cause) in each node
while each node’s size exceeds the threshold nmin. The PC cumulative incidence estimate
of the terminal node L of the w-th cumulative incidence tree is given by the AJ estimator
bFj,{w}(t | L), where w = 1, 2, . . . , ntree. Letting h = (a, Z), the RCIF estimate for priority
cause j is given by
bFj(t | h) =
1
ntree
ntree
X
w=1
#{L{w},l:l}
X
l=1
1(h ∈L{w},l) bFj(t | L{w},l),
6

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
where #{L{w},l : l} is the number of terminal nodes of the w-th tree.
Algorithm 1 The random cumulative incidence forest estimator
Input: {(Xi, δi, δji, Zi, Ai)}n
i=1
Output: bFj(·|Z, A = a)
Result: random cause-j cumulative incidence forest bFj(·|Z, A)
Parameters: number of trees ntree, minimum terminal node size nmin, minimum number
of events nminevent
For treatment arm a ∈A do
For tree w = 1, 2, . . . , ntree do
Partition the feature space with the input data {(Xi, δi, δji, Zi)}i:ai=a via
Gray’s test (3) until node size < 2nmin and there are at least nminevent events
from any cause in every node
Obtain the terminal node cumulative incidence probability bF a
j,{w}(t|Z) via
Aalen-Johanson estimator (2)
Obtain the random cumulative incidence forest estimator
bFj(·|Z, A = a) =
1
ntree
Pntree
w=1 bF a
j,{w}(t|Z)
3.2.2
Estimation Procedure
We propose a two-phase estimation procedure that prioritizes maximizing the criterion of
OS in Phase 1 but also minimizes the criterion of the CIF of a priority cause in Phase
2 over all treatments for each individual. Whether an individual’s treatment is obtained
from Phase 1 or Phase 2 depends on a pre-specified tolerance level 0 < αϕ < 1.
Let bS(·; a, Z) and bFj(·; a, Z) denote the estimated proposed RSF and RCIF forest es-
timators, respectively.
Letting the subscript denote the method phase, we define the
true and estimated functions of ϕ1(a, Z) and ϕ2(a, Z) as ϕ0(a, Z) =
ϕ0
1(a, Z)
ϕ0
2(a, Z)

and
bϕ(a, Z) =
 
bϕ1(a, Z)
bϕ2(a, Z)
!
, respectively.
Let the true optimal treatment for Phase 1 be
a0∗
1
= arg maxa∈A ϕ0
1(a, Z) with V 0∗
1 (Z) = V 0
1 (a0∗
1 , Z), and the estimated value as ba∗
1 =
arg maxa∈A bϕ1(a, Z) with bV ∗
1 (Z) = bV1(ba∗
1, Z). We can then use the following two-phase
procedure to estimate the optimal ITR. For each patient:
(i) estimate the conditional overall survival S(t|Z, A) for each treatment
(ii) estimate the conditional priority j-cause CIF Fj(t|Z, A) for each treatment
(iii) Phase 1: optimize (i) over feasible finite treatment space for all a ∈ψ(z) ⊂A to
obtain optimal treatment for overall survival
(iv) Find As, the set of treatments chosen using αϕ criteria to compare to the optimal
overall survival treatment
(a) if the cardinality of As is 1 then we have ITR estimate bd(z) = As
7

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
(b) if the cardinality of As is greater than 1 then optimize (ii) (Phase 2) over treat-
ment set As to obtain ITR estimate bd(z).
Algorithm 2 The proposed ITR estimator accounting for competing risks.
Input: Zi, Ai, αϕ
Output: bdopt
For each individual i, given covariates Zi and small 0 < αϕ < 1, consider feasible
treatments ai ∈ψ(zi) ⊂A (we drop i for simplicity):
1. Obtain bS(·|Z, A) via random survival forest (Cho et al., 2023)
2. Obtain bFj(·|Z, A) via random cumulative incidence forest (Algorithm 1)
3. Let the estimated optimal treatments for Phase 1 (overall survival) be
ˆa∗
1 = arg maxa∈ψ(z) bϕ1(a, Z) and bV ∗
1 (Z) = bV1(ˆa∗
1, Z)
4. Obtain overall survival treatment set As = {a ∈ψ(Z) : bϕ1(a, Z) ≥(1 −αϕ)bV ∗
1 (Z)}
• If As is singleton, As is the estimated optimal treatment: bdopt(Z) = As.
• If #As > 1, optimal treatment for Phase 2 is bdopt(Z) = arg mina∈As bϕ2(a, Z).
In other words, if ai̸ = As
i for individual i, then individual i stopped at either
Phase 1: bϕ1(a, Z) < (1 −αϕ)bV ∗
1 (Z) or
Phase 2: bϕ1(a, Z) ≥(1 −αϕ)bV ∗
1 (Z) but bϕ2(a = bdopt, Z) < bϕ2(a = ai, Z)
and As
i may have #As
i > 1.
Algorithm 2 provides a high-level outline of our proposed method. Briefly, if the areas
under the truncated survival curve between the treatments are within certain αϕ, then we
want to reduce PC cumulative incidence. We consider the competing risk of a priority
cause if the OS experience is not too different. However, if the OS experience is excessively
different, then we proceed as if the competing risk is not relevant. From Equation (1),
1 −
bϕ1(a,Z)
bV ∗
1 (Z) ≤αϕ =⇒bϕ1(a, Z) ≥(1 −αϕ)bV ∗
1 (Z). Thus, the optimal ITR when #As > 1 is
defined as bdopt(Z) = arg mina∈A:bϕ1(a,Z)≥(1−αϕ)bV ∗
1 (Z) bϕ2(a, Z).
4
Theoretical Properties
We show consistency of our proposed optimal ITR estimator bdopt(Z), as well as the ran-
dom survival forest in the single stage setting and our proposed RCIF. The proofs of all
theorems are presented in the Supplementary Material. We use the definition of regular
trees and random-split trees from the random forest literature (Meinshausen, 2006; Wager
and Walther, 2016; Cui et al., 2022).
Definition 1 (Random-split and α-regular trees and forests). A tree is called a random-
split tree if each feature is given a minimum probability (ψ/d) of being the split variable at
each intermediate node, where 0 < ψ < 1 and d is the dimension of the feature space. A
8

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
tree is α-regular if every daughter node has at least an α fraction of the training sample in
the corresponding parent node. A random forest is called a random-split (α-regular) forest
if each of its member trees is random-split (α-regular).
In addition to Assumptions 1-3 in Section 3.2, we also assume the following assump-
tions. Assumption 4 is important for asymptotic results, and is typical for survival analysis
(Fleming and Harrington, 2011; Cui et al., 2017). This assumption ensures we only calcu-
late each survival or cumulative incidence curve up to a time point with sufficiently large
sample size.
Assumption 4. There exists a fixed maximum follow-up time 0 < τ < ∞and a constant
M ∈(0, 1), such that Pr(Xτ ≥τ|Z = z) ≥M, for all z ∈Z.
Below are assumptions used for consistency of both forests. Assumptions 5-7 are nec-
essary and realistic for the tree-based estimator terminal node size and splitting rules.
Assumption 5 requires the terminal node size to be not only sufficiently large absolutely
but also sufficiently small relative to the sample size. Assumption 6 follows from Defini-
tion 1. Assumption 7 adds smoothness to the survival function and censoring cumulative
distribution function. Assumption 8 follows from Cui et al. (2017) and Wager and Walther
(2016), which allows for dependency between covariates. Thus, non-hyper-rectangular or
categorical history spaces are allowed with this assumption. Assumption 9 is necessary
for the random cumulative incidence forest because there is non-differentiability of the
treatment policy.
Assumption 5 (Terminal node size, polynomial). The minimum size nmin of the terminal
nodes grows at the rate nmin ▷◁nβ, 1
2 < β < 1, where a ▷◁b implies that both a = O(b) and
b = O(a).
Assumption 6 (α-regular and random-split trees). Trees are α-regular and random-split
with a constant 0 < ψ < 1.
Assumption 7 (Lipschitz continuous and bounded survival and censoring cumulative
densities). There exist constants LS and LG such that |S(t|h1) −S(t|h2)| ≤LS∥h1 −h2∥
and |G(t|h1)−G(t|h2)| ≤LG∥h1−h2∥for all h1, h2 ∈H, t ∈[0, τ], where G is the censoring
cumulative distribution function (CDF) and S(τ −| h)G(τ −| h) > c1 for all h and some
constant c1 > 0.
Assumption 8. The covariates Z ∈[0; 1]d are distributed according to a density function
p(·) satisfying 1/ζ ≤p(z) ≤ζ, for all z and some ζ ≥1.
Assumption 9. The kernel kh for the random cumulative incidence forest has bounded
total variation. Specifically, there exists a constant C such that the total variation of kh
satisfies
Z ∞
−∞
|k′
h(x)| dx ≤C,
where k′
h(x) denotes the derivative of the kernel kh.
Below are assumptions for the proposed estimator for consistency. We assume bounding
in Assumptions 10-11 to account for nonregularity of the value function. This is a necessary
and standard assumption for non-regularity conditions.
9

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
Assumption 10. Define the random function B(a, Z) = ϕ0
1(a, Z)−(1−αϕ)V 0∗
1 (Z), a ∈A.
Assume B(a, Z) has continuous, bounded densities at 0, for each a ∈A.
Assumption 11. supa,Z

ϕ0
1(a, Z)
ϕ0
2(a, Z)
 is bounded by some η < ∞.
4.1
Individualized Treatment Rule Estimator
For any fixed value of covariate Z, the difference in value functions between true optimal
ITR and estimated optimal ITR based on Algorithm 2 is
V(d0
opt(Z)) −V(bdopt(Z)) =
X
a∈A
E
ϕ0
1(a, Z)
ϕ0
2(a, Z)

·

1{d0
opt(Z) = a} −1{bdopt(Z) = a}

(4)
where V(d(Z)) is ϕ of a treatment regime d(Z) if all individuals in a population follow the
treatment regime. Showing Equation (4) converges in probability to 0 proves that bdopt con-
verges in probability to the true d0
opt. The following theorem states that the individualized
treatment regime estimator has a value consistent for the value of the optimal regime.
Theorem 1. (Consistency of the individualized treatment regime estimator) Assume As-
sumptions 4-8 hold. Let bdopt denote the optimal ITR estimator that is built following Al-
gorithm 2 and Assumptions 10-11. Assume Assumptions 1-3 hold and that the random
forests are built for each treatment arm. Then, for ϕµ =
ϕµ
1
ϕµ
2

,
lim
n→∞∥V(d0
opt(Z)) −V(bdopt(Z))∥
p−→0
where ∥· ∥is defined as the L2 norm.
4.2
Random Forests
Consistency of our proposed estimator depends on consistency of the forests. We show this
in Theorems 2 and 3. For simplicity, let h = (a, Z).
Theorem 2 (Uniform consistency of a random survival forest). Suppose that Assumptions
4-8 hold. Let bS(t | h) be an estimator of the survival probability S(t | h) that is uniformly
consistent in both h ∈H and t ∈[0, τ]. Then, the single-stage version of the random
survival forest bS(t | h) in Cho et al. (2023) built based on {Hi, δi}n
i=1 is uniformly consistent.
Specifically,
sup
t∈(0,τ]
h∈H
bS(t | h) −S(t | h)
 →0
in probability as n →∞.
Theorem 3 (Uniform consistency of a random cumulative incidence forest). Suppose that
bounded kernels for the random cumulative incidence forest (RCIF) hold and have total
bounded variation (Assumption 9). Let bFn(t | h) be an estimator of the cause-j cumulative
10

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
incidence function Fj(t | h) that is uniformly consistent in both h ∈H and t ∈[0, τ]. Then,
the RCIF bFn(t | h) built based on {Hi, δi, δji}n
i=1 is uniformly consistent. Specifically,
sup
t∈(0,τ]
h∈H
 bFn(t | h) −Fj(t | h)
 →0
in probability as n →∞.
5
Simulations
We conducted an extensive simulation study to assess the finite sample performance of our
proposed optimal ITR learning method. We examined two data generating mechanisms, an
independent failure time simulation setting using exponential distributions and a dependent
failure time simulation setting following Fine and Gray (1999). For both simulation settings,
we simulated two causes of failure: priority cause 1 with failure time T1 and cause 2 with
failure time T2. We generated p covariates Zi from independent Uniform(0,1) distributions.
We assumed two treatments, A = 0, 1. Let β1(A) and β2(A) denote the p × 1 vectors of
cause-specific coefficients dependent on treatment assignment A. The simulations varied by
censoring level, treatment assignment mechanisms (independent of covariates vs conditional
on covariates), training sample sizes, covariate dimensions, and (for Fine-Gray only) a low
vs. high probability mass for the priority cause. Treatment was allocated using a Bernoulli
trial with propensity π(H) =

1 + exp

−ZT
i βπ
	−1, where the propensity coefficient is
βπ = (0, −1
21p)T for the observational data setting and 0p+1 for the randomized trial setting.
We simulated 100 datasets and compared our method to dtrSurv which refers to the
method in Cho et al. (2023), AIPWE which refers to the method in He et al. (2021),
PMCR which refers to the method in Zhou et al. (2021), the zero-order model which is our
proposed method but assumes no individual variation in treatment effects across patients,
and the observed policy. We set the following forest parameters: ntree = 300, nmin = 5
and nminevents = 2. We chose αϕ = 0.07 for the truncated integration criterion ϕ(·).We
evaluated methods using a testing dataset with Neval = 1000 subjects,assessing ϕ1(a, Z)
and ϕ2(a, Z) across simulations. We calculated the OS and PC CIF value functions and
averaged the criteria across all subjects per simulation.We note that our proposed method
accommodates more than two treatments and causes.
5.1
Exponential Setting
In this simulation setting, we assume T1 is independent from T2, where T1 ∼exp(exp(ZT
i βA
1 )),
T2 ∼exp(exp(ZT
i βA
2 )). Since T1 ⊥T2, T ∼exp(exp(ZT
i βA
1 ) + exp(ZT
i βA
2 )). Let λA
1 =
exp(ZT
i βA
1 ) and λA
2 = exp(ZT
i βA
2 ). Then for the truncated mean criterion, we have ϕµ
1(t) =
R τ
0 S(t)dt =
R τ
0 exp(−(λA
1 + λA
2 )t)dt and ϕµ
2(t) =
R τ
0 Pr(T ≤t, ϵ = 1|Zi)dt =
R τ
0
λA
1
λA
1 +λA
2 −
e−λA
2 t +
λA
2
λA
1 +λA
2

e−(λA
1 +λA
2 )t
dt. The derivations can be found in the Supplementary Mate-
rial. Censoring is sampled from exponential distribution such that approximately 15% of
the final dataset is censored for low censoring, or approximately 50% for high censoring.
In Figure 1, we plot the results from our simulation setting, where each dot represents
a simulation iteration for each method. The left side shows the mean truncated OS and
11

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
the right side shows the area under the cause 1 cumulative incidence curve.
Overall, the variance of the truncated mean criterion across simulations for our proposed
method is generally smaller than those of other methods. The variance for simulations with
N = 700 training data is smaller than that for N = 300, but there does not appear to
be any obvious difference between the two treatment assigning mechanisms. The zero-
order model only picks one treatment for the entire sample, thereby having a single regime
across samples for the same setting. Thus, in the chance that the “worse” treatment is
selected, it can be harmful to patients. We can see that compared to the zero-order model
and observed policy, our proposed method has higher average survival. Compared to the
proposed model, both dtrSurv and PMCR have lower average survival and higher average
cumulative incidence. APIWE and the observed policy tend to have better CI but has a
lower average survival, meaning they are more catered towards the priority cause, at the
expense of OS.
Figure 1: Results from exponential setting simulations. (Left) Estimated mean truncated
OS time, and (right) the estimated integrated priority cause CIF under each estimated pol-
icy. Each dot represents one simulation replicate. The boxplots are the quartile summary
of the points and the black dots are the average values of each method. The rows and
columns of boxes represent a data generation scenario, study design and sample size.
5.2
Fine-Gray Setting
Following the simulation set-up in Fine and Gray (1999), we simulate two competing risks
for i = 1, . . . , N, where the CIF for failures from cause 1 (ϵ = 1) are given by a unit
exponential mixture with mass 1−p at ∞when covariate values are 0, and use proportional
subdistribution hazards model to obtain CIF for nonzero covariate values:
Pr(Ti ≤t, ϵ = 1|Zi) = 1 −[1 −p{1 −exp(−t)}]exp(ZT
i βA
1 ).
More details are provided in the supplementary material.
We first examine the mean
truncated restricted OS time (ϕµ
1 =
R τ
0 S(t)dt), then the mean truncated restricted PC
12

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
(cause 1) CIF (ϕµ
2 =
R τ
0 Pr(T ≤t, ϵ = 1)dt). The full simulation results are displayed in
Figure 2, where each dot represents a simulation iteration for each method, and the average
across simulations is presented. A higher truncated mean survival time (left) and lower
area under CIF for priority cause (right) is ideal.
Figure 2: Results from Fine-Gray setting simulations. (Left) Estimated truncated mean
overall survival time, and (right) the estimated integrated priority cause cumulative inci-
dence function under each estimated policy. Each dot represents one simulation replicate.
The boxplots are the quartile summary of the points and the black dots are the average
values of each method. The rows and columns of boxes represent a data generation sce-
nario, study design and sample size.
When pmass = 0.2, our proposed method generally has the same mean times for OS
(albeit slightly lower) and slightly lower mean times for CI. We note that while AIPWE and
the observed policy sometimes have a lower CIF average (e.g., 5 covariates and pmass = 0.2),
their mean survival time average is also much lower. We also note that in the second row,
our method has a mean lower than dtrSurv but higher than AIPWE and PMCR; and the
opposite is true for cumulative incidence (lower compared to dtrSurv, but higher compared
to AIPWE and PMCR). This is what we would expect, since dtrSurv determines optimal
ITRs based on OS, while AIPWE and PMCR determine based on cumulative incidence.
When pmass = 0.8, where PC has strong influence on the data, the OS for all methods are
similar with low variance across simulations (see Figure 3 for fixed y-axis scales). However,
when comparing the PC cumulative incidence, our model produces the lowest times on
average, with the exception of the observed policy (which also has very low OS on average).
Figure 3 displays just the setting of low censoring, high sample size, and 5 covariates
where the treatment assignment did not depend on covariates and pmass = 0.8 from Figure
2. We can see that our method performs well, with similar survival times to other methods
while producing lower mean truncated cumulative incidence for the PC times on average
across simulations.
13

````

## PDF page 14

Technical extraction; compare with original PDF page 14.

````text
Figure 3: Fine-Gray setting for low censoring, high sample size, high covariates, high PC
probability mass for covariate-independent treatment assignment mechanism. (Left) Esti-
mated truncated mean overall survival time, and (right) the estimated integrated priority
cause cumulative incidence function under each estimated policy. Each dot represents one
simulation replicate. The boxplots are the quartile summary of the points, and the black
dots are the average values of each method.
6
Analyses of Peripheral Artery Disease Cohort
We applied our proposed method to a cohort of patients treated for CLTI in a single
academic medical center.
The dataset was derived from the Carolina Data Warehouse
for Health, which is housed within the North Carolina Translational and Clinical Sciences
Institute (NC TraCS) and includes electronic health record data derived from care provided
at the University of North Carolina at Chapel Hill Medical Center. The cohort included
patients that met the hemodynamic and symptomatic diagnostic criteria for CLTI and
underwent an open surgical or endovascular revascularization to restore blood flow to the
lower limbs between April 2013 and October 2017. Details for this cohort were described
previously (McGinigle et al., 2021).
CLTI predominantly affects older adults, who have a history of smoking or other risk
factors for developing arterial occlusive disease like hypertension and elevated cholesterol.
Five-year mortality after a diagnosis of CLTI is 60% (Criqui et al., 1992; van Haelst et al.,
2018; Baubeta Fridh et al., 2017). Poor systemic cardiovascular health increases the risk of
heart attacks, stroke, and premature death, the severe arterial insufficiency in the arteries
of the legs puts patients with CLTI patients at risk for non-healing foot ulcers, gangrene,
or foot infections, all of which further elevate the risk of limb loss (Mills et al., 2014;
Browder et al., 2022; Crowner et al., 2022). However, despite multiple treatment options,
approximately half of patients with CLTI will experience limb loss or death within two years
following surgical intervention (Farber et al., 2022). Our goal is to derive the optimal ITR
14

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
for patients undergoing the two surgical treatments, endovascular therapy and open bypass
surgery, by prioritizing OS while minimizing the risk of death, with major amputation
before death considered as a competing risk.
Patients with more than one limb affected by disease were excluded from the study.
Among those who experienced major amputation, we only included patients who had the
amputation on the limb that underwent the index revascularization procedure. For in-
stance, patients who had major amputation on the left limb but received open surgical
revascularization on the right limb were excluded. Given that the decision to perform an
open bypass is largely based on surgeon and patient preference, which may be influenced
by the invasive nature of the procedure, we classified patients who initially underwent en-
dovascular surgery (such as angioplasty or stent) but subsequently received an open bypass
within a week as part of the open bypass treatment group. Our final analytic dataset had
N = 303, with 77.9% of patients in the endovascular treatment group and 22.1% in the
open bypass group. We analyzed 1-year follow-up data such that τ = 365 days, and any
observed events after τ were considered censored with Xi = τ. The tailoring variables were
age at treatment (in years), race, ethnicity, gender, severity of clinical presentation (limb-
based Rutherford class), degree of ischemia, severity of foot wound anatomic location of
arterial occlusive disease, previous revascularization history, and presences of clinical sig-
nificant comorbidities including diabetes, hypertension, hyperlipidemia, renal disease, coro-
nary artery disease, myocardial infarction, uncomplicated or complicated congestive heart
failure, cerebrovascular accident, obesity, smoking, chronic obstructive pulmonary disease,
coagulopathy, anemia, dementia, venous insufficiency, venous thromboembolism (VTE),
and unintentional weight loss. For more details, refer to the Supplementary Material.
Figure 4: (Left) Estimated truncated mean survival time for preventing failure from all
causes (major amputation before death or death) and (right) estimated truncated mean
survival time for preventing mortality of the individualized treatment regime estimators.
Each dot represents one cross-validation replicate. The black square dots are the average
values of each method.
Our results compared to the same methods in the simulation studies, the zero-order
model, and the observed policy are presented in Figure 4. We illustrated the truncated
mean failure time for both endpoints, where failure on the left is failure from any cause,
and failure on the right is failure from death, the priority cause.
AIPWE was unable
15

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
to perform with the sample size less than 500 for all CV iterations. Thus, we did not
include all KCV = 10 folds AIPWE in our results. From Figure 4, our method performs
well compared to other existing precision medicine methods. We note that the zero-order
model version of our method may outperform the precision medicine version of our method.
However, this implies that our proposed two-phase method works well, but heterogeneity
might not be enough in this dataset to distinguish between patients. We have already
show via simulations that heterogeneity is important to consider. The observed policy
average also performed slightly better than our method average for mean truncated OS
time. This suggested that the surgeon treatment recommendation is good for the patients,
as expected from the experts in the field. Because our method also considers minimizing
cumulative incidence of death, the average across folds for mean truncated death failure
time is still higher than the observed policy. However, limitations in this analysis include
an unbalanced number in the treatment groups and high censoring rate (70%).
7
Discussion
We proposed a novel precision medicine approach utilizing multi-utility value functions for
survival outcomes in the presence of competing risks to estimate optimal individualized
treatment regimes. Our main contributions are: 1) estimating optimal ITRs based on OS
and priority cause cumulative incidence simultaneously, 2) prioritizing maximum OS over
minimum priority cause risk, 3) introducing a multi-utility value function, and 4) developing
random survival and cumulative forests that output individualized CIF curves for single
stage treatment allocation. Under standard assumptions and mild regularity conditions,
we established uniform consistency of the value function of our optimal ITR estimator, as
well as for the proposed survival and cumulative incidence random forests.
Our work builds on the work of Cho et al. (2023), which is designed for finite decision
points for survival outcomes and do not consider cause-specific events. Additionally, our
work extends utility functions for multiple outcomes (Butler et al., 2018; Jiang et al., 2021;
Zitovsky et al., 2023) by presenting a multi-utility approach. Our work is closest to Jiang
et al. (2021), but they used multiple utility functions to construct a composite of equally
weighted outcomes, while we implement it directly, incorporating hierarchical structure
through a two-step procedure. With respect to the existing CR PM methods (Friedenre-
ich et al., 2016; Yavuz et al., 2018; Chen et al., 2020; Morzywo lek et al., 2022), our work
most closely relates to Zhou et al. (2021), who minimized side effects in a CR setting by
estimating the optimal ITR at a specific time point, with side effects constrained below
a set threshold. While our method is similar, we incorporate a pre-specified tolerance to
determine whether the CR is applied. Additionally, Zhou et al. (2021) only considered
linear decision rules whereas our approach uses flexible forest-based ensemble methods to
capture complex data patterns. We also compared to He et al. (2021), who’s approach is
doubly robust, while our nonparametric method entirely avoids the risk of model misspec-
ification by not relying on parametric assumptions. He et al. (2021) only considers binary
treatments. In contrast, our method accommodates a finite number of treatments.
Our proposed method has a few limitations. It assumes that one cause is more important
than others, which could affect its applicability in cases where the relative importance
of causes is unclear or varies. Additionally, our method does not include a tie-breaker
16

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
mechanism, meaning optimal ITRs may not be unique. Finally, the user determines the pre-
specified tolerance for our method, making it dependent on their judgment and expertise.
In this manuscript, we provide a meaningful advancement for decision-making in complex
scenarios through multi-utility optimization. Future research may include incorporating
tiebreakers for scenarios with multiple optimal ITRs or extending to multi-stage treatment
settings. Such investigations would provide valuable insights into the method’s versatility.
8
Acknowledgment
The authors thank Sydney Browder for her help cleaning the cohort study data, which was
from the 2017 UNC Center for Healthcare Innovation pilot grant.
9
Supplementary Material
The Supplementary Material contains more information on the random forests, all theorem
proofs, and more details on the simulation studies and PAD analysis. The R package is
available at https://github.com/cwzhou/itrSurv. All R code used in the simulations and
application are available at https://github.com/cwzhou/Analyses.
References
Austin, P. C., D. S. Lee, and J. P. Fine (2016, February). Introduction to the Analysis of
Survival Data in the Presence of Competing Risks. Circulation 133(6), 601–609.
Bakoyannis, G. (2023, December). Estimating Optimal Individualized Treatment Rules
with Multistate Processes. Biometrics 79(4), 2830–2842.
Baubeta Fridh, E., M. Andersson, M. Thuresson, et al. (2017). Amputation rates, mortality,
and pre-operative comorbidities in patients revascularised for intermittent claudication
or critical limb ischaemia: a population based study. European Journal of Vascular and
Endovascular Surgery 54(4), 480–486.
Breiman, L., J. Friedman, R. A. Olshen, and C. J. Stone (1984).
Classification and
Regression Trees (1st ed.). Chapman and Hall/CRC.
Browder, S. E., S. M. Ngeve, M. E. Hamrick, J. E. Wood, F. E. Parodi, L. E. Pascarella,
M. A. Farber, W. A. Marston, and K. L. McGinigle (2022, December).
Analysis of
wound healing time and wound-free period in patients with chronic limb-threatening
ischemia treated with and without revascularization. Journal of Vascular Surgery 76(6),
1667–1673.e1.
Butler, E. L., E. B. Laber, S. M. Davis, and M. R. Kosorok (2018, March).
Incorpo-
rating patient preferences into estimation of optimal individualized treatment rules.
Biometrics 74(1), 18–26.
Chen, L.-W., I. Yavuz, Y. Cheng, and A. S. Wahed (2020, April). Cumulative incidence
regression for dynamic treatment regimens. Biostatistics 21(2), e113–e130.
17

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
Cho, H., S. T. Holloway, D. J. Couper, and M. R. Kosorok (2023, May).
Multi-stage
optimal dynamic treatment regimes for survival outcomes with dependent censoring.
Biometrika 110(2), 395–410.
Choi, T., H. Lee, and S. Choi (2023, February). Accountable survival contrast-learning for
optimal dynamic treatment regimes. Scientific Reports 13(1), 2250.
Chung, J., N. L. B. Freeman, M. R. Kosorok, W. A. Marston, M. S. Conte, and K. L.
McGinigle (2022, March). Analysis of a Machine Learning–Based Risk Stratification
Scheme for Chronic Limb-Threatening Ischemia. JAMA Network Open 5(3), e223424.
Criqui, M. H., R. D. Langer, A. Fronek, et al. (1992). Mortality over a period of 10 years
in patients with peripheral arterial disease. New England Journal of Medicine 326(6),
381–386.
Criqui, M. H., K. Matsushita, V. Aboyans, C. N. Hess, C. W. Hicks, T. W. Kwan, M. M.
McDermott, S. Misra, F. Ujueta, on behalf of the American Heart Association Coun-
cil on Epidemiology, T. Prevention; Council on Arteriosclerosis, V. B. C. on Cardio-
vascular Radiology, I. C. on Lifestyle, C. H. C. on Peripheral Vascular Disease;, and
S. Council (2021). Lower extremity peripheral artery disease: Contemporary epidemiol-
ogy, management gaps, and future directions: A scientific statement from the american
heart association. Circulation 144(9), e171–e191.
Crowner, J. R., W. A. Marston, N. L. Freeman, J. Sperger, H. D. Austin, M. Steffan,
M. A. Farber, J. Chung, and K. L. McGinigle (2022, January). The Society for Vascular
Surgery Objective Performance Goals for Critical Limb Ischemia are attainable in select
patients with ischemic wounds managed with wound care alone.
Annals of Vascular
Surgery 78, 28–35.
Cui, Y., R. Zhu, and M. Kosorok (2017, January).
Tree based weighted learning for
estimating individualized treatment rules with censored data.
Electronic Journal of
Statistics 11(2), 3927–3953.
Cui, Y., R. Zhu, M. Zhou, and M. Kosorok (2022). Consistency of survival tree and forest
models: splitting bias and correction. Statistica Sinica 32, 1245–1267.
Devaux, A., C. Helmer, R. Genuer, and C. Proust-Lima (2023, February). Random survival
forests with multivariate longitudinal endogenous covariates. arXiv:2208.05801 [stat].
Doubleday, K., J. Zhou, H. Zhou, and H. Fu (2022, February). Risk controlled decision
trees and random forests for precision Medicine. Statistics in Medicine 41(4), 719–735.
Farber, A., M. T. Menard, M. S. Conte, J. A. Kaufman, R. J. Powell, N. K. Choudhry,
T. H. Hamza, S. F. Assmann, M. A. Creager, M. J. Cziraky, M. D. Dake, M. R. Jaff,
D. Reid, F. S. Siami, G. Sopko, C. J. White, M. Van Over, M. B. Strong, M. F. Villarreal,
M. McKean, E. Azene, A. Azarbal, A. Barleben, D. K. Chew, L. C. Clavijo, Y. Douville,
L. Findeiss, N. Garg, W. Gasper, K. A. Giles, P. P. Goodney, B. M. Hawkins, C. R.
Herman, J. A. Kalish, M. C. Koopmann, I. A. Laskowski, C. Mena-Hurtado, R. Mota-
ganahalli, V. L. Rowe, A. Schanzer, P. A. Schneider, J. J. Siracuse, M. Venermo, and
18

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
K. Rosenfield (2022, December). Surgery or Endovascular Therapy for Chronic Limb-
Threatening Ischemia. New England Journal of Medicine 387(25), 2305–2316.
Fine, J. P. and R. J. Gray (1999). A proportional hazards model for the subdistribution
of a competing risk. Journal of the American Statistical Association 94(446), 496–509.
Fleming, T. and D. Harrington (2011). Counting Processes and Survival Analysis. Wiley
Series in Probability and Statistics. New York: Wiley.
Friedenreich, C. M., H. K. Neilson, M. S. Farris, and K. S. Courneya (2016, Oct). Phys-
ical activity and cancer outcomes: A precision medicine approach.
Clinical Cancer
Research 22(19), 4766–4775.
Gehan, E. A. (1965). A generalized wilcoxon test for comparing arbitrarily singly censored
samples. Biometrics 21(3), 562–579.
Geurts, P., D. Ernst, and L. Wehenkel (2006).
Extremely randomized trees.
Machine
Learning 63, 3–42.
Gray, R. J. (1988). A class of k-sample tests for comparing the cumulative incidence of a
competing risk. The Annals of Statistics 16, 1141–1154.
Hager, R., A. A. Tsiatis, and M. Davidian (2018, December). Optimal Two-Stage Dy-
namic Treatment Regimes from a Classification Perspective with Censored Survival Data.
Biometrics 74(4), 1180–1192.
Hayes, C., R. R˘adulescu, E. Bargiacchi, et al. (2022). A practical guide to multi-objective
reinforcement learning and planning. Autonomous Agents and Multi-Agent Systems 36,
26.
He, Y., S. Kim, M.-O. Kim, W. Saber, and K. W. Ahn (2021, June). Optimal treatment
regimes for competing risk data using doubly robust outcome weighted learning with
bi-level variable selection. Computational Statistics & Data Analysis 158, 107167.
Ishwaran, H., U. B. Kogalur, E. H. Blackstone, and M. S. Lauer (2008, September). Random
survival forests. The Annals of Applied Statistics 2(3), 841–860.
Jetsupphasuk, M., M. G. Hudgens, H. Lu, S. R. Cole, J. K. Edwards, A. A. Adimora,
K. N. Althoff, M. J. Silverberg, P. F. Rebeiro, V. D. Lima, V. C. Marconi, T. R. Ster-
ling, M. A. Horberg, M. J. Gill, M. M. Kitahata, R. D. Moore, R. Lang, K. Gebo,
C. Rabkin, and J. J. Eron (2023, August). Optimizing treatment for human immunod-
eficiency virus to improve clinical outcomes using precision medicine. American Journal
of Epidemiology 192(8), 1341–1349.
Jiang, R., W. Lu, R. Song, and M. Davidian (2017, September). On Estimation of Optimal
Treatment Regimes for Maximizing t -Year Survival Probability. Journal of the Royal
Statistical Society Series B: Statistical Methodology 79(4), 1165–1185.
19

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
Jiang, X., A. E. Nelson, R. J. Cleveland, D. P. Beavers, T. A. Schwartz, L. Arbeeva,
C. Alvarez, L. F. Callahan, S. Messier, R. Loeser, and M. R. Kosorok (2021, May).
Precision Medicine Approach to Develop and Internally Validate Optimal Exercise and
Weight-Loss Treatments for Overweight and Obese Adults With Knee Osteoarthritis:
Data From a Single-Center Randomized Trial. Arthritis Care & Research 73(5), 693–
701.
Kalbfleisch, J. D. and R. L. Prentice (1980). Statistical Analysis of Failure Time Data.
New York: John Wiley & Sons.
Kidwell, K. M. (2016). DTRs and SMARTs: Definitions, designs, and applications. In
M. R. Kosorok and E. E. M. Moodie (Eds.), Adaptive Treatment Strategies in Practice:
Planning Trials and Analyzing Data for Personalized Medicine, pp. 7–24. Philadelphia,
PA and Alexandria, VA: ASA-SIAM Series on Statistics and Applied Probability.
Kosorok, M. R. (2008). Introduction to empirical processes and semiparametric inference.
New York: Springer.
Kosorok, M. R. and E. B. Laber (2019, Mar).
Precision medicine.
Annual Review of
Statistics and Its Application 6, 263–286.
Kosorok, M. R., E. B. Laber, D. S. Small, and D. Zeng (2021, January). Introduction to
the Theory and Methods Special Issue on Precision Medicine and Individualized Policy
Discovery. Journal of the American Statistical Association 116(533), 159–161.
Kosorok, M. R. and E. E. M. Moodie (2015). Adaptive Treatment Strategies in Practice:
Planning Trials and Analyzing Data for Personalized Medicine. ASA-SIAM Series on
Statistics and Applied Probability. Philadelphia, PA: SIAM.
Liu, Z., Z. Zhan, C. Lin, and B. Zhang (2023, December). Estimation in optimal treat-
ment regimes based on mean residual lifetimes with right-censored data. Biometrical
Journal 65(8), 2200340.
McGinigle, K. L., N. L. B. Freeman, W. A. Marston, A. Farber, M. S. Conte, M. R. Kosorok,
and C. A. Kalbaugh (2021, July). Precision Medicine Enables More TNM-Like Stag-
ing in Patients With Chronic Limb Threatening Ischemia. Frontiers in Cardiovascular
Medicine 8, 709904.
Meinshausen, N. (2006).
Quantile Regression Forests.
Journal of Machine Learning
Research 7, 983–999.
Mills, J. L., M. S. Conte, D. G. Armstrong, F. B. Pomposelli, A. Schanzer, A. N. Sidawy,
and G. Andros (2014, January).
The Society for Vascular Surgery Lower Extremity
Threatened Limb Classification System: Risk stratification based on Wound, Ischemia,
and foot Infection (WIfI). Journal of Vascular Surgery 59(1), 220–234.e2.
Moodie, E. E. M. and E. F. Krakow (2020). Precision medicine: Statistical methods for
estimating adaptive treatment strategies. Bone Marrow Transplant 55, 1890–1896.
20

````

## PDF page 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
Morzywo lek, P., J. Steen, S. Vansteelandt, J. Decruyenaere, S. Sterckx, and W. Van Biesen
(2022, November). Timing of dialysis in acute kidney injury using routinely collected
data and dynamic treatment regimes. Critical Care 26(1), 365.
Neuhauser, M. (2006). How to deal with multiple endpoints in clinical trials. Fundamental
& Clinical Pharmacology 20, 515–523.
Peto, J. and R. Peto (1972). Asymptotically efficient rank invariant test procedures. Journal
of the Royal Statistical Society: Series A (General) 135(2), 185–198.
Schrod, S., A. Sch¨afer, S. Solbrig, R. Lohmayer, W. Gronwald, P. J. Oefner, T. Beißbarth,
R. Spang, H. U. Zacharias, and M. Altenbuchinger (2022, June).
BITES: balanced
individual treatment effect for survival data. Bioinformatics 38(Supplement 1), i60–i67.
Tarone, R. E. and J. Ware (1977). On distribution-free tests for equality of survival distri-
butions. Biometrika 64(1), 156–160.
Teixeira-Pinto, A., J. Siddique, R. Gibbons, and S.-L. Normand (2009, July). Statistical ap-
proaches to modeling multiple outcomes in psychiatric studies. Psychiatric Annals 39(7),
729–735.
van Haelst, S., C. Koopman, H. den Ruijter, et al. (2018). Cardiovascular and all-cause
mortality in patients with intermittent claudication and critical limb ischaemia. British
Journal of Surgery 105(3), 252–261.
Wager, S. and G. Walther (2016, April). Adaptive Concentration of Regression Trees, with
Application to Random Forests. arXiv:1503.06388 [math, stat].
Wu, D., K. S. Goldfeld, E. Petkova, and H. G. Park (2024). Improving individualized treat-
ment decisions: A bayesian multivariate hierarchical model for developing a treatment
benefit index using mixed types of outcomes. medRxiv. Preprint.
Wu, P., D. Zeng, and Y. Wang (2020, January). Matched Learning for Optimizing Individ-
ualized Treatment Strategies Using Electronic Health Records. Journal of the American
Statistical Association 115(529), 380–392.
Yavuz, I., Y. Chng, and A. S. Wahed (2018, January). Estimating the Cumulative Incidence
Function of Dynamic Treatment Regimes. Journal of the Royal Statistical Society Series
A: Statistics in Society 181(1), 85–106.
Zhao, Y. Q., D. Zeng, E. B. Laber, R. Song, M. Yuan, and M. R. Kosorok (2015, March).
Doubly robust learning for estimating individualized treatment with censored data.
Biometrika 102(1), 151–168.
Zhong, Y., C. Wang, and L. Wang (2021, September). Survival Augmented Patient Pref-
erence Incorporated Reinforcement Learning to Evaluate Tailoring Variables for Person-
alized Healthcare. Stats 4(4), 776–792.
Zhou, J., J. Zhang, W. Lu, and X. Li (2021, April). On restricted optimal treatment regime
estimation for competing risks data. Biostatistics 22(2), 217–232.
21

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
Zhu, K., Y. Huang, and X.-H. Zhou (2018, January). Tree-based ensemble methods for
individualized treatment rules. Biostatistics & Epidemiology 2(1), 61–83.
Zitovsky, J. P., L. Wilson, and M. R. Kosorok (2023). A flexible framework for incorporating
patient preferences into q-learning.
22

````

## PDF page 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
Supplementary Material for “Optimal
individualized treatment regimes for survival
data with competing risks”
A
Notation Table
See Table S1 for notation summary.
B
Proposed Random Forests
B.1
Brief Review of Tree-based Methods
A random forest is an ensemble of trees, which are generated by recursively partitioning the
data into two daughter leaves, or nodes. Established tree-based approaches include Classi-
fication and Regression Trees (CART) (Breiman et al., 1984), CART extensions (Breiman
et al., 1984), and Extremely Randomized Trees (ERT) (Geurts et al., 2006). A random
survival forest is an extension of the random forest that accounts for censoring by allow-
ing censored outcomes as inputs and providing covariate-conditional survival probability
estimates as outputs (Ishwaran et al., 2008). This is a nonparametric survival regression
estimator that provides weighted Kaplan-Meier curves for each point in the feature space
with weights given by adaptive kernel estimates. Because of the presence of censoring, it
is not feasible to use a simple mean for splitting rules. Thus, the log-rank test is used
(Peto and Peto, 1972; Gehan, 1965; Tarone and Ware, 1977). At each terminal node of
a survival tree, the survival probability is estimated by the Kaplan-Meier estimator. A
random survival forest is obtained by averaging the survival trees.
Table S1: Summary of notation
Basic notation
τ
Study length
n
Number of training examples
ϵ
Event cause
i
Subject index. 1, 2, . . . , n
j
Cause index. 1, 2, . . . , J
k
Group or Node index. 1, 2, . . . , K
Predictors
A
Action
Z
Covariate information
H
History (a, Z)
d(Z)
Decision rule given Z
Overall outcomes
T
Failure time due to any cause. T = min(T1, T2, . . . , TJ)
C
Overall censoring time
X
Observed length. X = T ∧C
δ
Overall Censoring indicator. δ = 1(T ≤C)
Cause-specific outcomes
23

````

## PDF page 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
Tj
Failure time due to cause j
δj
Cause j Censoring indicator. δj = 1(T ≤C, T = Tj)
Theoretical settings
LS, LG
Lipschitz constants of Assumption 7
nmin
Minimum terminal node size in Assumptions 5
β
Rate of minimum terminal node size in Assumption 5
α
Regular split constant in Assumption 6
ζ
Covariate density bound in Assumptions 8
c1
At-risk probability bound at τ in Assumption 7
Survival and cumulative incidence functions
S
Overall failure survival function
Fj
Cause j cumulative incidence function. Fj(t) = Pr(T ≤t, ϵ = j)
G
Overall or generic censoring survival function
Values
ϕµ
1(S)
Mean truncated survival time. ϕµ(S) = E[S ∧τ]
ϕµ
2(Fj)
Mean truncated cumulative incidence time. ϕµ(Fj) = E[Fj ∧τ]
B.2
Proposed Forests
For our forest models, let ntree denote the number of trees. We assume that ntree ≥1. A
larger ntree is preferred in practice. Nevertheless, all theoretical results presented in this
paper remain valid for all ntree ≥1.
Random Survival Forest
We adapt the forest algorithm from Cho et al. (2023) to single stage treatment settings. We
provide a high-level algorithm of the forest in Algorithm S1. Briefly, we use the Kaplan-
Meier estimator to estimate the marginal survival probability of a node (or leaf) L, where
each individual’s failure time information is given by {(Xi, δi)}nL
i=1 where nL is the size of
node L, Xi is the observed failure time, and δi is the event indicator for any cause:
bS(t | L) =
Y
s≥0

1 +
P
i∈L dNi(s)
P
i∈L Yi(s)

,
(S1)
where Ni(t) = I(Xi ≤t, δi = 1) and Yi(t) = I(Xi ≥t). The Kaplan-Meier estimator is
used in both tree partitioning and terminal node survival probability estimation.
When the optimization criterion is the truncated mean survival time (ϕ = ϕµ), the
forest algorithm splits a node into two candidate daughter nodes, L1 and L2 by using the
mean difference test to maximize the difference in truncated mean survival times:
MD(L1, L2) =

Z
t>0
(t ∧τ)dbS(t | L1) −
Z
t>0
(t ∧τ)dbS(t | L2)
 .
(S2)
This splitting rule identifies the best split as (L1, L2) = arg maxL1,L2 MD(L1, L2).
The recursive partitioning process continues as long as the size of each node remains
above the threshold nmin. The survival probability estimate of the terminal node L of the
w-th (w = 1, 2, . . . , ntree) survival tree is given by the Kaplan-Meier estimator bSw(t | L).
Letting h = (a, Z), the random survival forest estimate is then given by
bS(t | h) =
1
ntree
ntree
X
w=1
#{L{w},l:l}
X
l=1
1(h ∈L{w},l)bS(t | L{w},l),
24

````

## PDF page 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
where #{L{w},l : l} is the number of terminal nodes of the w-th tree.
Algorithm S1 The random survival forest estimator
Input: {(Xi, δi, Zi, Ai)}n
i=1
Output: bS(·|Z, A = a)
Result: random survival forest estimate bS(·|Z, A)
Parameters: the number of trees ntree, the minimum terminal node size nmin
For treatment arm a ∈A do
For tree w = 1, 2, . . . , ntree do
Partition the feature space with the input data {(I(t ≤Xi), δji, Zi)}i:ai=a via
MD test (S2) until node size < 2nmin
Obtain the terminal node survival probability estimate bS{w}(t|a, Z) via
Kaplan-Meier estimator (S1)
Obtain the forest estimator bS(·|Z, A = a) =
1
ntree
Pntree
w=1 bS{w}(t|a, Z)
C
Proof of Theorem 1
Proof of Theorem 1. Note that
V(d0
opt(Z)) −V(bdopt(Z))
 =

X
a∈A
EZ
ϕ0
1(a, Z)
ϕ0
2(a, Z)

·

1{d0
opt(Z) = a} −1{bdopt(Z) = a}

≤
X
a∈A
EZ
ϕ0
1(a, Z)
ϕ0
2(a, Z)

·

1{d0
opt(Z) = a} −1{bdopt(Z) = a}

≤
X
a∈A
EZ

ϕ0
1(a, Z)
ϕ0
2(a, Z)

·

1{d0
opt(Z) = a} −1{bdopt(Z) = a}

≤
X
a∈A
EZ

ϕ0
1(a, Z)
ϕ0
2(a, Z)
 ·
1{d0
opt(Z) = a} −1{bdopt(Z) = a}


= EZ
"X
a∈A

1{d0
opt(Z)̸ = bdopt(Z)}

ϕ0
1(a, Z)
ϕ0
2(a, Z)

#
≤EZ

1{d0
opt(Z)̸ = bdopt(Z)}

sup
a,Z

ϕ0
1(a, Z)
ϕ0
2(a, Z)

= Pr(d0
opt(Z)̸ = bdopt(Z)|bdopt) sup
a,Z

ϕ0
1(a, Z)
ϕ0
2(a, Z)

≤ηPr(d0
opt(Z)̸ = bdopt(Z)|bdopt).
The third to last line holds because 1) only one term in the summation will have a non-zero
contribution and 2) the supremum represents the “worst case scenario” over all fixed combi-
nations of a and z and thus does not depend on the random variables. The last line holds be-
cause we assumed supa,Z

ϕ0
1(a, Z)
ϕ0
2(a, Z)
 is bounded by η via Assumption 11. Thus, the norm
25

````

## PDF page 26

FORMULA CHECK REQUIRED: original PDF page 26.

````text
of this distance, V(d0
opt)−V(bdopt), goes to 0 in probability if Pr(d0
opt(Z)̸ = bdopt(Z)| ˆdopt)
p−→0.
We complete the proof by first showing
X
a∈A
I{ϕ0
1(a, Z) −(1 −αϕ)V 0∗
1 (Z) ≥0} −I{bϕ1(a, Z) −(1 −αϕ)bV ∗
1 (Z) ≥0}
 →0.
(S3)
The proof of (S3) will be presented shortly. Now, (S3) implies
arg max
a∈A:bϕ1(a,Z)≥(1−αϕ)bV ∗
1 (Z)
bϕ2(a, Z)
p−→
arg max
a∈A:ϕ0
1(a,Z)≥(1−αϕ)V 0∗
1 (Z)
bϕ2(a, Z).
(S4)
Theorem 3 in our paper states that RCIFs are consistent. Thus, by the Continuous Mapping
Theorem, bϕ2(a, Z)
p−→ϕ0
2(a, Z). Then,
sup
a∈A
E
bϕ2(a, Z) −ϕ0
2(a, Z)

p−→0,
(S5)
which implies that the right hand side of (S4) converges to
arg maxa∈A:ϕ0
1(a,Z)≥(1−αϕ)V 0∗
1 (Z) ϕ0
2(a, Z). Thus, since Z is random,
Pr(d0
opt(Z)̸ = bdopt(Z)|bdopt)
p−→0.
This completes the proof of Theorem 1.
Proof of (S3). Let A0 = ϕ0
1(a, Z) −(1 −αϕ)V 0∗
1 (Z) and bAn = bϕ1(a, Z) −(1 −αϕ)bV ∗
1 (Z).
These are functions of random variable Z. Then, we can re-write (S3) as
X
a∈A
I{A0 ≥0} −I{ bAn ≥0}
 →0.
I{ bAn ≥0} −I{A0 ≥0}
 = I{ bAn < 0 ≤A0} + I{A0 < 0 ≤bAn}
= I{ bAn −A0 < −A0 ≤0} + I{0 < −A0 ≤bAn −A0}
= I{0 ≤A0 < −( bAn −A0)} + I{−( bAn −A0) ≤A0 < 0}.
(S6)
In (S6), the first equality holds because these are the only possible indicators such that
their sum is equal to 1. We get the 2nd equality by subtracting A0 on both sides within
the indicator functions. The third equality is due to multiplying by −1 and flipping the
inequalities within the indicators.
Since we know bϕ1(a, Z)
p−→ϕ0
1(a, Z) and bV ∗
1 (Z)
p−→V 0∗
1 (Z) as shown in Cho et al. (2023);
and bAn and A0 are linear combinations of bϕ1(a, Z) and bV ∗
1 (Z), and ϕ0
1(a, Z) and V 0∗
1 (Z),
respectively, then bAn
p−→A0 because the linear combination of consistent estimators is
consistent. This means
bAn −A0
p−→0.
(S7)
By definition of convergence in probability, (S7) implies ∃ϵn : Pr(| bAn −A0| > ϵn) →
0 as ϵn →0 for a fixed sequence ϵn. Then, using Assumption 10 and (S7), we can bound
(S6). Starting with the first term of (S6),
I{0 ≤A0 < −( bAn −A0), | bAn −A0| ≤ϵn} + I{0 ≤A0 < −( bAn −A0), | bAn −A0| > ϵn} ≤
I{0 ≤A0 < ϵn} + I{| bAn −A0| > ϵn},
26

````

## PDF page 27

FORMULA CHECK REQUIRED: original PDF page 27.

````text
where I{0 ≤A0 < ϵn} →0 by Assumption 10 (bounded density assumption) and I{| bAn −
A0| > ϵn} →0 by (S7) (and definition of consistency). Specifically, assuming Assumption
10, Pr(0 ≤A0 ≤ϵn) =
R ϵn
0 fA0(a0)da0 ≈fa0(0)ϵn ≤bϵn →0 as ϵn →0 for some bound b.
The second term can be shown to be bounded similarly.
I{−( bAn −A0) ≤A0 < 0} =
I{−( bAn −A0) ≤A0 < 0, | bAn −A0| ≤ϵn} + I{−( bAn −A0) ≤A0 < 0, | bAn −A0| > ϵn} ≤
I(−ϵn ≤A0 < 0) + I(| bAn −A0| > ϵn).
The first term for the inequality is because −( bAn −A0) < 0, bAn −A0 must be positive;
thus, −ϵn ≤bAn −A0 ≤ϵn. The second term is because the indicator is a subset.
Because of Equation (S7), Pr(| bAn −A0| > ϵn) →0, and Pr(−ϵn ≤A0 < 0) →0 due
to Assumption 10. Specifically, I(−ϵn ≤A0 < 0) =⇒Pr(−ϵn ≤A0 < 0) ≈ϵnfa0(0) <
ϵnb →0 as ϵn →0. This completes the proof of (S3).
D
Proof of Theorem 2
Proof of Theorem 2. It is sufficient to establish the consistency results for a single tree in
order to prove Theorem 2. By nature of the forest, which is the average of multiple trees
where the randomization process of the trees is independent of the data generative law, the
supremum error of averages is less than the average of supremum errors for the uniform
consistency, i.e., for ˆS =
1
ntree
Pntree
w=1 ˆS(w),
sup
t,h
 ˆS(tj|h) −S(tj|h)
 ≤
1
ntree
ntree
X
w=1
sup
t,h
 ˆS(w)(tj|h) −S(tj|h)
 .
Hence, we will prove prove Theorem 1 for just a single tree bS{w}, which is built based on
{Hi, δi}n
i=1. For ease of notation, we drop the tree index w throughout the proof.
Using a modified version of Lemma 2.10 from Kosorok (2008), let Ψ : Θ →L and
Ψn : Θ →L be maps between two normed spaces, where Θ is a parameter space, L is
some normed space, ∥·∥L denotes the uniform norm, Ψ is a fixed map, and Ψn is a data-
dependent map. This lemma is modified to allow Θn to be data-dependent. Let Θn be the
data-dependent survival function space, where survival functions are piecewise constant
over a hyper-rectangle, represented by a rectangular kernel kh in the feature space so that
S(t | kh) = S(t | h) for all h ∈H.
Lemma 1 (Consistency of Z-estimators). Let Ψ(S0) = 0 for some S0 ∈Θ, and assume
∥Ψ(Sn)∥L →0 implies ∥Sn −S0∥∞→0 for any sequence {Sn}n∈N ⊂Θn →Θ as n →∞.
Then, if
Ψn( ˆSn)

L →0 in probability for some sequence of estimators { ˆSn}n∈N ⊂Θn and
supS∈Θn ∥Ψn(S) −Ψ(S)∥L →0 in probability,
 ˆSn −S0

∞→0 in probability, as n →∞.
Proof of Lemma 1. Suppose a sequence ˆSn ∈Θn satisfies that
Ψn( ˆSn)

L →0 and
27

````

## PDF page 28

FORMULA CHECK REQUIRED: original PDF page 28.

````text
supS∈Θn ∥Ψn(S) −Ψ(S)∥L →0 both in probability as n →∞. Then we have
Ψ( ˆSn)

L ≤
Ψ( ˆSn) −Ψn( ˆSn)

L +
Ψn( ˆSn)

L
≤sup
S∈Θn
∥Ψ(S) −Ψn(S)∥L +
Ψn( ˆSn)

L →0,
in probability as n →∞. Thus, by the assumption,
 ˆSn −S0

∞→0.
Let Θ be the space of all covariate-conditional survival functions. Define a normed
space L = D[−1,1]{[0, τ] × Rd}, where DAB is the space of all right-continuous left-limits
functions with range A and support B. We use S0 to denote the true survival function.
We define the following estimating function and equations:
ψS,t = I(X > t) + (1 −δ)I(X ≤t) S(t | H)
S(X | H) −S(t | H),
(S8)
Ψ(S) = P{ψS,tδh}
P{δh}
≡P·|hψS,t,
(S9)
Ψn(S) = Pn{ψS,tkh}
Pn{kh}
≡Pn,·|khψS,t,
(S10)
where P is the population average of function values, i.e., Pf =
R
f(h)dP(h), Pn is the sam-
ple average of function values, i.e., Pnf = 1
n
Pn
i=1 f(Hi), S0 ∈Θ is the true survival proba-
bility of failure from any cause, δh(h′) = 1(h′ = h) is the unnormalized Dirac measure, and
kh is the unnormalized tree kernel. Define kh(h′) = 1(h′ ∈L(h)), where L(h) is the terminal
node of the tree that contains the point h. The term ‘unnormalized’ refers to not being mul-
tiplied by the sample (or population) size. Let bSn be the kernel-conditional Kaplan-Meier
estimator, the Kaplan-Meier applied to the data with weights indicated by the tree kernel,
kh. Then, by Lemma 1 and Propositions 1 to 4 stated below, limn→∞
bSn −S0

∞→p 0.
Since bS is an average of the trees, we have shown limn→∞
bS −S0

∞→p 0.
Proposition 1. Ψ(S0) = 0 for S0 ∈Θ
Proposition 2. Assume Assumptions 4-8. As n →∞,
Ψ(bSn)

L →0 implies
bSn −S0

∞→
0.
Proposition 3. Assume Assumptions 4-8. As n →∞,
Ψn(bSn)

L →0 in probability.
Proposition 4. Assume Assumptions 4-8. As n →∞, supS∈Θn ∥Ψn(S) −Ψ(S)∥L →0 in
probability.
28

````

## PDF page 29

FORMULA CHECK REQUIRED: original PDF page 29.

````text
Proof of Proposition 1. The numerator of Ψ(S0) is
E(δhψS0,t) = E

δh

I(X > t) + (1 −δ)I(X ≤t) S0(t | H)
S0(X | H) −S0(t | H)

= EδhEδhψS0,t|δh

δhI(X > t) + δh(1 −δ)I(X ≤t) S0(t | H)
S0(X | H) −δhS0(t | H)
δh

= Eδh

δhI(X > t)

+ Eδh

δh(1 −δ)I(X ≤t)EδhψS0,t|δh
 S0(t | H)
S0(X | H)
δh

−Eδh

δhEδhψS0,t|δh

S0(t | H)
δh

= Pr(δh = 1)

EδhψS0,t|δh=1

I(X > t)

(1.1)
+ EδhψS0,t|δh=1

(1 −δ)I(X ≤t) S0(t | H)
S0(X | H)

(1.2)
−EδhψS0,t|δh=1

S0(t | H)

= Pr(δh = 1)

S0(t|H = h)[1 −G(t|H = h)]
+ S0(t|H = h)G(t|H = h) −S0(t|H = h)

= Pr(δh = 1)

S0(t|H = h) −S0(t|H = h)G(t|H = h)
+ S0(t|H = h)G(t|H = h) −S0(t|H = h)

= 0,
where G(c) ≡FC(c) is the cumulative distribution function (CDF) for censoring time, and
(1.1) and (1.2) are derived below.
For (1.1), E(I(X > t0)) = Pr(X > t0) = Pr(T > t0, C > t0) = Pr(T > t0) Pr(C >
29

````

## PDF page 30

FORMULA CHECK REQUIRED: original PDF page 30.

````text
t0) = S0(t0)(1 −G(t0)). For (1.2):
EδhψS0,t|δh=1

(1 −δ)I(X ≤t0)I(S0(X) > 0) S0(t0)
S0(X)

=
Z t0
0
Z ∞
c
S0(t0)
S0(c) fT,C(t, c) dt dc
= S0(t0)
Z t0
0
1
S0(c)fC(c)FT(t)

∞
c
dc
= S0(t0)
Z t0
0
1
S0(c)fC(c)

FT(∞) −FT(c)

dc
= S0(t0)
Z t0
0
fC(c) dc
= S0(t0)FC(c)

t0
0
= S0(t0)[FC(t0) −FC(0)] ≡S0(t0)G(t0).
Proof of Proposition 2. By hypothesis,
Ψ(bSn)

L = supt∈(0,τ]
h∈H
P·|hψbSn,t
 →0. We want to
show that P·|hψbSn,t →0 uniformly over h ∈H and t ∈[0, τ] implies supt,h un(t | h) →0 for
un defined below. We know
P·|hψbSn,t = P·|h

I(X > t) + (1 −δi)(X ≤t)
bSn(t)
bSn(X)
−bSn(t)

.
(S11)
We individually examine each term in (S11). For the first term, because T ⊥C, we have
P·|h (I(X > t)) = E (I(X > t) | H = h) = Pr(X > t | H = h) = Pr(T > t, C > t | H = h)
= Pr(T > t | H = h) Pr(C > t | H = h) = S0(t | H = h) (1 −G(t | H = h)) .
(S11.1)
For the second term,
P·|h
(
(1 −δ)I(X ≤t)
bSn(t)
bSn(X)
)
= E
 
(1 −δ)I(X ≤t)
bSn(t)
bSn(X)
H = h
!
30

````

## PDF page 31

FORMULA CHECK REQUIRED: original PDF page 31.

````text
= E
 
I(C ≤t)
bSn(t)
bSn(C)
H = h, δ = 0
!
=
Z t
0
Z ∞
c
bSn(t | H = h)
bSn(C | H = h)
fT,C(u, c | H = h) du dc
=
Z t
0
1
bSn(c | H = h)
Z ∞
c
bSn(t | H = h)fT(u | H = h) du fC(c | H = h) dc
=
Z t
0
fC(c | H = h)S0(c | H = h)
bSn(c | H = h)
dc bSn(t | H = h),
(S11.2)
where the last equality holds because
Z ∞
c
bSn(t | H = h) fT(u | H = h) du = bSn(t | H = h) FT(u)

∞
c
= bSn(t | H = h) (1 −FT(c))
= bSn(t | H = h) (1 −S0(c)).
The last term is
P·|h{−bSn(t)} = −bSn(t | H = h).
(S11.3)
31

````

## PDF page 32

FORMULA CHECK REQUIRED: original PDF page 32.

````text
Combining (S11.1), (S11.2), (S11.3), we have
P·|hψbSn,t = S0(t | H = h) (1 −G(t | H = h))
+
Z t
0
fC(c | H = h)S0(c | H = h)
bSn(c | H = h)
dc bSn(t | H = h) −bSn(t | H = h)
= S0(t | H = h) −bSn(t | H = h) −S0(t | H = h)G(t | H = h)
+ bSn(t | H = h)
Z t
0
fC(c | H = h)S0(c | H = h)
bSn(c | H = h)
dc
=
bSn(t | H = h)
bSn(t | H = h)
S0(t | H = h) −bSn(t | H = h)
−
bSn(t | H = h)
bSn(t | H = h)
S0(t | H = h)G(t | H = h)
+ bSn(t | H = h)G(t | H = h) −bSn(t | H = h)G(t | H = h)
+ bSn(t | H = h)
Z t
0
S0(c | H = h)
bSn(c | H = h)
dG(c | H = h)
= bSn(t | H = h)
S0(t | H = h)
bSn(t | H = h)
−1 −
"
S0(t | H = h)
bSn(t | H = h)
−1
#
G(t | H = h)
−G(t | H = h) +
Z t
0
S0(c | H = h)
bSn(c | H = h)
dG(c | H = h)

.
Now, letting ϵn(t | H = h) = S0(t|H=h)
bSn(t|H=h) −1, and noting that
Z t
0
S0(c | H = h)
bSn(c | H = h)
dG(c | H = h) −G(t | H = h)
=
Z t
0
S0(c | H = h)
bSn(c | H = h)
dG(c | H = h) −
Z t
0
1 dG(c | H = h)
=
Z t
0
"
S0(c | H = h)
bSn(c | H = h)
−1
#
dG(c | H = h) =
Z t
0
ϵn(c | H = h) dG(c | H = h),
32

````

## PDF page 33

FORMULA CHECK REQUIRED: original PDF page 33.

````text
we have P·|hψbSn,t
= bSn(t | H = h)

ϵn(t | H = h)(1 −G(t | H = h))
+
Z t
0
S0(c | H = h)
bSn(c | H = h)
dG(c | H = h) −G(t | H = h)

= bSn(t | H = h)

ϵn(t | H = h)(1 −G(t | H = h)) +
Z t
0
ϵn(c | H = h) dG(c | H = h)

.
Setting un ≡ϵn(t | H = h)(1 −G(t | H = h)) +
R t
0 ϵn(c | H = h) dG(c | H = h), and taking
the derivative on both sides, we get
dun(t | H = h) = d

ϵn(t | H = h)(1 −G(t | H = h)) +
Z t
0
ϵn(c | H = h) dG(c | H = h)

= dϵn(t)(1 −G(t | H = h)) +

d(1 −G(t | H = h))

ϵn(t | H = h)
+ ϵn(t | H = h)dG(t | H = h)
= dϵn(t)(1 −G(t | H = h)) −dG(t | H = h) ϵn(t | H = h)
+ ϵn(t | H = h)dG(t | H = h)
= dϵn(t)(1 −G(t | H = h))
=⇒dϵn(t | H = h) =
dun(t)
1 −G(t | H = h).
Using integration by parts, we have
ϵn(t | H = h) =
Z t
0
dun(t)
1 −G(t | H = h)
=
un(u | H = h)
1 −G(u | H = h)

t
0
−
Z t
0
un(u | H = h) dG(u | H = h)
(1 −G(u | H = h))2
=
un(t | H = h)
1 −G(t | H = h) −
Z t
0
un(u | H = h) dG(u | H = h)
(1 −G(u | H = h))2
.
By Assumption 4 , 1 −G(t | H = h) ≥1 −G(τ | H = h) > 0. Thus, un(t | H = h) →0
implies ϵn(t | H = h) →0. Since un(t | H = h) →0 by hypothesis, we have S0(t|H=h)
bSn(t|H=h) −1 →
0. Thus,
bSn −S0

∞→0.
Proof of Proposition 3. We utilize proof by induction on t ∈(0, τ]. Pn
i=1 ψbSn,t=0(Xi) =
Pn
i=1

I(X > 0) + (1 −δi)I(X ≤0) S(0|H)
S(X|H) −S(0 | H)

= Pn
i=1

I(X > 0) −S(0 |
33

````

## PDF page 34

FORMULA CHECK REQUIRED: original PDF page 34.

````text
H)

= Pn
i=1

1 −1

= 0.
Then for all 0 < t ≤τ, if Pn
i=1 ψbSn,t−(Xi) = 0 implies
Pn
i=1 ψS,t(Xi) = 0, the desired result holds.
We re-write ψbSn,t in terms of counting notation, using jumps such that I(Xi ≤t) =
I(Xi ≤t−) + dI(Xi ≤t) and I(Xi > t) = I(Xi > t−) + dI(Xi > t).
n
X
i=1
ψbSn,t =
n
X
i=1
I(Xi > t) +
n
X
i=1

(1 −δi)I(Xi ≤t)
bSn(t | H)
bSn(Xi | H)
−bSn(t | H)

=
n
X
i=1
I(Xi > t) +
n
X
i=1
(1 −δi)I(Xi ≤t)
bSn(Xi | H)
−1

bSn(t | H)
=
n
X
i=1
I(Xi > t−) +
n
X
i=1
dI(Xi > t)
+
n
X
i=1
(1 −δi)I(Xi ≤t−)
bSn(Xi | H)
−1

bSn(t | H)
+
n
X
i=1
(1 −δi)dI(Xi ≤t)
bSn(Xi | H)

bSn(t | H)
=
n
X
i=1

I(Xi > t−) + dI(Xi > t)

+
n
X
i=1
(1 −δi)I(Xi ≤t−)
bSn(Xi | H)
−1

bSn(t−| H)
+
n
X
i=1
(1 −δi)I(Xi ≤t−)
bSn(Xi | H)
−1

bSn(t−| H)
Pn
j=1 δjdI(Xj > t)
Pn
j=1 I(Xj > t−)
+
n
X
i=1
(1 −δi)I(Xi ≤t)
bSn(Xi | H)

bSn(t | H),
34

````

## PDF page 35

FORMULA CHECK REQUIRED: original PDF page 35.

````text
where the second equality is because
n
X
i=1
(1 −δi)I(Xi ≤t−)
bSn(Xi | H)
−1

bSn(t | H)
=
n
X
i=1
(1 −δi)[I(Xi ≤t−) + dI(Xi ≤t)]
bSn(Xi | H)
−1

bSn(t | H)
=
n
X
i=1
(1 −δi)I(Xi ≤t−)
bSn(Xi | H)
+ (1 −δi)dI(Xi ≤t)
bSn(Xi | H)
−1

bSn(t | H)
=
n
X
i=1
(1 −δi)I(Xi ≤t−)
bSn(Xi | H)
−1

bSn(t | H) +
(1 −δi)dI(Xi ≤t)
bSn(Xi | H)

bSn(t | H),
and the third equality is because bSn(t | H) = bSn(t−| H) + bSn(t−| H)
Pn
i=1 δidI(Xi>t)
Pn
i=1 I(Xi>t−) from
the definition of modified Kaplan-Meier estimator in Cho et al. (2023).
Since we know by hypothesis that Pn
i=1 ψbSn,t−= Pn
i=1[I(Xi > t−) + (1 −δi)I(Xi ≤
t−)
bSn(t−|H)
bSn(Xi|H) −bSn(t | H)] = 0, we re-write ψbSn,t into smaller components.
n
X
i=1
ψbSn,t =
n
X
i=1
dI(Xi > t)
+
n
X
i=1
I(Xi > t−) +
n
X
i=1
(1 −δi)I(Xi ≤t−)
bSn(Xi | H)
−1

bSn(t−| H)
(3.1)
+
n
X
i=1
(1 −δi)I(Xi ≤t−)
bSn(Xi | H)
−1

bSn(t−| H)
Pn
j=1 δjdI(Xj > t)
Pn
j=1 I(Xj > t−)
(3.2)
+
n
X
i=1
(1 −δi)I(Xi ≤t)
bSn(Xi | H)

bSn(t | H)
(3.3)
=
n
X
i=1
dI(Xi > t) −
n
X
i=1
δidI(Xi > t) +
n
X
i=1
(1 −δi)I(Xi = t)
= −
n
X
i=1
I(Xi = t) +
n
X
i=1
δiI(Xi = t) +
n
X
i=1
(1 −δi)I(Xi = t)
= 0,
where (3.1) = Pn
i=1 ψbSn,t−= 0 by hypothesis, and the derivations from (3.2) and (3.3) to
the next line are given below.
We use the hypothesis for (3.2). Since Pn
i=1 ψbSn,t−= 0, then Pn
i=1

(1−δi)I(Xi≤t−)
bSn(Xi|H)
−
35

````

## PDF page 36

FORMULA CHECK REQUIRED: original PDF page 36.

````text
1

bSn(t−| H) = −Pn
i=1 I(Xi > t−), so Pn
i=1

(1−δi)I(Xi≤t−)
bSn(Xi|H)
−1

bSn(t−| H)
Pn
j=1 δjdI(Xj>t)
Pn
j=1 I(Xj>t−) =
−Pn
i=1 I(Xi > t−)
Pn
j=1 δjdI(Xj>t)
Pn
j=1 I(Xj>t−) = −Pn
i=1 δidI(Xi > t).
For (3.3), this term is not equal to 0 when δi = 0 and dI(Xi ≤t) = 1. We note
that dI(Xi ≤t) = I(Xi = t) = 1 when t = Xi, and 0 otherwise. In other words, when
dI(Xi ≤t) = 1, bSn(Xi) = bSn(t).
Because I(Xi ≤t) is increasing and the jump at
t = Xi is positive (from 0 to 1), the derivative is positive. Then, when (3.3) is not 0,
Pn
i=1

(1−δi)I(Xi≤t)
bSn(Xi|H)

bSn(t | H) = Pn
i=1

(1−δi)I(Xi=t)
bSn(t|H)

bSn(t | H) = Pn
i=1(1 −δi)I(Xi = t). We
note that, using the same logic, dI(Xi > t) = −I(Xi = t), since the function I(Xi > t) is
decreasing and the jump at t = Xi goes from 1 to 0.
Proposition 5 is needed to prove Proposition 4 below. This proposition shows that tree
kernels (and, consequently, the forest kernels) are Donsker, and that the Ψ(S) function is
also Donsker. The proof can be found in Cho et al. (2023). We use entropy calculation,
the Donsker theorem, empirical process theory, and Assumptions 4-8 to establish uniform
consistency in Proposition 4.
Proposition 5. (Bounded entropy integral of the tree and forest kernels). The collections
of the unnormalized tree and forest kernel functions are Donsker, where the tree kernels
ktree(·) are axis-aligned random hyper-rectangles, and the forest kernels kforest(·) are the
mean of arbitrarily many (ntree) tree kernels.
Proof of Proposition 4. We first show that the class of functions {ψS,t : S ∈Θn, t ∈[0, τ]}
is Donsker. Since the components of ψS,t are uniformly bounded Donsker classes, by Lemma
9.10 of Kosorok (2008), the class of functions is Donsker.
With Proposition 5 and the class of products of bounded Donsker classes being Donsker,
all of {ψS,tδh : S ∈Θn, t ∈[0, τ], h ∈H} and {ψS,tkh : S ∈Θn, t ∈[0, τ], h ∈H} are
Donsker. By Assumption 5, suph Pnkh ▷◁nβ−1. Then,
sup
S∈Θn
∥Ψn(S) −Ψ(S)∥L = sup
S∈Θn
∥PnψS,tkh −PψS,tδh∥L
= sup
S∈Θn
Pn,·|khψS,tψS,t −P·|khψS,t + P·|khψS,t −P·|hψS,t

L
≤sup
S∈Θn
t∈(0,τ]
h∈H

Pn{ψS,tkh}
Pn{kh}
−P{ψS,tkh}
P{kh}

(S12)
+ sup
S∈Θn
t∈(0,τ]
h∈H

P{ψS,tkh}
P{kh}
−P{ψS,tδh}
P{δh}

(S13)
= oP(1).
To see this, we show each component (S12) and (S13) are oP(1).
36

````

## PDF page 37

FORMULA CHECK REQUIRED: original PDF page 37.

````text
We can break (S12) down further.
(S12) = sup
S∈Θn
t∈(0,τ]
h∈H

Pn{ψS,tkh} −P{ψS,tkh}
Pn{kh}

(S12.1)
+ sup
S∈Θn
t∈(0,τ]
h∈H
P{ψS,tkh}

1
Pnkh
−
1
Pkh
 .
(S12.2)
Because (S12.1) ≤Op(n−1/2)
nβ−1
and (S12.2) = P{ψS,tkh}
Pkh
(Pn−P)kh
Pnkh
≤OP (n−1/2)
nβ−1
, we obtain S12 =
oP(1).
We now show (S13) = oP(1). We denote S(t | kh) as shorthand for S(t | H ∈L(h)) and
37

````

## PDF page 38

FORMULA CHECK REQUIRED: original PDF page 38.

````text
note that S(t | kh) = S(t | h) for all S ∈Θn. Then for all S ∈Θn, t ∈[0, τ] and h ∈H,
P·|khψS,t −P·|hψS,t

=
S0(t | kh)(1 −G(t | kh)) −S(t | kh) + S(t | kh)
Z t
0
S0(u | kh)
S(u | kh) dG(u | kh)
−S0(t | h)(1 −G(t | h)) + S(t | h) −S(t | h)
Z t
0
S0(u | h)
S(u | h) dG(u | h)

=
S0(t | kh)(1 −G(t | kh)) −S0(t | h)(1 −G(t | h))
+ S(t | h)
Z t
0
S0(u | kh)
S(u | h) dG(u | kh) −S0(u | h)
S(u | h) dG(u | h)

≤|S0(t | kh)(1 −G(t | kh)) −S0(t | h)(1 −G(t | h))|
+
S(t | h)
Z t
0
S0(u | kh)
S(u | h) dG(u | kh) −S0(u | h)
S(u | h) dG(u | h)
+ S0(u | kh)
S(u | h) dG(u | h) −S0(u | kh)
S(u | h) dG(u | h)

≤|S0(t | kh)(1 −G(t | kh)) −S0(t | h)(1 −G(t | h))|
+
S(t | h)
Z t
0
S0(u | kh)
S(u | h)

dG(u | kh) −dG(u | h)

+
S0(u | kh) −S0(u | h)
S(u | h)

dG(u | h)

≤
S0(t | kh)(1 −G(t | kh)) −S0(t | h)(1 −G(t | h))

(S13.1)
+
S(t | h)
Z t
0
S0(u | kh)
S(u | h)

dG(u | kh) −dG(u | h)

(S13.2)
+
S(t | h)
Z t
0
S0(u | kh) −S0(u | h)
S(u | h)

dG(u | h)
.
(S13.3)
(S13.1), (S13.2), and (S13.3) can be further bounded by using Assumption 7.
38

````

## PDF page 39

FORMULA CHECK REQUIRED: original PDF page 39.

````text
(S13.1) =
S0(t | kh)(1 −G(t | kh)) −S0(t | h)(1 −G(t | h))

=
S0(t | kh)(1 −G(t | kh)) −S0(t | h)(1 −G(t | h))
+ S0(t | kh)(1 −G(t | h)) −S0(t | kh)(1 −G(t | h))

=
S0(t | kh){(1 −G(t | kh)) −(1 −G(t | h))} + (1 −G(t | h)){S0(t | kh) −S0(t | h)}

= S0(t | kh)
(G(t | h) −G(t | kh))
 + (1 −G(t | h))
S0(t | kh) −S0(t | h)

≤LG
sup
h′∈H:kh(h′)>0
∥h −h′∥∞+ LS
sup
h′∈H:kh(h′)>0
∥h −h′∥∞,
where the last inequality holds because S0(t | kh) ≤1 and 1 −G(t | h) ≤1.
To bound (S13.2) further, we use dG(u) ≡dFC(u) = fC(u)du.
(S13.2) =
 S(t | h)
Z t
0
S0(u | kh)
S(u | h)

dG(u | kh) −dG(u | h)

≤
Z t
0
S0(u | kh) S(t | h)
S(u | h)
 dG(u | kh) −dG(u | h)

≤
Z t
0
 dG(u | kh) −dG(u | h)
 =
Z t
0
 fC(u | kh) −fC(u | h)
 du
≤
Z t
0
2LG
sup
h′∈H:kh(h′)>0
∥h −h′∥∞du
≤2t LG
sup
h′∈H:kh(h′)>0
∥h −h′∥∞,
where the second inequality holds by bringing in the absolute value inside the integral, the
third inequality holds because S0(u | kh) ≤1 and u ≤t =⇒S(u) ≤S(t) =⇒
S(t|h)
S(u|h) ≤1,
and the fourth inequality holds by derivative of Lipschitz function.
We now further bound (S13.3).
(S13.3) =

Z t
0
S(t | h)
S(u | h)

S0(u | kh) −S0(u | h)

dG(u | h)

≤sup
t sup
h
S0(t | kh) −S0(t | h)

Z t
0
dG(u | h)
≤LS
sup
h′∈H:kh(h′)>0
∥h −h′∥∞,
39

````

## PDF page 40

FORMULA CHECK REQUIRED: original PDF page 40.

````text
where the first inequality is obtained because S(t|h)
S(u|h) ≤1 and the double supremum comes
from maximizing S0 −S to obtain a constant that can be take outside of the integral, and
the second inequality is due to
R t
0 dG(u | h) = G(t | h) −G(0 | h) = G(t | h) ≤1. The last
line drops supt because ∥h −h′∥∞is no longer a function of t.
As a result, we have
(S13) = sup
S∈Θn
t∈(0,τ]
h∈H
P·|khψS,t −P·|hψS,t
 ≤{(2τ + 1)LG + 2LS}
sup
h′∈H:kh(h′)>0
∥h −h′∥∞.
Following similar arguments as in Meinshausen (2006) and Cho et al. (2023), with Assump-
tions 5, 6, 8, it can be shown that suph′∈H:kh(h′)>0 ∥h −h′∥∞= oP(1).
E
Proof of Theorem 3
Proof of Theorem 3. Our estimator is
bFn(t | h) =
Z t
0
bSh
n(u−)Pnkh(H)dN h
j (u)
Pnkh(H)Y (u) .
For simplicity, we drop the h superscript for any survival function when it does not
cause confusion (i.e., bSh
n ≡bSn), but keep in mind that the survival functions in this proof
use both arguments t and h, since the RCIF is built based on {Hi, δi, δji}n
i=1. We do the
same for Nj(t) such that N h
j (t) ≡Nj(t) where N h
j (t) are the events due to cause-j at time
t with history h.
=⇒bFn(t | h) ≡
Z t
0
bSn(u−)Pnkh(H)dNj(u)
Pnkh(H)Y (u)
=
Z t
0
bSn(u−)Pnkh(H)dNj(u)
Pnkh(H)Y (u) −
Z t
0
S0(u−)Pnkh(H)dNj(u)
Pnkh(H)Y (u)
+
Z t
0
S0(u−)Pnkh(H)dNj(u)
Pnkh(H)Y (u)
=
Z t
0

bSn(u−) −S0(u−)
Pnkh(H)dNj(u)
Pnkh(H)Y (u) +
Z t
0
S0(u−)Pnkh(H)dNj(u)
Pnkh(H)Y (u) .
(S14)
Let dbΛh
n(t) =
Pnkh(H)dNj(t)
Pnkh(H)Y (t)
and deΛh
n(t) =
Pkh(H)dNj(t)
Pkh(H)Y (t) .
First, we obtain a bound for

R t
0

bSn(u−) −S0(u−)

dbΛh
n(t)
 for t ∈(0, τ] and h ∈H:

Z t
0

bSn(u−) −
Z t
0
S0(u−)

dbΛh
n(u)
 ≤

sup
t∈(0,τ]
h∈H
bSn(t) −S0(t)

 Z t
0
dbΛh
n(u),
40

````

## PDF page 41

FORMULA CHECK REQUIRED: original PDF page 41.

````text
where supt∈(0,τ]
bSn(t) −S0(t)
 (with t−incorporated into supt∈(0,τ]) has the rate for Kaplan-
Meier for the single-stage generalized random survival forest, and
R t
0 dbΛh
n(s) ≤bΛh
n(τ) is
uniformly bounded over h. Then, the first term of (S14) converges to 0.
We next examine the second term of (S14). We can re-write it by dividing both the
numerator and denominator by Pnkh(H) to get
R t
0 S0(u−)Pnkh(H)dNj(u)/Pnkh(H)
Pnkh(H)Y (u)/Pnkh(H) . We will use
Lemma 12.3 from Kosorok (2008). Since {δjI(X ≤t), t ≥0} and {I(X ≥t), t ≥0} are
indicators and dNj is at most 1, they are bounded Donsker. Since Nj and Y are bounded
Donsker, kh is bounded Donsker, and the product of bounded Donsker is Donsker, then
√n ∆n(h, t) ≡√n


Pnkh(H)Nj(t) −Pkh(H)Nj(t)
Pnkh(H)Y (t) −Pkh(H)Y (t)
Pnkh(H) −Pkh(H)

⇝


G1(h, t)
G2(h, t)
G3(h, t)

,
(S15)
where G1, G2, and G3 are tight Gaussian processes.
Thus, √n ∆n(h, t) = O(h,t)
p
(1),
where O(h,t)
p
(1) is a quantity Rn(h, t) such that supt∈(0,τ]
h∈H
|Rn(h, t)| = Op(1), which implies
∆n(h, t) = O(h,t)
p
(n−1/2).
Since S0(t−) is bounded away from 0, we have from (S15),
√n


Pnkh(H)Nj(t) −Pkh(H)Nj(t)
1
S0(t−)Pnkh(H)Y (t) −
1
S0(t−)Pkh(H)Y (t)
Pnkh(H) −Pkh(H)

⇝


G1(h, t)
1
S0(t−)G2(h, t)
G3(h, t)

.
(S16)
First, we examine Nj. From (S15), we have
Pnkh(H)Nj(t)
Pnkh(H)
= Pkh(H)Nj(t) + O(h,t)
p
(n−1/2)
Pkh(H) + O(h,t)
p
(n−1/2)
.
(S17)
Assumption 5 implies that infh∈H Pkh(H) ≥k0nβ−1 for all h ∈H where k0 > 0 is
some constant. Note that n1−β × n−1/2 = n
1
2 −β. Multiplying n1−β to the numerator and
denominator of the right-hand side of (S17), we obtain
Pnkh(H)Nj(t)
Pnkh(H)
=n1−βPkh(H)Nj(t) + O(h,t)
p
(n
1
2 −β)
n1−βPkh(H) + O(h,t)
p
(n
1
2 −β)
.
(S18)
The denominator of the right-hand side of (S18) is greater than or equal to k0 + o(h,t)
p
(1)
because n1−βPkh(H) ≥n1−βk0nβ−1 = k0 and the residual error is going to zero since by
Assumption 5, β > 1
2. Therefore, we have
Pnkh(H)Nj(t)
Pnkh(H)
= n1−βPkh(H)Nj(t) + o(h,t)
p
(1)
n1−βPkh(H) + o(h,t)
p
(1)
.
(S19)
We note that
n1−βPkh(H) + o(h,t)
p
(1)
n1−βPkh(H)
= 1 +
o(h,t)
p
(1)
n1−βPkh(H) = 1 + o(h,t)
p
(1),
(S20)
41

````

## PDF page 42

FORMULA CHECK REQUIRED: original PDF page 42.

````text
where the last equality in (S20) holds because n1−βPkh(H) ≥k0 > 0.
Since (1 +
o(h,t)
p
(1))−1 = 1 + o(h,t)
p
(1), we can take the inverse of (S20).
=⇒
n1−βPkh(H)
n1−βPkh(H) + o(h,t)
p
(1)
= 1 + o(h,t)
p
(1)
=⇒
1
n1−βPkh(H) + o(h,t)
p
(1)
= 1 + o(h,t)
p
(1)
n1−βPkh(H).
(S21)
To continue from (S19), multiply both sides of (S21) by n1−βPkh(H)Nj(t) + o(h,t)
p
(1).
=⇒n1−βPkh(H)Nj(t) + o(h,t)
p
(1)
n1−βPkh(H) + o(h,t)
p
(1)
= n1−βPkh(H)Nj(t) + o(h,t)
p
(1)
n1−βPkh(H)

1 + o(h,t)
p
(1)

.
We re-write the numerator as n1−βPkh(H)Nj(t) = n
1
2 −βn
1
2Pkh(H)Nj(t). Since
√nPkh(H)Nj(t) = O(h,t)
p
(1) and n
1
2 −β →0, n1−βPkh(H)Nj(t) is bounded. The denomina-
tor is bounded away from 0 because n1−βPkh(H) ≥k0 > 0. This implies,
Pnkh(H)Nj(t)
Pnkh(H)
= n1−βPkh(H)Nj(t)
n1−βPkh(H)

1 + o(h,t)
p
(1)

+ o(h,t)
p
(1)
= Pkh(H)Nj(t)
Pkh(H)

1 + o(h,t)
p
(1)

+ o(h,t)
p
(1)
= Pkh(H)Nj(t)
Pkh(H)
+ o(h,t)
p
(1)
(because Pkh(H)Nj(t)
Pkh(H)
is bounded).
Hence,
Pnkh(H)Nj(t)
Pnkh(H)
= Pkh(H)Nj(t)
Pkh(H)
+ o(h,t)
p
(1).
Using similar arguments, we can show that the kernel version of Y ,
1
S0(t−)Pnkh(H)Y (t)
is consistent as well. Specifically, since S0(t) is bounded away from 0, similar to (S18), we
have
1
S0(t−)Pnkh(H)Y (t)
Pnkh(H)
=
n1−β
1
S0(t−)Pkh(H)Y (t) + O(h,t)
p
(n
1
2 −β)
n1−βPkh(H) + O(h,t)
p
(n
1
2 −β)
=
n1−β
1
S0(t−)Pkh(H)Y (t) + o(h,t)
p
(1)
n1−βPkh(H) + o(h,t)
p
(1)
.
Multiplying n1−β
1
S0(t−)Pkh(H)Y (t)+o(h,t)
p
(1) on the both sides of (S21) and simplifying the
expressions, we have
=⇒
n1−β
1
S0(t−)Pkh(H)Y (t) + o(h,t)
p
(1)
n1−βPkh(H) + o(h,t)
p
(1)
=
1
S0(t−)Pkh(H)Y (t)
Pkh(H)
+ o(h,t)
p
(1).
By Assumption 5, Pkh(H)Y (t) ≥MPkh(H).
Then
1
S0(t−)Pkh(H)Y (t)
Pkh(H)
≥
1
S0(t−)MPkh(H)
Pkh(H)
=
M
S0(t−). Since S0(t−) is bounded away from 0, we have
1
S0(t−)Pnkh(H)Y (t)
Pnkh(H)
is bounded away
from 0.
42

````

## PDF page 43

FORMULA CHECK REQUIRED: original PDF page 43.

````text
Let Ah(u) =
1
S0(u−)
Pnkh(H)Y (u)
Pnkh(H)
and Bh(u) = Pnkh(H)Nj(u)
Pnkh(H)
. Let Bh
0(t) = Pkh(H)Nj(t)
Pkh(H)
and
Ah
0(t) =
1
S0(t−)
Pkh(H)Y (t)
Pkh(H) .
Then our point of interest is (B, A) = (Bh
0(t), Ah
0(t)).
The
components of the second term of our estimator bFn(t | h) in (S14) can be mapped twice:
(B, A) 7→(B, 1
A) 7→
Z
[0,t]
1
Ah(u) dBh(u).
Using Lemma 12.3 and Lemma 6.19 from Kosorok (2008), this composition map is
Hadamard differentiable on a domain of type {(B, A) : suph∈H
R
[0,τ]|dBh(t)| ≤M,
inft∈[0,τ]
h∈H
|Ah(t)| ≥ϵ} for all h ∈H and for a given M < ∞and ϵ > 0, at every point (B, A)
such that
1
Ah(t) has bounded variation. Thus, the map is continuous. Using Assumption 9,
the total variation of the kernels is bounded. Since we have shown that Ah(t) and Bh(t)
are consistent, and Ah(t) is bounded below by 0 and the map
1
Ah(t) is smooth, we apply the
continuous mapping theorem so that the continuous map is also consistent.
Thus,
sup
t∈(0,τ]
h∈H
 bFn(t | h) −Fj(t | h)
 →0
in probability as n →∞.
F
Additional Simulation Details
The priority and competing event failure time hazard coefficients for both simulation set-
tings are provided in Table S2.
43

````

## PDF page 44

FORMULA CHECK REQUIRED: original PDF page 44.

````text
Table S2: Cause-specific failure time hazard coefficients and covariate dimensions in Expo-
nential and Fine-Gray simulation scenarios
Model
Scenario 1
Scenario 2
(low dimension)
(high dimension)
Exponential
p
3
6
β0
1
(0, −1.5, −1.9, −0.3)T
(0, −0.5, −1.2, 1.5, 0.1, 0.6)T
β1
1
(0, −0.6, −1.9, 1.5)T
(0, 0.3, −0.4, −0.2, 0.9, 1.6)T
β0
2
(0, 1, −0.1, 0.4)T
(0, −0.6, 1.4, 1.5, 2, 1)T
β1
2
(0, 1.2, 0.2, −1)T
(0, 1.5, −2.1, −0.8, 0.1, 1)T
Fine-Gray
p
3
6
β0
1
(0, 0.1, 0.3)T
(0, 0.9, −0.7, 0.6, −0.1, 0.5)T
β1
1
(0, −1.8, −1.5)T
(0, −1.2, 0.1, −0.5, −0.2, −1.2)T
β0
2
(0, −1.1, −0.3)T
(0, −0.5, −0.4, −1.1, −0.8, −0.4)T
β1
2
(0, −0.2, 1.2)T
(0, 0.4, −0.3, 0.6, 0.2, 1.1)T
Simple Exponential Simulation Setting
Since T follows an exponential distribution, S(t) = exp{−(λA
1 + λA
2 )t} by definition of
survival function. We derive Pr(T ≤t0, ϵ = 1|Zi) below using the property of independence
as well as 1 = Pr(ϵ = 1) + Pr(ϵ = 2) =
λA
1
λA
1 +λA
2 +
λA
2
λA
1 +λA
2 , and the derivation for Pr(T ≤
t0, ϵ = 2|Zi) is defined similarly.
44

````

## PDF page 45

FORMULA CHECK REQUIRED: original PDF page 45.

````text
Pr(T ≤t0, ϵ = 1|Zi) = Pr(T1 ≤t0, T2 ≤t0, T1 < T2)
= Pr(T1 < T2 ≤t0)
=
Z t0
0
Z t2
0
f(t1, t2)dt1dt2
=
Z t0
0
Z t2
0
f(t1)f(t2)dt1dt2
=
Z t0
0
Z t2
0
λA
1 exp(−λA
1 t1)λA
2 exp(−λA
2 t2)dt1dt2
=
Z t0
0
λA
2 exp(−λA
2 t2)
Z t2
0
λA
1 exp(−λA
1 t1)dt1dt2
=
Z t0
0
λA
2 exp(−λA
2 t2)[1 −exp(−λA
1 t2)]dt2
= λA
2
Z t0
0
e−λA
2 t2dt2 −
Z t0
0
e−(λA
1 +λA
2 )t2dt2

= −λA
2

−1
λA
2
(1 −e−λA
2 t0)

−λA
2

1
λA
1 + λA
2
(1 −e−(λA
1 +λA
2 )t0)

=

1 −e−λA
2 t0
−
λA
2
λA
1 + λA
2

1 −e−(λA
1 +λA
2 )t0
= 1 −e−λA
2 t0 −
λA
2
λA
1 + λA
2
+
λA
2
λA
1 + λA
2

e−(λA
1 +λA
2 )t0
= 1 −
λA
2
λA
1 + λA
2
−e−λA
2 t0 +
λA
2
λA
1 + λA
2

e−(λA
1 +λA
2 )t0
=
λA
1
λA
1 + λA
2
−e−λA
2 t0 +
λA
2
λA
1 + λA
2

e−(λA
1 +λA
2 )t0
.
Fine-Gray Simulation Setting
When covariates are 0, Pr(Ti ≤t, ϵ = 1|Zi) = p{1 −exp(−t)}, where 1 −exp(−t) is the
cumulative distribution function (CDF) of exp(1). Because of how we define the mixture
above, Pr(Ti < ∞, ϵ = 1) = p. Thus, Pr(Ti = ∞, ϵ = 1) = 1 −p. Then, Pr(ϵ = 1|Zi) =
Pr(T < ∞, ϵ = 1|Zi) = limt→∞1 −[1 −p(1 −exp(−t))]exp(ZT
i β1(A)) = 1 −[1 −p]exp(ZT
i βA
1 ).
To simulate cause 1 failure time, we use the property that the distribution of a CDF of a
random variable is uniform. We generate an uniform random variate u1 from Uniform(0,1)
distribution and set this equal to the CDF of failure time given cause 1 and covariates. By
definition of conditional probability, Pr(Ti ≤t|ϵ = 1, Zi) = Pr(Ti≤t,ϵ=1|Zi)
Pr(ϵ=1|Zi)
, so
Pr(Ti ≤t|ϵ = 1, Zi) = 1 −[1 −p{1 −exp(−t)}]exp(ZT
i βA
1 )
1 −(1 −p)exp(ZT
i βA
1 )
set
= u1.
45

````

## PDF page 46

FORMULA CHECK REQUIRED: original PDF page 46.

````text
We derive failure time from cause 1, t1, by solving for t.
1 −[1 −p(1 −exp(−t))]exp(ZT
i βA
1 )
1 −(1 −p)exp(ZT
i βA
1 )
= u1
1 −[1 −p(1 −exp(−t))]exp(ZT
i βA
1 ) = u1 ×

1 −(1 −p)exp(ZT
i βA
1 )
[1 −p(1 −exp(−t))]exp(ZT
i βA
1 ) = 1 −

u1 ×

1 −(1 −p)exp(ZT
i βA
1 )
exp(ZT
i βA
1 ) × log (1 −p(1 −exp(−t))) = log

1 −u1 ×

1 −(1 −p)exp(ZT
i βA
1 )
log (1 −p(1 −exp(−t))) =
log

1 −u1 ×

1 −(1 −p)exp(ZT
i βA
1 )
exp(ZT
i βA
1 )
1 −p(1 −exp(−t)) = exp


log

1 −u1 ×

1 −(1 −p)exp(ZT
i βA
1 )
exp(ZT
i βA
1 )

.
This implies
exp(−t) = 1 −p−1 ×

1 −exp


log

1 −u1 ×

1 −(1 −p)exp(ZT
i βA
1 )
exp(ZT
i βA
1 )




t = −log

1 −p−1 ×

1 −exp


log

1 −u1 ×

1 −(1 −p)exp(ZT
i βA
1 )
exp(ZT
i βA
1 )






=⇒t1 = t.
The CIF for failures from cause 2 was obtained by taking Pr(ϵ = 2|Zi) = 1 −Pr(ϵ =
1|Zi) = 1−(1−[1−p]exp(ZT
i βA
1 )) = (1−p)exp(ZT
i βA
1 ). We use the exponential distribution with
rate exp(ZT
i βA
2 ) for Pr(Ti ≤t|ϵ = 2, Zi). In other words, t2 ∼exp(exp(ZT
i βA
2 )). Without
loss of generality, we could also derive t2 similarly to t1 (see Supplementary Material).
Censoring time Ci follows a Uniform(0, τ = 4) distribution, independent of failure time.
Using the assumptions or derivations established earlier, the overall survival function
when the priority cause is cause 1 can be written as:
S(t) = Pr(T > t) = 1 −Pr(T ≤t) = 1 −

Pr(T ≤t, ϵ = 1) + Pr(T ≤t, ϵ = 2)
	
= 1 −

Pr(T ≤t, ϵ = 1) + Pr(T ≤t|ϵ = 2) × Pr(ϵ = 2)
	
= 1 −

1 −[1 −p{1 −exp(−t)}]exp(ZT
i βA
1 )
+ (1 −exp(−exp(ZT
i βA
2 ) ∗t)) × (1 −p)exp(ZT
i βA
1 )	
= [1 −p{1 −exp(−t)}]exp(ZT
i βA
1 ) −(1 −exp(−t × exp(ZT
i βA
2 ))) × (1 −p)exp(ZT
i βA
1 ).
We derive t2 from the Fine-Gray simulation setting in a similar manner as t1. Since
Pr(ϵ = 2|Zi) = 1−Pr(ϵ = 1|Zi), Pr(ϵ = 2|Zi) = 1−(1−[1−p]exp(ZT
i βA
1 )) = [1−p]exp(ZT
i βA
1 ).
Then, we have
Pr(Ti ≤t, ϵ = 2|Zi) = Pr(Ti ≤t|ϵ = 2, Zi) × Pr(ϵ = 2|Zi)
= (1 −exp(−exp(ZT
i β2(A))t)) × (1 −p)exp(ZT
i βA
1 ).
46

````

## PDF page 47

FORMULA CHECK REQUIRED: original PDF page 47.

````text
Setting this to a random variate u2 ∼Uniform(0, 1), solve for t2 to obtain failure time
for cause 2.
Set u2 = (1 −exp(−exp(ZT
i βA
2 )t2)) × (1 −p)exp(ZT
i βA
1 )
u2
(1 −p)exp(ZT
i βA
1 ) = 1 −exp(−exp(ZT
i βA
2 )t2)
1 −
u2
(1 −p)exp(ZT
i βA
1 ) = exp(−exp(ZT
i βA
2 )t2)
log

1 −
u2
(1 −p)exp(ZT
i βA
1 )

= −exp(ZT
i βA
2 )t2
t2 = −
log

1 −
u2
(1−p)exp(ZT
i βA
1 )

exp(ZT
i βA
2 )
.
G
Peripheral Artery Disease Cohort Details
We estimated the criterion ϕ for each policy d as:
ˆϕOS(d) =
P
i:test set(Ti ∧τ)W OS
i
(d)
P
i:test set W OS
i
(d)
and ˆϕPC(d) =
P
i:test set(T1i ∧τ)W PC
i
(d)
P
i:test set W PC
i
(d)
,
(S22)
where W OS
i
(d) =
I(d(zi)=Ai)δ0i
ˆ
Pr(Ai|zi) ˆ
Pr(Ci>Ti|zi) and W PC
i
(d) =
I(d(zi)=Ai)δ1i
ˆ
Pr(Ai|zi) ˆ
Pr(Ci∧T2i>T1i|zi).
Recall that
δ1i = I(T1i ≤Ci ∧T2i). Following Cho et al. (2023), we used the test set to estimate
the propensity scores and censoring probabilities via random forests and random survival
forests, respectively, adjusting for the same covariates as in the ITR estimation. However,
in the propensity score model, treatment is the outcome rather than a predictor.
We
performed 10-fold cross-validation (CV) to avoid overfitting (Kcv = 10). We split each CV
fold into training (80%) and testing (20%) datasets. We set αϕ = 0.1, and set the number
of trees to 300, minimum node size to 5, and minimum number of events to be 2.
47

````

