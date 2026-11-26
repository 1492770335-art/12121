# Safe Policy Learning through Extrapolation: Application to Pre-trial Risk Assessment

Original PDF: [original.pdf](original.pdf). SHA256: `ea9a0b62cdd7fbac2770bafa74bc6622fc5ce5db175117873a417c035119b5cc`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
Safe Policy Learning through Extrapolation:
Application to Pre-trial Risk Assessment∗
Eli Ben-Michael†
D. James Greiner‡
Kosuke Imai§
Zhichao Jiang¶
April 2, 2025
Abstract
Algorithmic recommendations and decisions have become ubiquitous in today’s
society. Many of these data-driven policies, especially in the realm of public policy, are
based on known, deterministic rules to ensure their transparency and interpretability.
We examine a particular case of algorithmic pre-trial risk assessments in the US criminal
justice system, which provide deterministic classification scores and recommendations
to help judges make release decisions.
Our goal is to analyze data from a unique
field experiment on an algorithmic pre-trial risk assessment to investigate whether the
scores and recommendations can be improved. Unfortunately, prior methods for policy
learning are not applicable because they require existing policies to be stochastic. We
develop a maximin robust optimization approach that partially identifies the expected
utility of a policy, and then finds a policy that maximizes the worst-case expected
utility. The resulting policy has a statistical safety property, limiting the probability
of producing a worse policy than the existing one, under structural assumptions about
the outcomes. Our analysis of data from the field experiment shows that we can safely
improve certain components of the risk assessment instrument by classifying arrestees
as lower risk under a wide range of utility specifications, though the analysis is not
informative about several components of the instrument.
∗We acknowledge the partial support from Cisco Systems, Inc. (CG# 2370386), National Science Founda-
tion (SES–2051196), Sloan Foundation (Economics Program; 2020–13946), National Natural Science Foun-
dation of China (Grant No. 12371285, 12292984), and Arnold Ventures. We thank Benedikt Koch and
anonymous reviewers of the IQSS’s Alexander and Diviya Magaro Peer Pre-Review Program for useful
feedback.
†Assistant Professor, Department of Statistics & Data Science and Heinz College of Information Systems
& Public Policy, Carnegie Mellon University. 4800 Forbes Avenue, Hamburg Hall, Pittsburgh PA 15213.
Email: ebenmichael@cmu.edu URL: ebenmichael.github.io
‡Honorable S. William Green Professor of Public Law, Harvard Law School, 1525 Massachusetts Avenue,
Griswold 504, Cambridge, MA 02138.
§Professor, Department of Government and Department of Statistics, Harvard University. 1737 Cam-
bridge Street, Institute for Quantitative Social Science, Cambridge MA 02138. Email: imai@harvard.edu
URL: https://imai.fas.harvard.edu
¶Professor, School of Mathematics, Sun Yat-sen University, Guangzhou Guangdong 510275, China. Email:
jiangzhch7@mail.sysu.edu.cn
arXiv:2109.11679v4  [stat.ML]  31 Mar 2025

````

## PDF page 2

Technical extraction; compare with original PDF page 2.

````text
1
Introduction
Algorithmic recommendations and decisions are ubiquitous in our daily lives. Many algo-
rithmic policies are used for consequential decisions in high stakes settings such as criminal
justice, social policy, and medical care. One common feature of such policies is that they are
based on known, deterministic rules. This is often because transparency and interpretability
are required to ensure accountability especially when used for public policy-making.
In this paper, we focus on a particular case: pre-trial risk assessment instruments (PRAI)
in the American criminal justice system. The goal of a PRAI is to aid judges in deciding
which arrestees should be released pending the disposition of any criminal charges.
We
consider a particular PRAI used in Dane County, Wisconsin, which includes the state capital,
Madison (Section 2). This PRAI assigns scores to arrestees according to the risk that they
are predicted to engage in undesirable behavior. It then aggregates these scores using a
deterministic function and provides an overall release recommendation to the judge.
We analyze data from a unique field experiment on the PRAI (Greiner et al., 2020; Imai
et al., 2023). Our goal is to learn new algorithmic scoring and recommendation rules that can
lead to better overall outcomes while retaining the transparency of the existing instrument.
Importantly, we focus on changing the algorithmic policies, which we can intervene on, rather
than judge’s decisions, which we cannot.
The large amounts of data collected after implementing deterministic policies such as
PRAIs provide an opportunity to learn new policies that improve on the status quo. Unfor-
tunately, prior approaches to policy learning are not applicable because they require existing
policies to be stochastic, typically relying on inverse probability weighting (Section 3).
To address this challenge (Section 4), we partially identify the expected utility of a policy
by calculating all potential values consistent with the observed data. This makes choosing
an “optimal” policy ambiguous: a policy can perform well under some outcome models
that are consistent with the data and poorly in others. We use the maximin criterion that
2

````

## PDF page 3

Technical extraction; compare with original PDF page 3.

````text
finds a policy that maximizes the worst-case performance relative to the status quo. The
resulting policy has a statistical safety property that limits the probability of yielding a
worse outcome than the status quo policy, under the structural assumptions made about
the outcomes. However, this safety property comes at the cost of potentially choosing a
sub-optimal policy, though it is no worse than the status quo. We formally characterize the
gap between this safe policy and the infeasible oracle policy.
We use this approach to explore whether the data from our field experiment support
alterations to the existing PRAI (Section 5). We explore the three risk measures based on
the predicted likelihood that an arrestee, upon release, will (i) fail to appear in court (FTA),
(ii) engage in new criminal activity (NCA), or (iii) engage in new violent criminal activity
(NVCA). We also inspect the algorithm that recommends to the judge the level of cash bail
and pre-trial supervision and monitoring conditions to impose.
We find that under several specifications of the utility function, it can be possible to
improve safely upon the existing NVCA scoring rule by classifying arrestees as lower risk;
if the policy maker is primarily focused on avoiding NVCAs, the resulting safe policy falls
back on the existing scoring rule. However, our approach has limitations. Conducting our
analysis requires several non-trivial choices that may be challenging in practice. In addition,
our analysis does not provide meaningful insights about components of the instrument other
than the NVCA scoring rule. This arises from identifiability issues caused by the structure
of the underlying rules, as well as a high degree of statistical uncertainty due to small sample
sizes for rare combinations of risk factors. We discuss these and other limitations in Section 6.
2
Pre-trial Risk Assessment
We now briefly describe the particular PRAI, called the Public Safety Assessment (PSA),
used in Dane County, Wisconsin. The PSA is an algorithmic recommendation designed to
help judges make their pre-trial release decisions. We will also describe an original ran-
domized experiment we conducted to evaluate the impact of the PSA on judges’ decisions.
3

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
In Section 5, we analyze this experimental dataset and consider how to improve outcomes
by modifying certain aspects of the PSA system. Interested readers should consult Greiner
et al. (2020) and Imai et al. (2023) for further details of the PSA and experiment; the study
dataset has been made publicly available.
2.1
The PSA-DMF system
The goal of the PSA is to help judges decide, at first appearance hearings, whether to allow
an arrestee’s release without bail or release them only if the arrestee posts bail/bond (or
meets other conditions). Because arrestees are presumed to be innocent, judges must avoid
unnecessary incarceration. The PSA has several outputs. First, it returns three classification
scores based on the predicted risk that each arrestee will engage in an FTA, NCA, or NVCA.
Law requires judges to balance between these risks and the cost of incarceration. These three
PSA scores are then combined via the so-called “Decision Making Framework” (DMF) into
two overall recommendations: (i) whether to require a signature bond (i.e., release on their
own recognizance) or some level of cash bail for release, and (ii) what, if any, monitoring
conditions to place on release. Given the complexity of the system, our empirical analysis
will focus on the question of how to improve each component separately (see Section 5).
FTA, NCA, and NVCA risk scores.
These scores are deterministic functions of eight
risk factors. The only demographic factor is the arrestee’s age, and neither gender nor race
is used. The other risk factors include the current offense and pending charges as well as
measures of criminal history based on prior convictions and prior FTAs. These scores are
constructed by assigning an integer-valued weight to each present risk factor, adding them
together, and thresholding this value into a number of bins. For the sake of transparency, the
foundation that funded the PSA’s creation made these weights and thresholds publicly (see
https://advancingpretrial.org/psa/factors; Appendix Table G.1 summarizes the weights.
The FTA score has six levels and is based on four risk factors. The values range from
0 to 7, and the final score is thresholded into values between 1 (lowest risk) and 6 (highest
4

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
2
4
6
2
4
6
NCA Score
FTA Score
Signature Bond
Modest Cash Bail
Moderate Cash Bail
Cash Bail
Figure 1: Decision Making Framework (DMF) matrix for cases where the current charge
is not a serious violent offense, the NVCA flag is not triggered, and the defendant was not
extradited. If the FTA score and the NCA score are both less than 5, then the recommenda-
tion is to only require a signature bond. Otherwise the recommendation is to require some
amount of cash bail. The dashed line indicates this boundary. Unshaded areas indicate
impossible combinations of FTA and NCA scores.
risk) by assigning {0 →1, 1 →2, 2 →3, (3, 4) →4, (5, 6) →5, 7 →6}. The NCA score
also has six levels, but is based on six risk factors and has a maximum value of 13 before
being collapsed into six levels by assigning {0 →1, (1, 2) →2, (3, 4) →3, (5, 6) →4, (7, 8) →
5), (9, 10, 11, 12, 13) →6}. Finally, the NVCA score is a binary flag based on five risk factors:
if the sum of the weights is greater than or equal to 4, the PSA flags the arrestee as being at
elevated risk of an NVCA. Otherwise, the NVCA score is 0, and the arrestee is not flagged
as being at elevated risk.
Recommendations via the DMF.
Next, the DMF transforms these three PSA risk
scores into a recommendation regarding cash bail and one regarding additional monitoring
conditions. For cases where the current charge is one of several serious violent offenses, the
defendant was extradited, or the NVCA score is 1, the DMF automatically recommends
cash bail with maximum supervision and monitoring conditions. For the remaining cases,
the FTA and NCA risk scores are combined into one of 7 overall risk levels. If the FTA and
NCA scores are both less than 5, and so the risk level is 3 or lower, then the recommendation
5

````

## PDF page 6

Technical extraction; compare with original PDF page 6.

````text
is to only require a signature bond. Otherwise the recommendation is to require cash bail
(limited to “modest” at levels 4–5 and “moderate” at level 6). Figure 1 visualizes the cash
bail portion of the DMF. The risk levels similarly encode a recommendation for an increasing
amount of pre-trial supervision and monitoring conditions, ranging from none (level 1) to
maximum supervision with biweekly phone and face-to-face contacts (level 7). Appendix
Figure G.10 shows these conditions along with the cash bail recommendations.
2.2
The experimental data
We analyze the data from a randomized controlled trial conducted in Dane County, Wis-
consin. In this experiment, the PSA was computed for each first appearance hearing that
a single judge oversaw during the study period. Across cases, we randomized whether the
PSA was made available in its entirety to the judge. If a case is assigned to the treatment
group, the judge received the three PSA scores, the DMF recommendations, and all of the
risk factors that were used to construct them on a single sheet of paper. For the control
group, the judge did not receive the PSA scores and DMF recommendations. Since the risk
factors that go into the PSA were made available in other case files, the judge could, in
principle, reconstruct the PSA output with enough time.
For each case, we observe the three scores (FTA, NCA, and NVCA) and the DMF
recommendation, the underlying risk factors used to construct the scores, the binary decision
by the judge (signature bond or cash bail), and three binary outcomes (FTA, NCA, and
NVCA). We focus on first arrest cases in order to avoid spillover effects between cases. All
told, there are 1,891 cases, 948 of which the judge was given access to the PSA.
Our goal is to improve the PSA recommendation system while taking into account the
judicial decisions that partly result from the algorithmic recommendations; see Appendix D
for further discussion on incorporating judicial decisions into the analysis. Crucially, each
component of the PSA is deterministic and no aspect of it was randomized as part of the
study. Therefore, there is a lack of overlap: the probability that any case would have had a
6

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
different algorithmic recommendation than it actually received is exactly zero. This makes
existing approaches to policy learning inapplicable because they rely on the inverse of this
probability. Instead, learning a new recommendation policy in the absence of overlap requires
extrapolation. Below, we will develop a methodological framework that provides a statistical
property that the new, learned rules perform at least as well as the original recommendation.
3
Policy Learning with Observational Data
3.1
Notation and setup
Suppose that we have a representative sample of n units independently drawn from a pop-
ulation P. For each unit i = 1, . . . , n, we observe a set of covariates Xi ∈X ⊆Rp (e.g., the
risk factors from Appendix Table G.1) and a binary outcome Yi ∈{0, 1}. In our analysis
presented in Section 5, we alternately consider the outcome Yi = 1 as the absence of an FTA,
NCA, or NVCA. We consider a set of K possible actions, denoted by A = {0, 1, 2, . . . , K −1}
that can be taken for each unit.
The actions correspond to the PSA recommendation: there are K = 6 possible actions
when we consider the FTA and NCA risk scores, K = 2 for the NVCA flag, K = 7 for
the overall DMF bail and monitoring recommendation, and K = 2 for the signature bond
versus cash bail recommendation. In our experimental evaluation, we have access to the
algorithm that generated the observed actions. Formally, we encode this as a known baseline
deterministic policy ˜π : X →A that generates the observed actions Ai = ˜π(Xi). Throughout
this paper, we will also refer to the baseline policy as ˜π(x, a) ≡1{˜π(x) = a}, the indicator
of whether the baseline policy yields action a given the covariates x.
We consider the effects of the algorithmic recommendation on the outcome, and assume
that the algorithmic action Ai may affect its own unit’s outcome Yi but has no impact on
the outcomes of other units (no interference between units; Rubin (1980)). Then, we can
write the potential outcome under each action Ai = a as Yi(a) where a ∈A and the observed
7

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
outcome as Yi = Yi(Ai) = Yi(˜π(Xi)) (Neyman, 1923). This setup focuses on the impacts of
the algorithmic recommendation whose provision was randomized in our experimental eval-
uation. We marginalize over the potential human judicial decisions that may be influenced
by the algorithmic recommendation (see Appendix D for further formalization). Finally,
our setting implies that ({Yi(a)}a∈A, Xi) are independent and identically distributed, so we
sometimes drop the i subscript.
3.2
Optimal policy learning
Our primary goal is to find a new deterministic policy π : X →A, that has a high expected
utility. We will again use the notation π(x, a) ≡1{π(x) = a} for the policy being equal to
action a given the covariates x. Let u(y, a) denote the utility for outcome y under action a.
Because the outcomes are binary, we can write this utility function as:1
Y (a)u(1, a) + {1 −Y (a)}u(0, a) = {u(1, a) −u(0, a)}Y (a) + u(0, a).
The two key components of this utility function are (i) the utility change between the two
outcomes for action a, u(a) ≡u(1, a)−u(0, a), which we assume is non-negative without loss
of generality, and (ii) the utility for an outcome of zero with an action a, c(a) ≡u(0, a). We
will refer to the latter term as the “cost” because it denotes the utility under action a when
the outcome event does not happen; c(a) = 0 corresponds to the action having no cost. We
define the utility using both the outcome y and the action a to capture the fact that some
actions are costly. For example, in Section 5, we will place a cost on triggering the NVCA
flag, recommending cash bail, or assigning a high NCA, FTA, or overall risk score. We note,
however, that our approach is agnostic to the particular choice of the utility function.
While this utility only takes into account the policy action and the outcome, policy
makers may also be concerned about the costs of subsequent human decisions that are
1While we focus here on binary potential outcomes, this form of the utility function shows that we can
extend our results to the case with continuous outcomes with utility functions that are linear in the (possibly
transformed) outcomes.
8

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
possibly affected by algorithmic recommendations or actions. In Appendix D, we show how
to incorporate such factors into the utility function.
The value of policy π is the expected utility under policy π across the population,
V (π, m∗) = E
"X
a∈A
π(X, a){u(a)Y (a) + c(a)}
#
= E
"X
a∈A
π(X, a){u(a)m∗(a, X) + c(a)}
#
,
(1)
where we have used the law of iterated expectations, with the first expection over X and
Y (a), and the second expectation over X, to show the dependence on the conditional ex-
pected potential outcome function m∗(a, x) ≡E[Y (a) | X = x].
We explicitly denote
the value under different potential models for our development below; in cases where it is
not ambiguous, we omit the m∗argument to indicate the value under the true conditional
expected potential outcome function.
Ideally, we would like to find a policy π that has the highest value within a policy
class Π. We can write a population optimal policy as one that maximizes the value, i.e.,
π∗∈argmaxπ∈ΠV (π). The policy class Π is an important object both in the theoretical
analysis and in applications. In Section 5, we discuss the substantive choice of policy class
when applied to a PRAI.
To find an optimal policy, we need to point-identify the value V (π, m∗) for all candidate
policies π ∈Π.
Existing methods rely on an overlap assumption for identification.
In
our context, this would require that each case has a non-zero probability of being assigned
algorithmic action A = a, i.e. that P(A = a | X) > 0 for all a ∈A. If the baseline policy
were stochastic, satisfying the overlap assumption, we could directly use inverse probability
weighting, model-based weighting, or a doubly robust approach to learn an optimal policy
from data (e.g. Qian and Murphy, 2011; Zhao et al., 2012; Kitagawa and Tetenov, 2018;
Dudik et al., 2011; Athey and Wager, 2021). In our application and many other settings,
however, the baseline policy ˜π is a deterministic function of covariates, implying a lack of
overlap. Thus, we cannot point-identify the value V (π, m∗) for all policies π ∈Π and hence
9

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
cannot using existing approaches. In Appendix E, we provide further discussion about this
identification issue.
4
Safe Policy Learning through Extrapolation
To deal with the lack of overlap brought on by the deterministic policy, we propose to first
partially identify the conditional expectation, and then use robust optimization to find the
best policy under the worst-case model. We will develop our optimal safe policy approach in
two parts. First, we show how to construct a safe policy if we had access to an infinite number
of samples, i.e., in the population. We then discuss how to construct policies empirically
from data, and establish finite-sample statistical properties of the policies. Finally, we show
how to incorporate the experimental control units to weaken the assumptions of our general
approach and discuss the practical implementation of the procedure for our analysis.
4.1
Partially identifying the value of a policy
To understand how the lack of overlap affects our ability to find a new policy, we will separate
the value of a policy into identifiable and unidentifiable components. We will then consider
scenarios where it is possible to at least partially identify the latter term. To do so, we can
write the value V (π, m∗) in terms of the observed outcome Y when our policy π agrees with
the baseline policy ˜π, and the unidentifiable full model m∗(a, x) when π disagrees with ˜π:
V (π, m∗) = E
"X
a∈A
π(X, a) {u(a) [˜π(X, a)Y + {1 −˜π(X, a)} m∗(a, X)] + c(a)}
#
.
(2)
Without further assumptions, we cannot point-identify the value of the conditional ex-
pectation when a is different from the baseline policy and so we cannot identify V (π, m∗) for
an arbitrary policy π. If we place restrictions on m∗(a, x), however, we can partially identify
a range of potential values for a given policy π (Manski, 2005). Specifically, we encode the
conditional expectation as a function m : A×X →[0, 1], and restrict it to be in a particular
model class F. We then combine this with the fact that we have identified some function
10

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
values, i.e., the conditional expectation of the observed outcome under the baseline policy
˜m(x) ≡m∗(˜π(x), x) = E[Y | X = x], to form a restricted model class:
M = {f ∈F | f(a, x) = ˜m(x) ∀x ∈X, a = ˜π(x)}.
(3)
This restricted model class combines the structural information from the underlying class
F (i.e., f ∈F) with the observable implications from the data (i.e., f(˜π(x), x) = ˜m(x)).
With this setup, a policy π can be associated with a range of possible values {V (π, m) | m ∈
M}, one for each observationally indistinguishable model. We discuss particular choices
of the model class F in our study (see Section 5), deferring computations to construct the
associated restricted model class M to Appendix C.
4.2
Criteria for decision-making under ambiguity
The lack of identifiability leads to an ambiguity in choosing an “optimal” policy: a policy
could have a high value under one model and a low value under another, and no amount of
data can help to adjudicate between the two scenarios. However, the value of the baseline
policy ˜π is point-identified using the observed policy values and outcomes:
V (˜π) = E
"X
a∈A
˜π(X, a){u(a)Y + c(a)}
#
.
The baseline policy ˜π is also already implemented, so a natural requirement of a new policy
is that it performs at least as well as the baseline.
To construct such a policy, we take a maximin approach by finding a policy that maxi-
mizes the improvement over the baseline in the worst case:
πinf ∈argmax
π∈Π
min
m∈M {V (π, m) −V (˜π)} .
(4)
Because the value of the baseline is point-identified, this is equivalent to finding a policy that
maximizes the worst-case value across the set of potential models M, i.e., argmax
π∈Π
min
m∈MV (π, m).
Such maximin criteria have been widely used for policy learning in various contexts with
11

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
partial identification (e.g., Kallus and Zhou, 2021; Pu and Zhang, 2021). Other applications
include decision problems with ambiguity more broadly, such as robust statistical learning
and robust optimization (e.g., Duchi and Namkoong, 2021; Bertsimas et al., 2011).
In
addition, Gilboa and Schmeidler (1989) show that the maximin expected utility criterion is
equivalent to having a preference relation among policies that satisfies a notion of uncertainty
aversion (in addition to other more standard properties).
A benefit of choosing the maximin criterion is that so long as the policy class Π includes
the baseline policy ˜π, and the underlying model lies in the restricted model class M, the
maximin optimal policy πinf will be at least as good as the baseline. We formalize this as
the following proposition.
Proposition 1 (Population safety). Let πinf be a solution to Eqn (4). If m∗∈M, and
˜π ∈Π, then V (˜π, m∗) ≤V (πinf, m∗).
We call this a “safety” property because the baseline policy acts as a fallback option. If
deviating from the baseline policy can lead to a worse expected utility, a maximin policy will
stick to the baseline. In this way, the new policy will change the baseline only when there
is sufficient evidence for improvement. We stress that this safety property only holds if the
structural assumptions about the true model m∗are correct, i.e., m∗∈M. Furthermore, this
notion of safety is from the point of view of the policy maker that sets the utility function: it
says nothing about the expected utility for other stakeholders with different utility functions.
Furthermore, this safety property comes at a cost: maximin policies can be conservative
and sub-optimal relative to the (infeasible) oracle policy, π∗∈argmaxπ∈Π V (π, m∗) (e.g.,
Manski, 2005; Cui, 2021). Because the maximin criterion limits the downside risks of deviat-
ing from the baseline policy, it can miss situations where doing so could lead to large utility
gains. We bound this sub-optimality at the population level in Appendix Theorem A.1 and
for policies learned empirically from finite samples in Theorem 2. An alternative criterion
that addresses this is the minimax regret criterion that measures the maximum value differ-
12

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
ence between the (infeasible) oracle and the chosen policy (e.g., Manski, 2007; Stoye, 2012;
Song, 2014). In addition, maximin policies can be sensitive to the existence of edge cases.
Searching for the worst case across all possible models ignores the fact that we may find
some models unlikely, even if they are possible. A Bayesian criterion that explicitly places
prior over models and computes the posterior expected utility given the observed data would
counteract this (Jia et al., 2023).
4.3
The empirical safe policy
Next, we show how to learn a policy from the observed data {Xi, ˜π(Xi), Yi(˜π(Xi))}n
i=1. We
begin with a sample analog to the value function in Eqn (2):
ˆV (π, m) = 1
n
n
X
i=1
X
a∈A
π(Xi, a) {u(a) [˜π(Xi, a)Yi + {1 −˜π(Xi, a)} m(a, Xi)] + c(a)} .
(5)
With this, we could find the worst-case sample value across all models in the restricted
model class M from Eqn (3). Unfortunately, since we do not have the true conditional
expectation ˜m(x) = E[Y (˜π(x))], we cannot compute the true restricted model class. One
potential approach is to obtain an estimator of the conditional expectation function, ˆ˜m(x),
and use the estimate in place of the true values. However, this fails to take into account the
estimation uncertainty, and could lead to a policy that improperly deviates from the baseline
due to noise, especially when the convergence rate of the estimated model ˆ˜m(x) is slow.
Instead, we construct a larger, empirical model class c
Mn(α), based on the observed
data, that contains the true restricted model class with a probability at least 1 −α, i.e.,
P

M ⊆c
Mn(α)

≥1 −α. Then, we construct our empirical policies by first finding the
worst-case in-sample value improvement, then maximizing this objective across policies π:
ˆπ ∈argmax
π∈Π
min
m∈c
Mn(α)
n
ˆV (π, m) −ˆV (˜π)
o
.
(6)
We refer to ˆπ as the empirical safe policy, as it is the empirical analog to the πinf. Note
that since the empirical restricted model class is larger than the true restricted model class,
13

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
a policy derived from it is more likely to fall back to the status quo rule.
To construct the empirical model class c
Mn(α), we use a uniform 1 −α confidence
band for the conditional expectation function ˜m(x), with lower and upper bounds bCα(x) =
[ bCαℓ(x), bCαu(x)] such that P

˜m(x) ∈bCα(x) ∀x

≥1 −α. With such a confidence band,
we construct the empirical restricted model class as
c
Mn(α) = {f ∈F | f(˜π(x), x) ∈bCα(x) ∀x ∈X}.
Throughout, we construct our confidence bands so that the 0% confidence band corresponds
to the point estimate: bCαℓ(x) = bCαu(x) = ˆ˜m(x), and therefore setting α = 1 creates the
restricted model class directly from the point estimates as described above. In our analysis
in Section 5, the covariates are all discrete. Thus, we first construct a point-wise confidence
interval for each unique data point, and then create a uniform confidence band by using a
Bonferonni correction for the number of unique data points. We discuss how to construct
the empirical model class and solve this optimization problem in Section 5.
4.4
Finite sample statistical properties
Compared to the population maximin problem, the empirical problem has an additional
layer of uncertainty due to sampling error that arises in finite samples. First, we establish
a statistical safety property: if the structural assumptions about the true model m∗are
correct, the learned policy will perform at least as well as the baseline policy with probability
approximately 1−α. We then characterize how conservative the solution is via the optimality
gap, V (π∗) −V (ˆπ): the policy value difference between the infeasible oracle that knows the
true model, and our data-driven maximin policy that uses the worst-case model.
The results below use the population Rademacher complexity of a function class G:
Rn(G) ≡E

supg∈G
 1
n
Pn
i=1 εig(Xi)

where εi is an i.i.d. Rademacher random variable,
i.e., Pr(εi = 1) = Pr(εi = −1) = 1/2, and the expectation is taken over both εi and Xi
(Wainwright, 2019, §4). We consider the maximum Rademacher complexity across the sub-
14

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
policy classes for actions a ∈A: Πa ≡{π(·, a) | π ∈Π}. This measures the ability of the
policy class to overfit. Using this measure, we establish a statistical safety property.
Theorem 1 (Statistical safety). If the baseline policy ˜π ∈Π and the true conditional
expectation m∗(a, x) ∈M, for any 0 < δ ≤e−1, the value of ˆπ relative to the baseline ˜π is,
V (˜π) −V (ˆπ) ≤6C(K −1)
"
max
a
Rn(Πa) + 2
r
1
n log K −1
δ
#
,
with probability at least 1 −α −δ, where C = maxy∈{0,1},a∈{0,1} |u(y, a)|.
Like Proposition 1, Theorem 1 is only meaningful if the assumptions about the true
model m∗are correct. If they are, Theorem 1 shows that the empirical safe policy will not
have a lower policy value than the baseline, up to standard empirical process terms: the
Rademacher complexity of the policy class Π, and an error term due to sampling variability
that decreases at a rate of n−1/2. The complexity of the policy class Πa controls the chance
that the learned policy is worse than the baseline due to overfitting.
For many standard policy classes, we expect the Rademacher complexity to decrease to
zero as the sample size increases, with the complexity determining the rate of convergence.
For simple policy classes, the bound will quickly go towards zero for any level α; complex
policy classes will require larger samples to ensure that the safety property is meaningful,
regardless of the level α. By using the larger model class c
Mn(α), the estimation error for
the conditional expectation ˆ˜m(x) −˜m(x) does not directly enter into the bound.2 However,
if we cannot estimate ˜m(x) well, the empirical restricted model class c
Mn(α) will be large,
and so the empirical safe policy may collapse to the baseline policy.
To quantify the optimality gap, we denote c
W c
Mn(α)(π∗(1−˜π)) as the width of the empirical
model class c
Mn(α) in the direction that π∗and ˜π disagree, where
c
WF(g) = sup
f∈F
1
n
n
X
i=1
X
a∈A
f(a, Xi)g(a, Xi) −inf
f∈F
1
n
n
X
i=1
X
a∈A
f(a, Xi)g(a, Xi)
2In Appendix A.2, we extend these results to consider the case where 1−α = 0 and we use point estimates
rather than confidence bounds. We show that the bounds have additional terms due to estimation error of
the model.
15

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
is the usual notion of the width of a set, for the set defined by all possible values of a function
f ∈F at the data points X1, . . . , Xn for actions a ∈A, in the direction defined by the vector
of all values of another function g(a, Xi).
Theorem 2 (Optimality gap). Let u(a) = u > 0 for all actions. If the true conditional
expectation m∗∈M, then for any 0 < δ ≤e−1 the optimality gap is
V (π∗) −V (ˆπ)
≤2C c
W c
Mn(α) (π∗(1 −˜π)) + 6C(K −1)
"
max
a
Rn(Πa) + 2
r
1
n log K −1
δ
#
,
with probability at least 1 −α −δ, where C = maxy∈{0,1},a∈{0,1} |u(y, a)|.
To simplify the statement, we have assumed that the utility gain across different actions is
constant and, without loss of generality, positive.
The bound on the empirical optimality gap contains the width term c
W c
Mn(α) (π∗(1 −˜π)),
in addition to the standard empirical process terms found in Theorem 1. If the baseline
policy is the oracle policy, then this width is zero, the bounds in Theorems 1 and 2 coincide,
and the regret of ˆπ relative to the oracle π∗will converge to zero so long as the complexity
of the policy class goes to zero. Otherwise, the width term does not necessarily converge
to zero: if the baseline and oracle policies disagree for many cases, the empirical safe policy
could perform substantially worse than the oracle.
This leads to a tradeoff between statistical safety (Theorem 1) and optimality (The-
orem 2). Increasing the confidence level will yield a greater probability that the learned
policy is safe relative to the baseline, but it will also widen the potential optimality gap
when the baseline and oracle policies disagree. This is similar to the tradeoff between a low
type I error rate (α low) and high power (c
W c
Mn(α) (π∗(1 −˜π)) low) in hypothesis testing.
The trade-off extends to the choice of model class as well: statistical safety requires that the
model class contains the true conditional expectation function, i.e., m∗∈M. This is palat-
able if we choose a complex model class, but complex model classes may lead to a greater
amount of uncertainty due to severe lack of identification and/or greater estimation error.
16

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
This tradeoff does not exist if the baseline policy is stochastic and there is overlap between
actions. In this case, the conditional expectation function is non-parametrically identifiable.
While we can still account for statistical uncertainty by constructing the empirical model
class c
Mn(α), we stress that our approach is not appropriate when the baseline policy is
stochastic. It only uses a model for the outcomes and so will rely on stronger assumptions on
the outcome model and be inefficient relative to a doubly robust approach that incorporates
the action probabilities as proposed by Athey and Wager (2021).
In practice, we do not know the oracle policy. To operationalize the bound in Theorem 2,
we can further upper bound the optimality gap by finding the policy that leads to the worst-
case width, were it the oracle policy: bS(F, Π; ˜π) ≡supπ∈Π c
W c
Mn(α) (π(1 −˜π)). We refer to
this quantity as the “size” of the empirical restricted model class because it measures the
degree of uncertainty about the true model m∗in regions of the covariate space where a
policy π ∈Π could deviate from the baseline.
We use this as a diagnostic measure in Section 5. Note that the policy class Π affects
the size. Restricting to policies that can only disagree with the baseline in only a few cases
will lead to a small size. Conversely, if we attempt to optimize over an expansive policy
class, the size diagnostic can be large. However, the size term is a loose upper bound: even
if the size is large, the optimality gap may still be small if it happens that the oracle policy
π∗is similar to the baseline ˜π. Therefore, a large size term is a warning that there may be
insufficient information to learn an improved policy, but it does not rule it out entirely.
4.5
Learning from experiments evaluating a deterministic policy
In our empirical study, the existing PSA-DMF system was compared to not providing algo-
rithmic recommendations. While a primary goal of this randomized controlled trial was to
evaluate whether one should adopt the algorithmic policy, we can leverage the control group
data to weaken the restrictions of the underlying model class M by placing assumptions on
treatment effects rather than the expected potential outcomes.
17

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
We consider an expanded set of actions that includes all actions in A and a “null”
action (i.e., do not provide an algorithmic recommendation). We denote the null action as
a = −1, with potential outcome Y (−1). Let Zi ∈{0, 1} be a treatment assignment indicator
where Zi = 0 if no policy is enacted (i.e., the null policy), and Zi = 1 if the policy follows the
baseline policy ˜π. Let e(x) = P(Z = 1 | X = x) be the probability of assigning the treatment
condition for an individual with covariates x. This is the propensity score for the treatment
assignment and since this is an experiment, it is known and strictly between 0 and 1. While
we consider general propensity scores when describing the method, in our experiment e(x) =
0.5 for all cases. This allows us to identify the conditional expectation function, m∗(−1, x) =
E[Y | X = x, Z = 0]. Defining the true conditional average treatment effect (CATE) of
the action a relative to the null action −1 as τ ∗(a, x) ≡m∗(a, x) −m∗(−1, x), we can also
identify the CATE under the baseline policy ˜π(x), ˜τ(x) = τ ∗(˜π(x), x).
We now write the value function in terms of the (partially-identified) CATE and the
(point-identified) expected outcome under the null action.
With a constant utility gain
u(a) = u, we can write it as:3
V (π) = E
"X
a∈A
π(X, a){u · τ ∗(a, X) + c(a)}
#
+ u · E[m∗(−1, X)].
Because the baseline term E[m∗(−1, X)] does not depend on π and is point-identified, we
can re-parameterize the model class to impose restrictions on the treatment effects T =
{f(a, x) ≡m∗(−1, x) + h(a, x) | h ∈F, h(˜π(x), x) = τ(˜π(x), x)}. The CATE function is
sometimes assumed to be simpler (e.g. smoother, sparser, fewer interaction terms) than the
conditional expected potential outcome (see, e.g., K¨unzel et al., 2019, who argue that the
CATE should be easier to estimate). Therefore, we may consider a smaller model class for
the treatment effects than for the baseline outcomes, leading to a smaller optimality gap in
Theorem 2. We can also construct the empirical analog by creating a larger empirical model
class bTn(α) as in Section 4.3.
3Proposition A.1 in the Appendix shows this result for the general utility case.
18

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
Finally, following Kitagawa and Tetenov (2018), to account for potential unequal as-
signment into treatment, we can solve the population and empirical robust optimization
problems using the inverse probability weighted outcome Γ(Z, X, Y ) ≡Y {Z(1 −2e(X)) +
e(X)}/{e(X)(1 −e(X))}, which equals the conditional expected potential outcome in ex-
pectation, i.e., E[Γ(Z, X, Y ) | Z = z, X = x] = z · m∗(˜π(x), x) + (1 −z) · m∗(−1, x).
5
Empirical Analysis of the Pre-trial Risk Assessment
5.1
Implementation details
For our empirical analysis, we will represent the empirical restricted model classes as the
set of functions that are upper and lower bounded point-wise by two bounding functions,
bTn(α)
=
{f : A × X →R
|
bBαℓ(a, x) ≤f(a, x) ≤bBαu(a, x)}, where the upper and
lower bounds are chosen to satisfy P

T ⊆bTn(α)

≥1−α. In Appendix C, we show how to
compute these bounds using simultaneous confidence intervals when the underlying model
class is the set of Lipschitz functions or linear models.
The point-wise bound allows us to solve for the worst-case empirical value ˆV inf(π) by
finding the minimal value for each action-covariate pair (see Pu and Zhang, 2021). Finding
the empirical safe policy by solving Eqn (6) is equivalent to solving an empirical welfare
maximization problem using a quasi-outcome that imputes the counterfactual outcome with
the lower bound when the action disagrees with the baseline policy:
max
π∈Π
1
n
n
X
i=1
X
a∈A
π(Xi, a)
n
u(a)
h
˜π(Xi, a){Γ(1, Xi, Yi) −Γ(0, Xi, Yi)} + {1 −˜π(Xi, a)} bBαℓ(a, Xi)
i
+ c(a)
o
,
(7)
where we have omitted terms that do not depend on π. A similar implementation strategy
is applicable to cases where we model potential outcomes rather than treatment effects.
19

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
5.2
Learning a new NVCA flag threshold
We begin our analysis by considering a small change to the existing system: learning a new
threshold for the NVCA flag. Our goal here is to find the optimal NVCA threshold in the
worst case, where our preferred outcome is no NVCA.
Choosing the policy class.
We first formalize our choice of policy class. Let xnvca ∈
{0, . . . , 6} be the total number of NVCA points for an arrestee, computed using the point
system in Appendix Table G.1. Recall that the baseline NVCA algorithm is to trigger the
flag if the number of points is greater than or equal to 4, i.e., ˜π(xnvca) = 1{xnvca ≥4}. Our
policy learning problem is to choose a policy among the class of threshold policies, Πthresh =
{π(x) = 1{xnvca ≥η} | η ∈{0, . . . , 7}} . We will keep the baseline weighting on arrestee risk
factors and only change the threshold η. Since this policy class only has eight elements, we
can compute the empirical maximin policy ˆπ by solving Eqn (7) via an exhaustive search.
Choosing the model class.
We next choose a model class for the CATE on no NVCA
occurring, τ ∗(a, xnvca). There are many potential ways to characterize the complexity of
functions of one variable such as τ ∗(a, ·). Here, we characterize it via a Lipschitz constraint
that |τ(a, xnvca) −τ(a, x′
nvca)| ≤λa|xnvca −x′
nvca| for any pair of NVCA points xnvca, x′
nvca.
To construct the empirical restricted model class, we set the level to 1 −α = 0.8, allow-
ing some tolerance for statistical uncertainty and construct a simultaneous 80% confidence
interval for the CATE via a Bonferroni correction for the 7 unique values (see Appendix C.2
for details on computing the bounds). We also restrict the treatment effects to be bounded
between −1 and 1, since the outcome is binary.4
For this model class, we need to specify the Lipschitz constants for the CATE when
the flag is and is not triggered (λ1 for τ(1, xnvca)) and λ0 for τ(0, xnvca), respectively). We
adapt a suggestion from Imbens and Wager (2019) for model classes with a bounded second
4This is not the tightest possible bound, since the restriction is that 0 ≤m(−1, x) + τ(a, x) ≤1. To
incorporate the uncertainty in estimating m(−1, x) in finite samples we could use analogous techniques to
those in Section 4.3; we leave this to future work.
20

