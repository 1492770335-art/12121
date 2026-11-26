# MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES WHEN A QUANTILE IS THE OBJECT OF INTEREST

Original PDF: [original.pdf](original.pdf). SHA256: `767c9d83d02ad8408c7f0846b73605baf8bce554d7a6023f18c025a7ad906298`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1; PDF label 1

Technical extraction; compare with original PDF page 1.

````text
Econometric Theory, 0, 2026, 1–36.
doi:10.1017/S0266466626100498
MINIMAX REGRET TREATMENT
RULES WITH FINITE SAMPLES WHEN
A QUANTILE IS THE OBJECT OF
INTEREST
PATRIK GUGGENBERGER
Pennsylvania State University, USA
NIHAL MEHTA
Keystone Strategy, USA
NIKITA PAVLOV
Pennsylvania State University, USA
Consider a setup in which a decision maker is informed about the population by
a finite sample and, based on that sample, has to decide whether or not to apply a
certain treatment. We work out finite sample minimax regret treatment rules under
various sampling schemes when potential outcomes are restricted onto the unit
interval. In contrast to Stoye (2009, Journal of Econometrics 151, 70–81), where
the focus is on the maximization of expected utility, the focus here is instead on a
particular quantile of the outcome distribution. We find that in the case where the
sample consists of a fixed number of untreated and a fixed number of treated units,
any treatment rule is minimax regret optimal. The same is true in the case of random
treatment assignment in the sample with any assignment probability and in the case
of testing an innovation when the known quantile of the untreated population equals
1/2. However, if the known quantile exceeds 1/2, then never treating is the unique
optimal rule, and if it is smaller than 1/2, always treating is optimal. We also consider
the case where a covariate is included.
1. INTRODUCTION
Consider a setup in which a decision maker (DM) has to decide whether or not to
assign a treatment after observing data with observations from the untreated and
We would like to thank the Editors Peter Phillips and Liangjun Su, the Co-Editor Xiaoxia Shi, and two anonymous
referees for many helpful suggestions. We also would like to thank Antonio Galvao, Kei Hirano, seminar participants
at (in chronological order) UC Davis, UC Riverside, Colorado Boulder, SUNY Stony Brook, McGill, München,
Konstanz, Frankfurt, Heidelberg, Regensburg, NTU, SMU, NUS, Macquarie University, University of Sydney,
UNSW, Brisbane, UCL, Exeter, Cambridge, Manchester, and Oxford in 2023–2024, and conference participants
at the New York Camp Econometrics, Lake Placid, the Rochester Conference in Econometrics, and the 35th
EC2 Conference, Amsterdam, for helpful comments. Address correspondence to Patrik Guggenberger, Economics,
Pennsylvania State University, USA, email: pxg27@psu.edu.
© The Author(s), 2026. Published by Cambridge University Press. This is an Open Access article, distributed
under the terms of the Creative Commons Attribution licence (https://creativecommons.org/licenses/by/4.0),
which permits unrestricted re-use, distribution and reproduction, provided the original article is properly cited.
1
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 2; PDF label 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
2
PATRIK GUGGENBERGER ET AL.
treated populations.1 The DM could be a policymaker who applies a treatment to
the entire population or a person who is applying the treatment to an individual
(e.g., herself). As examples of the latter setup, think of an individual who chooses
between two hotels on an internet platform after observing a certain number of
ratings or a medical doctor who considers a treatment for a patient after observing
a certain number of outcomes from treated and untreated patients.
This article adds to a short but growing literature on finding treatment rules that
have finite-sample optimality properties. In most of the literature, the focus is on
the expected outcome under the chosen treatment rule.2 Given that typically there
is no treatment rule that is uniformly best over all possible joint distributions for
(Y0,Y1), where Y0 and Y1 denote random variables for outcomes without and with
treatment, respectively, one has to resort to other criteria for optimality. One option
is to consider a prior over the space of joint distributions and maximize expected
outcome for this particular prior. Another option is to focus on admissible treat-
ment rules, but that criterion typically does not single out an individual treatment
rule (see Manski and Tetenov, 2023; Montiel Olea et al., 2026). Alternatively, one
might consider finding a treatment rule that maximizes minimal expected outcome
where the minimum is taken over all joint distributions of (Y0,Y1). However, if
there exists a distribution that assigns the minimal possible values in the shared
domains of Y0 and Y1 with probability one, then any treatment rule is going to be
optimal according to this criterion and therefore also the “max–min” approach is
not pinning down a unique rule. For that reason, instead, the so-called “minimax
regret” criterion is often adopted that determines treatment rules that minimize
the maximal regret where regret is defined as the difference between the largest
expected outcome that could be achieved for any treatment rule and the expected
outcome under the treatment rule under consideration, and the maximum is taken
with respect to all possible distributions for (Y0,Y1). Stoye (2009) derives minimax
regret rules in finite samples for the case of two treatments under various sampling
schemes, namely, matched pairs, random sampling, and testing an innovation, and
furthermore provides near-uniqueness results.
In this project, we are interested in a setup where, rather than expected out-
come, the DM is concerned about the α-quantile of the outcome (for a given
α ∈[0,1]). Wang et al. (2018) consider robust estimation of the quantile-optimal
1A treatment rule δ, formally introduced in (2.2) below, is a mapping from the data wN (with N denoting the
sample size) into the unit interval, with δ(wN) denoting the probability with which treatment is assigned. Therefore,
randomized treatment assignment is allowed for.
Alternatively, rather than framing the options as “treatment” and “no treatment,” one could frame the setup as a
choice between two treatments.
2See, for example, Manski (2004), Manski and Tetenov (2007), Stoye (2007, 2009, 2012), Tetenov (2012), Masten
(2023), Yata (2023), Chen and Guggenberger (2026), Kitagawa, Lee, and Qiu (2026), Montiel Olea, Qiu, and
Stoye (2026), and additional references in these papers. Hirano and Porter (2009), Kitagawa and Tetenov (2018),
Christensen, Moon, and Schorfheide (2026), and many other references therein also use the minimax regret criterion
but consider an asymptotic, rather than a finite sample, framework. This literature is inspired by the classical work
of Wald (1950). In a recent paper, Manski and Tetenov (2023) study several potential features of the state-dependent
distribution of loss (rather than just its expectation) that a treatment rule generates across potential samples.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 3; PDF label 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
3
treatment regime and provide arguments as to why focusing on a quantile rather
than the mean may be sensible in certain applications. In fact, in many appli-
cations, the tail of the outcome distribution is at the center of interest. For
example, when evaluating job training programs to improve earnings, the focus
is often on earnings in the lower tail, and likewise in survival analysis (e.g.,
survival time of cancer patients), the lower tail is of key importance. Wang et al.
(2018, Sect. 2) provide numerical evidence where the mean-optimal treatment is
detrimental for patients in the lower tail. In Economics, one might be interested
in median income (case α = 1/2) or a minimal level of educational achievement
for schoolchildren, “no child left behind” (case α = 0). See Manski (1988) who
studies the “quantile utility” model whose predictions, unlike the expected utility
model, are invariant under ordinal transformations of utility. Subsequently, Rostek
(2010) axiomatizes quantile preference and, recently, Manski and Tetenov (2023)
suggest considering various deviations from mean loss including quantiles. Also,
see Chambers (2009).3
As the main contribution of this article, we derive minimax regret treatment rules
δ in finite samples when an α-quantile of the outcome distribution is the focus
of interest and outcomes Y0 and Y1 take values in the unit interval. That is, the
objective function for the DM is qs,α(YB(δ(wN))), where YB(δ(wN)) denotes random
outcomes generated when the treatment rule δ is used, with B representing a
Bernoulli random variable that equals 1 with probability δ(wN), and qs,α(YB(δ(wN)))
denotes the α-quantile of YB(δ(wN)) when the joint distribution of (Y0,Y1) equals s.
Somewhat surprisingly, we show that under various sampling schemes all
treatment rules are minimax regret, namely, in case i), when the sample consists of
a fixed number of treated and a fixed number of untreated units (i.e., unbalanced
panels are allowed for) and in case ii), under random assignment with arbitrary
treatment assignment probability in the sample equal to p ∈(0,1). In both cases
i) and ii), maximal regret equals 1 for any treatment rule.
On the other hand, in case iii), “testing an innovation,” that is, the case where
only data on Y1 is observed and the α-quantile qs,α(Y0) of Y0 is known, where again
the subscript s denotes the joint distribution of (Y0,Y1), if qs,α(Y0) > 1/2, then δ ≡
0 is the unique minimax rule, if qs,α(Y0) < 1/2, then δ ≡1 is a minimax rule, and
finally, if qs,α(Y0) = 1/2, then any treatment rule δ is minimax regret; in each case,
for minimax treatment rules δ, we obtain the formula min{qs,α(Y0),1 −qs,α(Y0)}
for the maximal regret.
Obviously, like for the case where expected outcomes are the focus, also here the
max–min criterion is not informative. Namely, as long as the joint distribution of
(Y0,Y1) can be chosen such that qs,α(Y0) = qs,α(Y1) = 0, that is, the worst possible
outcome under the given restriction that Y0,Y1 ∈[0,1], any treatment rule would
3Related (but in a non-finite-sample setup), Qi et al. (2019) and Qi, Pang, and Liu (2023) consider optimal decision
rules based on the conditional value at risk (CVaR) measure. Quantile preferences have been attracting growing
interest in the literature, for example, De Castro, Galvao, and Ota (2026) consider a model in which an economic
agent maximizes the discounted value of a stream of future α-quantile utilities.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 4; PDF label 4

Technical extraction; compare with original PDF page 4.