````

## PDF page 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
derivative to the Lipschitz case. We estimate the CATE function by taking the difference in
NVCA rates with and without provision of the PSA at each level of xnvca. Then, we measure
the largest consecutive difference between CATE estimates (0.016 and 0.433 for a = 0, 1,
respectively). Finally, we set the Lipschitz constants to be a constant multiple C of this
difference yielding λ0 = C × 0.016 and λ1 = C × 0.433. Setting C = 1 gives the smallest
Lipschitz constants supported by the data; increasing C will be more conservative.
Choosing the utility function.
Recall that in our parameterization we must define the
difference in utilities when there is and is not an NVCA, u(a) = u(1, a) −u(0, a), for both
actions a ∈{0, 1}. This captures the benefits of avoiding an NVCA. Countering this benefit
is the baseline cost of action a, c(a) = u(0, a). The marginal monetary cost of triggering the
NVCA flag is zero given the initial fixed cost of collecting the data for the PSA. However,
to the extent that triggering the NVCA flag increases the likelihood of pre-trial detention, it
will lead to an increase in fiscal costs — e.g., housing, security, and transportation — for the
jurisdiction. Furthermore, there are potential socioeconomic costs to the defendant and their
community that balance against potential benefits from avoiding more criminal activity.
To represent these costs, we will place zero cost on not triggering the NVCA flag, c(0) = 0,
and a cost of 1 on triggering the flag, c(1) = −1. We then assign an equal utility gain from
avoiding an NVCA, u(1) = u(0) = u (equivalently, the cost of an NVCA is −u). This yields
a utility function of the form u(y, a) = u×y −a, where u is the ratio of the cost of an NVCA
to the cost of triggering the flag. Choosing a particular value of u is outside the scope of
this paper and indeed would be inappropriate for us to do: the choice depends on societal
preferences and should be arrived at in a collaborative process between policy-makers in
the criminal justice system and the communities impacted by it. Instead, we examine how
adjusting the ratio u affects the policies we learn.5
5Note that mathematically one could use a negative cost of triggering the flag, but this would encourage
triggering the flag even if it would not avoid an NVCA.
21

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
(a)
−100%
−50%
0%
50%
100%
0
2
4
6
Total NVCA Points
Effect of Providing PSA on No NVCA
NVCA Flag
Not Triggered
Triggered
(b)
1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20
Cost of NVCA
Lipschitz Multiplicative Factor
Threshold Value
4
6
7
Figure 2: Learning a new NVCA flag threshold. (a) Empirical restricted model class and
maximin threshold with a Lipschitz multiplicative factor of C = 3. The points and thin
lines around them are point estimates and a simultaneous 80% confidence interval for the
partial CATE function τ(˜π(xnvca), xnvca) when the NVCA flag is not triggered (˜π(xnvca) = 0,
in orange) and is triggered (˜π(xnvca) = 1, in blue). The thick solid lines represent the partial
identification set for the unobservable components of the CATE, τ(1, xnvca) for xnvca < 4 and
τ(0, xnvca) for xnvca ≥4. The purple dashed line represents the baseline policy of triggering
the flag when xnvca ≥4, and the pink dashed line is the empirical safe policy that only
triggers the flag when xnvca ≥6. (b) Maximin threshold values solving Eqn (7) for the
NVCA flag threshold rule with a level of 1 −α = 80% as the cost of an NVCA increases
from 1 to 20 times of the cost of triggering the NVCA flag, and the multiplicative factor on
the estimated Lipschitz constant varies from 1 to 10.
Learning a maximin NVCA threshold.
Figure 2a presents the empirical restricted
model class with a particular multiplicative constant of C = 3 by showing point estimates and
simultaneous 80% confidence intervals for the observable component of the CATE function
τ ∗(˜π(xnvca), xnvca) and the partial identification set for the unobservable component. There
is substantially more information when extrapolating the CATE for the case that the NVCA
flag is triggered. This is because the point estimates do not vary much with the NVCA
points, leading to a small Lipschitz constant. On the other hand, when extrapolating in the
other direction, there is a large jump in the point estimates between xnvca = 5 and xnvca = 6,
leading to a large Lipschitz constant. This means that the empirical restricted model class
puts essentially no restrictions on τ ∗(1, xnvca) for xnvca < 4.
Estimating this policy requires choosing the Lipschitz multiplicative factor C ≥1. We
22

````

## PDF page 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
fit the empirical safe policy across a range of values to see if the results are stable. Figure 2b
shows the learned thresholds as we vary both the relative cost u of an NVCA in the utility
function and the multiplicative factor C. When the cost of an NVCA is u ≤7, the data
support increasing the threshold to at least 6 even in the worst case and even with C = 10,
only triggering the flag for arrestees with the observed maximum of 6 total NVCA points.
The results for larger costs are more sensitive to the choice of C, and the learned threshold
collapses back to the baseline of 4 for intermediate choices of C.
Raising the threshold to η = 6 is a much more lenient policy than the status quo, reducing
the number of arrestees flagged as at risk of an NVCA by 95%. We find evidence for such
a large change because there is no meaningful effect of providing the PSA on the absence
of an NVCA, except for those arrestees who have the maximum of 6 points (Figure 2a).
One possible reason for these small effects is that the judge’s behavior is not affected. This
appears to be the case when xnvca ≤4: there is little effect on the judge’s bail decision in
these cases. However, for xnvca > 4, providing the PSA increases cash bail decisions by over
30 pp (see Appendix G.1 for further discussion). This suggests that PSA provision is leading
to additional bail decisions without a requisite decrease in NVCAs for xnvca = 5.
Thus, even in the worst case, the threshold could be raised to η = 6 without an increase
in the NVCA rate that outweighs costs from triggering the flag. As we increase the cost of
an NVCA, however, at some point (e.g., u ≥13 for C = 3), the cost becomes large enough,
making the empirical safe policy revert to the status quo with the threshold at η = 4.
5.3
Learning new FTA, NCA, and NVCA risk scoring rules
We next turn to constructing new, maximin optimal FTA, NCA, and NVCA risk scores. For
each risk score, we focus on the absence of the corresponding negative outcome.
Choosing the policy classes.
A key consideration is the form of the policy classes used
for each risk score. One possibility is to allow the policies to be flexible functions of all the
information available in the system. Although the oracle policy may have a high expected
23

````

## PDF page 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
utility in this case, in finite samples a complex policy can over-fit and reduce the quality
of the safety property in Theorem 1. In addition, the oracle policy may be substantially
different from the baseline policy, leading to a large optimality gap in Theorem 2. Lastly,
in real-world applications, policy makers might be reluctant to adapt the existing system to
an entirely new policy. For these reasons, we use the same set of risk factors and focus on
changing the weight applied to each risk factor (see Appendix Table G.1).
For each risk score, we formally describe the status quo rule as consisting of a vector of
integer-valued weights ˜θ on the risk factors x, and a mapping from the linear combination
of the risk factors ˜θ⊤x to the K risk levels via thresholds. We consider the policy class
that consists of all possible vectors of integer-valued weights and all possible thresholds,
restricting to inter-valued weights in order to mimic the structure of the existing risk scores.
For example, recall that the NVCA flag has K = 2 risk levels (a flag for elevated NVCA
risk), 7 binary risk factors, and the baseline policy is ˜π(x) = 1
nP7
j=1 ˜θjxj ≥4
o
. We then
write the corresponding NVCA flag policy class as:
Πnvca =
(
π(x) = 1
(
7
X
j=1
θjxj ≥η
)  θj ∈Z, η ≥0
)
.
(8)
This policy class includes the original NVCA flag rule as a special case. We can construct
the policy classes for the FTA and NCA rules similarly by including multiple thresholds (see
Appendix G.2 for a formal definition).
To simplify comparisons to the status quo and
avoid identifiability issues, we will primarily constrain the thresholds η to be equal to the
status quo values. This allows us to understand any differences from the status quo rule by
comparing the learned weight vector to the baseline weight vector ˜θ. With this policy class,
the optimization problem is a mixed integer program; we solve this with the Gurobi solver.
Choosing the model class.
In contrast to changing only the NVCA threshold above,
here the CATE is a function of multiple binary variables.
A natural way to character-
ize the complexity of such models is by the number and strength of interaction terms be-
24

````

## PDF page 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
Additive Effect Model
Second Order Effect Model
0%
25%
50%
75%
100%0%
25%
50%
75%
100%
0%
25%
50%
75%
100%
Confidence Level 1 − α
Size of model class
Thresholds
Fixed
Learned
Risk Score
FTA
NCA
NVCA
Figure 3: The size (as a percentage of its maximum value) of two different model classes
with respect to the linear threshold policy class versus the confidence level 1−α for the FTA
(green), NCA (orange), and NVCA (purple) scoring rules. The dashed purple line shows
the size for the NVCA model class when the threshold is included as a decision variable and
learned in addition to the weights.
tween the variables. We focus on the two simplest models: an additive effect model Tadd ≡
n
τ(a, x) = P
j τajxj
o
and a second order effect model Ttwo ≡
n
τ(a, x) = P
j
P
k<j τajkxjxk
o
.
Because the covariates are discrete, we can write these using linear models. We again restrict
the treatment effects to be bounded between −1 and 1. These two model classes lead to
different restrictions and ultimately affect what policies we learn from the experiment (see
Appendix C.3 for details). This is partly because even with infinite data the models may
not be identifiable. But it is also because with finite data there is a different amount of
uncertainty in each model class.
To diagnose the amount of information available in each model class, we use the size
measure bS(bTn(α), Π; ˜π). Figure 3 depicts this information by showing how the size of the
model class (vertical axis), changes with the desired confidence level 1 −α (horizontal axis)
for each risk score and model class. We also show the difference in the size for the NVCA
rule when fixing the threshold to the existing value versus including it as a decision variable.
There is a stark difference in the amount of information between the different risk scores
within the same model class. Under the additive model for the NVCA rule, the size is zero
when the confidence level is zero, implying that this model is identifiable. This is due to the
structure of the NVCA flag rule: for any given value of a covariate, it is possible to observe
25

````

## PDF page 26

Technical extraction; compare with original PDF page 26.

````text
cases with the flag set to zero or one. When accounting for the statistical uncertainty, the
size increases, but it is substantially smaller than the size for the FTA and NCA rules, both
of which are near or at the maximum value of 2. Because these risk scores have 6 levels, we
would need to observe cases with all 6 levels for any given value of a covariate in order to
identify the additive model. Overall, there is little information available to support changing
the FTA and NCA scoring rules.
Turning to the second order treatment effect model for the NVCA score, which makes
weaker assumptions, we find that it is likely too large a class for us to learn a new NVCA
rule, with roughly twice the size as for the additive effect model. This is because there are
several pairs of variables that always trigger the NVCA flag (e.g., if both the current offense
is violent and the arrestee has 3 or more prior violent convictions). Finally, we observe that
increasing the flexibility of the policy class by including the threshold as a decision variable
rather than keeping it fixed increases the size because it is a function of both the model class
and the policy class.
These diagnostics point to focusing on the NVCA score with an additive effect model.
There is likely not enough information to make any changes to the NCA and FTA scores
under either model, and the 2nd order effect model for the NVCA flag is not well enough
identified. However, in Appendix G.1, we find some evidence for the existence of interactions
for the NVCA score via classical model testing procedures.
Therefore, we caution over-
interpreting our results. For completeness, we show these results in Appendix G and indeed
find that the optimal solution for the worst case is to not deviate from the status quo rules.
Choosing the utility function.
We use the same utility parameterization as in Sec-
tion 5.2. For this value function, the marginal decrease in the utility from triggering the
flag is constant regardless of the proportion of arrestees that are classified as an NVCA risk.
However, higher levels of pre-trial incarceration can have additional negative impacts on the
community above and beyond the cost to the individual. In Appendix G.1, we include an
26

````

## PDF page 27

FORMULA CHECK REQUIRED: original PDF page 27.

````text
(a) Varying the confidence level
0%
25%
50%
75%
5
10
15
Cost of NVCA
Confidence Level 1 − α
Change in % flaged for NVCA risk (pp)
−16%
−12%
−8%
−4%
(b) Maximin NVCA flag weights
2
1
1
1
1
1
2
0
0
0
0
0
0
0
1
1
1
1
0
0
1
1
1
1
1
0
0
1
1
1
1
1
0
0
1
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
2
0
1
1
1
1
2
2
0
1
1
1
1
2
2
0
1
1
1
1
2
2
0
1
1
1
1
2
2
0
1
1
1
1
2
2
1
1
1
1
1
2
2
1
1
1
1
1
2
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Three or more prior violent convictions
Two prior violent convictions
One prior violent conviction
Prior conviction (felony or misdemeanor)
Pending Charge at time of arrest
Current violent offense and 20 years old or younger
Current violent offense
Cost of NVCA
Difference from original weights
−2
−1
0
1
2
Figure 4: (a) The percentage point difference in the proportion of arrestees flagged for NVCA
risk between the maximin policy and the original NVCA score as the cost of an NVCA
increases from 1 to 15 times of the cost of triggering the NVCA flag and the confidence level
varies between 0% and 100%. (b) Change in Maximin NVCA flag weights θ (in Eqn (G.2))
as the cost of an NVCA increases from 1 to 15 times the cost of triggering the NVCA flag,
at a confidence level of 1 −α = 80%.
additional penalty to triggering the NVCA flag that scales with the proportion of arrestees
classified as being at risk.
Learning a maximin NVCA flag.
Figure 4a presents the changes to the original rule
made by the maximin policy that solves the optimization problem given in Eqn (7) under
the additive treatment effect class Tadd. The changes are shown in terms of the proportion of
arrestees flagged for an NVCA risk as we vary the cost of an NVCA −u and the confidence
level 1 −α. Across every confidence level, the maximin policy differs less and less from the
original rule as the cost of an NVCA increases, moving from never triggering the flag at a
1–1 cost to eventually collapsing back to the status quo if the cost crosses an α dependent
threshold. For a given cost of an NVCA, policies at lower confidence levels are more aggressive
in deviating from the original rule, prioritizing a potentially lower regret relative to the
(infeasible) optimal policy at the expense of a higher chance that the new policy is worse
than the original rule.6
6Except for when the cost of an NVCA is greater than 12 and the confidence level is 0%, the maximin
policies do not trigger the flag when the original rule does not.
27

````

## PDF page 28

FORMULA CHECK REQUIRED: original PDF page 28.