````text
4
PATRIK GUGGENBERGER ET AL.
be max–min optimal. In contrast though, to the case where expected outcomes are
the focus, for quantiles also minimax regret is not informative for sampling designs
i) and ii) and also for iii) when qs,α(Y0) = 1/2.
The typical strategy in the extant literature for determining minimax regret
rules when the focus is on expected outcomes is via a Nash equilibrium approach
in a fictitious zero sum game in which the DM plays against an antagonistic
nature whose payoff equals regret. To establish that a particular treatment rule δ is
minimax regret, one attempts to guess a “state of nature” s, allowed to be mixed
strategy (over a finite number of states), called a least favorable distribution, for
which the pair (δ,s) constitutes a Nash equilibrium. Existence of such a pair (δ,s)
implies that δ is indeed a minimax regret rule (see, e.g., Berger, 1985; Stoye, 2009;
Chen and Guggenberger, 2026). Often, in a first step, one restricts outcomes to be
Bernoulli and finds a minimax rule in this simplified setup and then, in a second
step, uses the so-called coarsening approach to tackle the general case (see, e.g.,
Cucconi, 1968; Gupta and Hande, 1992; Schlag, 2003, 2006). When nature picks a
state of the world trying to inflict high regret, it faces the trade-off that, on the one
hand, a high differential between expected outcomes with and without treatment
is needed, but, on the other hand, the more different the distributions of Y0 and Y1
are the easier the DM can tell them apart using the sample information.
The proof structure for the main results in this article differs from the one
just described. Namely, for cases i) and ii), we show that for any treatment
rule δ, one can find a state of nature s = sδ such that s inflicts the highest possible
regret, namely, 1. That insight is sufficient to establish that all rules are minimax
regret and that maximal regret equals 1 for all treatment rules. It is noteworthy and
remarkable that, despite the trade-off just described, nature is powerful enough to
inflict maximal regret on the DM. Even more surprisingly, the conclusions under i)
and ii) continue to be true even if nature is restricted to only Bernoulli distributions.
The proof for part iii) relies on the main insight that if δ̸ = 0, then there exists a
state of nature such that regret equals the known α-quantile of Y0. For that to be
true, it is sufficient for nature to have discrete distributions, supported on N + 1
points, at its disposal.
We start off with the case with no covariates and then allow for a discrete-
valued covariate in the model. In the latter case, a treatment rule maps a sample
onto treatment probabilities for each of the K possible outcomes of the covariate.
Not surprisingly, given the results without a covariate, we find that in cases i) and
ii), and case iii) with known quantile equal to 1/2, again, each treatment rule is
minimax regret, while in case iii) when the known quantile is different from 1/2,
no-data rules are minimax regret.
We include a small finite sample simulation study in the case of “testing an
innovation” where we simulate regret of various treatment rules, namely, the
empirical success rule and several no-data rules. The study corroborates our
theoretical findings about minimax regret treatment rules and the formulas for
maximal regret that we derive.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 5; PDF label 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
5
The remainder of the article is organized as follows. Section 2 introduces the
theoretical setup for our notion of a minimax regret rule with quantiles and contains
analytical results when no covariates are included. In Section 2.1, we present
various approaches for how quantiles could be incorporated into the Waldean
framework of statistical decision theory and juxtapose them with our approach.
Section 2.2 derives minimax regret treatment rules under various sampling
schemes and also provides a brief discussion of minimax regret treatment rules
when certain restrictions are imposed on the states of nature. Section 2.3 simulates
the performance of various treatment rules in finite samples in the case of testing
an innovation. Finally, Section 3 derives minimax regret treatment rules in the case
where covariates are included in the model. All proofs are given in the Appendix.
2. THEORETICAL SETUP WITHOUT COVARIATES
A DM has to decide whether or not to assign treatment after being informed
about the population by a finite sample. The setup is very similar to the one in
Stoye (2009) with one key modification. Namely, rather than focusing on mean
outcomes, here we are concerned with the α-quantile of the outcome distribution.
For most parts of the article, potential outcomes Y0 and Y1 for untreated/treated
individuals are restricted to the unit interval
Y0,Y1 ∈S := [0,1],
(2.1)
where S is assumed known to the DM. At first, different members of the population
are all identical to the DM. Later, we will consider the case where a covariate is
included and treatment assignment can be made conditional on the realization of
the covariate.
By S, we denote the set of “states of the world” s, where an s denotes a possible
joint probability distribution over the potential outcomes for Y0 and Y1. Unless
otherwise stated, S is unrestricted and contains all possible joint distributions for
Y0 and Y1 on S2. Upon observing a sample wN = (t,y) of size N of treatment statuses
t = (t1,...,tN) and outcomes y = (y1,...,yN), where the i-th component of y, yi, is
an independent realization of Yti and ti denotes the treatment received by individual
i, the task for the DM is to choose
δ(wN) ∈[0,1],
(2.2)
which denotes the probability with which treatment is assigned.4 Namely, which
treatment the DM assigns is determined as an independent draw of the Bernoulli
random variable B = B(δ(wN)) ∈{0,1} that equals 1 with probability δ(wN) and is
assumed to be independent of all other random objects. Therefore, the setup here
allows for randomized treatment rules.
4We do not index t and y by N because it would make the notation too cumbersome.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 6; PDF label 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
6
PATRIK GUGGENBERGER ET AL.
Let α ∈[0,1]. Given a state of the world s and a statistical treatment rule δ, the
objective function for the DM is
u(δ,s) = qs,α(YB(δ(wN))),
(2.3)
where YB(δ(wN)) denotes random outcomes generated when the treatment rule δ is
used, and qs,α(YB(δ(wN))) denotes the α-quantile of YB(δ(wN)) when the state of the
world is s ∈S. In particular, when the treatment rule δ(wN) equals 0 (or 1), then
with probability 1 YB(δ(wN)) equals Y0 (or Y1).
By definition, an α-quantile of a scalar-valued random variable X with domain
D is any number q ∈D that satisfies
P(X ≤q) ≥α and P(X ≥q) ≥1−α.
(2.4)
Clearly then, any α-quantile of Y0, Y1, and YB(δ(wN)) is an element of [0,1]. In
general, this definition does not lead to a unique α-quantile. The definition allows
for the case where a quantile has a nonzero point mass. To be explicit in cases
where there is non-uniqueness, we make the following definition that hinges on a
choice r ∈[0,1].
Definition (α-quantile): Let Q denote the set of all α-quantiles q. For α ∈(0,1),
we define the α-quantile as
rsupQ+(1−r)inf Q.
(2.5)
When α = 0, we use supQ (i.e., we use r = 1) and when α = 1, we use inf Q (i.e.,
we use r = 0).
From now on, by qs,α(YB(δ(wN))), we denote the α-quantile of YB(δ(wN)) when the
state of the world is s. For simplicity of notation, unless needed for clarity, we do
not index that expression by r.
By definition, regret of the treatment rule δ for a given distribution s of (Y0,Y1)
equals
R(δ,s) = sup
d∈D
u(d,s)−u(δ,s),
(2.6)
where D denotes the set of all possible treatment rules. In words, regret equals the
difference between the highest α-quantile that could have been achieved for any
treatment rule d ∈D and the α-quantile obtained for the particular treatment rule
δ for the given state of nature s. If qs,α(Y1) ≥qs,α(Y0) ( qs,α(Y1) < qs,α(Y0)) and
d∗= 1 ( d∗= 0) is an element of D, then supd∈D u(d,s) is taken on by d∗and equals
qs,α(Y1) ( qs,α(Y0)) (see Lemma 3(ii) in the Appendix). If restrictions are imposed
on D, then supd∈D u(d,s) may not be taken on by any element in D. Again, without
restrictions, 1(qs,α(Y1) ≥qs,α(Y0)) is an infeasible optimal rule, where 1(·) denotes
the indicator function.
In this article, we focus on minimax regret treatment rules. By definition, if it
exists, such a rule satisfies
δ∗∈argmin
δ∈D sup
s∈S
R(δ,s).
(2.7)
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 7; PDF label 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
7
In contrast, a maximin treatment rule, if it exists, satisfies
δ+ ∈argmax
δ∈D inf
s∈Su(δ,s).
(2.8)
As discussed already elsewhere (see, e.g., Manski, 2004; Stoye, 2009), the max-
imin criterion may lead to the uninformative result that all δ ∈D are maximizers.
That occurs, for example, if for a particular s+ ∈S, u(δ,s+) does not depend on δ
and takes on its smallest possible value, u(δ,s+) = infs∈S u(δ,s). That situation also
occurs in our setup where the objective is to maximize the quantile of the outcome
distribution, namely, when s+ ∈S is chosen such that qs,α(Y0) = qs,α(Y1) = 0.
In contrast to the setup where expected outcomes are the objective, as we will
establish next, it turns out that for quantiles, depending on the particular sampling
design, also the minimax regret criterion may be uninformative.
2.1. Waldean Statistical Decision Theory and Quantiles5
In this section, we further discuss the proposed criterion introduced in (2.3) and
juxtapose it with other possible approaches of how quantiles could be incorporated
into a Waldean framework of statistical decision theory.
In a series of pathbreaking contributions, Wald (1945, 1947, 1950) introduced a
framework for statistical decision theory whose main components are a statistical
model, an action space, statistical decision rules, a welfare and an expected welfare
function, and finally an evaluation criterion. Instead of welfare and expected wel-
fare the presentation could be framed in terms of loss (defined as negative welfare)
and risk (defined as expected loss). See Hirano (2026) for a comprehensive review
that also includes contemporary developments.
In the particular context considered here where the DM needs to pick treatment
0 or 1 after observing the i.i.d. sample wN, a minimax regret rule in the Waldean
formulation solves
argmin
δ∈D max
s∈S [max{μ0,μ1}−EsYB(δ(wN))],
(2.9)
where μt = EsYt for t = 0,1 and Es denotes the expectation operator under s. It is
easily shown that s matters only via (μ0,μ1). By the law of iterated expectations,
EsYB(δ(wN)) = EwNEs(YB(δ(wN))|wN)
= μ0EwN(1−δ(wN))+μ1EwNδ(wN),
(2.10)
overall uncertainty can be separated into sampling uncertainty through wN,
(potential) randomness through the treatment assignment B, and randomness
through the potential outcome variables (Y0,Y1); risk is defined as the average
loss over sampling uncertainty.
To adapt the Waldean framework to one that is based on the notion of α-quantile
rather than expectation, we propose replacing expectations by α-quantiles in the
5This section is inspired by the constructive comments of an anonymous referee.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 8; PDF label 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
8
PATRIK GUGGENBERGER ET AL.
formulation (2.9), that is, we suggest solving (2.7) which is
argmin
δ∈D max
s∈S [max{qs,α(Y0),qs,α(Y1)}−qs,α(YB(δ(wN)))].
(2.11)
Given that there is no equivalent to the law of iterated expectations for quantiles,
by doing so, one loses the separation of the regret criterion into loss without
sampling uncertainty and sampling uncertainty. Our proposed criterion aggregates
joint uncertainty (sampling, treatment assignment, and outcome) before taking the
quantile.6
Instead, to maintain such separation, one could first define regret loss given a
realized sample wN as
L(δ(wN),s) = max{qs,α(Y0),qs,α(Y1)}−qs,α(YB(δ(wN))|wN)
(2.12)
and then define an alternative regret to (2.6) as the average of regret loss over the
sampling distribution wN
R′(δ,s) = max{qs,α(Y0),qs,α(Y1)}−EwNqs,α(YB(δ(wN))|wN).
(2.13)
The first term in (2.12) is a benchmark attainable if one could pick the better
treatment in terms of quantile outcome without sampling uncertainty; the second
term is the α-quantile of YB(δ(wN)) conditional on the realized sample wN. This
criterion may be misaligned when the DM cares about tails in the distribution
of qs,α(YB(δ(wN))|wN) over realized samples rather than the average over sampling
uncertainty. As yet another alternative, one could consider a regret function defined
as the β-quantile (for some β in the unit interval) of the loss function in (2.12), that
is,
R′′(δ,s) = qs,β(L(δ(wN),s)).
(2.14)
By the monotone transform identity of quantiles, it follows that
R′′(δ,s) = max{qs,α(Y0),qs,α(Y1)}−qs,1−β(qs,α(YB(δ(wN))|wN))
(2.15)
and the interpretation of the criterion is not straightforward.
Manski and Tetenov (2023, Sect. 6.1) suggest an entire class of alternative
approaches that also maintain separation. Starting with an arbitrary loss function
(for instance, negative welfare) for a given action by the DM (i.e., in our setup, a
choice of treatment 0 or 1) and DGP s, the suggestion is to consider, for example, an
α-quantile of the loss function over the sampling distribution. In our setup, such
an approach could be formulated as
argmin
δ∈D sup
s∈S
[max{μ0,μ1}−qs,α(μB(δ(wN)))].
(2.16)
6Note that qs,α(YB(δ(wN))|wN) does not in general equal δ(wN)qs,α(Y1)+(1−δ(wN))qs,α(Y0) in cases where δ(wN) ∈
(0,1).
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 9; PDF label 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
9
One issue with the implementation of the various criteria is that analytical
formulas are not generally available.7
We do not have a strong opinion about which one of the above criteria is
generally preferable. However, we find our criterion very natural in situations
where a DM applies treatment to an individual (e.g., herself) after observing the
sample. Consider, for example, an individual who books a hotel accommodation on
an internet platform, picking one of two options after observing a certain number
of ratings on each (or picks one of two restaurants after having observed a number
of ratings for each on the internet). The outcome is the rating the DM assigns to
the hotel she booked, which could be interpreted as a proxy for the welfare the DM
received from staying at the hotel. Another example is a medical doctor who picks
one of two treatments for a patient after observing a certain number of outcomes
on the two treatments.
In that type of example, when repeating the exercise, every observed outcome
combines the randomness of the sample, (potential) randomness of treatment
assignment, and the randomness of (Y0,Y1). If the DM is concerned about quantiles
of the outcome distribution, it seems that the criterion proposed in (2.11) is a
natural choice.
2.2. Minimax Regret Treatment Rules
Recall that a sample of size N has the general structure wN = (t,y). We consider
three different sample designs, namely:
(i) Fixed number of untreated/treated units with N0 ∈{0,...,N} i.i.d. obser-
vations of Y0 and N1 := N −N0 i.i.d. observations of Y1 for some N ∈N ∪{0}.
Here, the notation for a sample can be simplified by dropping t. We write
wN = (y(0)′,y(1)′)′ ∈[0,1]N, where y(0) ∈[0,1]N0 contains the N0 observations
on untreated units and y(1) ∈[0,1]N1 contains the N1 observations on the treated
units. A treatment rule δ ∈D is then any mapping [0,1]N →[0,1]. It assigns a
treatment probability δ(wN) ∈[0,1] after observing the sample.
(ii) Random assignment with N ∈N ∪{0} i.i.d. observations, where in the
sample, the treatment probability equals p ∈(0,1).8 A treatment rule δ ∈D is
any mapping {0,1}N × [0,1]N →[0,1]. The rule δ assigns a treatment proba-
bility δ(wN) ∈[0,1] after observing a sample wN = (t,y) of treatment statuses
t = (t1,...,tN) and realizations y = (y1,...,yN), where the i-th component of y, yi,
is an independent realization of Yti.
(iii) Testing an innovation is the case where aspects of the distribution of Y0 are
known to the DM; in particular, we assume that the α-quantile of Y0 is known (but
nature can pick arbitrary distributions for Y0 subject to that restriction). That is, in
this case, the set S consists of all joint distributions s for (Y0,Y1) with the restriction
7Recently suggested numerical procedures for the implementation of minimax rules by Aradillas Fernández et al.
(2025) and Guggenberger and Huang (2025) might be applicable also for these scenarios.
8Note that p ∈{0,1} leads back to design (i) with N0 or N1 equal to N.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 10; PDF label 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
10
PATRIK GUGGENBERGER ET AL.
that the α-quantile of the marginal for Y0 equals a certain value qα(Y0). In this case,
N ∈N ∪{0} i.i.d. observations of Y1 are observed. Here again, the notation for a
sample can be simplified. We write wN = y(1) ∈[0,1]N, where y(1) contains the N
observations of the treated units. A treatment rule δ ∈D is any mapping [0,1]N →
[0,1]. The rule δ assigns a treatment probability δ(wN) ∈[0,1] after observing a
sample wN = (y1,1,...,y1,N) of N independent realizations y1,i, i = 1,...,N of Y1.
The designs above nest the ones in Stoye (2009). In contrast to Stoye (2009), in
design (i), we allow for arbitrary numbers of treated and untreated units rather than
N/2 units each as in “matched pairs” and in design (ii), the treatment probability
is any fixed number p ∈(0,1) rather than necessarily p = 0.5.
The following statement provides the analog to Proposition 1 in Stoye (2009)
and is the main contribution of this article.
Proposition 1. (i) Consider the case where the sample consists of a “fixed
number of treated/untreated units.” If (α ∈(0,1) and r ∈[0,1]) or (α = 0 and
r = 1), then any treatment rule δ ∈D is minimax regret and maxs∈S R(δ,s) = 1 for
any δ ∈D. If (α = 1 and r = 0), then exactly those treatment rules δ ∈D, that
are not equal to 1 wp1 and not equal to 0 wp1, are minimax regret and satisfy
maxs∈S R(δ,s) = 0.
(ii) Consider the case where the sample is generated via “random assignment.”
Then the same statement as in part (i) holds.
(iii) In the case of “testing an innovation,” let (α ∈(0,1) and r ∈[0,1]) or
(α = 0 and r = 1). If the known α-quantile of Y0, qα(Y0), equals 1/2, then any
treatment rule δ ∈D is minimax regret; if instead qα(Y0) > 1/2, then δ0 ≡0 is
the unique minimax regret rule; if qα(Y0) < 1/2, then δ1 ≡1 is a minimax regret
rule; in each case, for minimax regret treatment rules δ, we obtain maxs∈S R(δ,s) =
min{qα(Y0),1 −qα(Y0)}. If (α = 1 and r = 0), then exactly those treatment rules
δ ∈D, that are not equal to 1 wp1 and not equal to 0 wp1, are minimax regret and
satisfy maxs∈S R(δ,s) = 0.
Comments. 1. Proposition 1 establishes that the minimax regret criterion when
applied to α-quantiles does not favor data-driven rules. In fact, in the “testing an
innovation” case, data-driven rules are strictly dominated by δ0 ≡0 when qα(Y0)
> 1/2 and weakly dominated by δ1 ≡1 when qα(Y0) < 1/2. When qα(Y0) = 1/2,
all treatment rules are minimax. This is in stark contrast to the results in Stoye
(2009) about minimax regret treatment rules when the focus is on mean outcomes.
Namely, Stoye (2009) shows that, for example, in the case of binary outcomes,
where the sample is obtained as a matched pair, to be minimax regret optimal, the
treatment that has more successes in the sample must be chosen with probability
one.
2. To provide intuition of the result in (i) and (ii), assume α ∈(0,1) and consider
first the simplest case where the sample size N is 0. In that case, a treatment rule δ
is simply an element in [0,1] that denotes the probability of assigning treatment.
For given δ, the objective for nature is to find a distribution for (Y0,Y1) such that
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 11; PDF label 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
11
the α-quantiles of the marginals have maximal distance (i.e., distance 1) and such
that the α-quantile of YB(δ) is zero. Let δ > 0 first. Assume nature picks Y0 and Y1
as independent Bernoulli
P(Y1 = 0) = 1, P(Y0 = 0) = α −ε for some ε ∈(0,α]
(2.17)
and, consequently, P(Y0 = 1) = 1 −(α −ε). Thus, qs,α(Y1) = 0 and qs,α(Y0) = 1
and
P(YB(δ) = 0) = δ +(1−δ)(α −ε).
(2.18)
Thus, P(YB(δ) = 0) > α iff δ(1 −α) > ε(1 −δ) which holds for ε small enough.
Thus,
max
s∈S R(δ,s) = 1
(2.19)
for all δ ∈(0,1]. If instead δ = 0, then nature chooses P(Y1 = 1) = 1 and P(Y0 =
0) = 1 which leads to regret of 1.
This result may be surprising at first. For example, if the DM tries to be
completely balanced and picks δ = 1/2 (which seems reasonable in the no data
case), nature can inflict regret equal to one by picking P(Y1 = 0) = 1 and, for
example, P(Y0 = 0) = α−min{α/2,(1−α)/2}. This is in stark contrast to the case
considered in Stoye (2009) where the DM cares about expected outcome under
δ, that is, μ0(1 −δ) + μ1δ, where μt for t = 0,1 denotes the expectation of Yt
under s. Regret for given δ and s (which only matters via (μ0,μ1)) then equals
max{μ0,μ1}−(μ0(1−δ)+μ1δ). When the DM picks a δ with δ ≥1/2, then the
maximal regret nature can inflict equals δ obtained for any s with EsY0 = 1 and
EsY1 = 0. Therefore, the DM’s minimax regret choice is δ = 1/2. What explains
the different results with quantiles and expectations? What drives the results with
quantiles is the discontinuity of the α-quantile of a random variable X with respect
to the cdf FX of X. In the above construction, the random variables Y0 and YB(δ) have
cdfs that are uniformly “very close” yet their α-quantiles differ by 1. For example,
take again δ = 1/2 and consider α = 0.99. Then both Y0 and YB(δ) are Bernoulli with
P(Y0 = 0) = 0.99−0.005 = 0.985 and P(YB(δ) = 0) = 1/2+1/2·0.985 = 0.9925.
Thus, their cdfs are almost identical but their 0.99-quantiles differ by 1. Instead
the expectations of these two random variables are very close.
Surprisingly, the intuition of the no-data example generalizes to cases with
arbitrary sample size N > 0. Again, for any given treatment rule δ ∈D, one
constructs an sδ ∈S for which max{qsδ,α(Y0),qsδ,α(Y1)} = 1 and u(δ,sδ) = 0 and
thus R(δ,sδ) = 1. Again sδ ∈S can be chosen such that Y0 and Y1 are independent
and both have Bernoulli distributions. That is, sδ is then fully described by the two
parameters Psδ(Y0 = 0) and Psδ(Y1 = 0). Denote by 0N0 an N0-dimensional column
vector of zeros.
In case (i) of Proposition 1, if δ is such that δ((0N0′,v′)′) = 1 for all v ∈{0,1}N1,
then nature attempts punishing the DM for always using treatment 1 when no
successes are observed for treatment 0, by choosing Psδ(Y1 = 0) = 1 and by
choosing Psδ(Y0 = 0) “big enough” that only zeros are observed for the untreated
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 12; PDF label 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
12
PATRIK GUGGENBERGER ET AL.
individuals “sufficiently often” guaranteeing YB(δ(w)) has α-quantile 0, but “small
enough” that Y0 has α-quantile 1. The proof shows that this can indeed be achieved
by picking Psδ(Y0 = 0) = α −ε for some small enough ε > 0.
If on the other hand δ is such that δ((0N0′,v′)′) < 1 for at least one v ∈{0,1}N1,
then nature attempts punishing the DM for not using treatment 1 often enough
when no successes are observed for treatment 0, by choosing Psδ(Y0 = 0) = 1 and
by choosing Psδ(Y1 = 0) “small enough” that Y1 has α-quantile 1 but “big enough”
that YB(δ(w)) has α-quantile 0. The proof shows that this can indeed be achieved by
picking Psδ(Y1 = 0) = α −ε for some small enough ε > 0.
A surprising fact about the proof is that exploiting properties of δ on the set
of samples {(0N0′,v′)′, v ∈{0,1}N1} alone gives nature enough leverage to inflict
maximal regret.
Next, we provide additional insights for this fact. The proof of Proposition 1(i)
reveals that for any δ ∈D, one can find sδ ∈S with Y0 and Y1 independent Bernoulli
distributions such that R(δ,sδ) = 1. In fact, the proof reveals that for any treatment
rule δ for which
δ0,j := 
v∈{0,1}N1, v=jδ((0N0′,v′)′) <
N1
j