````text
Figure 4b shows the integer weights on the risk factors for the maximin policy at the
1−α = 80% level as the cost of an NVCA increases. In the limiting setting where an NVCA
is given the same cost as triggering the NVCA flag, the maximin policy never triggers the
flag because it cannot be worth the cost. Once the cost is at least 14 times the cost of
triggering the flag, the learned policy reduces to the original rule. In light of the sizes shown
in Figure 3, this behavior is primarily due to increased uncertainty in the effect of triggering
the NVCA flag. If the policy maker were to set the cost of an NVCA above a certain point,
any change in the policy would be too risky to act upon. For intermediate values, the learned
policy places less weight on the number of prior violent convictions and whether the current
offense is violent than the original rule. In Appendix G.1, we consider a more flexible policy
class that includes additional risk factors.
5.4
Learning a new DMF matrix for bail recommendation
Finally, we analyze the overall recommendation given by the DMF matrix (see Figure 1).
This aggregates the FTA and NCA scores into an overall recommendation on the level of
cash bail and pre-trial supervision and monitoring conditions. Below, we focus on using the
absence of an NVCA as the primary outcome.
Choosing the policy class.
We consider constructing a new DMF matrix based on
the FTA and NCA scores, which we combine into a vector (xfta, xnca) ∈{1, . . . , 6}2, re-
stricting our analysis to the 1,544 cases that used the DMF matrix rather than those for
whom cash bail was automatically recommended.
We will focus on a policy class that
keeps the structure of the existing rule encoded by the DMF matrix. An important as-
pect of the rule is that it is monotonic; the risk level cannot decrease if either the FTA
or NCA score increases. Formally, we can encode the monotonic policy class as, Πmono ≡
{π((xfta, xnca)) ≤π((xfta + 1, xnca)) and π((xfta, xnca)) ≤π((xfta, xnca + 1))}. Again, this leads
to an integer program, which we solve via the Gurobi solver. We will consider four variations
of the policy: (i) the overall risk level from 1 to 7; (ii) the quaternary recommendation of
28

````

## PDF page 29

FORMULA CHECK REQUIRED: original PDF page 29.

````text
(a) Empirical size
0%
25%
50%
75%
100%
0%
25%
50%
75%
100%
Confidence Level 1 − α
Size of model class
Cash Bail + Monitoring Conditions
No vs Modest vs Moderate vs Full Cash Bail
No vs Modest/Moderate vs Full Cash Bail
Signature Bond vs Cash Bail
(b) Maximin DMF Matrices
Cost: 1
Cost: 2
Cost: 5
Cost: 10
Cost: 15
Confidence
0%
Confidence
20%
Confidence
80%
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
NCA Score
FTA Score
PSA Recommendation
Signature Bond
Cash Bail
Figure 5: (a) The size (as a percentage of the maximum value) of the additive model class
with respect to the monotone policy class as the confidence level varies for cash bail recom-
mendation policies, collapsing together successively more gradations on bail. The coarsest
policy—Signature Bond vs any Cash Bail—has the most information available. (b) Maximin
monotone cash bail recommendations under an additive model for the treatment effects, as
the cost of an NVCA and the confidence level vary. The dashed black line indicates the
original decision boundary between a signature bond (above and to the left) and cash bail
(below and to the right). The original decision boundary is modified only when the cost and
confidence are low.
a signature bond, modest cash bail, moderate cash bail, or (full) cash bail; (iii) the ternary
recommendation that combines modest and moderate cash bail; and (iv) the binary recom-
mendation that collapses together all cash bail recommendations.
Choosing the model class.
We again focus on the class of additive treatment effect
models τadd(a, x) = τfta(a, xfta) + τnca(a, xnca). We only condition on the FTA and NCA
scores since they are the two components of the DMF decision matrix. Because xfta and
xnca are discrete with six values, we can further parameterize the additive terms as six-
dimensional vectors. Importantly, this rules out interactions between the FTA and NCA
scores in the effect. In Appendix G.3 we test for the presence of interactions and do not find
evidence against the null of an additive model.7
Figure 5a presents the size of this model class relative to the monotone policy class for
the three types of recommendations as we vary the confidence level for the three types of
7Note that we could also use a Lipschitz restriction as in Section 5.2. This alternative assumption may
be significantly weaker, though it would require choosing the Lipschitz constant.
29

````

## PDF page 30

Technical extraction; compare with original PDF page 30.

````text
DMF recommendations. There is no information to learn reliably a new fine-grained overall
risk score or quaternary bail recommendation. This is due to the structure of the DMF
matrix: some risk levels are only possible for a single NCA score, and others (such as the
moderate cash bail condition) only for a single combination of FTA and NCA scores.
Therefore, we focus here on the binary cash bail recommendation, where the size of the
model class is large, but smaller than for the ternary bail recommendation. This is because
we can never observe a case where the DMF recommends a signature bond with either an
FTA score or NCA score above 4, nor can we observe a case where the DMF recommends
cash bail with either an FTA score below 2 or an NCA score below 3. In the middle is
an intermediate area with FTA scores between 2 and 4 and NCA scores between 3 and 4
where we can fully identify the effect of assigning cash bail under the additive model. For
this intermediate area, there is a significant amount of uncertainty due to small sample
sizes: there are only 3 cases where cash bail is recommended that have an NCA score of 3.
Appendix Figure G.14 visualizes this uncertainty.
Choosing the utility function.
We follow Sections 5.2 and 5.3, and parameterize the
utility as a fixed cost of 1 for recommending cash bail and varying the cost of an NVCA.
Learning a maximin DMF Matrix.
Figure 5b shows the learned policies when varying
the cost of an NVCA and different confidence levels. In the limiting case where the cost of
an NVCA is equal to recommending cash bail, the safe policy recommends cash bail only
for the most extreme cases. In the other limiting case, where we set the confidence level
to 0 and rely on the the point estimates directly rather than accounting for the statistical
uncertainty, increasing the cost of an NVCA leads to more of the intermediate area with FTA
scores between 2 and 4 and NCA scores between 3 and 4 being assigned cash bail until the
cost is high enough that the entire identified area is assigned cash bail. However, this does
not hold up to even the slightest degree of statistical uncertainty due to the uncertainty in
the treatment effects. Because the effects of assigning cash bail are both small and uncertain,
30

````

## PDF page 31

Technical extraction; compare with original PDF page 31.

````text
the learned policy reduces to the existing DMF matrix.
6
Discussion
Data-driven algorithmic policies and recommendations have become an integral part of our
society. An important challenge when learning a new policy is to ensure that it does not
perform worse than the existing one. In settings like ours where decisions are highly con-
sequential, policy makers should be able to limit the probability that a new algorithmic
recommendation system achieves a worse outcome than the existing system. This is par-
ticularly essential when it is impossible to randomize the algorithm output for ethical and
logistical reasons. The lack of identification necessitates extrapolation, making it impossible
to learn a new policy using standard statistical methods.
We address these challenges by partially identifying the value of potential policies. Since
this leads to a decision-making problem under ambiguity, we use the maximin criterion that
selects the best policy in the worst case. Our methodology has a statistical safety property:
if we make correct structural assumptions about the true model, the resulting policy will not
be worse than the status quo policy with some probability, up to sampling uncertainty.
Our goal is to understand what changes to the PSA-DMF recommendation system should
be made, if any. We do not find strong support to change the existing FTA and NCA scores,
nor the overall risk score and bail recommendation. This is due to a confluence of factors.
Foremost is the conservative nature of the maximin criterion that yields a strong bias towards
the status quo. However, we emphasize that failing to find strong evidence to change the
status quo policy does not necessarily imply that the status quo is desirable.
With the conservative criterion, our analysis is not informative about the FTA and NCA
scores and the overall risk level due to the design of these algorithms. They have many
fine gradations and in some cases only a single unique combination of inputs can lead to
a particular output. This means that there is little to extrapolate from and the bounds
are uninformative, even with strong structural assumptions. In contrast, our analysis is not
31

````

## PDF page 32

FORMULA CHECK REQUIRED: original PDF page 32.

````text
informative about the binary bail recommendation due to a combination of identifiability
issues and limited sample sizes. With an additive model, we can only identify impacts for
cases with intermediate FTA and NCA scores, but the sample sizes in this intermediate area
are too small to make strong conclusions.
However, the data do support altering the NVCA flag, even with this conservative cri-
terion, either by raising the threshold or by putting less weight on violent convictions and
offenses. Both of these would lead to a more lenient rule that flags fewer arrestees, and
the data support these changes even when the cost of an NVCA is 8–13 times the cost of
triggering the flag. Stevenson and Mayson (2022) present survey evidence showing that 50%
of individuals rate being a victim of an assault as bad as between 5 days and 6 months of
detention; implying a cost ratio for one month of detention between 1
6 and 6. Choosing any
ratio within this range would lead to a change to the system, though since our focus is on
triggering the flag, rather than detention, a larger benchmark may be more appropriate.
Our analysis serves as an initial proof of concept, probing various elements of the ex-
isting risk assessment system. As such, there are several limitations and various ways that
the analysis has been simplified. In particular, we place costs on the algorithmic outputs
(the PSA recommendations) rather than on the resulting human decisions (the judge’s bail
decision). In Appendix D, we directly incorporate the costs of the judges’ decisions, but find
that this adds too much statistical uncertainty to improve reliably upon the existing rule.
Another limitation of our analysis in Section 5.3 is that we separately consider each
outcome and its risk score. Since each risk score can effect each outcome, all pairs of risk
scores and outcomes could be considered. This issue is also present in our analysis of the
DMF matrix (Section 5.4), where we focus on NVCAs but the bail recommendations can
impact all three outcomes.
A fuller analysis may consider all three risk scores and the
bail recommendation simultaneously for all three outcomes, using a utility function that
incorporates all of the outcomes and includes measures of costs such as economic and social
32

````

## PDF page 33

Technical extraction; compare with original PDF page 33.

````text
outcomes. However, such an analysis may not be informative, given the limitations in the
design and the data discussed above.
An important limitation of our methodology is that learning algorithmic policies requires
making many non-trivial choices. For example, focusing on the simple setting of changing
the NVCA flag threshold in Section 5.2 requires (a) specifying a model class; (b) specifying
a significance level; and (c) choosing a utility function, among other things. The analyses
in Sections 5.3 and 5.4 include even more involved analytical and implementation decisions.
Therefore, it is important to examine the sensitivity of empirical results to these choices.
Choosing the model class can be difficult. With randomized evaluations of the status
quo policy, simple treatment effect structures may be plausible because treatment effects
are often far less heterogeneous than baseline outcomes. We inspected the sensitivity and
stability of the maximin policy to modeling choices and hyper-parameters, such as the choice
of Lipschitz constant. Formalizing these heuristics is an important direction for future work.
Another key choice is the policy class to optimize over.
We recommend choosing a
policy class that can lead to limited adjustments to the baseline policy rather than wholesale
changes. While more flexible policy classes could yield better results, we are unlikely to
achieve them, and large changes to existing systems may not be practically feasible.
Finally, our methodological approach has a wide range of potential applications. For
transparency and interpretability, many data-driven algorithms in public policy and medicine
are based on known, deterministic rules rather than randomized rules. Examples include the
SNAP eligibility rule, the MELD score for liver transplantation, and other risk assessment in-
struments used across public policy contexts (see Coston et al., 2020, and references therein).
These instances will all have identifiability issues due to lack of overlap, and our methodology
addresses this challenge by learning a new, safe policy that improves upon the status quo.
If the algorithm is designed in such a way that there is little to extrapolate from—as
was the case for the FTA and NCA scores—our approach is unlikely to be informative. Our
33

````

## PDF page 34

Technical extraction; compare with original PDF page 34.

````text
methodology may be more effective when the baseline policy includes multiple inputs, each
with a large region where multiple actions are possible. This can be true when there are
group-specific thresholds for a common risk score or decision variable, for example as with
school enrollment and loan access, and income limits for social programs (Zhang et al., 2023).
However, different studies may require other implementation details. For instance, our study
only includes discrete covariates; incorporating continuous covariates will require additional
implementation work. In addition, analyzing continuous outcomes with non-linear utility
functions, incorporating other criteria such as fairness measures, or changing the optimality
criterion to minimax regret, would require additional implementation and analysis.
34

````

## PDF page 35

FORMULA CHECK REQUIRED: original PDF page 35.

````text
A
Additional theoretical results
A.1
Population optimality gap
We define the population width of function class F as
WF(g) = sup
f∈F
E
"X
a∈A
f(a, X)g(a, X)
#
−inf
f∈F E
"X
a∈A
f(a, X)g(a, X)
#
.
Given this definition, the following theorem shows that the population optimality gap is
bounded by the width of the function class.
Theorem A.1 (Population optimality gap). Let u(a) = u > 0 for all actions a ∈A, and
πinf be a solution to Eqn (4). If m∗∈M, the regret of πinf relative to the optimal policy
π∗∈argmaxπ∈Π V (π) is
V (π∗) −V (πinf)
u
≤WM(π∗(1 −˜π)).
A.2
Extension of Theorems 1 and 2 to the case where α = 1
In this section we extend Theorems 1 and 2 to include results for the case where we set
α = 1. We do so by providing bounds that hold regardless of the level α. In addition, we
also provide a tighter bound on the optimality gap involving the difference between the true
optimal policy π∗and the baseline policy ˜π. For clarity, we present them with the bounds
in Theorems 1 and 2 restated.
For a model class define the empirical support function as
hF(z) ≡sup
f∈F
1
n
n
X
i=1
X
a∈A
ziaf(Xi, a),
where z = (z10, . . . , z1K−1, . . . , zn0, . . . , znK−1) is a length n(K −1) vector.
Theorem A.2 (Statistical safety (with α = 1)). If the baseline policy ˜π ∈Π and the true
conditional expectation m∗(a, x) ∈M, for any 0 < δ ≤e−1, the value of ˆπinf relative to the
baseline ˜π is,
V (˜π) −V (ˆπ) ≤6C(K −1)
"
max
a
Rn(Πa) + 2
r
1
n log K −1
δ
#
+ sup
π∈Π
|h c
Mn(α) (−π(1 −˜π)u(·)) −hM (−π(1 −˜π)u(·)) |,
with probability at least 1 −δ, where C = maxy∈{0,1},a∈{0,1} |u(y, a)|.
35

````

## PDF page 36

FORMULA CHECK REQUIRED: original PDF page 36.

````text
For the point-wise bounded model class that we consider, the extra term simplifies to be
the worst-case difference between the true lower bound and the estimated lower bound.
Corollary A.1 (Statistical safety (with α = 1)). Under the setting of Theorem A.2, let
the restricted model class M and the empirical restricted model class c
Mn(α) consist of
point-wise bounded functions, M = {f : A × X →R | Bℓ(a, x) ≤f(a, x) ≤Bu(a, x)} and
c
Mn(α) = {f : A × X →R
|
bBαℓ(a, x) ≤f(a, x) ≤bBαu(a, x)}. Then the value of ˆπinf
relative to the baseline ˜π is,
V (˜π) −V (ˆπ) ≤6C(K −1)
"
max
a
Rn(Πa) + 2
r
1
n log K −1
δ
#
+ 2C sup
a,x | bBαℓ(a, x) −Bℓ(a, x)|,
with probability at least 1 −δ, where C = maxy∈{0,1},a∈{0,1} |u(y, a)|.
Theorem A.3 (Optimality gap (with α = 1)). Let u(a) = u > 0 for all actions. If the true
conditional expectation m∗∈M, then for any 0 < δ ≤e−1 the optimality gap is
V (π∗) −V (ˆπinf) ≤2C c
W c
Mn(α) (π∗(1 −˜π)) + 6C(K −1)
"
max
a
Rn(Πa) + 2
r
1
n log K −1
δ
#
+ 2C sup
π∈Π
|h c
Mn(α) (−π(1 −˜π)) −hM (−π(1 −˜π)) |,
with probability at least 1 −δ, where C = maxy∈{0,1},a∈{0,1} |u(y, a)|.
The statement similarly simplifies under the point-wise bounded setting.
Corollary A.2 (Optimality gap (with α = 1)). Under the setting of Theorem A.3, let the
restricted model class M and the empirical restricted model class c
Mn(α) consist of point-
wise bounded functions, M = {f : A × X →R
|
Bℓ(a, x) ≤f(a, x) ≤Bu(a, x)} and
c
Mn(α) = {f : A × X →R |
bBαℓ(a, x) ≤f(a, x) ≤bBαu(a, x)}. Then for any 0 < δ ≤e−1,
the optimality gap is
V (π∗) −V (ˆπinf) ≤2C c
W c
Mn(α) (π∗(1 −˜π)) + 6C(K −1)
"
max
a
Rn(Πa) + 2
r
1
n log K −1
δ
#
+ 2C sup
a,x | bBαℓ(a, x) −Bℓ(a, x)|,
with probability at least 1 −δ, where C = maxy∈{0,1},a∈{0,1} |u(y, a)|.
A.3
Learning from experiments evaluating a deterministic policy:
a generic form of value function
Below we state a generic form of the value function with access to experimental data as in
Section 4.5. The first line shows how to write the value of π in terms of the true CATE
36

````

## PDF page 37

FORMULA CHECK REQUIRED: original PDF page 37.

````text
τ ∗and the conditional expected outcome under the null action m∗(−1, x). The second line
further shows how to identify this expression with observable data via inverse probability
weighting.
Proposition A.1. If Z ⊥⊥Y (a) | X and 0 < e(x) < 1, then the expected utility can be
written as
V (π) = E
"X
a∈A
π(X, a){u(a)τ ∗(a, X) + c(a) + u(a)m∗(−1, X)}
#
= E
"X
a∈A
π(X, a)u(a) [˜π(X, a) (Γ(1, X, Y ) −Γ(0, X, Y )) + c(a) + u(a)Γ(0, X, Y )]
#
+ E
"X
a∈A
π(X, a)u(a) {1 −˜π(X, a)} τ ∗(a, X)
#
,
where Γ(Z, X, Y ) ≡Y {Z(1 −2e(X)) + e(X)}/{e(X)(1 −e(X))} is the inverse probability
weighted outcome.
Note that when the utility gain is constant, (u(a) = u for all a ∈A), we have that
E
"X
a∈A
π(X, a)u(a)m(−1, X)
#
= uE[m∗(−1, X)],
and does not depend on the policy, because P
a∈A π(X, a) = 1.
B
Proofs
Proof of Proposition 1.
V (˜π) = V inf(˜π) ≤V inf(πinf) ≤V (πinf).
Proof of Theorem A.1. Since V inf(π) ≤V (π) for all policies π, the regret is bounded by
V (π∗) −V (πinf) ≤V (π∗) −V inf(πinf)
= V (π∗) −V inf(π∗) + V inf(π∗) −V inf(πinf).
37

````

## PDF page 38

FORMULA CHECK REQUIRED: original PDF page 38.

````text
Now since πinf is a maximizer of V inf(π), V inf(π∗) −V inf(πinf) ≤0. Now note that for any π,
V (π) = E
"X
a∈A
π(X, a)˜π(X, A)(u(a)m∗(a, X) + c(a))
#
+ E
"X
a∈A
π(X, a)(1 −˜π(X, A))(u(a)m∗(a, X) + c(a))
#
= V (˜π) + E
"X
a∈A
π(X, a)(1 −˜π(X, A))(u(a)m∗(a, X) + c(a))
#
.
This yields that
V (π∗) −V (πinf) ≤
X
a∈A
u(a)E [π∗(X, a){1 −˜π(X, a)}m∗(a, X)]
−inf
f∈M
X
a∈A
u(a)E [π∗(X, a){1 −˜π(X, a)}f(a, X)]
≤sup
f∈M
(X
a∈A
u(a)E [π∗(X, a){1 −˜π(X, a)}f(a, X)]
)
−inf
f∈M
(X
a∈A
u(a)E [π∗(X, a){1 −˜π(X, a)}f(a, X)]
)
= |u|WM (π∗(1 −˜π)) .
Lemma B.1. Define ˆV (π) ≡ˆV (π, m∗) Then for any 0 < δ < e−1,
sup
π∈Π
|ˆV (π) −V (π)| ≤3C(K −1) max
a
Rn(Πa) + 5C(K −1)
r
1
n log K −1
δ
with probability at least 1 −δ, where C = maxy∈{0,1},a∈{0,1} |u(y, a)|.
Proof of Lemma B.1. First, since P
a∈A π(x, a) = 1 for all x, we can write the empirical
value as
ˆV (π) = 1
n
n
X
i=1
K−1
X
a=1
π(Xi, a) {u(a) [(˜π(Xi, a) −˜π(Xi, 0)) Yi
+ {1 −˜π(Xi, a)}m∗(a, Xi) −(1 −˜π(Xi, 0)m∗(0, Xi))] + c(a) −c(0)}
+ u(0) [˜π(Xi, 0)Yi + (1 −˜π(Xi, 0))m∗(0, Xi)] + c(0).
38

````

## PDF page 39

FORMULA CHECK REQUIRED: original PDF page 39.

````text
Now, define the function class with functions fa(x, y) as
Fa = {π(Xi, a) {u(a) [(˜π(Xi, a) −˜π(Xi, 0)) Yi + {1 −˜π(Xi, a)}m∗(a, Xi) −(1 −˜π(Xi, 0)m∗(0, Xi))]
+c(a) −c(0)} | π(Xi, a) ∈Πa} ,
where Πa = {1{π(·) = a} | π ∈Π} is the set of all potential policy assignments to action a.
Now notice that
sup
π∈Π
|ˆV (π) −V (π)| ≤EX,Y,ε
"
1
n
n
X
i=1
(u(0) [˜π(Xi, 0)Yi + (1 −˜π(Xi, 0))m∗(0, Xi)] + c(0))εi

#
+
K−1
X
a=1
sup
fa∈Fa

1
n
n
X
i=1
fa(Xi, Yi) −E [fa(X, Y )]
 .
The class Fa is uniformly bounded by twice the maximum absolute utility C = maxy∈{0,1},a∈{0,1} |u(y, a)|,
so by Theorem 4.5 in Wainwright (2019)
sup
fa∈Fa

1
n
n
X
i=1
fa(Xi, Yi) −E [fa(X, Y )]
 ≤2Rn(Fa) + t,
with probability at least 1 −exp

−nt2
8C2

. Now because
u(0) [˜π(Xi, 0)Yi + (1 −˜π(Xi, 0))m∗(0, Xi)] ≤u(0),
and by independence of the data points and ε, we can get the bound
EX,Y,ε
"
1
n
n
X
i=1
(u(0) [˜π(Xi, 0)Yi + (1 −˜π(Xi, 0))m∗(0, Xi)] + c(0))εi

#
≤
1
n

Eε


 n
X
i=1
(u(0) [˜π(Xi, 0)Yi + (1 −˜π(Xi, 0))m∗(0, Xi)] + c(0))εi
!2



1
2
= 1
n
 
E
" n
X
i=1
(u(0) [˜π(Xi, 0)Yi + (1 −˜π(Xi, 0))m∗(0, Xi)] + c(0))2ε2
i
#! 1
2
≤1
n
 n
X
i=1
(u(0) + c(0))2
! 1
2
= |u(0) + c(0)|
√n
≤2C
√n.
Furthermore, since Fa consists of compositions of functions g ∈Πa with linear functions
39

````

## PDF page 40

FORMULA CHECK REQUIRED: original PDF page 40.

````text
with a bounded slope,
|u(a) [(˜π(Xi, a) −˜π(Xi, 0)) Yi + {1 −˜π(Xi, a)}m∗(a, Xi) −(1 −˜π(Xi, 0)m∗(0, Xi))] + c(a) −c(0)| ≤3C,
we can use the Talagrand contraction principle (Theorem 4.12 Ledoux and Talagrand, 1991)
to bound the Rademacher complexity for Fa by
Rn(Fa) ≤3CRn(Πa).
Doing this for each a = 1, . . . , K −1 and using the union bound gives that
sup
π∈Π
|ˆV (π) −V (π)| ≤2C(K −1)
√n
+ 3C(K −1) max
a∈A Rn(Πa) + t
with probability at least 1 −(K −1) exp

−nt2
8C2

. Choosing t = C
q
8
n log K−1
δ
and noting
that 2(K −1) +
q
8 log K−1
δ
≤(2(K −1) +
√
8)
q
log K−1
δ
≤(2 +
√
8)(K −1)
q
log K−1
δ
≤
5(K −1)
q
log K−1
δ
gives the result.
Lemma B.2. For the empirical restricted model class c
Mn(α) and for a policy π ∈Π
ˆV inf(ˆπ) −ˆV (ˆπ) ≤sup
π∈Π
|h c
Mn(α) (−π(1 −˜π)u(·)) −hM (−π(1 −˜π)u(·)) |,
where the function (π(1 −˜π)u(·))(x, a) = π(x, a) ∗(1 −˜π(x, a))u(a). Furthermore, if M ⊆
c
Mn(α), then
ˆV inf(ˆπ) −ˆV (ˆπ) ≤0.
Proof of Lemma B.2. For a model class F, define ˜V (π, F) = inff∈F ˆV (π, f), and define
ˆV inf(π) = minm∈c
Mn(α) ˆV (π, m), so that ˆV inf(π) = ˜V (π, c
Mn(α)). This implies that
ˆV inf(ˆπ) −ˆV (ˆπ) ≤ˆV inf(ˆπ) −˜V (ˆπ, M)
= ˜V (ˆπ, c
Mn(α)) −˜V (ˆπ, M).
Now note that if M ⊆c
Mn(α), then ˜V (ˆπ, c
Mn(α)) −˜V (ˆπ, M) ≤0. Otherwise we can
40

````

## PDF page 41

FORMULA CHECK REQUIRED: original PDF page 41.

````text
write this difference as
˜V (ˆπ, c
Mn(α)) −˜V (ˆπ, M) =
inf
m∈c
Mn(α)
(
1
n
n
X
i=1
X
a∈A
π(Xi, a)(1 −˜π(Xi, a))u(a)m(a, Xi)
)
−inf
m∈M
(
1
n
n
X
i=1
X
a∈A
π(Xi, a)(1 −˜π(Xi, a))u(a)m(a, Xi)
)
= −
sup
m∈c
Mn(α)
(
−1
n
n
X
i=1
X
a∈A
π(Xi, a)(1 −˜π(Xi, a))u(a)m(a, Xi)
)
+ sup
m∈M
(
−1
n
n
X
i=1
X
a∈A
π(Xi, a)(1 −˜π(Xi, a))u(a)m(a, Xi)
)
= −h c
Mn(α)(−π(1 −˜π)u(·)) + hM(−π(1 −˜π)u(·))
Taking the supremeum over all possible policies ˆπ ∈Π gives the result.
Proof of Theorems 1 and A.2. The difference in values between ˜π and ˆπ is
V (˜π) −V (ˆπ) = V (˜π) −ˆV (˜π) + ˆV (˜π) −ˆV (ˆπ) + ˆV (ˆπ) −V (ˆπ)
≤2 sup
π∈Π
|ˆV (π) −V (π)| + ˆV (˜π) −ˆV (ˆπ)
We have bounded the first term in Lemma B.1. To bound the second term, notice that
ˆV (˜π) −ˆV (ˆπ) = ˆV inf(˜π) −ˆV (ˆπ)
= ˆV inf(˜π) −ˆV inf(ˆπ)
|
{z
}
≤0
+ˆV inf(ˆπ) −ˆV (ˆπ)
≤ˆV inf(ˆπ) −ˆV (ˆπ),
where we have used that ˆπ maximizes ˆV inf(π).
In Lemma B.2 we have bounded this difference. Combining the two bounds we have that
V (˜π) −V (ˆπ) ≤6C(K −1) max
a
Rn(Πa) + 10C(K −1)
r
1
n log K −1
δ
+ sup
π∈Π
|h c
Mn(α) (−π(1 −˜π)u(·)) −hM (−π(1 −˜π)u(·)) |,
with probability at least 1 −δ. And if M ⊆c
Mn(α), then we have the further bound
V (˜π) −V (ˆπ) ≤6C(K −1) max
a
Rn(Πa) + 10C(K −1)
r
1
n log K −1
δ
,
with probability at least 1 −δ. Noting that P(M ⊆c
Mn(α)) ≥1 −α, and taking the union
bound gives that this second bound holds with probability at least 1 −δ −α.
41

````

## PDF page 42

FORMULA CHECK REQUIRED: original PDF page 42.

````text
Proof of Theorems 2 and A.3. The regret of ˆπ relative to π∗is
V (π∗) −V (ˆπ) = V (π∗) −ˆV (π∗) + ˆV (π∗) −ˆV (ˆπ) + ˆV (ˆπ) −V (ˆπ)
≤sup
π∈Π
2|ˆV (π) −V (π)| + ˆV (π∗) −ˆV (ˆπ).
We have bounded the first term in Lemma B.1, and we now turn to the second term.
ˆV (π∗) −ˆV (ˆπ) = ˆV (π∗) −ˆV inf(ˆπ) + ˆV inf(ˆπ) −ˆV (ˆπ)
= ˆV (π∗) −ˆV inf(π∗) + ˆV inf(π∗) −ˆV inf(ˆπ)
|
{z
}
≤0
+ˆV inf(ˆπ) −ˆV (ˆπ)
≤ˆV (π∗) −ˆV inf(π∗) + ˆV inf(ˆπ) −ˆV (ˆπ),
where we have again used that ˆπ maximizes ˆV inf(π). We have bounded the second term in
Lemma B.2, now we turn to the first term:
ˆV (π∗) −ˆV inf(π∗) ≤1
n
n
X
i=1
X
a∈A
u(a)π∗(Xi, a){1 −˜π(Xi, a)}m∗(a, Xi)
−
inf
f∈c
Mn(α)
1
n
n
X
i=1
X
a∈A
u(a)π∗(Xi, a)){1 −˜π(Xi, a)}f(a, Xi)
≤
sup
f∈c
Mn(α)
1
n
n
X
i=1
X
a∈A
u(a)π∗(Xi, a)){1 −˜π(Xi, a)}f(a, Xi)
−
inf
f∈c
Mn(α)
1
n
n
X
i=1
X
a∈A
u(a)π∗(Xi, a)){1 −˜π(Xi, a)}f(a, Xi)
= |u|c
W c
Mn(α) (π∗(1 −˜π)) .
Combined with Lemmas B.1 and B.2 and the union bound this gives that
V (π∗) −V (ˆπ) = |u|c
W c
Mn(α) (π∗(1 −˜π)) + 6C(K −1) max
a
Rn(Πa) + 10C(K −1)
r
1
n log K −1
δ
+ |u| sup
π∈Π
|h c
Mn(α) (−π(1 −˜π)) −hM (−π(1 −˜π)) |,
with probability at least 1 −δ and
V (π∗)−V (ˆπ) = |u|c
W c
Mn(α) (π∗(1 −˜π))+6C(K−1) max
a
Rn(Πa)+10C(K−1)
r
1
n log K −1
δ
,
with probability at least 1 −δ −α. Noting that |u| ≤2C gives the result.
42

````

## PDF page 43

FORMULA CHECK REQUIRED: original PDF page 43.

````text
Proof of Corollary A.1 and A.2. These Corollaries follow from noting that
h c
Mn(α) (−π(1 −˜π)u(·)) −hM (−π(1 −˜π)u(·))
=1
n
n
X
i=1
π(Xi, a)(1 −˜π(Xi, a))u(a) bBαℓ(Xi, a) −1
n
n
X
i=1
π(Xi, a)(1 −˜π(Xi, a))u(a)Bℓ(Xi, a)
=1
n
n
X
i=1
π(Xi, a)(1 −˜π(Xi, a))u(a)( bBαℓ(Xi, a) −Bℓ(Xi, a))
≤C sup
x,a | bBαℓ(x, a) −Bℓ(x, a)|.
Proof of Proposition A.1. For the first equality, note that m∗(a, X) = τ ∗(a, X)+m∗(−1, X).
So the first equality follows by plugging in this equality to Equation (1). Next, note that we
can decompose this expression as in Equation (2) to get that
V (π, m∗) = E
"X
a∈A
π(X, a) {u(a) [˜π(X, a)˜τ(x) + {1 −˜π(X, a)} τ ∗(a, X)] + c(a) + u(a)m∗(−1, X)}
#
.
Now using that E[Γ(Z, X, Y ) | Z = z, X = x] = z · m∗(˜π(x), x) + (1 −z) · m∗(−1, x), and
noting that ˜τ(x) = E[Γ(1, X, Y ) −Γ(1, X, Y ) | X = x], gives the second expression.
C
Computation for restricted model classes
In this section, we show, in detail, how to compute the population and empirical model
classes in a variety of cases: no restrictions, Lipschitz functions, linear models, and additive
models.
First, for point-wise bounded model classes, we can compute the size term in Theorem 2
by looking for the policy π ∈Π that disagrees with the baseline policy ˜π when the upper
and lower bounds are farthest apart:
bS(bTn(α), Π; ˜π) = sup
π∈Π
1
n
n
X
i=1
X
a∈A
π(Xi, a)(1 −˜π(Xi, a))

bBαu(a, Xi) −bBαℓ(a, Xi)

.
(C.1)
C.1
No restrictions
Suppose that the conditional expectation has no restrictions, other than that it must lie
between L and U, i.e., F = {f | L ≤f(a, x) ≤U ∀a ∈A, x ∈X}. The restricted model
class M = {f ∈F | f(a, x) = ˜m(x) for a with ˜π(x) = a} provides no additional information
when the policy π disagrees with the baseline policy ˜π. The upper and lower bounds are
given by Bu(a, x) = ˜π(x, a) ˜m(x)+{1−˜π(x, a)}U and Bℓ(a, x) = ˜π(x, a) ˜m(x)+{1−˜π(x, a)}L,
respectively.
43

````

## PDF page 44

FORMULA CHECK REQUIRED: original PDF page 44.

````text
To construct the empirical model class c
Mn(α), we begin with a simultaneous 1 −α
confidence interval for the conditional expectation function ˜m(x), with lower and upper
bounds bCα(x) = [ bCαℓ(x), bCαu(x)] such that
P

˜m(x) ∈bCα(x) ∀x ∈X

≥1 −α.
(C.2)
See Srinivas et al. (2010); Chowdhury and Gopalan (2017); Fiedler et al. (2021) for examples
on constructing such simultaneous bounds via kernel methods in statistical control settings.
With this confidence band, we can use the upper and lower bounds of the confidence band
in place of the true conditional expectation ˜m(x), i.e.
bBαu(a, x) = ˜π(X, a) bCαu(x) + {1 −
˜π(X, a)}U and bBℓ(a, x) = ˜π(X, a) bCαℓ(x){1 −˜π(x, a)}L.
C.2
Lipschitz functions
We next consider the case where the covariate space X has a norm ∥· ∥, and that m(a, ·) is
a λa-Lipschitz function,
F = {f : A × X →R
|
|f(a, x) −f(a, x′)| ≤λa∥x −x′∥}.
Taking the greatest lower bound and least upper bound implied by this model class leads
to lower and upper bounds, Bℓ(a, x) = supx′∈˜
Xa { ˜m(x′) −λa∥x −x′∥}, and Bu(a, x) =
infx′∈˜
Xa { ˜m(x′) + λa∥x −x′∥}, where ˜
Xa = {x ∈X | ˜π(x) = a} is the set of covariates
with the baseline policy giving action a. The further we extrapolate from the area where the
baseline action ˜π(x) = a, the larger the value of ∥x −x′∥will be and so there will be more
ignorance about the values of the function.
The size of M will depend on the expected distance to the boundary between baseline
actions and the value of the Lipschitz constant. If most individuals are close to the boundary,
or the Lipschitz constant is small, M will be small and the safe policy will be close to optimal.
Conversely, a large number of individuals far away from the boundary or a large Lipschitz
constant will increase the potential for suboptimality.
To construct the empirical version, we again use a simultaneous confidence band bCα(x)
satisfying Equation (C.2). Then, the lower and upper bounds use the lower and upper con-
fidence limits in place of the function values, bBαℓ(a, X) = supx′∈˜
Xa
n
bCαℓ(x′) −λa∥X −x′∥
o
and bBαu(a, X) = infx′∈˜
Xa
n
bCαu(x′) −λa∥X −x′∥
o
. In our analysis of the NVCA flag thresh-
old in Section 5.2, the covariate space X is discrete, so we construct a simultaneous confidence
interval via the a Bonferroni correction on the 7 unique values.
Note that it is also possible to construct bounds using a finite set of evaluation points.
For example, if ˇ
Xa is a finite set of points such that the baseline policy satisfies ˜π(x) = a,
an alternative procedure to construct a lower bound is to take the greatest lower bound over
44