(2.20)
for at least one j = 0,...,N1 (where v denotes the number of observations in the
sample for which Y1 equals 1), one can achieve R(δ,sδ) = 1 when Y0 and Y1 are
independent Bernoulli distributions with Y0 = 0 with probability 1. For such a
treatment rule δ, we now discuss regret of δ as a function of a ∈[0,1] when
nature picks sa ∈S and under sa, Y0 = 0 with probability 1 and Y1 is Bernoulli
with Psa(Y1 = 0) = a. We will focus on the case α = 1/2, r = 0, and on two
particular treatment rules, namely, δ0.5 ≡1/2 (the treatment rule that always picks
1/2 independent of the data wN) and the empirical success rule δES, defined by
δES(wN) = I(qα(Y1,wN) > qα(Y0,wN))+.5I(qα(Y1,wN) = qα(Y0,wN)),
(2.21)
where qα(Yj,wN) denotes the α-sample quantile of Yj for the sample wN for j = 0,1
and the α-sample quantile is defined with r = 0 in (2.5). We will take N0 > 0
and N1 even. When Y0 = 0 with probability 1, it follows that qα(Y0,wN) = 0 with
probability 1 and qα(Y1,wN) > 0 occurs if strictly more than N1/2 observations on
Y1 in the sample equal 1. (In that case, qα(Y1,wN) = 1; otherwise, qα(Y1,wN) = 0.)
Note that δ0,j in (2.20) equals 0.5
N1
j

for δ = δ0.5; it equals 0.5
N1
j

if j ≤N1/2 and
N1
j