````

## PDF page 45

FORMULA CHECK REQUIRED: original PDF page 45.

````text
the finite set ˇ
Xa, i.e.
ˇBℓ(a, x) = max
x′∈ˇ
Xa
˜m(x′) −λa∥x −x′∥.
Because the finite set ˇ
Xa ⊆˜
Xa, the greatest lower bound over ˇ
Xa will be less than or equal
to the greatest lowest bound over the entire set ˜
Xa, i.e. ˇBℓ(a, x) ≥Bℓ(a, x). With this finite
set, we can create the empirical version using a simultaneous confidence band ˇCα(x) over
only ˇ
Xa that satisfies
P
 ˜m(x) ∈ˇCα(x) ∀x ∈ˇXa

≥1 −α.
Such a bound can be constructed with a simple Bonferroni correction, or via a more tailored
approach. Then the empirical lower bound would be ˇBαℓ(a, X) = maxx′∈ˇ
Xa
 ˇCαℓ(x′) −λa∥X −x′∥
	
.
Unlike in the population case, the empirical lower bound using the finite set, ˇBαℓ(a, x), may
be greater than the empirical lower bound using the simultaneous confidence band bBαℓ(a, x)
if the simultaneous confidence band over the entire set X is wider than that over the smaller,
finite set ˇXa.
C.3
Linear models
We next consider, as a model class, a linear model in a set of basis functions ϕ : A×X →Rd,
F = {f(a, x) = h−1(b⊤ϕ(a, x))}, where we still enforce the upper and lower bounds of U
and L. The restricted model class is the set of coefficients b that satisfy ˜m(x) = b⊤ϕ(a, x)
for all x and a such that ˜π(x) = a. With discrete covariates, this is a linear system of
equations. Slightly abusing notation, define ϕ(A, X) ∈Rp×dK as the matrix of values ϕ(a, x)
for the p unique combinations observable in the data, and ˜m ∈Rp as the corresponding
values of ˜m(x). If the model class is not point identified (e.g. if p < dK), then there will be
infinitely many solutions to the equation ˜m = ϕ(A, X)b. To characterize these, define β∗as
the minimum norm solution:
min
b∈Rd ∥b∥2
subject to ˜m = ϕ(A, X)b.
There will also be an unidentified component arising from the null space of the system of
linear equations, N = {b ∈Rd | ϕ(A, X)b = 0}. Let D ∈Rd×d⊥be an orthonormal basis for
this null space. Then, any solution to the linear equations ˜m = ϕ(A, X)b can be written as
the minimum norm solution β∗plus a vector in the null space, which we can write as DbN,
where bN are free parameters. Therefore, we can re-write the restricted model in terms of
these free parameters:
M = {f(a, x) = (β∗+ DbN)⊤ϕ(a, x)
|
bN ∈Rd⊥}.
45

````

## PDF page 46

FORMULA CHECK REQUIRED: original PDF page 46.

````text
Finding the worst-case value will involve a non-linear optimization over bN. Rather than
taking such an approach, we will consider a larger class M ≡{f
| Bℓ(a, x) ≤f(a, x) ≤
Bu(a, x)} that contains the restricted model class M. To construct it, we choose the upper
and lower bounds
Bℓ(a, x) = β∗⊤ϕ(a, x)1{D⊤ϕ(a, x) = 0} + 1{D⊤ϕ(a, x)̸ = 0}L,
Bu(a, x) = β∗⊤ϕ(a, x)1{D⊤ϕ(a, x) = 0} + 1{D⊤ϕ(a, x)̸ = 0}U.
For a given action a and covariate vector x, we first check whether ϕ(x, a) is in the null space
N by checking whether D⊤ϕ(a, x) = 0. If it is not in the null space (i.e. D⊤ϕ(a, x) = 0),
then the lower and upper bounds are equal, Bℓ(a, x) = Bu(a, x) = h−1(β∗⊤ϕ(a, x)) because
for any choice of free parameter bN, b⊤
ND⊤ϕ(a, x) = 0. In contrast, if ϕ(a, x) is in the null
space (i.e. D⊤ϕ(a, x)̸ = 0), then the free parameter is unrestrained and (β∗+ DbN)⊤ϕ(a, x)
can take on any value between L and U.
To construct the empirical model class we again begin with a simultaneous confidence
band, this time for the minimum norm prediction, β∗· ϕ(a, x) ∈[ bCαℓ(a, x), bCαu(a, x)] where
we apply a Bonferroni correction for the p unique observed values
β∗· ϕ(a, x) ∈ˆβ∗· ϕ(a, x) ± ˆσtn−p−1,1−α
2p
p
ϕ(a, x)⊤(Φ⊤Φ)†ϕ(a, x),
where ˆβ∗is the least squares estimate of the minimum norm solution, ˆσ2 is the estimate of
the variance from the MSE, Φ = [ϕ(˜π(xi), xi)]n
i=1 ∈Rn×d is the design matrix,tn−p−1,1−α
2p is
the is the 1 −α/p quantile of an t distribution n −p −1 degrees of freedom, and A† denotes
the pseudo-inverse of a matrix A. This gives lower and upper bounds,
bBαℓ(a, x) = max{L, bCαℓ(a, x)}1{D⊤ϕ(a, x) = 0} + L1{D⊤ϕ(a, x)̸ = 0},
bBαu(a, x) = min{U, bCαu(a, x)}1{D⊤ϕ(a, x) = 0} + U1{D⊤ϕ(a, x)̸ = 0},
where we enforce the constraint that the predictions must be between L and U post-hoc.
C.4
Additive models
If the model class for action a consists of additive models, we have
F =
(
f(a, x) =
d
X
j=1
fj(a, xj) +
X
j<k
fjk(a, (xj, xk)) + . . .
 fj(a, ·), fjk(a, ·), . . . , λa −Lipschitz
)
,
where the component functions fj(a, ·), fjk(a, ·), . . . can be subject to additional restrictions
so that the decomposition is unique. This additive decomposition formulation amounts to
an assumption that no interactions exist above a certain order.
By using the same additive decomposition for ˜m(x) into ˜m(x) = P
j ˜mj(Xj)+P
j<k ˜mjk(Xj, Xk)+
46

````

## PDF page 47

FORMULA CHECK REQUIRED: original PDF page 47.

````text
. . ., we can follow the same bounding approach as in Appendix C.2 for each of the compo-
nent functions. For example, for the additive term for covariate j, mj(a, xj), the Lipschitz
property implies that,
˜mj(x′
j) −λa|xj −x′
j| ≤mj(a, xj) ≤˜m(x′
j) + λa|xj −x′
j|
∀x′ ∈˜
Xa.
Taking the greatest lower bound and least upper bound for each component function, the
overall lower and upper bounds are,
Bℓ(a, X) =
X
j
sup
x′∈˜
Xa

mj(x′
j) −λa|Xj −x′
j|
	
+
X
j<k
sup
x′∈˜
Xa

mjk(x′
j, x′
k) −λa∥X(j,k) −x′
(j,k)∥
	
+ · · ·
Bu(a, X) =
X
j
inf
x′∈˜
Xa

mj(x′
j) + λa|Xj −x′
j|
	
+
X
j<k
inf
x′∈˜
Xa

mjk(x′
j, x′
k) + λa∥X(j,k) −x′
(j,k)∥
	
+ · · · ,
(C.3)
where x(j,k) is the subvector of components j and k of x. Unlike in Appendix C.2, this
extrapolates covariate by covariate, finding the tightest bounds for each component. For
instance, for a first-order additive model, the level of extrapolation depends on the distance
in each covariate |xj −x′
j| separately.
To construct the empirical model class for the class of additive models, we use a 1 −α
confidence interval that holds simultaneously over all values of x and for all components, i.e.,
˜mj(xj) ∈bC(j)
α (xj), mjk(xj, xk) ∈bC(j,k)
α
(xj, xk), . . . , ∀j = 1, . . . , d, k < j, . . . ,
with probability at least 1 −α. Analogous to the Lipschitz case in Appendix C.2 above, we
can then construct the lower and upper bounds using the lower and upper bounds of the
confidence intervals,
bBαℓ(a, X) =
X
j
sup
x′∈˜
Xa
n
bC(j)
αℓ(x′
j) −λ|Xj −x′
j|
o
+
X
j<k
sup
x′∈˜
Xa
n
bC(j,k)
αℓ(x′
j, x′
k) −λ∥X(j,k) −x′
(j,k)∥
o
+ . . .
Bαu(a, X) =
X
j
inf
x′∈˜
Xa
n
bC(j)
αu(x′
j) + λ|Xj −x′
j|
o
+
X
j<k
inf
x′∈˜
Xa
n
bC(j,k)
αu (x′
j, x′
k) + λ∥X(j,k) −x′
(j,k)∥
o
+ . . . .
D
Incorporating human decision-making
The PSA-DMF system we study is an example of a “human-in-the-loop” framework: rather
than an algorithmic policy being the final arbiter of decisions, the policy merely provides
recommendations to a human that makes an ultimate decision (Imai et al., 2023; Ben-Michael
et al., 2024). In this section, we formalize and extend the potential outcomes framework to
incorporate human decisions, and then briefly explore how our framework can be extended
to explicitly model human decisions and apply it to learn a new NVCA system.
47

````

## PDF page 48

FORMULA CHECK REQUIRED: original PDF page 48.

````text
D.1
Potential human decisions and potential outcomes
We first show how to extend our framework to incorporate human decisions. Let Di(a) ∈
{0, 1} be the potential (binary) decision for individual i under action a ∈A (an algorithmic
recommendation in our application), and Yi(d, a) ∈{0, 1} be the potential (binary) outcome
for individual i under human decision d ∈{0, 1} and algorithmic action a ∈A. This setup
nests our main framework. To see this, note that we can re-define the the potential outcome
under algorithmic action a as the potential outcome when the algorithmic action is set to a
and the human decision is the natural value under algorithmic action a:
Yi(a) ≡Yi(Di(a), a) = Yi(0, a)(1 −D(a)) + Yi(1, a)D(a).
If the human decision under algorithmic action a is D(a) = 0, then the potential outcome
under algorithmic action a is Yi(a) = Yi(0, a).
Conversely, if the human decision under
algorithmic action a is D(a) = 1, the potential outcome under algorithmic action a is Yi(a) =
Yi(1, a).
Then, the observed decision is given by Di = D(˜π(Xi)) whereas the observed
outcome is Yi = Yi(˜π(Xi)) = Yi(Di(˜π(Xi)), ˜π(Xi)).
Finally, we denote the expected potential human decision under algorithmic action a,
conditional on covariates x, as d(a, x) = E[D(a) | X = x] and represent the conditional
expectation of the potential outcome under algorithmic action a, conditional on covariates
x, as m(a, x) = E[Y (a) = 1 | X = x].
D.2
Incorporating human decisions into the utility function
To incorporate human decisions into the utility function, we write the utility for outcome y
under human decision d as u(y, d). With this setup, the value for a policy π is:
V (π) = E
"X
a∈A
π(X, a)
1
X
d=0
[u(1, d)Y (d, a) + u(0, d)(1 −Y (d, a))] 1{D(a) = d}
#
.
If we make the simplifying assumption that the utility gain is constant across decisions,
i.e., u(1, d) −u(0, d) = u for d ∈{0, 1}, we can index the utility for y = 0 and d = 0 as
u(0, 0) = 0, and denote the added cost of taking decision 1 as c = u(0, 1) −u(0, 0). This
allows us to write the value by marginalizing over the potential decisions, yielding,
V (π) = E
"X
a∈A
π(X, a) (uY (a) + cD(a))
#
.
(D.1)
Comparing Equation (D.1) to the value in Equation (2) when actions are taken directly,
we see that the key difference is the inclusion of the potential decision D(a) in determining
the cost of an action. Rather than directly assigning a cost to an action a, there is an indirect
48

````

## PDF page 49

FORMULA CHECK REQUIRED: original PDF page 49.