if j > N1/2 for δ = δES.
From simple calculations in (A.6) in the Appendix, it follows that, for any
δ ∈D,
Psa(YB(δ(wN)) = 0) = N1
j=0[aN1−j(1−a)j(a−1)]δ0,j +1.
(2.22)
Note that qsa,α(YB(δ(wN))) = 0 if Psa(YB(δ(wN)) = 0) ≥0.5 and qsa,α(YB(δ(wN))) = 1
otherwise. It follows that regret equals 1 if a < 1/2 and Psa(YB(δ(wN)) = 0) ≥0.5
and regret equals 0 otherwise.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 13; PDF label 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
13
For δ = δ0.5, it follows that Psa(YB(δ(wN)) = 0) = 0.5a + 0.5. Therefore, regret
equals 1 if a < 1/2 and 0 otherwise. For δ = δES, we can evaluate Psa(YB(δ(wN)) = 0)
given the formulas above. The results do not depend on N0 > 0. We find that for a
given N1 regret equals 1 if a ∈[l(N1),0.5) and 0 otherwise, for an l(N1) < 0.5. For
example, if N1 = 10, 20, 30, 40, and 50, l(N1) = 0.394, 0.416, 0.426, 0.433, and
0.437, respectively.
3. In part (iii) of Proposition 1, in the case qα(Y0) < 1/2, we could not rule out
that there are other minimax regret rules besides δ1 ≡1 when N > 0. When N = 0,
it is obvious that δ1 is the unique minimax rule. A minimax regret treatment rule, if
it is not unique, may be inadmissible. In the case of “testing an innovation,” δ0 ≡0
(when qα(Y0) > 1/2) is admissible, but we have not determined whether that is
true for δ1 (when qα(Y0) < 1/2) and for δ0.5 ≡1/2 (when qα(Y0) = 1/2).
4. In case Y0,Y1 ∈(0,1) rather than Y0,Y1 ∈[0,1], maxs∈S R(δ,s) does not
generally exist when S denotes the set of all joint probability distributions over
the potential outcomes for Y0,Y1 ∈(0,1). For example, in cases (i) and (ii), nature
choosing only distributions with support on [ε,1 −ε] for some small ε > 0, it
can generate regret of 1 −2ε and therefore sups∈S R(δ,s) = 1 for the unrestricted
space of distributions for Y0,Y1 ∈(0,1). This result can be proven using the exact
same proof technique as for Proposition 1. Therefore, if minimax rules are defined
with sups∈S R(δ,s) (as we do in (2.7)) rather than maxs∈S R(δ,s), the results in
Proposition 1(i) and (ii) continue to hold.
5. If Y0,Y1 ∈[0,∞) rather than Y0,Y1 ∈[0,1], then maxs∈S R(δ,s) does not
typically exist when S denotes the set of all joint probability distributions over the
potential outcomes for Y0,Y1 ∈[0,∞). For example, in cases (i) and (ii), nature
choosing only distributions with support on [0,M] for M > 0, it can generate
regret of M and therefore sups∈S R(δ,s) = ∞when S denotes the set of all joint
distributions for Y0,Y1 ∈[0,∞). This result can be proven using the exact same
proof technique as for Proposition 1. Therefore, if minimax rules are defined with
sups∈S R(δ,s) (as we do in (2.7)) rather than maxs∈S R(δ,s), then for α ∈(0,1), any
treatment rule is minimax regret optimal in cases (i) and (ii).
Given the limit experiment results in Hirano and Porter (2009), it would also
be interesting to study the case where potential outcomes are restricted to be
normally distributed. However, in that case, one would need to employ other proof
techniques than the ones used in the current article.
Restrictions on nature’s action space: In what follows, we impose various
restrictions on nature’s action space and study the implications on the results
obtained in Proposition 1. For simplicity, assume α ∈(0,1).
Corollary 1. (a) The results in Proposition 1 (i) and (ii) remain valid when
rather than Y0,Y1 ∈[0,1], the setup is altered to Y0,Y1 ∈{0,1}. Similarly, the result
in (iii) remains valid if the distributions of Y0 and Y1 are restricted to be discrete
and supported on at most N +1 points in [0,1].
(b) If S equals the set of distributions for Y0,Y1 ∈[0,1] whose marginals are all
continuous (with respect to Lebesgue measure), then Proposition 1 continues to
hold.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 14; PDF label 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
14
PATRIK GUGGENBERGER ET AL.
Comments. 1. Corollary 1(a) is a direct corollary from the proof of Proposi-
tion 1. In the proof of Proposition 1(i) and (ii), only Bernoulli distributions are
used for nature, while in part (iii), only discrete distributions are used.
2. Corollary 1(b) considers the case where nature is restricted to continuous
distributions. We have seen in Proposition 1 that in cases (i) and (ii) any treatment
rule δ ∈D is minimax and maxs∈S R(δ,s) = 1. Because without point masses, it
is impossible for a random variable to have α-quantile equal to 0, it follows that
R(δ,s) is always strictly smaller than 1 for any pair (δ,s) when s is continuous with
respect to Lebesgue measure. The main construction in the proof of Proposition 1
still goes through when one considers a sequence of continuous distributions that
converge to the Bernoulli distributions that are used in that proof. As a technical
detail, it is important to use sups∈S R(δ,s) rather than maxs∈S R(δ,s) in the definition
of regret, because maxs∈S R(δ,s) would not exist in the case considered here. One
can establish that sups∈S R(δ,s) = 1 for any treatment rule δ ∈D.
3. In the case of “testing an innovation,” a restriction on nature’s action space
occurs if one assumes that the entire distribution of Y0 is known, not just its
α-quantile. Namely, in that case, the set S consists of all possible distributions s for
Y1 ∈[0,1] (while the distribution of Y0 is given). The analysis of that problem is
more difficult. Denote by FY0 and qα(Y0) the cdf and α-quantile of Y0, respectively.
Take r = 0 in (2.5) and assume FY0(qα(Y0)) > α. Consider the case N = 0 in
which case a treatment rule δ ∈[0,1] denotes the treatment probability. Under
these assumptions, the following statements hold.
Denote by q(δ) the smallest q ∈[0,qα(Y0)] such that
δ +(1−δ)FY0(q) ≥α.
(2.23)
Then, when qα(Y0) < 1/2, δ1 ≡1 is the only minimax regret rule and
maxs∈S R(δ1,s) = qα(Y0). When qα(Y0) = 1/2, any δ ∈[0,1] is minimax regret
with maximal regret equal to qα(Y0). Finally, when qα(Y0) > 1/2, δ ∈[0,1] is
minimax regret iff
qα(Y0)−q(δ) ≤1−qα(Y0).
(2.24)
Given that qα(Y0) −q(δ) is a weakly increasing function in δ, if we denote by
δ∗∈[0,1] an intersection of qα(Y0) −q(δ) and 1−qα(Y0), then any δ ∈[0,δ∗] is
minimax regret and for those δ we have maxs∈S R(δ,s) = 1−qα(Y0).
In the Appendix, we give a proof of the statements made above. The results
for the case qα(Y0) > 1/2 are partly in contrast to Proposition 1(iii) where there
is a unique minimax regret rule. However, maximal regret is the same here as in
Proposition 1(iii). We have not yet generalized the results to arbitrary sample sizes
N > 0 and to the case FY0(qα(Y0)) = α.
2.3. Finite Sample Simulation
For the case of “testing an innovation,” Proposition 1(iii) establishes that the min-
imax regret criterion when applied to α-quantiles does not favor data-driven rules.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 15; PDF label 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
15
In this section, we conduct a simulation experiment to juxtapose the pointwise
(in s) regret of the data-driven empirical success rule δES, defined (in the case of
“testing an innovation”) by
δES(w) = I(qα(Y1,w) > qα(Y0))+.5I(qα(Y1,w) = qα(Y0)),
(2.25)
where qα(Y1,w) denotes the α-sample quantile of Y1 for the sample w, with the
regret of the minimax regret rule δ1 ≡1 (in the case when qα(Y0) ≤1/2), δ0.5 ≡1/2
(in the case, when qα(Y0) = 1/2), and the minimax regret rule δ0 ≡0 (in the case,
when qα(Y0) ≥1/2).
Obviously, when simulating regret we cannot possibly include all states of
nature s ∈S. For the simulation experiment, we create a “sufficiently rich” subset
of distributions for (Y0,Y1). Namely, for some n,w ∈N, we consider the set of
states of nature SE = SE(n,w) that consists of all discrete distributions s for Y1
supported on a grid
{0,1/n,2/n,...,n/n}
(2.26)
with probabilities
Ps(Y1 = j/n)
(2.27)
being of the form i/w, i = 0,...,w; while for the distribution of Y0, we consider
two choices, namely,
I) Y0 ∈{0,qα(Y0)} with P(Y0 = 0) = α −ε and P(Y0 = qα(Y0)) = 1 −(α −ε)
for ε = 0.000001, and
II) Y0 being continuously distributed on [0,1] with density f(x) equal to α/qα(Y0)
for x ≤qα(Y0) and equal to (1−α)/(1−qα(Y0)) otherwise. Note that, in both I) and
II), the α-quantile of Y0, qs,α(Y0), equals qα(Y0). We report results for all choices of
α ∈{0.1,0.5,0.9}, qα(Y0) ∈{0.1,0.5,0.9}, sample size N = 30, and (n,w) = (6,12).
The latter leads to SE having cardinality 18,564.
For the given choices of n,w, and N and for each choice of α and qα(Y0), for each
state of nature s ∈SE(n,w) and one (of the two possible) choice of distribution for
Y0 we simulate regret for the four treatment rules δES, δ1, δ0.5, and δ0 by generating
R = 100K samples of size N by drawing i.i.d. observations of the distribution of Y1.
We use r = 0 when simulating α-quantiles of the outcome distribution under the
various treatment rules. We analytically calculate α-quantiles for Y1 for YB(δ0.5),
and likewise use the true α-quantile qα(Y0) of Y0 when calculating regret. For a
given treatment rule δ and a given state of nature s, regret is calculated as R(δ,s) =
max{qα(Y0),qs,α(Y1)}−qs,α(YB(δ(w))).
We compare the treatment rules along several dimensions, namely,
a) mean regret over all 18,564 states of nature s ∈SE(n,w),
b) maximal regret over all states of nature s ∈SE(n,w),
c) minimal regret over all states of nature s ∈SE(n,w), and
d) the proportion of s ∈SE(n,w) for which regret for the empirical success rule
δES is smaller than regret for each one of its three competitors.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 16; PDF label 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
16
PATRIK GUGGENBERGER ET AL.
Table 1. Maximal and mean regret over all 18,564 states of nature s ∈SE(6,12)
for four different treatment rules.
Case I)
δES
δ1
δ0.5
δ0
δES
δ1
δ0.5
δ0
δES
δ1
δ0.5
δ0
α
0.1
0.1
0.1
0.1
0.5
0.5
0.5
0.5
0.9
0.9
0.9
0.9
qα(Y0) = 0.1
max
0.9
0.1
0.9
0.9
0.1
0.1
0.9
0.9
0.1
0.1
0.9
0.9
mean
0.08
0.04
0.14
0.1
0.01
0.01
0.37
0.37
0
0
0.08
0.75
qα(Y0) = 0.5
max
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
mean
0.43
0.35
0.36
0
0.13
0.11
0.15
0.08
0.01
0
0.07
0.35
qα(Y0) = 0.9
max
0.9
0.9
0.9
0.1
0.9
0.9
0.9
0.1
0.9
0.9
0.9
0.1
mean
0.9
0.75
0.75
0
0.8
0.44
0.37
0
0.33
0.1
0.11
0.04
Case II)
δES
δ1
δ0.5
δ0
δES
δ1
δ0.5
δ0
δES
δ1
δ0.5
δ0
α
0.1
0.1
0.1
0.1
0.5
0.5
0.5
0.5
0.9
0.9
0.9
0.9
qα(Y0) = 0.1
max
0.84
0.1
0.9
0.9
0.1
0.1
0.9
0.9
0
0.1
0.9
0.9
mean
0.05
0.04
0.14
0.1
0.01
0.01
0.37
0.37
0
0
0.08
0.75
qα(Y0) = 0.5
max
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.02
0.5
0.5
0.5
mean
0.06
0.35
0.36
0
0.08
0.11
0.15
0.08
0
0
0.07
0.35
qα(Y0) = 0.9
max
0.9
0.9
0.9
0.1
0.9
0.9
0.9
0.1
0.03
0.9
0.9
0.1
mean
0
0.75
0.75
0
0.04
0.44
0.37
0
0.01
0.1
0.11
0.04
Just for clarity, in a), for each treatment rule, we sum up its regret over all 18,564
states of nature s ∈SE(n,w) and then report that sum divided by 18,564. For a
given s ∈SE(n,w), in our simulations, we interpret regret of δES as smaller than
regret of another rule, say δ0, if the simulated regret of δES is smaller than the
simulated regret of the rule δ0 minus a threshold of ξ. If instead the simulated
regret of δES falls into the interval [(simulated regret of δ0)−ξ,(simulated regret of
δ0)+ξ], we record regrets of the two rules as equal for that state of nature. We take
ξ = 0.00000001 below. Similarly, when programming the empirical success rule in
(2.25), the event “ qα(Y1,w) = qα(Y0)” is implemented as the simulated α-quantile
of Y1 falling into the interval [qα(Y0)−ξ,qα(Y0)+ξ].
All reported results are rounded to the second digit after the comma and so a
reported zero could be as large as 0.004.
In Tables 1 and 2, we do not include results for c) because those results turn
out to be equal to zero for all treatment rules and all designs except for δ0.5 when
qα(Y0) ∈{0.1,0.9} in which case minimal regret equals 0.067 for all choices of α
and both choices of distributions for Y0.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 17; PDF label 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
17
Table 2. Proportion (in %) of states s ∈SE(6,12) for which regret for the
empirical success rule δES is smaller than regret of non-data rules δ ∈{δ1,δ0.5,δ0}.
Case I)
δ1
δ0.5
δ0
δ1
δ0.5
δ0
δ1
δ0.5
δ0
α
0.1
0.1
0.1
0.5
0.5
0.5
0.9
0.9
0.9
qα(Y0) = 0.1
Prop(R(δES,s) < R(δ,s))
0
33.3
33.3
0
92.5
92.5
0
33.3
100
Prop(R(δES,s) ≤R(δ,s))
76.5
100
56.9
97.5
97.5
95.0
100
100
100
qα(Y0) = 0.5
Prop(R(δES,s) < R(δ,s))
0
0.5
0.5
3.0
30.8
30.8
0
31.6
91.7
Prop(R(δES,s) ≤R(δ,s))
61.0
62.7
8.3
90.7
76.2
58.6
99.5
99.5
97.8
qα(Y0) = 0.9
Prop(R(δES,s) < R(δ,s))
0
0
0
0
2.5
2.5
0
16.2
43.1
Prop(R(δES,s) ≤R(δ,s))
43.3
43.4
0
21.0
11.7
2.5
66.7
66.7
43.1
Case II)
δ1
δ0.5
δ0
δ1
δ0.5
δ0
δ1
δ0.5
δ0
α
0.1
0.1
0.1
0.5
0.5
0.5
0.9
0.9
0.9
qα(Y0) = 0.1
Prop(R(δES,s) < R(δ,s))
16.2
73.0
73.0
0.3
95.3
95.3
0
33.4
100
Prop(R(δES,s) ≤R(δ,s))
76.5
100
73.0
100
97.5
95.3
100
100
100
qα(Y0) = 0.5
Prop(R(δES,s) < R(δ,s))
71.2
73.4
71.6
13.6
40.7
39.8
2.2
33.8
91.7
Prop(R(δES,s) ≤R(δ,s))
98.3
100
79.6
100
86.6
65.3
100
100
97.8
qα(Y0) = 0.9
Prop(R(δES,s) < R(δ,s))
99.5
99.6
99.6
84.0
82.1
75.6
56.9
73.0
43.1
Prop(R(δES,s) ≤R(δ,s))
100
100
99.6
100
95.7
75.6
100
100
43.1
Table 1 provides results for maximal and mean regret over all 18,564 states of
nature s ∈SE(6,12) for the four different treatment rules. Results for rules that are
minimax regret in a given setting are reported in bold.
We first discuss results for maximal regret. The treatment rules that are known
to be minimax regret for unrestricted S also have smallest maximal regret over
SE(n,w) (relative to the other treatment rules considered here) for all cases except
for case II) with α = 0.9, when qα(Y0) = 0.1 (in which case, δES has smaller
maximal regret than the optimal rule δ1), when qα(Y0) = 0.5 (in which case,
it is known that all four rules are optimal but in finite samples for SE(n,w)
again δES does best), and finally when qα(Y0) = 0.9 (in which case, δES has
smaller maximal regret than the optimal rule δ0). The explanation is of course
that SE(n,w) does not contain those states of nature that would inflict the highest
regret on δES (like the particular Bernoulli and discrete distributions for Y0 and
Y1, respectively, that are used in the proof of Proposition 1(iii)). Furthermore,
reported finite sample maximal regret over SE(n,w) for the optimal rules matches
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 18; PDF label 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
18
PATRIK GUGGENBERGER ET AL.
the theoretical value min{qα(Y0),1−qα(Y0)} reported in Proposition 1(iii) except
for case II) with α = 0.9 when qα(Y0) = 0.5 where the optimal rule δES has maximal
regret smaller than 0.5 (which occurs, again, because SE(n,w) is not rich enough).
An open question from Proposition 1(iii) is whether for qα(Y0) < 0.5 other
minimax regret rules besides δ1 might exist. The simulations for qα(Y0) = 0.1 are
compatible with the possibility that when α = 0.5 or 0.9 also δES might be minimax
regret.
We next discuss results for mean regret. In most cases where qα(Y0) ∈{0.1,0.9}
in which case either δ0 or δ1 are minimax regret, their mean performance is also
best (or very close to best) among the four treatment rules. On the other hand, when
qα(Y0) = 0.5 (in which case all four treatment rules are minimax regret according
to Proposition 1(iii)) we see huge differences in mean performance across the
four treatment rules for a given case I) or II) and α, but also huge differences in
performance for a given treatment rule and α across cases I) and II). With respect
to the former point, in case I), when α = 0.1, mean regret for the four rules is in
the interval [0,0.43]. With regards to the latter point, for example, for δES, when
α = 0.1, mean regret equals 0.43 and 0.06, in cases I) and II), respectively.
Differences across cases I) and II) are also often huge for other quantiles. For
example, again for δES, when qα(Y0) = 0.9 and α = 0.1, mean regret equals 0.9
and 0, in cases I) and II), respectively. (Recall that we round results to the second
digit. When qα(Y0) = 0.9 and α = 0.1, there are not many distributions for Y1 in
SE(n,w) that have an α-quantile that exceeds 0.9.)
We next discuss the results for exercise d) contained in Table 2 where we report
the proportion of the 18,564 states of nature s ∈SE(6,12) for which the regret of
δES is smaller than the regret of δ where we consider all δ from the set of no-data
rules {δ1,δ.5,δ0}. The results indicate that for many states s, choices of qα(Y0),
α, and the distribution for Y0, R(δES,s), and R(δ,s) are very close which leads to
numerically unstable results. To deal with the instability, we introduce the buffer
ξ as explained above and Prop(R(δES,s) < R(δ,s)) and Prop(R(δES,s) ≤R(δ,s))
in Table 2 represent the proportion of states s for which R(δES,s) < R(δ,s) −ξ
and R(δES,s) < R(δ,s)+ξ, respectively. Those two proportions can be drastically
different, suggesting that, in many scenarios, regrets for δES and δ are (virtually)
identical. According to the measure Prop(R(δES,s) ≤R(δ,s)), maybe somewhat
surprisingly given the results from Table 1, δES is to be preferred over the other
three rules in all scenarios considered in Case II) (except the case α = qα(Y0) =
0.9 for δ0) and in the majority of scenarios in Case I) (except compared to δ0 when
qα(Y0) = 0.5, α = 0.1 and except for most cases with qα(Y0) = 0.9 and all three
rules ). Quite often Prop(R(δES,s) ≤R(δ,s)) is reported as higher than 95%, but
the improvement in regret for many states of nature is minuscule. For example,
compared to δ0.5 in Case I) with α = qα(Y0) = 0.1 only in 33.3% of the cases
(R(δES,s) < R(δ,s)) while for 100% of the cases (R(δES,s) ≤R(δ,s)) implying
that the regret of δES in 66.7% of the cases is at most ξ smaller than the regret
of δ0.5.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 19; PDF label 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
19
3. TREATMENT CHOICE WITH A COVARIATE
As in Stoye (2009) we next allow for a discrete covariate X ∈X = {x1,...,xK}
that is observed both in the sample and in the treatment data. Outcomes Yt,x now
carry a double subindex to indicate the treatment status t ∈{0,1} and the value of
the covariate x ∈X. It is assumed that xk occurs with positive probability for each
k = 1,...,K. Denote by FX the distribution of X. A state of the world s ∈S now
represents a joint distribution for (Yt,x)t∈{0,1}, x∈X .
A sample w = wN now consists of realizations (ti,xi,yi) for i = 1,...,N of
(T,X,YT,X), where yi is a realization of Yti,xi, and we consider again sampling
designs (i)–(iii) from Section 2.2. It is assumed that xi, i = 1,...,N, are i.i.d. and
FX is independent of s and T.
In design (i), “fixed number of treated/untreated units,” there are N0 observa-
tions (0,xi,yi) with yi being i.i.d. draws of Y0,xi, i = 1,...,N0 and N1 = N −N0
observations (1,xi,yi) with yi being i.i.d. draws of Y1,xi, i = N0 + 1,...,N. Note
that there are not typically equally many treated and untreated observations for
each covariate xk, k = 1,...,K. In fact, there may be zero observations altogether
in the sample for a given xk.
In design (ii), “random sampling,” the observations (ti,xi,yi) for i = 1,...,N
are i.i.d. realizations of (T,X,YT,X) with P(Ti = 1) = p ∈(0,1) with T,X, and the
potential outcomes (whose distribution is s) being independent of each other.
In design (iii), “testing an innovation,” (1,xi,yi) for i = 1,...,N are observed,
where yi is an independent realization of Y1,xi, for i = 1,...,N.
In design (iii), we assume the DM knows the α-quantile, denoted by qα(Y0,X),
of Y0,X and nature can choose from joint distributions s ∈S for (Yt,x)t∈{0,1}, x∈X
such that the α-quantile of Y0,X equals qα(Y0,X).
A treatment rule δ maps a sample wN onto treatment probabilities for each xk for
k = 1,...,K, that is, δ(wN) ∈[0,1]K, where the k-th component of δ(wN) indicates
the treatment probability for individuals with covariate xk for k = 1,...,K. Denote
the k-th component of δ(wN) by δxk(wN) for k = 1,...,K. With some abuse of
notation, for each design (i)–(iii), we denote the set of all treatment rules by the
same symbol D (even though it means something different for different designs).
The object of interest is
u(δ,s) = qs,FX,α(YB(δX(wN)),X)
(3.1)
the α-quantile of the outcome distribution. With that definition, regret is
then defined formally analogously to the setup without a covariate, namely,
R(δ,s) = supd∈D u(d,s)−u(δ,s). Alternatively, one could focus on the α-quantile
of the outcome distribution for a particular covariate only, x1 say, ux1(δ,s) =
qs,FX,α(YB(δx1(wN)),x1) and obtain analogous results to the ones in Corollary 2 below.
If the space of probability distributions for nature S is unrestricted and thus
equals the space of all distributions for (Yt,x)t∈{0,1}, x∈X one can show in designs
(i) and (ii) (as an implication of the proof of Proposition 1) that for every
treatment rule δ maximal regret over S equals 1, maxs∈S R(δ,s) = 1. This result then
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 20; PDF label 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
20
PATRIK GUGGENBERGER ET AL.
immediately implies that every treatment rule is minimax regret. The corollary (to
Proposition 1) that follows gives a stronger result; it shows that maximal regret
continues to be 1 even if certain restrictions are imposed on S. For simplicity of
the presentation, assume α ∈(0,1).
Corollary 2. (i) and (ii). In the case of the designs “fixed number
of treated/untreated units” and “random sampling” for any treatment rule
δ ∈D, maxs∈S R(δ,s) = 1 if S includes as a subset all joint distributions
for (Yt,x)t∈{0,1}, x∈X whose marginals are independent Bernoulli distributions.
Therefore, any δ ∈D is minimax regret.
(iii) In the case of “testing an innovation” assume the DM knows the
α-quantile, denoted by qα(Y0,X), of Y0,X. If qα(Y0,X) = 1/2, then any δ ∈D is
minimax regret; if qα(Y0,X) > 1/2, then δ0 = 0 is the unique minimax regret
rule, and if qα(Y0,X) < 1/2, then δ1 = 1 is a minimax regret rule. In each case,
maxs∈SR(δ,s) = min{qα(Y0,X),1−qα(Y0,X)}.
Comments: 1. Various variants could be considered in design (iii). For example,
one could instead assume that the joint distribution (Y0,x)x∈X is known (in which
case nature only chooses a joint distribution for (Y1,x)x∈X ) or one could assume
that the DM knows the vector (qα(Y0,x1),...,qα(Y0,xK)) of α-quantiles of all the
marginal distributions (Y0,x)x∈X and nature can choose from joint distributions s ∈
S for (Yt,x)t∈{0,1}, x∈X such that all the marginals (Y0,x)x∈X have the required α-
quantiles.
2. One could also consider alternative sampling designs (i)–(iii), where in the
sampling stage, rather than being randomly assigned, the values of the covariate
X are assigned deterministically, as is done for treatment status in design (i). This
could be referred to as “stratified sampling.”
For brevity, we do not explicitly deal with these variations.
4. CONCLUSION
We derive minimax regret treatment rules in finite samples when an α-quantile
of the outcome distribution is the focus of interest. We establish that when the
sample i) consists of a fixed number of untreated/treated units or ii) is generated
via random treatment assignment then all treatment rules are minimax regret and
therefore the minimax regret criterion is not helpful in singling out a recommended
treatment rule. Given that the same shortcoming applies to the max–min criterion,
an important question concerns finding a meaningful criterion in this setup based
on which an optimal treatment rule should be chosen. The idea from Montiel Olea
et al. (2026) to look for rules that randomize “the least” in a situation where there
are multiple minimax regret rules would not lead to a unique rule in our setup
because in cases i) and ii) both δ0 and δ1 are minimax regret and never randomize.
Given all these facts, it seems reasonable to simply adopt a rule that is minimax
regret optimal when regret is based on the notion of expected welfare (in particular,
such a rule is optimal according to criterion (2.7)).
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 21; PDF label 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
21
We also establish that when iii) the sample consists of only realizations from
the treated population while the α-quantile of the untreated population is known,
never treating is the unique minimax rule if the known quantile exceeds 0.5, while
always treating is a minimax rule if that quantile is strictly smaller than 0.5, and
finally, if the quantile equals 0.5, then any treatment rule is minimax regret. It
follows that based on the minimax regret criterion, rules that take the data into
consideration are never strictly preferred.
An interesting but quite difficult extension concerns applying the minimax regret
criterion in finite samples to CVaR, defined as Ss,α(Y) := α−1Es[Y1(Y ≤qs,α(Y))]
for a random variable Y rather than to the α-quantile of Y.9 Another extension
involves modifying the analysis in Huang and Guggenberger (2025) that considers
pilot data from a setup where the objective is expected outcome to one where the
objective is a quantile.
A. APPENDIX
A.1. Proof of Proposition 1
We use the notation Ps(A) to denote the probability of the event A when nature chooses the
state of the world s ∈S and we write shorthand w instead of wN for the sample of size N.
Note that, for a state of the world s ∈S and treatment rule δ ∈D,
Ps(YB(δ(w)) ≤q)
= Ps(B(δ(w)) = 1 & Y1 ≤q)+Ps(B(δ(w)) = 0 & Y0 ≤q)
= Ps(B(δ(w)) = 1)Ps(Y1 ≤q)+Ps(B(δ(w)) = 0)Ps(Y0 ≤q)
(A.1)
and analogously for Ps(YB(δ(w)) ≥q), where the second equality uses independence. By
definition, an α-quantile q of YB(δ(w)) satisfies Ps(YB(δ(w)) ≤q) ≥α and Ps(YB(δ(w)) ≥
q) ≥1−α.
The proofs of (i) and (ii) proceed by showing that for any treatment rule δ ∈D, there
exists a state of the world sδ ∈S for which R(δ,sδ) = 1. Because it is also true that for any
treatment rule δ ∈D, maxs∈S R(δ,s) ≤1, it follows that any treatment rule is minimax.
Lemma 3(ii) below establishes the (unsurprising) result that for any arbitrary s ∈S,
max
d∈D u(d,s) = max
d∈D qs,α(YB(d(w))) = max{qs,α(Y0),qs,α(Y1)}.
(A.2)
This result implies a simplified formula for R(δ,s) that we will use from now on.
In the proof of (i) and (ii) that follows, for any given treatment rule δ ∈D, we will
construct an sδ ∈S for which max{qsδ,α(Y0),qsδ,α(Y1)} = 1 and u(δ,sδ) = 0. Namely,
throughout the proof of (i) and (ii) for an arbitrary treatment rule δ ∈D, we construct an
sδ ∈S whose independent marginals for Y0 and Y1 are Bernoulli (supported on {0,1}) and
for which R(δ,sδ) = 1. Under these restrictions, the distribution sδ for (Y0,Y1) is then fully
9Or, using the more general definition Ss,α(Y) := supγ ∈R{γ −α−1Es[γ −Y]+}, see Qi et al. (2023), where [Y]+ =
max{Y,0} denotes the positive part of Y.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 22; PDF label 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
22
PATRIK GUGGENBERGER ET AL.
defined by
a0 := Psδ(Y0 = 0) and a1 := Psδ(Y1 = 0).
(A.3)
The α-quantiles of Y0, Y1, and YB(δ(w)) in the constructions below will be unique when
α ∈(0,1). Therefore, the particular value of r ∈[0,1] has no impact on the results.
Part (i). As in (A.1) and with sδ just defined
Psδ(YB(δ(w)) = 0)
= 
u∈{0,1}N0

v∈{0,1}N1 aN0−u
0
(1−a0)uaN1−v
1
(1−a1)v
[δ((u′,v′)′)a1 +(1−δ((u′,v′)′))a0]
= N0
i=0
N1
j=0aN0−i
0
(1−a0)iaN1−j
1
(1−a1)j

δi,ja1 +
N0
i
N1
j

−δi,j

a0

,
(A.4)
where for a vector u ∈{0,1}N0, we denote by u ∈N the sum of its components (i.e., the
number of 1’s in the vector) and similarly for other vectors, and
δi,j := 
u∈{0,1}N0,v∈{0,1}N1
u=i and v=j
δ((u′,v′)′).
(A.5)
Note that in the second line of (A.4), the term aN0−u
0
(1−a0)uaN1−v
1
(1−a1)v is the proba-
bility to observe particular vectors u and v while the term δ((u′,v′)′)a1 +(1−δ((u′,v′)′))a0
is the probability that an outcome 0 is reached when the sample consists of u and v.
Assume α ∈(0,1) first. When in the definition of sδ in (A.3), we take (a0,a1) = (1,α)
we obtain from (A.4),
Psδ(YB(δ(w)) = 0) = N1
j=0αN1−j(1−α)j

δ0,jα +
N1
j

−δ0,j

= N1
j=0[αN1−j(1−α)j(α −1)]δ0,j +N1
j=0αN1−j(1−α)j
N1
j

.
(A.6)
Given that the coefficient αN1−j(1−α)j(α −1) in front of δ0,j is negative (noting that α ∈
(0,1)), it follows that Psδ(YB(δ(w)) = 0) is strictly decreasing in each δ0,j. Therefore, we
obtain
Psδ(YB(δ(w)) = 0) ≥N1
j=0αN1−j(1−α)jα
N1
j

= α,
(A.7)
where the right-hand bound follows from (A.6) by replacing δ0,j by its maximal value
N1
j

.
Consider first the case where at least one of the δ0,j (for j = 0,...,N1) is smaller
than
N1
j

. In that case, it follows that Psδ(YB(δ(w)) = 0) > α. Furthermore, notice that
Psδ(YB(δ(w)) = 0) is continuous in a1 and therefore Psδ(YB(δ(w)) = 0) > α when instead of
(a0,a1) = (1,α), sδ is taken as (a0,a1) = (1,α −ε) for some small enough ε > 0. But then
for that choice of sδ, u(δ,sδ) = 0 and max{qsδ,α(Y0),qsδ,α(Y1)} = qsδ,α(Y1) = 1. Therefore,
R(δ,sδ) = 1 as desired.
Next, consider the case where δ0,j =
N1
j

for all j = 0,...,N1 (which implies that
δ((0N0′,v′)′) = 1 for all v ∈{0,1}N1, where 0N0 denotes an N0-dimensional column vector
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 23; PDF label 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
23
of zeros). In that case, from (A.4), we obtain with (a0,a1) = (α,1)
Psδ(YB(δ(w)) = 0)
= N0
i=0αN0−i(1−α)i

δi,0 +
N0
i

−δi,0

)α

= αN0 +N0
i=1αN0−i(1−α)i

δi,0(1−α)+
N0
i

α

≥αN0 +αN0
i=1αN0−i(1−α)i
N0
i

= αN0 +α(1−αN0)
> α,
(A.8)
where the second equality uses δ0,0 =
N1
0

= 1, the first inequality follows from setting
δi,0 = 0 for i = 1,...,N0, and the second inequality follows from α ∈(0,1). The remainder
of the proof is as above, namely, by continuity Psδ(YB(δ(w)) = 0) > α for an sδ with
(a0,a1) = (α −ε,1) for a small enough ε > 0. For such sδ, regret equals 1.
Now consider the case α = 0. Take any δ and define sδ by setting a0 = Psδ(Y0 = 0) = 0
and a1 = Psδ(Y1 = 0) = ε > 0. Then, qsδ,0(Y1) = 0 and any q ∈[0,1] satisfies the condition
in (2.4) for X = Y0. Thus, with r = 1, the 0-quantile of Y0 equals 1. Thus, in order for regret
to equal 1 under sδ, it is enough to establish that the 0-quantile of YB(δ(w)) equals 0. The
latter follows if Psδ(YB(δ(w)) = 0) > 0. From (A.4),
Psδ(YB(δ(w)) = 0) = εN1
j=0εN1−j(1−ε)jδN0,j
(A.9)
with δN0,j = 
v∈{0,1}N1, v=jδ((1,...,1,v′)′). If Psδ(YB(δ(w)) = 0) > 0, the proof is
complete. If not, and Psδ(YB(δ(w)) = 0) = 0, it must be that δ((1,...,1,v′)′) = 0 for all v ∈
{0,1}N1. If δ((1,...,1,v′)′) = 0 for all v ∈{0,1}N1, define s′
δ by setting a0 = Ps′
δ(Y0 = 0) = ε
and a1 = Ps′
δ(Y1 = 0) = 0. Then, by (A.4), with δi,N1 = 
u∈{0,1}N0,u=iδ((u′,1,...,1)′)
≤
N0
i

,
Ps′
δ(YB(δ(w)) = 0) = εN0
i=0εN0−i(1−ε)i
N0
i