````text
cost associated with the eventual decision D(a) that action a induces in the decision maker.
Therefore, the unidentifiability of the expected potential decision under an action given the
covariates, d(a, x), also must enter the robustness procedure.
We can treat the unidentifiability of the potential decisions in a manner parallel to the
outcomes. Denoting the conditional expected observed decision as d(˜π(x), x) = E[D | X =
x], we can posit a model class for the decisions F′ and create the restricted model class
D = {f ∈F′ | f(˜π(x), x) = d(˜π(x), x)}.8 We can now construct a population safe policy by
maximizing the worst case value across the model classes for both the outcomes M and the
decisions D,
max
π∈Π
(
E
"X
a∈A
π(X, a)˜π(X, a)uY
#
+ min
f∈M E
"X
a∈A
π(X, a){1 −˜π(X, a)}uf(a, X)
#
+E
"X
a∈A
π(X, a)˜π(X, a)cD
#
+ min
g∈D E
"X
a∈A
π(X, a){1 −˜π(X, a)}cg(a, X)
#)
.
(D.2)
By allowing for actions to affect decisions through the decision maker rather than directly,
the costs of actions are not fully identified. Therefore, we now find the worst-case expected
outcome and decision when determining the worst case value in Equation (D.2). In essence,
we solve the inner optimization twice: once over outcomes for the restricted outcome model
class M and once over decisions for the restricted decision model class D.
From here, we can follow the development in the previous sections. We create empirical
restricted model classes for the outcome and decision functions, c
Mn(α/2) and bDn(α/2) using
a Bonferonni correction so that P(M ∈c
Mn(α/2), D ∈bDn(α/2)) ≥1 −α. Then, we solve
the empirical analog to Equation (D.2). Finally, we can incorporate experimental evidence as
above. In this case, the conditional expected potential decision d(a, x) and outcome m(a, x)
— and their model classes — are replaced with the conditional average treatment effect on
the decision E[D(a) −D(−1) | X = x] and on the outcome τ(a, x).
D.3
Learning a new NVCA point system
In Section 5, we only considered the outcomes of triggering the NVCA flag and have assigned
costs directly to the flag. However, the PSA serves as a recommendation to the presiding
judge who is the ultimate decision maker. Following the discussion above, we can incorporate
this into the construction of the robust policy. Rather than place a cost on triggering the
NVCA flag, we use the judge’s binary decision of whether to assign a signature bond or cash
bail and place a cost of −1 to assigning cash bail. Unlike the cost directly placed on the
NVCA flag, this allows us to address the cost of cash bail decision. As discussed in Section 5,
8These restrictions being on the decisions gives more opportunities for structural restrictions on the
model. For example, we could make a monotonicity assumption that d(a, x) ≤d(a′, x) for a ≤a′.
49

````

## PDF page 50

FORMULA CHECK REQUIRED: original PDF page 50.

````text
the cost of the judge’s decision to assign cash bail includes the fiscal and socioeconomic costs,
indexed to be −1.
Following the same analysis as in Section 5, we find maximin policies that take the
decisions into account for increasing costs of an NVCA relative to assigning cash bail, at
various confidence levels. For the additive and second order effect models, however, we find
policies that differ from the original rule only when we do not take the statistical uncertainty
into account — with confidence level 1 −α = 0 — and have no finite sample guarantee that
the new policy is not worse than the existing rule. In this case, the policy is extremely
aggressive, responding to noise in the treatment effects. Otherwise, we cannot find a new
policy that safely improves on the original rule. This is primarily because the overall effects
of the PSA on both the judge’s decisions and defendant’s behavior are small (Imai et al.,
2023). Therefore, there is too much uncertainty to ensure that a new policy would reliably
improve upon the existing rule.
E
Imputation, IPW, and double robust methods
Here we briefly discuss how standard approaches to policy learning are not applicable in our
setting. First, as discussed in Section 3.2, the key identification issue is that we can cannot
point-identify the conditional expectation of the potential outcome m∗(a, x) = E[Y (a) | X =
x] for all pairs of actions a and covariates x. In settings with overlap (P(A = a | X = x) > 0
for all a ∈A and x ∈X), and unconfounded action assignment (A ⊥⊥{Y (0), Y (1), . . . , Y (K−
1)} | X), we can identify m∗(a, x) via the conditional expectation of the observed outcome
given the action and the covariate ˜m(a, x) ≡E[Y | A = a, X = x]. In such settings, we could
then identify the value V (π) using model-based imputation, IPW, or augmented IPW:
V (π, m∗) = E
"X
a∈A
π(X, a){u(a) ˜m(a, X) + c(a)}
#
(Imputation)
= E
"X
a∈A
π(X, a)

u(a)
1{A = a}
P(A = a | X)Y + c(a)
#
(IPW)
= E
"X
a∈A
π(X, a)

u(a)

˜m(a, X) +
1{A = a}
P(A = a | X)(Y −m(a, X))

+ c(a)
#
(AIPW)
In our setting, where the observed actions are the actions under the deterministic baseline
policy Ai = ˜π(Xi), the actions are unconfounded given the covariates X (indeed, we know
exactly how the actions are assigned), but there is no overlap because P(A = a | X) =
P(˜π(X) = a | X) is either 0 or 1. The implication is that the outcome model m∗(a, x) is not
point identifiable. It is impossible to estimate the conditional expectation of the observed
outcome given A = a and X = x, ˜m(a, x), if a̸ = ˜π(x) because it is an event of measure zero
50

````

## PDF page 51

FORMULA CHECK REQUIRED: original PDF page 51.

````text
(i.e. P(A̸ = ˜π(X)) = 0).
Nonetheless, we may try to use the imputation approach by estimating a model ˆm(a, x)
and relying on it for extrapolation. We would then solve
ˆπimpute ∈max
π∈Π
1
n
n
X
i=1
X
a∈A
π(Xi, a) {u(a) (˜π(Xi, a)Y + (1 −˜π(Xi, a)) ˆm(a, Xi)) + c(a)} . (E.1)
This imputation-based policy will be highly sensitive to how the estimated model ˆm(a, Xi)
extrapolates to combinations of a and x that are not possible under the baseline policy, as
we show via simulation in Section F.
The identification problem is more transparent for the IPW and AIPW-based approaches.
Note that the inverse probability term with a deterministic baseline policy is 1{A = a}/˜π(a, Xi),
which is equal to ˜π(a, Xi)/˜π(a, Xi). If ˜π(a, Xi) = 1, then this term is equal to 1, but if
˜π(a, Xi) = 0, it is 0/0, which is undefined. Again, we may nonetheless try to use IPW by
setting 0/0 = 0. This would give:
ˆπipw ∈max
π∈Π
1
n
n
X
i=1
X
a∈A
π(Xi, a) {u(a)˜π(Xi, a)Y + c(a)} .
As long as u(a) > c(a), then defining the IPW-based policy in this way will give that
ˆπipw = ˜π, and so we will always keep the baseline policy.
Finally, we might try to consider the AIPW estimator, again setting 0/0=0, but note
that
ˆm(a, Xi) + ˜π(Xi, a)(Yi −ˆm(a, Xi)) = ˜π(Xi, a)Yi −(1 −˜π(Xi, a)) ˆm(a, Xi),
and so the AIPW approach would recover the model-based imputation approach.
F
Simulation study
We have a single discrete covariate with 10 levels, x ∈{0, . . . , 9}, and a binary action so
that the action set is A = {0, 1}. We choose a baseline policy ˜π = 1{x ≥5}, and set the
utility gain to be u(0) = u(1) = 10 and the costs to be c(0) = 0, c(1) = −1, so that action 0
is costless and action 1 costs one tenth of the potential utility gain. For each simulation we
draw n i.i.d. samples X1, . . . , Xn uniformly on {0, . . . , 9}. Then we draw a smooth model
for the expected control potential outcome m(0, x) ≡E[Y (0) | X = x] via random Fourier
features. We draw three random vectors: ω ∈R100 with i.i.d. standard normal elements;
b ∈R100 with i.i.d. components drawn uniformly on [0, 2π]; and β ∈R100 with i.i.d. standard
normal elements. Then we set
m(0, x) = logit−1
 r
2
100β · cos

ωx
9 + b
!
,
51

````

## PDF page 52

FORMULA CHECK REQUIRED: original PDF page 52.

````text
where the cosine operates element-wise. See Rahimi and Recht (2008) for more discussion
on random features. For the potential outcome under treatment, m(1, x) = E[Y (1) | X = x],
we add a linear treatment effect on the logit scale:
m(1, x) = logit−1

logit (m(0, x)) + 1
2

x −9
2

−8
10

.
We then generate the potential outcomes Yi(0), Yi(1) as independent Bernoulli draws with
probabilities m(0, Xi) and m(1, Xi), respectively.
With each simulation draw, we consider finding a safe empirical policy by solving Equa-
tion (7) under a Lipschitz restriction on the model as in Appendix C.2 and with the threshold
policy class Πthresh. Note that the true model is in fact much smoother than Lipschitz; here
we consider using the looser assumption. Following our empirical analysis in Section 5.2,
we take the average outcome at each value of x, and compute the largest difference in con-
secutive averages as pilot estimates for the Lipschitz constants λ0 and λ1. We then solve
Equation (7) using 1
2, 1, and 2 times these pilot estimates as the Lipschitz constants, and
setting the significance level to 0, 80% and 95%.
We also consider using a model-based imputation estimator without accounting for partial
identification. Because the baseline policy assigns 0 for x ∈{0, 1, 2, 3, 4} and 1 for x ∈
{5, 6, 7, 8, 9}, there are 5 unique values of the covariate when ˜π(x) is 0 or 1. Therefore, we fit
two separate non-parametric models for ˆm(0, x) and ˆm(1, x) by fitting a logistic regression
of Y on X with a degree four polynomial of X. This creates 5 parameters for each model,
one for each unique observed data point. We then use each estimated 4-degree polynomial
logistic regression model to extrapolate ˆm(0, x) for x ≥5 and ˆm(1, x) for x < 5 and estimate
an imputation-based policy ˆπimpute solving Equation (E.1). We additionally compute the
oracle threshold policy that uses the true model values m(0, x) and m(1, x). We do this for
sample sizes n ∈(500, 1000, 1500, 2000).
Figure F.1 shows how the empirical safe policy ˆπ and the model-based imputation policy
ˆπimpute compare to both the baseline policy ˜π and the oracle policy π∗in terms of expected
utility. First, we see that on average, the empirical safe policy improves over the baseline, no
matter the confidence level and the choice of Lipschitz constant. This improvement is larger
the less conservative we are, e.g. by choosing a lower confidence level or a smaller Lipschitz
constant. Furthermore, as the sample size increases, the utility of the empirical safe policy
also increases due to a lower degree of statistical uncertainty. We find similar behavior when
comparing it to the oracle policy. Less conservative choices lead to lower regret, and the
regret decreases with the sample size. Importantly, the regret does not decrease to zero;
even when removing all statistical uncertainty the safe policy can still be suboptimal due to
the lack of identification.
52

````

## PDF page 53

FORMULA CHECK REQUIRED: original PDF page 53.

````text
Figure F.1: Monte Carlo simulation results as the sample size n increases, varying the
multiplicative factor on the empirical Lipschitz constant and the significance level 1 −α.
The left panel shows the difference in the expected utility between the empirical safe policy
ˆπ, and the baseline policy ˜π, normalized by the regret of the baseline relative to the oracle,
i.e.
V (ˆπ)−V (˜π)
V (π∗)−V (˜π). The right panel shows the regret of the safe policy relative to the oracle,
scaled by the regret of the baseline relative to the oracle, i.e. V (π∗)−V (ˆπ)
V (π∗)−V (˜π). In both panels, the
grey dashed line represents the imputation-based policy.
In contrast, model-based imputation without accounting for identification issues performs
poorly, yielding a policy that has much lower expected utility than the baseline, let alone
the oracle. This is because the extrapolation to unseen data does not perform well with the
modeling approach that we used. It could have been possible to choose an imputation esti-
mator that performs better in that the extrapolation proved to be correct. However, for any
imputation estimator we can come up with an adversarial example where the extrapolation
is incorrect and leads to a worse policy than the status quo. Indeed, this is precisely what
the maximin criterion is designed to defend against.
G
Additional empirical results
In this section, we present additional empirical results for the FTA, NCA, and NVCA scores,
as well as the results for the combined bail level and monitoring conditions recommendation.
For reference, Table G.1 displays the existing risk-factor weights for the FTA, NCA, and
NVCA risk scores.
G.1
Additional results for the NVCA threshold and score
We begin by presenting the results regarding the NVCA threshold. Figure G.1 shows how
the maximin threshold changes as we vary the confidence level 1−α while setting C = 3. The
overall relationship between the threshold and the cost is robust to the choice of confidence
level. The results show that when the cost of an NVCA is low and/or the confidence level is
53

````

## PDF page 54

FORMULA CHECK REQUIRED: original PDF page 54.

````text
Risk factor
FTA
NCA
NVCA
Current violent offense
> 20 years old
2
≤20 years old
3
Pending charge at time of arrest
1
3
1
Prior conviction
misdemeanor or felony
1
1
1
misdemeanor and felony
1
2
1
Prior violent conviction
1 or 2
1
1
3 or more
2
2
Prior sentence to incarceration
2
Prior FTA in past 2 years
only 1
2
1
2 or more
4
2
Prior FTA older than 2 years
1
Age
22 years or younger
2
Table G.1: Weights placed on risk factors to construct the failure to appear (FTA), new
criminal activity (NCA), and new violent criminal activity (NVCA) scores. The sum of
the weights is then thresholded into six levels for the FTA and NCA scores and a binary
“Yes”/“No” for the NVCA score.
low the learned safe policy will raise the threshold, implying that fewer arrestees will trigger
the NVCA flag.
Figure G.2 shows estimates of the effect of providing the PSA on whether the judge
makes a cash bail decision, and on whether the arrestee engages in an NVCA, conditioned
on the number of total NVCA points. We find that when the NVCA flag is not triggered
(i.e. xnvca < 4) there is little to no effect of providing the PSA on either the judge’s decision
or the presence of an NVCA. This appears to remain true when xnvca = 4, even though the
flag is triggered. For xnvca ≥5, providing the PSA increases the proportion of decisions
that are cash bail by over 30 percentage points (though this is not significant for xnvca = 6.)
However, NVCAs do not meaningfully change for xnvca = 5, even though there are over 30
percentage points more cash bail decisions, but they decrease for xnvca = 6.
Next, we present several additional empirical results for the NVCA threshold and score.
Second order effect model and model testing.
First, Figure G.3a shows how the
maximin NVCA flag differs from the original rule as the cost of an NVCA and the confidence
level vary under the second order effect model. We find that under the second order effect
model, there is too much uncertainty to safely deviate from the original NVCA flag rule with
any reasonable degree of confidence if the cost of an NVCA is greater than 1. This is in
contrast to the results under the additive effect model shown in Figure 4a; the addition of
unidentifiable second order interaction terms precludes safely changing the policy.
To understand whether the additive effects assumption is reasonable for the NVCA rule,
54

````

## PDF page 55

FORMULA CHECK REQUIRED: original PDF page 55.

````text
0%
10%
20%
30%
40%
50%
60%
70%
80%
90%
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
Cost of NVCA
Confidence Level 1 − α
Threshold Value
4
6
7
Figure G.1: Learned threshold values solving Equation (7) for the NVCA flag threshold rule
as the cost of an NVCA increases from 1 to 20 times the cost of triggering the NVCA flag,
and the confidence level varies between 0% and 90%.
we estimate the CATE separately for arrestees with and without the NVCA flag triggered via
a similar spirit to the DR-learner (Kennedy, 2022) by regressing the IP-weighted outcomes
Γ(1, X, Y ) −Γ(0, X, Y ) on the 7 binary risk factors and all observed pair-wise interactions.
Note that this partial second order model is point identified because it omits the unidentified
terms and so it is only a rough proxy for the full second order model. We then test whether
the interaction terms are all zero using a Wald test with Huber-White heteroskedastic robust
standard errors. We do not find evidence against the null of the additive model for cases
where the flag is not triggered (p = 0.75), but there is some evidence for the existence of
interactions when the flag is triggered (p = 0.067).
Using a quadratic cost.
We consider an alternative value function that assigns a larger
marginal utility loss to triggering the NVCA flag for an arrestee if a larger proportion of
arrestees have the flag triggered. Formally, defining ¯π ≡E[π(X)], the policy value function
is given by:
V quad(π) ≡E [π(X) {u × (m∗(1, X) −m∗(0, X)) −(1 + ζ¯π)}] + E[m∗(0, X)].
This induces a quadratic cost, with ζ determining the additional marginal penalization
per percent flagged as an NVCA risk. Note that this value function is not an expectation
of individual utilities, because the cost of flagging one individual for NVCA risk depends on
how many other individuals are also flagged. As with the cost of an NVCA u, it is beyond
the scope of this paper to argue for a particular value of the quadratic penalty term ζ, and so
55

````

## PDF page 56

FORMULA CHECK REQUIRED: original PDF page 56.

````text
0%
30%
60%
2
4
6
Total NVCA Points
Effect of Providing PSA
Cash Bail Decision
No NVCA
Figure G.2: The effect of providing the PSA on (a) whether the judge makes a cash bail de-
cision and (b) whether the arrestee does not engage in an NVCA, conditioned on the number
of total NVCA points. Error bars indicate 95% confidence intervals using heteroskedastic
robust standard errors. The vertical dashed line represents the existing NVCA threshold.
(a) Second order effect model class
0%
25%
50%
75%
5
10
15
Cost of NVCA
Confidence Level 1 − α
Change in % flaged for NVCA risk (pp)
−12%
−10%
−8%
−5%
−2%
(b) Using all risk factors in Table G.1
0%
25%
50%
75%
5
10
15
Cost of NVCA
Confidence Level 1 − α
Change in % flaged for NVCA risk (pp)
0%
20%
40%
60%
Figure G.3: The percentage point difference in the proportion of arrestees flagged for NVCA
risk between the maximin policy and the original NVCA score as the cost of an NVCA
increases from 1 to 15 times of the cost of triggering the NVCA flag and the confidence level
varies between 0% and 100% (a) in the second order effect model class and (b) under the
additive effect model class using all risk factors in Table G.1.
56

````

## PDF page 57

FORMULA CHECK REQUIRED: original PDF page 57.

````text
0%
25%
50%
75%
100%
5
10
15
Cost of NVCA
Quadratic Cost Term
Change in % flaged for NVCA risk (pp)
−16%
−12%
−8%
−4%
Figure G.4: The percentage point difference in the proportion of arrestees flagged for NVCA
risk between the maximin policy and the original NVCA score as the cost of an NVCA
increases from 1 to 15 times of the cost of triggering the NVCA flag as ζ varies with a
confidence level of 80%.
we will document how the policy changes as it varies. Note that other forms of such utilities
are possible, for example, we could consider a step function that adds an additional penalty
if the number of arrestees flagged as an NVCA risk exceeds some threshold.
Figure G.4 shows how the maximin rule compares to the original rule, again in terms of
the the performance of the maximin proportion of arrestees flagged for an NVCA risk as we
vary both u and ζ while keeping the confidence level fixed to 1 −α = 80%. For any given
cost of an NVCA, the maximin policy triggers the flag less often as the quadratic penalty
increases.
Figure G.5 shows the integer weights on the risk factors for the maximin policy at the
1 −α = 80% level as the quadratic penalty ζ increases with the cost of an NVCA set to 9.
Increasing the quadratic penalty eventually changes the maximin policy back to placing less
weight on violent convictions and offenses, similar to the results when we only vary the cost
of an NVCA and keep ζ = 0 (e.g. in Figure 4b).
Using the full set of risk factors.
We also consider learning a new NVCA flag rule that
incorporates the full set of risk factors listed in Table G.1. The scale of the weight placed
on each factor is not necessarily meaningful for comparisons across rules that use different
risk factors and thresholds. For this reason, we place an upper bound on the weights of 5.
Figure G.3b shows how the resulting maximin rules differ from the original NVCA flag
rule, again as the cost of an NVCA and the confidence level vary under the additive effect
57

````

## PDF page 58

FORMULA CHECK REQUIRED: original PDF page 58.

````text
model, with a quadratic penalty term of zero, i.e., ζ = 0. We find broadly similar results
as when using the original reduced set of risk factors. For all confidence levels at lower
NVCA costs, the maximin rule classifies fewer arrestees as NVCA risks, eventually collapsing
back to the status quo as the cost of an NVCA relative to the cost of triggering the flag
increases. Relative to the reduced covariate set, including more risk factors increases the
level of statistical uncertainty, and so the maximin rule collapses back to the original rule
more quickly.
Relative to the reduced covariate set, including more risk factors increases the level of
statistical uncertainty, and so the maximin rule collapses back to the original rule more
quickly. In addition, at a confidence level of 0%, the learned NVCA flag rule eventually
begins to flag far more arrestees as NVCA risks than the original rule as the cost of an
NVCA increases. However, because more risk factors are included, even when the maximin
policy does not differ from the baseline in terms of which arrestees it triggers the flag for,
the underlying risk factor weights can be different, as multiple combinations of weights can
produce the same recommendations. Figure G.6 shows the set of weights found during the
optimization problem with a confidence level of 80%, but as the solutions are not unique and
the scales arbitrary, these weights are not directly comparable to the other sets of results.
2
1
1
1
1
1
2
2
0
1
1
1
1
2
2
0
1
1
1
1
2
2
0
1
1
1
1
2
2
0
1
1
1
1
2
2
0
1
1
1
1
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
1
1
1
1
0
0
2
0% 7%14%21%29%36%43%50%57%64%71%79%86%93%100%
Three or more prior violent convictions
Two prior violent convictions
One prior violent conviction
Prior conviction (felony or misdemeanor)
Pending Charge at time of arrest
Current violent offense and 20 years old or younger
Current violent offense
Quadratic cost term
Difference from original weights
−2
−1
0
1
2
Figure G.5: NVCA flag weights θ in Equation (G.2). Change in θ as the quadratic penalty
ζ increases from 0 to with a cost an NVCA equal to 9 and a confidence level of 80% (right
panel).
58

````

## PDF page 59

FORMULA CHECK REQUIRED: original PDF page 59.

````text
4
1
0
0
0
0
0
0
0
5
0
1
0
2
0
0
0
0
2
0
1
5
1
3
4
1
1
0
0
3
5
0
1
3
1
1
3
1
0
0
0
0
5
0
1
2
4
0
4
1
0
0
0
1
5
1
2
3
4
1
2
2
1
1
3
0
5
1
1
0
5
1
0
2
1
1
3
0
5
1
1
0
5
1
0
2
1
0
3
3
5
1
1
1
5
1
3
2
2
0
2
3
5
0
0
1
5
2
3
2
2
0
2
3
5
0
0
1
5
2
1
2
2
0
2
3
5
0
0
1
5
1
3
2
2
0
2
3
5
0
0
1
5
1
1
2
2
0
2
3
4
0
0
1
5
1
1
2
2
0
2
3
5
0
0
1
5
1
1
2
2
0
2
3
4
0
0
1
5
1
101010 8 1010 8 8 1010 8 10 8 8 8
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15
Current violent offense and 20 years old or younger
Current violent offense
Prior Sentence to Incarceration
2 or More Prior FTA in Past 2 Years
1 Prior FTA in Past 2 Years
Three or more prior violent convictions
Two prior violent convictions
One prior violent conviction
Prior Felony Conviction
Prior Misdemeanor Conviction
Pending Charge at time of arrest
Age below 23
Threshold
Cost of NVCA
Weight placed on risk factor
0
1
2
3
4
5
Figure G.6: Change in the NVCA flag weights θ using all of the risk factors in Table G.1 as
the cost of an NVCA increases from 1 to 15 times the cost of triggering the NVCA flag, at
a confidence level of 1 −α = 80% and no quadratic penalty ζ = 0 .
G.2
Additional results for the FTA and NCA scores
Next, we present additional empirical results for the FTA and NCA scoring systems. We
begin by formalizing the FTA and NCA policy classes as follows:
Π =
(
π(x) =
K−1
X
a=1
a1 {ηa−1 < θ · x ≤ηa}
 θ ∈Zd, ηa > ηa−1 ≥0 ∀a ∈{1, 2, . . . , K −1}
)
,
where x are the corresponding risk factors in either the FTA or NCA rule, θ are the integer
weights placed on the risk factors, and η0, . . . , ηK−1 are thresholds that determine what the
final score is. For example, the baseline FTA rule has thresholds (0, 1, 2, 4, 6, 7) and the
baseline NCA rule has thresholds (0, 2, 4, 6, 8, 13).
There are K = 6 possible actions for the FTA and NCA scores, each giving scores between
1 and 6. Indexing the cost of the first action to be zero, we must characterize the cost of the
remaining 5 actions. There are many potential ways to do so. However, recall from Figure 3
that there is little information to extrapolate from the NCA score and none for the FTA
score, so we do not expect to be able to learn maximin policies that are different from the
status quo here. Therefore, we extend our utility function from the binary case to a simple
linear parameterization of the costs, writing the utility function as u(y, a) = u × y −a where
|u| is the cost of either an FTA or an NCA depending on the risk score. This utility function
and these costs are not directly comparable to the binary utility function for the NVCA flag,
because the cost for choosing the highest score is indexed to 5 rather than 1 as in the binary
59

````

## PDF page 60

FORMULA CHECK REQUIRED: original PDF page 60.

````text
(a) FTA Score
0%
25%
50%
75%
5
10
15
Cost of FTA
Confidence Level 1 − α
Average Change in FTA Score
−1
0
1
(b) NCA Score
0%
25%
50%
75%
5
10
15
Cost of NCA
Confidence Level 1 − α
Average Change in NCA Score
−2.0
−1.5
−1.0
−0.5
Figure G.7: The average difference in (a) the FTA score and (b) the NCA score for arrestees
under the maximin policy and the original FTA and NCA scores as the cost of an FTA (left
panel) and NCA (right panel) increases from 1 to 15 and the confidence level varies between
0% and 100%.
case.9 We note that it is straightforward to encode different cost structures.
Figure G.7 shows how the maximin FTA and NCA scores differ from the original rules
as we vary the cost of an FTA or NCA and the confidence level 1 −α. Overall, we find
that with any degree of statistical confidence, if the cost of an FTA or NCA is above 2, the
maximin rule collapses to the status quo rule. This is not surprising given the discussion in
Section 5.3.
It may be possible, however, to learn simplified versions of the FTA and NCA scores that
are collapsed into low and high risk. To inspect this, we create truncated versions of the
scores that are indicators for whether the scores are greater than or equal to 4. Figure G.8
shows the sizes of the resulting model classes with respect to the truncated policy classes for
both the additive and second order effect models as the confidence level varies, keeping the
NVCA flag for comparison. We find that truncating the scores leads to much smaller model
classes. This suggests that it might be possible to learn maximin policies that deviate from
the status quo.
We learn such maximin policies using the binary utility function used for the NVCA, and
truncating the policy class to output either a low or high risk. Figure G.9 shows how the
resulting truncated scores differ from the original truncated scores under the additive effect
9Recall that we index the first action to be a = 0.
60

````

## PDF page 61

FORMULA CHECK REQUIRED: original PDF page 61.

````text
Additive Effect Model
Second Order Effect Model
0%
25%
50%
75%
100%0%
25%
50%
75%
100%
0%
25%
50%
75%
100%
Confidence Level 1 − α
Size of model class
Risk Score
FTA (truncated)
NCA (truncated)
NVCA
Figure G.8: The size (as a percentage of its maximum value) of two different model classes
with respect to the linear threshold policy class versus the confidence level 1−α for the FTA
(green) and NCA (orange), both truncated into an indicator for high risk (score greater than
or equal to 4) and NVCA (purple) scoring rules.
(a) FTA Score (truncated)
0%
25%
50%
75%
5
10
15
Cost of FTA
Confidence Level 1 − α
Change in % flaged for FTA risk
−20%
0%
20%
40%
(b) NCA Score (truncated)
0%
25%
50%
75%
5
10
15
Cost of NCA
Confidence Level 1 − α
Change in % flaged for NCA risk
−40%
−30%
−20%
−10%
0%
Figure G.9: The percentage point difference in the proportion of arrestees flagged for (a)
FTA risk and (b) NCA risk under the maximin policy and the original FTA and NCA scores
truncated into low and high risk values as the cost of an FTA (left panel) and NCA (right
panel) increases from 1 to 15 and the confidence level varies between 0% and 100%.
class as the cost of an FTA or NCA and the confidence level vary. We find the same pattern
as in Figure G.7. With any degree of statistical confidence, it is not possible to safely change
the underlying scores. Since the sizes of the model classes are smaller with respect to the
61

````

## PDF page 62

FORMULA CHECK REQUIRED: original PDF page 62.

````text
(a) Bail recommendation
2
4
6
2
4
6
NCA Score
FTA Score
Signature Bond
Modest Cash Bail
Moderate Cash Bail
Cash Bail
(b) Release and monitoring conditions rec-
ommendation
2
4
6
2
4
6
NCA Score
FTA Score
None
None + Conditions
Level 1
Level 2
Level 3 + GPS Monitoring
Level 3 + Maximum Conditions
Figure G.10: Decision Making Framework (DMF) matrix recommendation for (a) the cash
bail decision, and (b) additional release and monitoring conditions, for cases where the
current charge is not a serious violent offense, the NVCA flag is not triggered, and the
defendant was not extradited. If the FTA score and the NCA score are both less than 5, then
the recommendation is to only require a signature bond. Otherwise, the recommendation
is to require cash bail. The dashed line indicates this boundary. Unshaded areas indicate
impossible combinations of FTA and NCA scores. In (b) “Levels” 1,2 and 3 correspond to
pre-defined levels of pretrial supervision, “None + Conditions” denotes minor conditions the
signature bond if appropriate, “Level 3 + Maximum Conditions” corresponds to the highest
level of pretrial supervision along with additional measures such as biweekly face-to-face and
phone contact with arrestee.
truncated policy classes, the results suggest that there exist substantial uncertainty as to
the heterogeneous effects even for the truncated FTA and NCA scores.
G.3
Additional results for the overall DMF risk score and quater-
nary and ternary bail recommendations
Testing for interactions.
In our main analysis for the binary cash bail recommendation,
we use an additive model effective model where τadd(a, x) = τfta(a, xfta) + τnca(a, xnca). We
can assess the plausibility of this assumption following the same procedure as in Section G.1
above. We regress the difference in IP-weighted outcomes Γ(1, X, Y ) −Γ(0, X, Y ) on all
observed interactions between the FTA and NCA scores separately for the signature bond
and cash bail groups. We then again use a heteroskedastic robust Wald test to test whether
there is evidence for the coefficients for the interaction terms being non-zero, for each of the
signature bond and cash bail groups. We find some weak evidence for interaction terms in
the signature bond region (p = 0.07), but not in the cash bail region (p = 0.13).
Overall DMF risk score.
Now we turn to the overall DMF 1–7 risk score that encodes
recommendations on both the level of cash bail and the level and type of pre-trial supervision
and monitoring conditions. Recall from Section 5.4 that due to the structure of the DMF
62

````

## PDF page 63

FORMULA CHECK REQUIRED: original PDF page 63.

````text
Cost: 1
Cost: 2
Cost: 5
Cost: 10
Cost: 15
Confidence
0%
Confidence
20%
Confidence
80%
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
NCA Score
FTA Score
PSA Recommendation
Risk Level: 1
Risk Level: 2
Risk Level: 3
Risk Level: 4
Risk Level: 5
Risk Level: 6
Risk Level: 7
Figure G.11: Maximin monotone risk level cash bail and pre-trial supervision recommenda-
tions under an additive model for the treatment effects, as the cost of an NVCA and the
confidence level vary. The dashed black line indicates the original decision boundary between
a signature bond (above and to the left) and cash bail (below and to the right).
matrix, it is not possible to identify the CATE for most risk levels at most combinations
of FTA and NCA scores. Because we have K = 7 possible actions, we again usethe linear
utility specification used for the FTA and NCA scores above, though other costs are also
possible. For the DMF matrix, we again use the NVCA as the outcome.
Figure G.11 shows the resulting maximin DMF risk score recommendations for different
costs of an NVCA and confidence levels. We find that it is not possible to safely change
the DMF matrix for the full recommendation if the cost of an NVCA is larger than 5, even
without requiring any degree of statistical certainty.
Quaternary cash bail recommendation.
We also consider the quaternary cash bail
recommendation between a signature bond, modest cash bail, moderate cash bail, and (full)
cash bail. Here we have K = 4 actions and use the linear utility function. Figure G.12
shows the resulting maximin quaternary cash bail recommendation. This is broadly similar
to what we find for the overall DMF risk score.
Ternary cash bail recommendation.
We also consider the ternary cash bail recommen-
dation between a signature bond, moderate/modest cash bail, and full cash bail, collapsing
the moderate and modest cash bail recommendations. Here we have K = 3 actions and
use the linear utility function. Figure G.13 shows the resulting maximin ternary cash bail
63

````

## PDF page 64

Technical extraction; compare with original PDF page 64.

````text
Cost: 1
Cost: 2
Cost: 5
Cost: 10
Cost: 15
Confidence
0%
Confidence
20%
Confidence
80%
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
NCA Score
FTA Score
PSA Recommendation
Signature Bond
Modest Cash Bail
Moderate Cash Bail
Cash Bail
Figure G.12: Maximin monotone risk level ternary cash bail recommendations under an
additive model for the treatment effects, as the cost of an NVCA and the confidence level
vary. The dashed black line indicates the original decision boundary between a signature
bond (above and to the left) and cash bail (below and to the right).
recommendation. This is broadly similar to what we find for the binary cash bail recommen-
dation. When the confidence level is set to zero and the cost of an NVCA is high enough,
the maximin policy will extend the region where moderate cash bail is assigned to include
the intermediate region between a signature bond and moderate cash bail. However, if any
degree of statistical confidence is required, the maximin policy reverts to the status quo.
Note that the maximin policy does not change the boundary between modest cash bail and
cash bail, only between a signature bond and modest cash bail.
64

````

## PDF page 65

FORMULA CHECK REQUIRED: original PDF page 65.

````text
Cost: 1
Cost: 2
Cost: 5
Cost: 10
Cost: 15
Confidence
0%
Confidence
20%
Confidence
80%
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
NCA Score
FTA Score
PSA Recommendation
Signature Bond
Modest Cash Bail
Moderate Cash Bail
Figure G.13: Maximin monotone risk level ternary cash bail recommendations under an
additive model for the treatment effects, as the cost of an NVCA and the confidence level
vary. The dashed black line indicates the original decision boundary between a signature
bond (above and to the left) and cash bail (below and to the right).
Confidence Level: 0%
Confidence Level: 20%
Confidence Level: 50%
Confidence Level: 80%
2
4
6
2
4
6
2
4
6
2
4
6
2
4
6
NCA Score
FTA Score
Upper bound on effect
−1.0
−0.5
0.0
0.5
1.0
Figure G.14: Upper bound on the treatment effects under the additive model τadd(a, x) for
FTA and NCA scores. Values below and to the right of the dashed white line are areas where
cash bail is recommended, and the bounds are on the effect of recommending a signature
bond. Values above and to the left are areas where a signature bond is recommended, and
the bounds are on the effect of recommending cash bail.
65

````

## PDF page 66

FORMULA CHECK REQUIRED: original PDF page 66.

````text
References
Athey, S. and S. Wager (2021). Policy learning with observational data. Econometrica 89(1),
133–161.
Ben-Michael, E., D. J. Greiner, M. Huang, K. Imai, Z. Jiang, and S. Shin (2024). Does
AI help humans make better decisions? A statistical evaluation framework for experimental
and observational studies. arXiv:2403.12108.
Bertsimas, D., D. B. Brown, and C. Caramanis (2011). Theory and applications of robust
optimization. SIAM Review 53(3), 464–501.
Chowdhury, S. R. and A. Gopalan (2017). On kernelized multi-armed bandits. 34th Inter-
national Conference on Machine Learning, ICML 2017 2, 1397–1422.
Coston, A., A. Mishler, E. H. Kennedy, and A. Chouldechova (2020). Counterfactual risk
assessments, evaluation, and fairness. FAT* 2020, 582–593.
Cui, Y. (2021). Individualized decision making under partial identification: three perspec-
tives, two optimality results, and one paradox. Harvard Data Science Review.
Duchi, J. C. and H. Namkoong (2021).
Learning models with uniform performance via
distributionally robust optimization. Annals of Statistics 49(3), 1378–1406.
Dudik, M., J. Langford, and L. Li (2011). Doubly robust policy evaluation and learning. In
Proceedings of the 28th International Conference on Machine Learning.
Fiedler, C., C. W. Scherer, and S. Trimpe (2021).
Practical and Rigorous Uncertainty
Bounds for Gaussian Process Regression. In Association for the Advancement of Artificial
Intelligence.
Gilboa, I. and D. Schmeidler (1989). Maxmin expected utility with non-unique prior. Journal
of Mathematical Economics 18(2), 141–153.
Greiner, D. J., R. Halen, M. Stubenberg, and J. Chistopher L. Griffen (2020). Random-
ized control trial evaluation of the implementation of the psa-dmf system in dane county.
Technical report, Access to Justice Lab, Harvard Law School.
Imai, K., Z. Jiang, D. J. Greiner, R. Halen, and S. Shin (2023). Experimental evaluation
of computer-assisted human decision-making: Application to pretrial risk assessment in-
strument (with discussion). Journal of the Royal Statistical Society, Series A (Statistics in
Society) 186(2), 167–189.
Imbens, G. and S. Wager (2019). Optimized regression discontinuity designs. The Review
of Economics and Statistics 101(May), 264–278.
Jia, Z., E. Ben-Michael, and K. Imai (2023). Bayesian safe policy learning with chance
constrained optimization: Application to military security assessment during the vietnam
war.
66

````

## PDF page 67

FORMULA CHECK REQUIRED: original PDF page 67.

````text
Kallus, N. and A. Zhou (2021). Minimax-optimal policy learning under unobserved con-
founding. Management Science 67(5), 2870–2890.
Kennedy, E. H. (2022). Towards optimal doubly robust estimation of heterogeneous causal
effects.
Kitagawa, T. and A. Tetenov (2018). Who should be treated? empirical welfare maximization
methods for treatment choice. Econometrica 86(2), 591–616.
K¨unzel, S. R., J. S. Sekhon, P. J. Bickel, and B. Yu (2019). Metalearners for estimating
heterogeneous treatment effects using machine learning. Proceedings of the National Academy
of Sciences of the United States of America 116(10), 4156–4165.
Ledoux, M. and M. Talagrand (1991). Probability in Banach Spaces. Berlin, Heidelberg:
Springer.
Manski, C. F. (2005). Social Choice with Partial Knowledge of Treatment Response. Prince-
ton University Press.
Manski, C. F. (2007). Minimax-regret treatment choice with missing outcome data. Journal
of Econometrics 139(1), 105–115.
Neyman, J. (1990 [1923]). On the application of probability theory to agricultural experi-
ments. essay on principles. section 9. Statistical Science 5(4), 465–472.
Pu, H. and B. Zhang (2021).
Estimating optimal treatment rules with an instrumental
variable: A partial identification learning approach. Journal of the Royal Statistical Society
Series B, 1–28.
Qian, M. and S. A. Murphy (2011). Performance guarantees for individualized treatment
rules. The Annals of Statistics 39(2), 1180–1210.
Rahimi, A. and B. Recht (2008). Random Features for Large-Scale Kernel Machines. In
Advances in Neural Information Processing Systems, Volume 20.
Rubin, D. B. (1980). Comment on “randomization analysis of experimental data: The fisher
randomization test”. Journal of the American Statistical Association 75(371), 591–593.
Song, K. (2014). Point decisions for interval-defined parameters. Econometric Theory 96(2),
334–356.
Srinivas, N., A. Krause, S. M. Kakade, and M. Seeger (2010). Gaussian Process Optimiza-
tion in the Bandit Setting: No Regret and Experimental Design. Proceedings of the 27th
International Conference on Machine Learning (ICML 2010), 1015–1022.
Stevenson, M. T. and S. G. Mayson (2022). Pretrial detention and the value of liberty.
Virginia Law Review 108(2), 709–782.
Stoye, J. (2012). Minimax regret treatment choice with covariates or with limited validity
of experiments. Journal of Econometrics 166(1), 138–156.
67

````

## PDF page 68

FORMULA CHECK REQUIRED: original PDF page 68.

````text
Wainwright, M. J. (2019). High-Dimensional Statistics: A Non-Asymptotic Viewpoint. Cam-
bridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press.
Zhang, Y., E. Ben-Michael, and K. Imai (2023). Safe Policy Learning under Regression
Discontinuity Designs with Multiple Cutoffs.
Zhao, Y., D. Zeng, A. J. Rush, and M. R. Kosorok (2012). Estimating individualized treat-
ment rules using outcome weighted learning. Journal of the American Statistical Associa-
tion 107(499), 1106–1118.
68

````