−δi,N1

.
(A.10)
But 1−δ((1,...,1,v′)′) = 1 for all v ∈{0,1}N1 implies
N0
i

−δi,N1 = 1 when i = N0. Thus,
by (A.10), Ps′
δ(YB(δ(w)) = 0) > 0. But, the latter implies that regret equals 1 under s′
δ.
Finally, consider the case (α = 1 and r = 0). Consider a treatment rule δ that is not equal
to 1 wp1 and not equal to 0 wp1. We will show that maxs∈S R(δ,s) = 0. To see this, fix
s ∈S. By the definition of an α-quantile in (2.4) and the choice r = 0 note that, for any
q < qs,1(Y0), it must be that Ps(Y0 ≤q) < 1, and likewise for any q < qs,1(Y1), it must be
that Ps(Y1 ≤q) < 1. Therefore, using (A.1), for any q < max{qs,1(Y0),qs,1(Y1)}, we have
Ps(YB(δ(w)) ≤q) = Ps(B(δ(w)) = 1)Ps(Y1 ≤q)+Ps(B(δ(w)) = 0)Ps(Y0 ≤q) < 1,
which implies q < qs,1(YB(δ(w))). By Lemma 3, qs,1(YB(δ(w))) ≤max{qs,1(Y0),qs,1(Y1)}
and thus qs,1(YB(δ(w))) = max{qs,1(Y0),qs,1(Y1)}. But that implies that R(δ,s) = 0 and
because s ∈S that proves the desired result .
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 24; PDF label 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
24
PATRIK GUGGENBERGER ET AL.
Part (ii). The proof of (ii) is similar to case (i). Again we start off with α ∈(0,1) and
define sδ as in (A.3). We obtain
Psδ(YB(δ(w)) = 0)
= 
t=(t1,...,tN)′∈{0,1}N,
y=(yt1,...,ytN )′∈{0,1}N
pt(1−p)N−taN0ty
0
(1−a0)N−t−N0tyaN1ty
1
(1−a1)t−N1ty
×[δ((t,y))a1 +(1−δ((t,y)))a0]
= 
T=0,...,N,
i=0,...,N−T,
j=0,...,T
pT(1−p)N−Tai
0(1−a0)N−T−iaj
1(1−a1)T−j
×[δT,i,ja1 +(
N
T
N −T
i
T
j

−δT,i,j)a0]
= 
T=0,...,N,
i=0,...,N−T,
j=0,...,T
pT(1−p)N−Tai
0(1−a0)N−T−iaj
1(1−a1)T−j
×[(a1 −a0)δT,i,j +
N
T
N −T
i
T
j

a0],
(A.11)
where for given vectors t ∈{0,1}N and y ∈{0,1}N, N0ty denotes the number of yti, i =
1,...,N, for which yti = 0 and ti = 0, N1ty is the number of yti, i = 1,...,N, for which yti = 0
and ti = 1, where again t ∈N for a vector t ∈{0,1}N denotes the sum of its components,
and
δT,i,j := 
t=(t1,...,tN)′∈{0,1}N,
y=(yt1,...,ytN )′∈{0,1}N,
t=T, N0ty=i, N1ty=j
δ((t,y)).
(A.12)
Note that N0ty ≤N −t and N1ty ≤t. In the second line of (A.11), the factor pt(1 −p)N−t
captures the probability of observing exactly t treatments and N −t controls in the sample,
while the factor aN0ty
0
(1 −a0)N−t−N0ty captures the probability that among the N −t
observations from the control group exactly N0ty zeros are observed, while, finally, the
factor aN1ty
1
(1−a1)t−N1ty captures the probability that among the t observations from treated
individuals exactly N1ty zeros are observed.
Evaluating Psδ(YB(δ(w)) = 0) when sδ takes (a0,a1) = (1,α), we obtain
Psδ(YB(δ(w)) = 0) = 
T=0,...,N,
j=0,...,T
pT(1−p)N−Tαj(1−α)T−j
[(α −1)δT,N−T,j +
N
T
T
j

].
(A.13)
Because (α −1) < 0 and α > 0, Psδ(YB(δ(w)) = 0) is strictly decreasing in δT,N−T,j for all
T = 0,...,N and j = 0,...,T and is minimized when δT,N−T,j takes on its maximal value
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 25; PDF label 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
25
N
T
T
j

. Therefore,
Psδ(YB(δ(w)) = 0) ≥
T=0,...,N,
j=0,...,T
pT(1−p)N−Tαj(1−α)T−jα
N
T
T
j

= α
T=0,...,N
N
T

pT(1−p)N−T
j=0,...,T
T
j

αj(1−α)T−j
= α.
(A.14)
If δT,N−T,j <
N
T
T
j

for any T = 0,...,N and j = 0,...,T, then by an argument as in
part (i), it follows that an sδ with (a0,a1) = (1,α −ε) for ε > 0 small enough leads to
regret of 1. This holds because for that sδ we have qsδ,α(Y0) = 0, qsδ,α(Y1) = 1, and
qsδ,α(YB(δ(w))) = 0.
If on the other hand, δT,N−T,j =
N
T
T
j

for all T = 0,...,N and j = 0,...,T, then, as in
part (i), one can show that sδ defined by (a0,a1) = (α −ε,1) for a small enough ε > 0 leads
to regret of 1. Namely, for sδ with (a0,a1) = (α,1), we get from (A.11)
Psδ(YB(δ(w)) = 0)
= 
T=0,...,NpT(1−p)N−T
i=0,...,N−Tαi(1−α)N−T−i
[(1−α)δT,i,T +
N
T
N −T
i

α]
= 
T=0,...,NpT(1−p)N−T
×{αN−T
N
T

+
i=0,...,N−T−1αi(1−α)N−T−i[(1−α)δT,i,T +
N
T
N −T
i

α]}
≥
T=0,...,N
N
T

pT(1−p)N−T{αN−T +α
i=0,...,N−T−1
N −T
i

αi(1−α)N−T−i}
= 
T=0,...,N
N
T

pT(1−p)N−T{αN−T +α(1−αN−T)}
> α
T=0,...,N
N
T

pT(1−p)N−T
= α,
(A.15)
where the second equality simply takes the last summand with index i = N −T out of the
second summation sign and uses δT,N−T,T =
N
T

, the inequality is obtained by setting
δT,i,T = 0 for all T = 0,...,N and i = 0,...,N−T −1, and the strict inequality uses αN−T +
α(1−αN−T) > α. By an argument as in part (i), (A.15) implies that for s′
δ with (a0,a1) =
(α −ε,1) with sufficiently small ε > 0 regret of 1 can be obtained because, under s′
δ, we
have qs′
δ,α(Y0) = 1, qs′
δ,α(Y1) = 0, and qs′
δ,α(YB(δ(w))) = 0.
Next, assume α = 0. Define sδ such that a0 = Psδ(Y0 = 0) = 0 and a1 = Psδ(Y1 = 0) =
ε > 0. That and r = 1 imply that qsδ,α(Y0) = 1 and qsδ,α(Y1) = 0. Then, from (A.11),
Psδ(YB(δ(w)) = 0) = 
t=(t1,...,tN)′∈{0,1}N,
y=(yt1,...,ytN )′∈{0,1}N,
ytj=1 if tj=0 for j=1,...,N
pt(1−p)N−tεN1ty(1−ε)t−N1tyδ((t,y))ε.
(A.16)
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 26; PDF label 26

FORMULA CHECK REQUIRED: original PDF page 26.

````text
26
PATRIK GUGGENBERGER ET AL.
Thus, Psδ(YB(δ(w)) = 0) > 0 (which implies R(δ,sδ) = 1), unless δ((t,y)) = 0 for all vectors
t,y ∈{0,1}N such that ytj = 1 if tj = 0 for j = 1,...,N. For such δ consider instead s′
δ such
that a0 = Ps′
δ(Y0 = 0) = ε > 0 and a1 = Ps′
δ(Y1 = 0) = 0. Then
Ps′
δ(YB(δ(w)) = 0) = 
t=(t1,...,tN)′∈{0,1}N,
y=(yt1,...,ytN )′∈{0,1}N
ytj=1 if tj=1 for j=1,...,N
pt(1−p)N−tεN0ty(1−ε)N−t−N0ty(1−δ((t,y)))ε
(A.17)
exceeds zero, because 1 −δ((0N′,1N′)′) = 1 and the vectors t = 0N and y = 1N appear in
the sum in (A.17) . Thus, R(δ,s′
δ) = 1.
Finally, the case (α = 1 and r = 0) is handled exactly as in part (i).
Part (iii). We first show the following lemma
Lemma 1. Let (α ∈(0,1) and r ∈[0,1]) or (α = 0 and r = 1). If δ̸ = 0, then there exists
an sδ ∈S such that R(δ,sδ) = qα(Y0).
A.2. Proof of Lemma 1
The case qα(Y0) = 0 is trivial. Simply take sδ such that Psδ(Y0 = 0) = Psδ(Y1 = 0) = 1.
Thus, from now on, we assume qα(Y0) > 0.
Assume first α ∈(0,1). Because δ̸ = 0, there exists a vector
	w = (y1,1,...,y1,N) such that δ(	w) > 0,
(A.18)
where y1,i ∈[0,1] for i = 1,...,N. (When N = 0, then we don’t need to define 	w).
Definition of Distributions of Y0 and Y1 : We now define an sδ ∈S for which R(δ,sδ) =
qα(Y0) and under sδ ∈S, Y0 and Y1 have independent discrete marginals. Namely, Y0 is
defined by Psδ(Y0 = 0) = α −ε for some small ε > 0(and obviously ε < α) to be further
restricted below and Psδ(Y0 = qα(Y0)) = 1−(α −ε). Thus, qsδ,α(Y0) = qα(Y0).
When N = 0, set Psδ(Y1 = 0) = 1 and note that Psδ(YB(δ) = 0) = δ+(1−δ)(α−ε) which
exceeds α for ε small enough (using α < 1). Thus, qsδ,α(Y1) = 0 and qsδ,α(YB(δ)) = 0 which
implies the desired result R(δ,sδ) = qα(Y0).
When N ≥1, the discrete distribution of Y1 under sδ is defined by
Psδ(Y1 = 0) = α +1
2
+ 1
N

1−α +1
2
N
j=1I(y1,j = 0),
Psδ(Y1 = y1,i) = 1
N

1−α +1
2
N
j=1I(y1,j = y1,i) for all i = 1,...,N s.t. y1,i̸ = 0,
(A.19)
where the y1,i for i = 1,...,N appear as the components of 	w in (A.18). Note that all
probabilities in (A.19) are properly defined, that is, they are all in the interval (0,1], and
sum up to 1. Just for clarity, N
j=1I(y1,j = 0) equals the number of zero components in the
vector 	w. Note that several of the y1,i for i = 1,...,N may be identical and therefore Y1 may
be supported on strictly fewer than N +1 points.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 27; PDF label 27

FORMULA CHECK REQUIRED: original PDF page 27.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
27
With these definitions, we obtain qsδ,α(Y1) = 0 (because 0.5 (α +1) > α) and
Psδ(YB(δ(w)) = 0)
= 

w=(w1,...,wN)
wi∈{0,y1,1,...,y1,N}, i=1,...,N
N
i=1Psδ(Y1 = wi)
[δ(
w)Psδ(Y1 = 0)+(1−δ(
w))Psδ(Y0 = 0)]
=



w=(w1,...,wN)
wi∈{0,y1,1,...,y1,N}, i=1,...,N
N
i=1Psδ(Y1 = wi)δ(
w)[Psδ(Y1 = 0)−Psδ(Y0 = 0)]

+Psδ(Y0 = 0)
≥
N
i=1Psδ(Y1 = y1,i)δ(	w)
α +1
2
−(α −ε)

+α −ε,
(A.20)
where the inequality is obtained by setting δ(
w) = 0 except for when 
w = 	w, using that
Psδ(Y1 = 0) −Psδ(Y0 = 0) ≥α+1
2
−(α −ε) > 0. We claim that Psδ(YB(δ(w)) = 0) > α
(and thus qsδ,α(YB(δ(w))) = 0) for sufficiently small ε > 0. But the claim is equivalent to
N
i=1Psδ(Y1 = y1,i)δ(	w)
1−α
2
+ε

> ε,
(A.21)
which clearly holds true for ε > 0 sufficiently small (using α < 1).
When α = 0 (in which case, we take r = 1), we can use the same proof structure except
we use sδ such that Psδ(Y0 = qα(Y0)) = 1 (which implies qsδ,α(Y0) = qα(Y0)) and the
distribution for Y1 defined in (A.19) with α = 0.
□
Note throughout that for s ∈S, we have qα(Y0) = qs,α(Y0).
Consider first the case qα(Y0) > 1/2. For δ0 ≡0, we will show next that
max
s∈S R(δ0,s) = 1−qα(Y0).
(A.22)
The statement in (A.22) follows easily because for any s ∈S for which qs,α(Y1) = 1, we
obtain R(δ0,s) = 1−qα(Y0). Furthermore, because always
qs,α(YB(δ(w))) ∈[min{qs,α(Y0),qs,α(Y1)}, max{qs,α(Y0),qs,α(Y1)}]
(A.23)
(as proven in Lemma 3(i) below) 1−qs,α(Y0) is the maximal possible regret for any s ∈S
for which qs,α(Y1) > qs,α(Y0). For any s ∈S, such that qs,α(Y1) ≤qs,α(Y0) regret is zero.
That proves (A.22).
Because when qα(Y0) > 1/2, we have 1−qs,α(Y0) < qs,α(Y0), (A.22) combined with
the lemma implies the desired result when qα(Y0) > 1/2.
Next, consider the case qα(Y0) = 1/2. Statement (A.22) (that also holds when qα(Y0) =
1/2), Lemma 1, together with the fact that regret is bounded by 1/2 (by (A.23) when
qs,α(Y0) = 1/2), establish that all treatment rules are minimax regret.
Finally, consider the case qα(Y0) < 1/2. We have maxs∈S R(δ∗,s) = qs,α(Y0) for
δ∗= 1. Lemma 1 establishes that for δ̸ = 0 maxs∈S R(δ,s) ≥qs,α(Y0) while for
δ0 ≡0, maxs∈S R(δ0,s) = 1 −qs,α(Y0) > qs,α(Y0). It follows that δ∗= 1 is a minimax
rule.
Finally, the case where α = 1 and r = 0 is proven as in part (i).
□
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 28; PDF label 28

FORMULA CHECK REQUIRED: original PDF page 28.

````text
28
PATRIK GUGGENBERGER ET AL.
A.3. Proof of Corollary 1
(a) This statement follows as a corollary from the proof of Proposition 1 because that proof
only used Bernoulli distributions for nature for parts (i) and (ii) and discrete distributions in
part (iii).
(b) (i) Consider an arbitrary treatment rule δ. Consider a state of nature s = sα,ε,n for
n ∈N such that Y0 has density n on [0,1/n] and Y1 has density f = fα,ε,n which equals
n(α −ε) on [0,1/n] and n(1 −α + ε) on [1 −1/n,1] (and zero elsewhere) for some small
ε ∈[0,α/2] to be specified more precisely below. Note that these continuous distributions
are chosen in order to approximate as n →∞the Bernoulli distributions used in the proof
of Proposition 1(i). With these definitions,
qs,α(Y0) = α/n and qs,α(Y1) = 1−1/n+ε/(n(1−α +ε)).
(A.24)
Consider an arbitrary q ∈(0,1). Then for all n such that 1/n < q < 1−1/n
Ps(YB(δ(w)) ≤q)
=
 1/n
0
n...
 1/n
0
n
 1
0 f(y11)...
 1
0 f(y1N1)
[δ(y)(α −ε)+(1−δ(y))]dy1N1 ... dy11dy0N0 ... dy01
≥(α −ε)
 1/n
0
n...
 1/n
0
n
 1
0 f(y11)...
 1
0 f(y1N1)dy1N1 ... dy11dy0N0 ... dy01
= (α −ε),
(A.25)
where y := (y01,...,y0N0,y11,...,y1N1)′ and the inequality comes from picking δ1 ≡1
given that α −ε −1 < 0.
Note that if Ps(δ(w) = 1) < 1 for one choice of ε ∈[0,α/2], then it holds for any
ε ∈[0,α/2].
Case 1: Ps(δ(w) = 1) < 1. By the same steps as in (A.25) with ε = 0, we obtain
Ps(YB(δ(w)) ≤q) > α and, by continuity in ε, then also for ε > 0 sufficiently small. It
follows that the α-quantile of YB(δ(w)) is not greater than q.
Case 2: Ps(δ(w) = 1) = 1. In that case, consider a state of nature	s =	sα,ε,n for n ∈N
such that Y1 has density n on [0,1/n] and Y0 has density	f =	fα,ε,n which equals n(α −ε)
on [0,1/n] and n(1−α +ε) on [1−1/n,1] (and zero elsewhere). Thus,
q	s,α(Y1) = α/n and q	s,α(Y0) = 1−1/n+ε/(n(1−α +ε))
(A.26)
and, analogously to (A.25),
P	s(YB(δ(w)) ≤q)
=
 1
0	f(y01)...
 1
0	f(y0N0)
 1/n
0
n...
 1/n
0
n[δ(y)+(1−δ(y))(α −ε)]
dy1N1 ... dy11dy0N0 ... dy01
=
 1/n
0
	f(y01)...
 1/n
0
	f(y0N0)
 1/n
0
n...
 1/n
0
ndy1N1 ... dy11dy0N0 ... dy01
+

...

An	f(y01)...	f(y0N0)
 1/n
0
n...
 1/n
0
n[δ(y)+(1−δ(y))(α −ε)]
dy1N1 ... dy11dy0N0 ... dy01
≥(α −ε)N0 +(α −ε)

...

An	f(y01)...	f(y0N0)dy0N0 ... dy01
= (α −ε)N0 +(α −ε)(1−(α −ε)N0),
(A.27)
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 29; PDF label 29

FORMULA CHECK REQUIRED: original PDF page 29.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
29
where An := [0,1]N0\[0,1/n]N0, the second equality uses that δ(w) = 1 a.s. on [0,1/n]N
(under s and therefore also under	s), and the inequality is obtained by taking δ(y) = 0 on
the domain of integration. If ε was equal to zero, the final expression in (A.27) would be
strictly larger than α. By continuity in ε, that is then also true for sufficiently small ε > 0.
It follows that the α-quantile of YB(δ(w)) is not greater than q.
As q can be chosen arbitrarily small in that construction it follows that, both in Cases 1
and 2, regret arbitrarily close to 1 can be inflicted by nature given (A.24) and (A.26).
Parts (ii) and (iii) follow from similar constructions.
□
A.4. Proof of the Statements in Comment 3 below Corollary 1
Note first that q(δ) indeed exists because cdfs are continuous from the left. For example,
q(0) = qα(Y0) and q(1) = 0. Also note that for any q ∈[0,1], the function g(δ) := δ +(1−
δ)FY0(q) is weakly increasing in δ. It follows that q(δ) is weakly decreasing in δ. Therefore,
qα(Y0)−q(δ) is weakly increasing in δ.
If δ < 1, then regret of 1−qα(Y0) can be achieved by nature by defining the distribution
of Y1 as Ps(Y1 = 0) = α −ε and Ps(Y1 = 1) = 1 −(α −ε) for some small ε > 0 (to be
specified further below). Namely, with that definition, for qα(Y0) < 1, we have
Ps(YB(δ) ≤qα(Y0)) = δ(α −ε)+(1−δ)FY0(qα(Y0)),
(A.28)
which exceeds α for ε small enough because FY0(qα(Y0)) > α and δ < 1. And of course
Ps(YB(δ) ≤qα(Y0)) ≥α when qα(Y0) = 1. Because the α-quantile of YB(δ) can clearly not
be smaller than qα(Y0) it follows that it is equal to qα(Y0).
But then, in the case qα(Y0) < 1/2, it follows that for any δ ∈[0,1), maxs∈S R(δ,s) ≥
1−qα(Y0) > qα(Y0). Given that for δ1 ≡1 maximal regret equals qα(Y0), it is the unique
minimax regret rule. When qα(Y0) = 1/2, regret cannot exceed 1/2 and given regret of
1−qα(Y0) can always be achieved by the argument above (for δ < 1 and for qα(Y0) = 1/2
also for δ = 1), it follows that all rules are minimax regret.
Furthermore, for any δ ∈[0,1], regret of qα(Y0) −q(δ) can be achieved by nature by
defining s, the distribution of Y1, by Ps(Y1 = 0) = 1. Then Ps(YB(δ) ≤q(δ)) = δ + (1 −
δ)FY0(q(δ)) which by (2.23) and r = 0 implies qs,α(YB(δ)) = q(δ). By construction, no
bigger regret than qα(Y0) −q(δ) can be achieved by nature for setups where qα(Y1) ≤
qα(Y0). That proves the claim in the case where qα(Y0) > 1/2.
□
A.5. Proof of Corollary 2
Part (i). Let δ be an arbitrary treatment rule. We will construct a state of nature sδ that yields
regret equal to 1. Consider the case where all marginals under sδ are independent Bernoulli
distributions and define
a0xk = Psδ(Y0,xk = 0) and a1xk = Psδ(Y1,xk = 0)
(A.29)
for k = 1,...,K (and, of course, 1−a0xk = Psδ(Y0,xk = 1) and 1−a1xk = Psδ(Y1,xk = 1)).
Notationwise, we index probabilities by those distributions that they depend on. Then,
Psδ,FX(YB(δX(w)),X = 0) = K
k=1PFX(X = xk)Psδ,FX(YB(δxk(w)),xk = 0)
(A.30)
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 30; PDF label 30

FORMULA CHECK REQUIRED: original PDF page 30.

````text
30
PATRIK GUGGENBERGER ET AL.
and
Psδ,FX(YB(δxk(w)),xk = 0)
= 
	x=(	x1,...,	xN)∈X N
y=(yt1,...,ytN )∈{0,1}N
N0
l=1PFX(X =	xl)a
1−ytl
0	xl
(1−a0	xl)ytl
N
l′=N0+1PFX(X =	xl′)a
1−ytl′
1	xl′
(1−a1	xl′ )ytl′
×[δxk(	w(	x,y))a1xk +(1−δxk(	w(	x,y)))a0xk],
(A.31)
where in the last line 	w(	x,y) denotes the sample associated with 	x and y. Note that
expressions like Psδ,FX(YB(δxk(w)),xk = 0) are still indexed by FX because the distribution
of w depends on FX. In the case (a0xk,a1xk) = (1,α) for all k = 1,...,K, (A.31) becomes
Psδ,FX(YB(δxk(w)),xk = 0) = 
˜x=(˜x1,...,˜xN)∈X N
y′
N0+1,...,y′
N∈{0,1}N1
N0
l=1 PFX(X = ˜xl)
N
l′=N0+1 PFX(X = ˜xl′)α1−yl′ (1−α)yl′ ×[(α −1)δxk

˜w(˜x,y)

+1]
≥[
˜x=(˜x1,...,˜xN)∈X N
(y′
N0+1,...,y′
N)∈{0,1}N−N0
N0
l=1 PFX(X = ˜xl)N
l′=N0+1 PFX(X = ˜xl′)α1−yl′ (1−α)yl′ ]α
= α,
(A.32)
where the inequality follows from taking δxk(	w(	x,y)) = 1.
If for some k ∈{1,...,K}δxk(	w(	x,y)) < 1 for some 	w(	x,y) (with	x = (	x1,...,	xN) ∈X N
and y = (0,...,0,ytN0+1,...,ytN ) with ytj ∈{0,1} for j = N0 + 1,...,N) it follows that
Psδ,FX(YB(δxk(w)),xk = 0) > α and by (A.30) therefore also Psδ,FX(YB(δX(w)),X = 0) > α.
Notice that Psδ,FX(YB(δX(w)),X = 0) is continuous in a1xk for k = 1,...,K and therefore
Psδ,FX(YB(δX(w)),X = 0) > α when instead of (a0xk,a1xk) = (1,α) for k = 1,...,K, sδ is
defined by (a0xk,a1xk) = (1,α −ε) for k = 1,...,K for some small enough ε > 0. But then
for that choice of sδ, regret equals 1 (as can be seen by comparing to the quantile obtained
for the treatment rule δ ≡1) as desired.
If instead for all k ∈{1,...,K}δxk(	w(	x,y)) = 1 for all 	w(	x,y) (with	x = (	x1,...,	xN) ∈X N
and y = (0,...,0,ytN0+1,...,ytN ) with ytj ∈{0,1} for j = N0 + 1,...,N), nature can cause
regret of 1 by using distributions defined by (a0xk,a1xk) = (α −ε,1) for some small enough
ε > 0. Namely, note first that for sδ defined by (a0xk,a1xk) = (α,1) for k = 1,...,K, we
obtain from (A.31)
Psδ,FX(YB(δxk(w)),xk = 0)
= 
	x=(	x1,...,	xN)∈X N
y=(yt1,...,ytN0,0,...,0)∈{0,1}N0×{0}N1
N0
l=1PFX(X =	xl)α1−ytl (1−α)ytl
N
l′=N0+1PFX(X =	xl′)
×[δxk(	w(	x,y))(1−α)+α]
≥αN0
	x=(	x1,...,	xN)∈X N
N
l=1PFX(X =	xl)
+α
	x=(	x1,...,	xN)∈X N
y=(yt1,...,ytN0,0,...,0)∈{0,1}N0×{0}N1,y̸=0N
N0
l=1PFX(X =	xl)α1−ytl (1−α)ytl
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 31; PDF label 31

FORMULA CHECK REQUIRED: original PDF page 31.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
31
(N
l′=N0+1PFX(X =	xl′))
= αN0 +α −α[
	x=(	x1,...,	xN)∈X N
N0
l=1(PFX(X =	xl)α)(N
l′=N0+1PFX(X =	xl′))]
= αN0 +α −αN0+1,
(A.33)
where the inequality follows from setting δxk(	w(	x,y)) = 0 for all elements in the sum except
for those when y = 0N in which case we use δxk(	w(	x,y)) = 1. The second to last equality
follows by first considering a sum over all y = (yt1,...,ytN0,0,...,0) ∈{0,1}N0 × {0}N1
in the second sum and then subtracting the summand associated with y = 0N. The final
expression is strictly larger than α which by an argument as above allows us to conclude that
Psδ,FX(YB(δxk(w)),xk = 0) > α when sδ is defined by (a0xk,a1xk) = (α−ε,1) for k = 1,...,K
for some small enough ε > 0.
The proof of part (ii) is very similar to part (i) and omitted.
Part (iii). The key input of the proof is the following lemma.
Lemma 2. For any treatment rule δ ∈D such that δ̸ = 0, there exists an sδ ∈S such that
R(δ,sδ) = qα(Y0,X).
A.6. Proof of Lemma 2
We define an sδ ∈S by letting all marginals (Yt,xk) be independent and discrete, namely,
for an ε > 0 (to be specified later), let Psδ(Y0,xk = 0) = α −ε and Psδ(Y0,xk = qα(Y0,X)) =
1−(α −ε) for every xk ∈X. Because Psδ,FX(Y0,X = 0) = K
k=1 PFX(X = xk)Psδ(Y0,xk =
0) = α −ε, it follows that qs,FX,α(Y0,X) = qα(Y0,X) as required.
For N = 0, complete the definition of sδ by setting Psδ(Y1,xk = 0) = 1 for every xk ∈X.
Wlog assume δxl > 0. Note that Psδ(YB(δxl),xl = 0) = δxl + (1 −δxl)(α −ε) which, given
that δxl > 0, is strictly larger than α when ε > 0 is chosen sufficiently small. For every
xk ∈X such that xk̸ = xl, we have Psδ(YB(δxk),xk = 0) ≥α −ε. Therefore,
Psδ,FX(YB(δX),X = 0)
=
K

k=1
PFX(X = xk)Psδ(YB(δxk),xk = 0)
≥PFX(X = xl)(δxl +(1−δxl)(α −ε))+
K

k=1,k̸=l
PFX(X = xk)(α −ε)
= PFX(X = xl)δxl(1−(α −ε))+(α −ε)
> α,
(A.34)
where the second equality follows by including the summand PFX(X = xl)(α −ε) into the
summation sign, and the inequality holds for ε > 0 chosen small enough.
Next consider the case N > 0. Because δ̸ = 0, there exists some vector 	w =
((	x1,	y1),...,(	xN,	yN)) with (	xi,	yi) ∈X × [0,1] for every i = 1,...,N and some covariate
xl ∈X such that δxl( ˜w) > 0. Similarly to the proof of Proposition 1(iii), for every xk ∈X,
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 32; PDF label 32

FORMULA CHECK REQUIRED: original PDF page 32.

````text
32
PATRIK GUGGENBERGER ET AL.
define the distribution of Y1,xk under sδ as
Psδ(Y1,xk = 0) = α +1
2
+ 1
N [1−α +1
2
]
N

j=1
I(	yj = 0),
Psδ(Y1,xk =	yi) = 1
N [1−α +1
2
]
N

j=1
I(	yj =	yi) for i = 1,...,N such that	yi̸ = 0.
(A.35)
Because Psδ,FX(Y1,X = 0) = K
k=1 PFX(X = xk)Psδ(Y1,xk = 0), it then follows that
qs,FX,α(Y1,X) = 0. Now, focus on Psδ,FX (YB(δxl(w)),xl = 0). Furthermore,
Psδ,FX (YB(δxl(w)),xl = 0)
=

w=((a1,b1),...,(aN,bN));
ai∈X ; bi∈{0,	y1,...,	yN},
i=1,...,N
N

i=1
Psδ,FX(Y1,ai = bi,X = ai)
(δxl(w)Psδ(Y1,xl = 0)+(1−δxl(w))Psδ(Y0,xl = 0))
= Psδ(Y0,xl = 0)+

w=((a1,b1),...,(aN,bN));
ai∈X ; bi∈{0,	y1,...,	yN},
i=1,...,N
N

i=1
Psδ,FX(Y1,ai = bi,X = ai)(δxl(w)
(Psδ(Y1,xl = 0)−Psδ(Y0,xl = 0))
≥α −ε +
N

i=1
Psδ(Y1,	xi =	yi)PFX(X =	xi)δxl( ˜w)(α +1
2
−(α −ε))
> α,
(A.36)
where the first inequality follows by replacing δxl(w) by zero for every w̸ = ˜w and the last
inequality holds for small enough ε > 0. By the same derivations, for any other xk̸ = xl, it
follows that Psδ,FX(YB(δxk(w)),xk = 0) ≥α −ε. Therefore, for sufficiently small ε > 0, we
have
Psδ,FX(YB(δX(w)),X = 0)
=
K

k=1
PFX(X = xk)Psδ(YB(δxk(w)),xk = 0)
≥α −ε +PFX(X = xl)
N

i=1
Psδ(Y1,	xi =	yi)PFX(X =	xi)δxl( ˜w)(α +1
2
−(α −ε))
> α,
(A.37)
where for the inequality we use Psδ(YB(δxk(w)),xk = 0) ≥α −ε and the second to last
line in (A.36). Therefore, we have qs,FX,α(Y0,X) = qα(Y0,X) and qs,FX,α(Y1,X) =
qs,FX,α(YB(δX(w)),X) = 0. Hence, the statement of the lemma follows.
□
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 33; PDF label 33

FORMULA CHECK REQUIRED: original PDF page 33.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
33
Given Lemma 2, the remainder of the proof of part (iii) is exactly the same as the last
part of the proof of Proposition 1(iii). The only detail to think about is establishing that
qs,FX,α(YB(δX(w)),X) ∈[min{qs,FX,α(Y0,X),qs,FX,α(Y1,X)},
max{qs,FX,α(Y0,X),qs,FX,α(Y1,X)}].
(A.38)
The proof of that statement is analogous to the proof of Lemma 3 and therefore omitted. □
The following is a technical lemma that is used in the proof of Proposition 1 above. It
states that 1(qs,α(Y1) ≥qs,α(Y0)) is an infeasible optimal rule.
Lemma 3. For any given r ∈[0,1] and arbitrary s ∈S, we have (i)
qs,α(YB(δ(w))) ∈[min{qs,α(Y0),qs,α(Y1)}, max{qs,α(Y0),qs,α(Y1)}]
and (ii)
max
δ∈D u(δ,s) = max
δ∈D qs,α(YB(δ(w))) = max{qs,α(Y0),qs,α(Y1)}.
A.7. Proof of Lemma 3
(i) Denote by q0,α, q1,α, and qδ,α the largest α-quantile (meaning employing r = 1 in
definition (2.5)) of Y0,Y1, and YB(δ(w)), respectively. Likewise, denote by q0,α, q1,α, and
qδ,α the smallest α-quantile (meaning employing r = 0 in definition (2.5)) of Y0,Y1, and
YB(δ(w)), respectively. As in (A.1),
Ps(YB(δ(w)) ≥q) = Ps(B(δ(w)) = 1)Ps(Y1 ≥q)+Ps(B(δ(w)) = 0)Ps(Y0 ≥q).
(A.39)
We first show that
qδ,α ∈[min{q0,α,q1,α}, max{q0,α,q1,α}].
(A.40)
Indeed, if qδ,α > max{q0,α,q1,α}, then, from (A.39),
Ps(YB(δ(w)) ≥qδ,α)
= Ps(B(δ(w)) = 1)Ps(Y1 ≥qδ,α)+Ps(B(δ(w)) = 0)Ps(Y0 ≥qδ,α)
< 1−α,
(A.41)
a contradiction to the definition of an α-quantile. On the other hand, if qδ,α <
min{q0,α,q1,α}, then there exists ε > 0 such that qδ,α + ε < min{q0,α,q1,α}. But then
Ps(YB(δ(w)) ≥qδ,α +ε)
= Ps(B(δ(w)) = 1)Ps(Y1 ≥qδ,α +ε)+Ps(B(δ(w)) = 0)Ps(Y0 ≥qδ,α +ε)
≤Ps(B(δ(w)) = 1)Ps(Y1 ≥q1,α)+Ps(B(δ(w)) = 0)Ps(Y0 ≥q0,α)
= 1−α,
(A.42)
contradicting the fact that qδ,α is the largest α-quantile of YB(δ(w)).
By an analogous argument, it follows that
qδ,α ∈[min{q0,α,q1,α}, max{q0,α,q1,α}].
(A.43)
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 34; PDF label 34

FORMULA CHECK REQUIRED: original PDF page 34.

````text
34
PATRIK GUGGENBERGER ET AL.
Define the interval I = [min{q0,α,q1,α}, max{q0,α,q1,α}].
If I = [qi,α,qj,α] for i,j ∈{0,1}, i̸ = j, then
qs,α(YB(δ(w))) = rqδ,α +(1−r)qδ,α
(A.44)
and thus by (A.40) and (A.43),
qs,α(YB(δ(w))) ≤rqj,α +(1−r)qj,α = qs,α(Yj) ≤max{qs,α(Y0),qs,α(Y1)} and
qs,α(YB(δ(w))) ≥rqi,α +(1−r)qi,α = qs,α(Yi) ≥min{qs,α(Y0),qs,α(Y1)}.
(A.45)
For the remaining case, we have I = [qi,α,qi,α] for an i ∈{0,1}. By (A.40) and (A.43), it
follows that [qδ,α,qδ,α] ⊂I and [qj,α,qj,α] ⊂[qδ,α,qδ,α].
If Ps(B(δ(w)) = i) = 1, then YB(δ(w)) = Yi wp1 and the lemma trivially holds. If
Ps(B(δ(w)) = i) < 1, we must have [qj,α,qj,α] = [qδ,α,qδ,α]. If not, if, for example,
qj,α < qδ,α, then Ps(Yj ≥qδ,α) < 1 −α and Ps(Yi ≥qδ,α) = 1 −α. But then, by (A.39),
we get the contradiction
Ps(YB(δ(w)) ≥qδ,α) = Ps(B(δ(w)) = 1)Ps(Y1 ≥qδ,α)
+Ps(B(δ(w)) = 0)Ps(Y0 ≥qδ,α) < 1−α,
(A.46)
where the last inequality uses Ps(B(δ(w)) = i) < 1. But if [qj,α,qj,α] = [qδ,α,qδ,α], then
qs,α(YB(δ(w))) = qs,α(Yj) and the claim in the lemma holds.
(ii) Considering the two rules δ1 ≡1 or δ0 ≡0 (i.e., the rules that pick 1 (or 0)
with probability 1), it follows that maxδ∈D qs,α(YB(δ(w))) ≥max{qs,α(Y0),qs,α(Y1)}. But
given that qs,α(YB(δ(w))) ≤max{qs,α(Y0),qs,α(Y1)} for any δ ∈D by part (i), the claim
follows.
□
FUNDING STATEMENT
The authors declare that no specific funding has been received for this article.
COMPETING INTEREST
The authors declare that no competing interests exist.
REFERENCES
Aradillas Fernández, A., Blanchet, J., Montiel Olea, J. L., Qiu, C., Stoye, J., & Tan, L. (2025a).
ε-Minimax solutions of statistical decision problems. Unpublished working paper, Cornell Univer-
sity.
Berger, J. (1985). Statistical decision theory and Bayesian analysis. (2nd ed.) Springer-Verlag.
Chambers, C. (2009). An axiomatization of quantiles on the domain of distribution functions.
Mathematical Finance, 19, 335–342.
Chen, H., & Guggenberger, P. (2026). A note on minimax regret rules with multiple treatments in finite
samples. Econometric Theory, 42(3), 723–749.
Christensen, T., Moon, R., & Schorfheide, F. (2026). Optimal discrete decisions when payoffs are
partially identified. Review of Economic Studies. Forthcoming.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 35; PDF label 35

FORMULA CHECK REQUIRED: original PDF page 35.

````text
MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES
35
Cucconi, O. (1968). “Contributi all’analisi Sequenziale nel Controllo di Accettazione per Variabili”.
Atti dell’Associazione Italiana per il Controllo della Qualità, 6, 171–186.
De Castro, L., Galvao, A., & Ota, H. (2026). Quantile approach to intertemporal consumption with
multiple assets. Journal of Econometrics, 253, 106161.
Guggenberger, P., & Huang, J. (2025). On the numerical approximation of minimax regret rules via
fictitious play. Unpublished working paper, Pennsylvania State University.
Gupta, S., & Hande, S. (1992). On some nonparametric selection procedures. In A. K. Md. E. Saleh
(Ed.), Nonparametric statistics and related topics, 33–49. Elsevier.
Hirano, K. (2026). Wald’s statistical decision theory for policy analysis and adaptive experiments. In
preparation for the ES monograph series" let’s write "Unpublished working paper, Pennsylvania
State University. Available at https://keihirano.github.io/papers/eswc.pdf.
Hirano, K., & Porter, J. (2009). Asymptotics for statistical treatment rules. Econometrica, 77,
1683–1701.
Huang, J., & Guggenberger, P. (2025). On minimax regret rules with pilot data. Unpublished working
paper, Pennsylvania State University.
Kitagawa, T., Lee, S., & Qiu, C. (2026). Treatment choice with nonlinear regret. Biometrika. Forth-
coming.
Kitagawa, T., & Tetenov, A. (2018). Who should be treated? Empirical welfare maximization methods
for treatment choice. Econometrica, 86, 591–616.
Manski, C. (1988). Ordinal utility models of decision making under uncertainty. Theory and Decision,
25, 79–104.
Manski, C. (2004). Statistical treatment rules for heterogeneous populations. Econometrica, 72,
221–246.
Manski, C., & Tetenov, A. (2007). Admissible treatment rules for a risk-averse planner with
experimental data on an innovation. Journal of Statistical Planning and Inference, 137,
1998–2010.
Manski, C., & Tetenov, A. (2023). Statistical decision theory respecting stochastic dominance. The
Japanese Economic Review, 74, 447–469.
Masten, M. (2023). Minimax-regret treatment rules with many treatments. The Japanese Economic
Review, 74, 501–537.
Montiel Olea, J. L., Qiu, C., & Stoye, J. (2026). Decision theory for treatment choice with partial
identification. Review of Economic Studies. Forthcoming.
Qi, Z., Cui, Y., Liu, Y., & Pang, J.-S. (2019). Estimation of individualized decision rules based on
an optimized covariate-dependent equivalent of random outcomes. SIAM Journal on Optimization,
29(3), 2337–2362.
Qi, Z., Pang, J., & Liu, Y. (2023). On robustness of individualized decision rules. Journal of the
American Statistical Association, 118(543), 2143–2157.
Rostek, M. J. (2010). Quantile maximization in decision theory. The Review of Economic Studies, 77,
339–371.
Schlag, K. (2003). How to minimize maximum regret under repeated decision-making. EUI working
paper.
Schlag, K. (2006). ELEVEN—Tests needed for a recommendation. EUI working paper, ECO No.
2006/2.
Stoye, J. (2007). Minimax regret treatment choice with incomplete data and many treatments.
Econometric Theory, 23(1), 190–199.
Stoye, J. (2009). Minimax regret treatment choice with finite samples. Journal of Econometrics, 151,
70–81.
Stoye, J. (2012). Minimax regret treatment choice with covariates or with limited validity of experi-
ments. Journal of Econometrics, 166, 138–156.
Tetenov, A. (2012). Statistical treatment choice based on asymmetric minimax regret criteria. Journal
of Econometrics, 166, 157–165.
Wald, A. (1945). Statistical decision functions which minimize the maximum risk. Annals of Mathe-
matics, 46(2), 265–280.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

## PDF page 36; PDF label 36

FORMULA CHECK REQUIRED: original PDF page 36.

````text
36
PATRIK GUGGENBERGER ET AL.
Wald, A. (1947). Foundations of a general theory of sequential decision functions. Econometrica,
15(4), 279–313.
Wald, A. (1950). Statistical decision functions. Wiley.
Wang, L., Zhou, Y., Song, R., & Sherwood, B. (2018). Quantile-optimal treatment regimes. Journal of
the American Statistical Association, 113(523), 1243–1254.
Yata, K. (2023). Optimal decision rules under partial identification. Unpublished working paper.
https://doi.org/10.1017/S0266466626100498 Published online by Cambridge University Press

````

