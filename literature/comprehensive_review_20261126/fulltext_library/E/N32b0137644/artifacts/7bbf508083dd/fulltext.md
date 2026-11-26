# Offline Minimax Soft-Q-learning Under Realizability and Partial Coverage

Original PDF: [original.pdf](original.pdf). SHA256: `7bbf508083dd373022ae6c8b2000006d40e8ad59a45586109561fb111cf1ed09`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

FORMULA CHECK REQUIRED: original PDF page 1.

````text
arXiv:2302.02392v2  [cs.LG]  13 Nov 2023
Ofﬂine Minimax Soft-Q-learning Under
Realizability and Partial Coverage
Masatoshi Uehara* †1, Nathan Kallus ‡1, Jason D. Lee§2, and Wen Sun ¶1
1Genentech
2Princeton University
Abstract
In ofﬂine RL, we have no opportunity to explore so we must make assumptions
that the data is sufﬁcient to guide picking a good policy, and we want to make these
assumptions as harmless as possible. In this work, we propose value-based algorithms
for ofﬂine RL with PAC guarantees under just partial coverage, speciﬁcally, coverage
of just a single comparator policy, and realizability of the soft (entropy-regularized) Q-
function of the single policy and a related function deﬁned as a saddle point of certain
minimax optimization problem. This offers reﬁned and generally more lax conditions
for ofﬂine RL. We further show an analogous result for vanilla Q-functions under a
soft margin condition. To attain these guarantees, we leverage novel minimax learning
algorithms and analyses to accurately estimate either soft or vanilla Q-functions with
strong L2-convergence guarantees. Our algorithms’ loss functions arise from casting
the estimation problems as nonlinear convex optimization problems and Lagrangify-
ing. Surprisingly we handle partial coverage even without explicitly enforcing pes-
simism.
1
Introduction
In ofﬂine Reinforcement Learning (RL), we must learn exclusively from ofﬂine data and
are unable to actively interact with the environment (Levine et al., 2020). Ofﬂine RL has
garnered considerable interest in a range of applications where experimentation may be
prohibitively costly or risky.
*uehara.masatoshi@gene.com
†This work is done when the author was at Cornell University.
‡kallus@cornell.edu
§jasonlee@princeton.edu
¶ws455@cornell.edu
1

````

## PDF page 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
Table 1: Summary of partial-coverage-type guarantees with model-free general function
approximation. Here, w⋆:= dπ⋆,µ0/Pb where dπ⋆,µ0 is the occupancy distribution under the
optimal policy π⋆starting from µ0 and Pb is the distribution over the ofﬂine data. A function
˜w⋆
α is a regularized marginal density ratio that satisﬁes ˜w⋆
0 = w⋆. Functions q⋆, q⋆
α, qπ are the
optimal Q⋆-function, the soft Q-function, and the Q-function under a policy π, respectively.
Functions v⋆
α, l⋆
α are Lagrange multipliers of speciﬁc minimax optimization problems. The
operator Bπ is a Bellman operator under a policy π. Function classes W, Q, L, V consist
of functions that map states (and actions) to real numbers. Note the guarantees provided
by Jiang and Huang (2020); Xie et al. (2021) are more general than the below in that the
output policy can compete with any policy in the policy class Π. For simplicity, we set
the comparator policy to be the optimal policy π⋆in this table. Note that other studies
(Ozdaglar et al., 2023; Rashidinejad et al., 2022; Zhu et al., 2023) proposing model-free
general function approximation under partial coverage rely on the completeness-type as-
sumption as in (Xie et al., 2021) or realizability for any π as in Jiang and Huang (2020).
Primary Assumptions
Jiang and Huang (2020)
w⋆∈W, qπ ∈Q ∀π ∈Π
Xie et al. (2021)
qπ ∈Q, BπQ ⊂Q ∀π ∈Π
Zhan et al. (2022)
˜w⋆
α ∈W, v⋆
α ∈V
MSQP
q⋆
α ∈Q, l⋆
α ∈L
Chen and Jiang (2022)
Hard margin, w⋆∈W, q⋆∈Q
MQP
Soft margin, q⋆∈Q, l⋆∈L
Ofﬂine RL is generally based on two types of assumptions: sufﬁcient coverage in the of-
ﬂine data and sufﬁcient function approximation. For instance, classical Fitted-Q-iteration
(Antos et al., 2008; Chen and Jiang, 2019) requires (a) full coverage in the ofﬂine data,
max(s,a) dπ,µ0(s, a)/Pπb(s, a) < ∞for any policy π where Pπb(s, a) is the ofﬂine data’s
distribution on the states and actions and dπ,µ0(s, a) is the state-action occupancy distribu-
tion under a policy π and initial-state distribution µ0(s); (b) realizability of the Q∗-function
in a hypothesis class; and (c) Bellman completeness, i.e., the Bellman operator applied to
any function in the hypothesis class remains in the class. Full coverage (a) and Bellman
completeness (c) can be particularly stringent because ofﬂine data is often insufﬁciently
exploratory and Bellman completeness signiﬁcantly restricts transition dynamics.
To overcome these challenges, we here propose algorithms with guarantees under re-
2

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
alizability of single functions and reﬁned partial coverage of single policies, and without
Bellman completeness. We tackle this by introducing two novel value-based algorithms.
The ﬁrst algorithm, MSQP (mimimax soft-Q-learning with penalization), comprises of
two steps: learning soft Q-functions (a.k.a., entropy-regularized Q-functions, as deﬁned
in Fox et al., 2015; Schulman et al., 2017) from ofﬂine data, and using the softmax policies
of the learned soft Q-functions. The second algorithm, MQP (mimimax Q-learning with
penalization), consists of two steps: learning standard Q-functions from ofﬂine data and
employing the greedy policy of the learned Q function on the ofﬂine data.
Using the above-mentioned two algorithms, we attain PAC guarantees under partial
coverage and realizability, yet without Bellman completeness. In particular, in MSQP using
soft Q-functions, we ensure strong performance under the realizability of q⋆
α, l⋆
α and the
(density-ratio-based) partial coverage max(s,a) dπ⋆α,µ0(s, a)/Pb(s, a) < ∞. Here q⋆
α is a soft
Q-function, l⋆
α is a function that possesses a certain dual relation to q⋆
α, π⋆
α is the soft-max
optimal policy, and α is the temperature parameter for the entropy-regularization. Notably,
max(s,a) dπ⋆α,µ0(s, a)/Pb(s, a) < ∞is signiﬁcantly less stringent than the uniform coverage
in that the coverage is only imposed against a policy π⋆
α. In MQP using Q-functions, we
similarly ensure strong performance under a soft margin, the realizability of q⋆, l⋆, and
the partial coverage max(s,a) dπ⋆,µ0(s, a)/Pb(s, a) < ∞. Here q⋆is the vanilla Q-function
and l⋆is a function that possesses a certain dual relation to q⋆, and π⋆is the usual optimal
policy. Note the soft margin is introduced to allow realizability on standard Q-functions
rather than soft Q-functions. However, the conditions max(s,a) dπ⋆α,µ0(s, a)/Pb(s, a) < ∞
or max(s,a) dπ⋆,µ0(s, a)/Pb(s, a) < ∞may still be strong as these marginal density ratios
may not exist in large-scale MDPs. For example, this condition is easily violated when the
initial distribution µ0 is not covered by Pb (i.e., maxs µ0(s)/Pb(s) = ∞where Pb(s) :=
P
a Pb(s, a)). Therefore, as an additional innovation, in our algorithms we can further relax
these density-ratio-based partial coverage conditions. Speciﬁcally, we can demonstrate
results under a reﬁned partial coverage, which is adaptive to Q-function classes, even when
the initial distribution µ0 is not covered by Pb.1
The primary challenge lies in the design of loss functions for effectively learning soft
Q-functions and vanilla Q-functions from ofﬂine data without Bellman completness. To
tackle this, we devise new minimax loss functions with certain regularization terms to
achieve favorable L2-convergence rates on the ofﬂine data (i.e., in terms of E(s,a)∼Pb[{ˆqα −
q}2(s, a)] given an estimator ˆq). This result serves as the key building block for obtain-
ing reﬁned partial coverage under realizability and is of independent interest in its own
right. Existing results are often constrained to speciﬁc models, such as linear models
(Shi et al., 2022a), or they require Bellman completeness (Antos et al., 2008; Chen and Qi,
2022; Chen and Jiang, 2019). In contrast, our guarantee is applicable to any function ap-
proximation method, without the need for Bellman completeness. To the best of our knowl-
1Note µ0 and Pb could be generally different even in the contextual bandit setting. This important setting
is often considered in the literature on external validity/transportability in causal inference, as results of
randomized clinical trials cannot be directly transported because covariate distributions in ofﬂine data and
target data are different (Cole and Stuart, 2010; Pearl and Bareinboim, 2014; Dahabreh et al., 2019).
3

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
edge, this is the ﬁrst guarantee of its kind.
Our work exhibits marked improvements over two closely related studies (Zhan et al.,
2022; Chen and Jiang, 2022). Similar to our work, they propose algorithms that operate
under the realizability of speciﬁc functions and partial coverage, yet without Bellman com-
pleteness. Zhan et al. (2022) ensures a PAC guarantee under (a’) partial coverage in the
ofﬂine data max(s,a) d˜π⋆α,µ0(s, a)/Pb(s, a) < ∞where ˜π⋆
α is a speciﬁc near-optimal policy
under the regularization, which differs from the soft optimal policy, and (b’) realizability of
d˜π⋆α,µ0/Pb and the regularized value function. However, unlike MSQP, it is unclear how to
reﬁne the abovementioned coverage, i.e., the guarantee could be vacuous when the initial
distribution is not covered by ofﬂine data. A similar guarantee, but without regulariza-
tion, is obtained under the additional hard margin (a.k.a., gap) condition in Chen and Jiang
(2022). Our soft margin is a strict relaxation of the hard margin, which is important because,
unlike the soft margin, the hard margin generally does not hold in continuous state spaces
and involves very large constants in discrete state spaces. Lastly, although Chen and Jiang
(2022); Zhan et al. (2022) use completely different algorithms and attain guarantees for
regularized value-functions and non-regularized value functions, respectively, our guaran-
tee can afford guarantees for regularized and non-regularized value-functions in a uniﬁed
manner since MQP can be seen as a limit of MSQP when α goes to 0.
Our contributions are summarized below and in Table 1.
1. We establish that the optimal policy can be learned under partial coverage and realiz-
ability of the optimal soft Q-function and its dual. Notably, we abstain from the use
of possibly stronger conditions in ofﬂine RL, such as full coverage, Bellman com-
pleteness, and uniform realizability over the policy class (such as qπ ∈Q for any
π as in Jiang and Huang, 2020). In particular, while a similar guarantee is provided
in Zhan et al. (2022), our partial coverage guarantee has an advantage in that we are
able to potentially accommodate scenarios where the initial distribution is not cov-
ered by Pb. This is feasible because our algorithm is value-based in nature, which
allows us to leverage the structure of the Q-function classes and reﬁne the coverage
condition.
2. We demonstrate that the optimal policy can be learned under partial coverage, realiz-
ability of the Q-function and its dual, and a soft margin. While a similar guarantee
is obtained in Chen and Jiang (2022), our guarantee has the advantage that the soft
margin is signiﬁcantly less stringent than the hard margin required therein.
1.1
Related Works
We summarize related works as follows. Further related works is discussed in Section A.
Ofﬂine RL under partial coverage.
There is a growing number of results under partial
coverage following the principle of pessimism in ofﬂine RL (Yu et al., 2020; Kidambi et al.,
2020). In comparison to works that focus on tabular (Rashidinejad et al., 2021; Li et al.,
4

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
2022; Shi et al., 2022b; Yin and Wang, 2021) or linear models (Jin et al., 2020; Chang et al.,
2021; Zhang et al., 2022; Nguyen-Tang et al., 2022; Bai et al., 2022), our emphasis is on
general function approximation (Jiang and Huang, 2020; Uehara and Sun, 2021; Xie et al.,
2021; Zhan et al., 2022; Zhu et al., 2023; Rashidinejad et al., 2022; Zanette and Wainwright,
2022; Ozdaglar et al., 2023). Among them, we speciﬁcally focus on model-free methods.
The representative work is summarized in Table 1.
Soft (entropy-regularized) Q-functions.
Soft Q-functions are utilized in various con-
texts in RL (Geist et al., 2019; Neu et al., 2017). They have been shown to improve per-
formance in online RL settings, as demonstrated in Soft Q-Learning (Fox et al., 2015;
Schulman et al., 2017) and Soft Actor Critic (Haarnoja et al., 2018). In the ﬁeld of imita-
tion learning, they play a crucial role in Maximum Entropy IRL (Ziebart et al., 2008, 2010).
Furthermore, within the realm of ofﬂine RL, these soft Q-functions are utilized to make the
learned policy and behavior policy sufﬁciently similar (Wu et al., 2019; Fakoor et al., 2021).
However, to the best of the authors’ knowledge, none of these proposals in the context of
ofﬂine RL have provided sample complexity results under partial coverage.
Lagrangian view of ofﬂine RL.
In the realm of ofﬂine policy evaluation (OPE), Nachum and Dai
(2020); Yang et al. (2020); Huang and Jiang (2022) have formulated the problem as a con-
strained linear optimization problem. Notably, within the context of policy optimization,
Zhan et al. (2022) have proposed estimators for regularized density ratios with L2-convergence
guarantees, which is a crucial step in obtaining a near-optimal policy. Our work is similarly
motivated, but with a key distinction: our target functions are the soft Q-function and
Q-function, rather than the regularized density ratio, which presents additional analytical
challenges due to the nonlinear constraint.
2
Preliminaries
We consider an inﬁnite-horizon discounted MDP M = ⟨S, A, P, r, γ, µ0⟩where S is the
state space, A is the ﬁnite action space, γ ∈[0, 1) is the discount factor, reward r is
a random variable following Pr(· | s, a) on [Rmin, Rmax] (Rmin ≥0), µ0 is the initial
distribution. A policy π : S →∆(A) is a map from the state to the distribution over actions.
We denote the discounted state-action occupancy distribution under a policy π starting
from an initial distribution µ0 by dπ,µ0(s, a). With slight abuse of notation, we denote
dπ,µ0(s) = P
a dπ,µ0(s, a). We deﬁne the value under π as J(π) := Eπ[P∞
t=0 γt˜r(st, at)]
where the expectation is taken under π. We denote the optimal policy arg maxπ J(π) by
π⋆, and its Q-function Eπ⋆[P
t γt˜r(st, at) | s0 = s, a0 = a] by q⋆(s, a).
In ofﬂine RL, using ofﬂine data D = {(si, ai, ri, s′
i) : i = 1, . . . , n}, we search for the
policy π⋆that maximizes the policy value. We suppose each (si, ai, ri, s′
i) is sampled i.i.d.
from si ∼Pb, ai ∼πb(· | s), ri ∼Pr(· | si, ai), s′
i ∼P(· | si, ai). We denote the sample
average of f by En[f(s, a, r, s′)] = 1
n
Pn
i=1 f(si, ai, ri, s′
i), and the expectation of f with
5

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
respect to the ofﬂine data distribution by E[f(s, a, r, s′)] (without any scripts). The policy
πb used to collect data is typically referred to as a behavior policy. With slight abuse of
notation, we denote Pb(s, a) = Pb(s)πb(a | s).
Notation. We denote the support of Pb(·) by (S × A)b, and the L∞-norm on (S × A)b
by ∥· ∥∞,b. The L∞-norm on (S × A) is denoted by ∥· ∥∞. We deﬁne wπ(s, a) =
dπ,µ0(s, a)/Pb(s, a) (if it exists). We deﬁne sofmax(h) =
exp(h(s,a))
P
a exp(h(s,a)) and ∥h∥2 = E(s,a)∼Pb[h2(s, a)]1/2
for h : S × A →R. We denote universal constants by c1, c2, . . . . We use the convention
a/0 = ∞when a̸ = 0 and 0/0 = 0.
3
Algorithms
In this section, we present two algorithms. The ﬁrst algorithm aims to estimate the soft
optimal policy by ﬁrst estimating a soft Q-function. The second algorithm estimates the
optimal policy after estimating the Q-function.
3.1
Minimax Soft-Q-learning with Penalization
Our ultimate aim is to mimic the optimal policy π⋆. As a ﬁrst step, we begin by ﬁnding
a policy that maximizes the following regularized objective: arg maxπ Jα(π) where for
α > 0 we deﬁne
Jα(π) = (1 −γ)−1E(s,a)∼dπ,µ0,r∼Pr(·|s,a)[r −α log{π(a | s)/πb(a | s)}]
|
{z
}
KL penalty (between π and πb)
This objective function is used in a variety of contexts in RL as mentioned in Section 1.1.
The optimal policy that maximizes Jα(π) with respect to π is
π⋆
α = softmax(q⋆
α/α + log πb),
(1)
where q⋆
α : S × A →R is the soft Q-function uniquely characterized by the soft Bellman
equation:
∀(s, a); Es′∼P (·|s,a)[γΩα,πb(q⋆
α)(s′) + r −q⋆
α(s, a) | s, a] = 0,
where Ωα,πb : [S×A →R] →[S →R] has Ωα,πb(q)(s) = α log P
a{exp(q(s, a′)/α)πb(a′ |
s)}. As opposed to the standard objective function with α = 0, the KL penalty term serves
as a regularization term that renders π⋆
α sufﬁciently proximate to πb. As α approaches ∞,
the optimal policy π⋆
α approaches πb. On the other hand, when α = 0, π⋆
α is π⋆. Thus, in
order to compete with π⋆, it is necessary to keep α sufﬁciently small. We elaborate on this
selection procedure in Section 5.
The natural method for ofﬂine RL using this formulation involves learning q⋆
α from the
ofﬂine data and plugging it into (1). The question that remains is how to accurately learn
q⋆
α from the ofﬂine data. We consider the following optimization problem:
arg minq∈Q′ 0.5E(s,a)∼Pb[q2(s, a)]
(2)
6

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
Algorithm 1 MSQP (Minimax Soft-Q-learning with Penalization)
1: Require: Parameter α ∈R+, Models Q, L ⊂[S × A →R+].
2: Estimate q⋆
α as follows:
ˆqα ∈arg min
q∈Q
max
l∈L En[q2(s, a)/2 + {γΩα,πb(q)(s′) + r −q(s, a)}l(s, a)].
(5)
3: Estimate the soft optimal policy: ˆπα = softmax(ˆqα/α + log πb).
where Q′ consists of all functions q : S × A →R satisfying
Es′∼P (·|s,a)[γΩα,πb(q)(s′) + r −q(s, a) | s, a] = 0 ∀(s, a) ∈(S × A)b.
(3)
Here, because of the constraint (3), the solution is q⋆
α. Furthermore, we use q2(s, a) in (2)
because this choice relaxes the equality in (3) to an inequality ≤0 as we will demonstrate in
Section B. Consequently, the entire optimization problem outlined in (2) and (3) transforms
into a convex optimization problem.
Then, using the method of Lagrange multipliers, (2) is transformed into
minq maxl Lα(q, l),
Lα(q, l) := E [q2(s, a)/2 + {γΩα,πb(q)(s′) + r −q(s, a)}l(s, a)] .
(4)
Being motivated by the above formulation, our MSQP algorithm, speciﬁed in Algorithm 1,
approximates this formulation by replacing expectations with sample averages and restrict-
ing optimization to function classes with bounded complexity.
Remark 1 (Computation). Although minimax optimization is generally difﬁcult to solve,
it is computationally feasible when we choose RKHS or linear function classes for L. In
this case, we can solve the inner maximization problem analytically in closed form, as the
objective function is linear in l. As a result, the minimax optimization problem reduces to
empirical risk minimization.
3.2
Minimax Q⋆-learning with Penalization
Next, we examine a policy learning algorithm utilizing Q⋆-functions. To learn Q⋆, our
objective function is derived from the constrained optimization problem:
arg minq∈Q⋆′ 0.5E(s,a)∼Pb[q2(s, a)]
(6)
where Q⋆′ consists of all functions q : S × A →R satisfying
∀(s, a) ∈(S × A)b; Es′∼P (·|s,a)[γ maxa′∈A q(s′, a′) + r −q(s, a) | s, a] = 0.
Next, again using the method of Lagrange multipliers, (6) is transformed into
minq maxl L0(q, l), L0(q, l) := E[q2(s, a)/2 + {γ maxa′ q(s′, a′) + r −q(s, a)}l(s, a)].
(7)
7

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
Algorithm 2 MQP (Minimax Q⋆-learning with Penalization)
1: Require: Models Q, L ⊂[S × A →R+].
2: Estimate q⋆as follows:
ˆq0 ∈arg min
q∈Q
max
l∈L En[q2(s, a)/2 + {γ max
a′
q(s′, a′) + r −q(s, a)}l(s, a)].
(8)
3: Estimate the optimal policy: ˆπ0(a | s) = arg maxa:πb(a|s)>0 ˆq0(s, a).
Note L0 is the limit of Lα as α →0.
Our MQP algorithm, speciﬁed in Algorithm 2, similarly approximates this formulation
by replacing expectations with sample averages and restricting optimization to function
classes with bounded complexity. Our ﬁnal policy is greedy with respect to the learned Q-
function but restricting to the support of the ofﬂine data in order to avoid exploiting regions
not covered by the ofﬂine data.
Remark 2 (Prominent differences). There exist several other minimax estimators for Q⋆
including BRM (Antos et al., 2008) and MABO (Xie and Jiang, 2020). Although these en-
sure convergence guarantees in terms of Bellman residual errors, they do not ensure the
guarantee in terms of L2-errors, which is our focus.
Our minimax objective function differs signiﬁcantly from that of the aforementioned
approaches, and its unique design plays a pivotal role in enabling L2-rates.
4
L2-convergence Rates for Soft Q-functions and Q⋆-functions
To analyze our Q-estimators we ﬁrst establish conditions that ensure q⋆
α = arg minq∈Q maxl∈L Lα(q, l)
on the support (S × A)b. Building on this, we prove L2-convergence rates for ˆqα and ˆq0.
These L2-convergence guarantees are subsequently translated into performance guarantees
of the policies we output in Section 5.
4.1
Identiﬁcation of Soft Q-functions
Consider an L2-space H where the inner product is deﬁne as ⟨h1, h2⟩= E(s,a)∼Pb[h1(s, a)h2(s, a)].
Then we deﬁne two operators and a key function:2
P ⋆
α : H ∋f 7→Es′∼P (s,a),a′∼π⋆α[f(s′, a′) | (s, a) = ·] ∈H,
{P ⋆
α}⊤: H ∋f 7→
R
P(· | s, a)π⋆
α(· | ·)f(s, a)d(s, a) ∈H,
l⋆
α(s, a) :=
((I−γ{P ⋆
α}⊤)−1(Pb(s,a)q⋆
α(s,a))
Pb(s,a)
(s, a) ∈(S × A)b,
0
(s, a)̸ = (S × A)b.
2We use the notation ·⊤because P ⋆
α
⊤is interpreted as the adjoint operator in the non-weighted L2-space.
8

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
These satisfy a key adjoint property, which we leverage to show (q⋆
α, l⋆
α) is a saddle point
of Lα(q, l).
Lemma 1. ∀q ∈H, we have ⟨l⋆
α, (I −γP ⋆
α)q⟩H = ⟨q⋆
α, q⟩H.
Our ﬁrst assumption ensures that l⋆
α exists.
Assumption 1. Suppose ∥dπ⋆α,Pb/Pb∥∞< ∞. Note the inﬁnity norm ∥· ∥∞is over S × A.
Proposition 1. Under Assumption 1, we have ∥l⋆
α∥∞< ∞.
Proposition 1 is immediate noting that (I−γ{P ⋆
α}⊤)−1(Pb(·)q⋆
α(·)) = P∞
t=0 γt({P ⋆
α}⊤)t(Pbq⋆
α)
and recalling the discounted occupancy measure under π⋆
α with initial distribution µ0 is writ-
ten as dπ⋆α,µ0 = (1−γ)(I −γ{P ⋆
α}⊤)−1(µ0). Hence, ∥l⋆
α∥∞≤(1−γ)−1Rmax∥dπ⋆
α,Pb/Pb∥∞.
Note that ∥dπ⋆
α,Pb/Pb∥∞crucially differs with the standard density-ratio-based concen-
trability coefﬁcient ∥dπ∗α,µ0/Pb∥∞in ofﬂine RL. Unlike ∥dπ∗α,Pb/Pb∥∞, the value of ∥dπ∗α,µ0/Pb∥∞
can be inﬁnite when the initial distribution µ0 is not covered by ofﬂine data Pb as the prac-
tical motivating example is explained in the footnote in Section 1 and Example 2.
Our next assumption ensures q⋆
α ≥0, which also guarantees that l⋆
α ≥0.
Assumption 2. Suppose α log ∥π∗
α/πb∥∞≤Rmin.
Assumption 2 can be satisﬁed by rescaling reward (i.e., rescaling Rmin) as long as
∥π∗
α/πb∥∞is ﬁnite. Hence, it is very mild. Putting Lemma 1 together with our assumptions
we have the following.
Lemma 2. Suppose Assumptions 1 and 2 hold. Then, (q⋆
α, l⋆
α) is a saddle point of Lα(q, l)
over q ∈H, l ∈H, i.e., Lα(q, l⋆
α) ≥Lα(q⋆
α, l⋆
α) ≥Lα(q⋆
α, l) ∀q ∈H, ∀l ∈H.
Recall that a point (˜q, ˜l) is a saddle point if and only if the strong duality holds, and
˜q ∈arg minq∈H supl∈H Lα(q, l), ˜l ∈arg maxl∈H infq∈H Lα(q, l) using the general charac-
terization (Bertsekas, 2009). Hence, Lemma 2 ensures q⋆
α ∈arg minq∈H maxl∈H Lα(q, l).
Next, we consider the constrained optimization problem when we use function classes
Q ⊂H, L ⊂H. As long as the saddle point is included in (Q, L), we can prove that q⋆
α is
a unique minimaxer.
Lemma 3. Suppose Assumptions 1 and 2 hold, q⋆
α ∈Q, and l⋆
α ∈L. Then, we have that
q⋆
α = arg minq∈Q supl∈L Lα(q, l) on the support (S × A)b.
This establishes that realizability (q⋆
α ∈Q, l⋆
α ∈L) is sufﬁcient to identify q⋆
α on the
ofﬂine data distribution. At a high level, q⋆
α ∈arg minq∈Q supl∈L Lα(q, l) is established
through the invariance of saddle points, i.e., saddle points over original sets remain saddle
points over restricted sets. Its uniqueness is veriﬁed by the strong convexity in q of Lα(q, l)
induced by E(s,a)∼Pb[q2(s, a)].
9

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
4.2
L2-convergence Rate for Soft Q-estimators
Based on the population-level results in Section 4.1, we give a ﬁnite-sample error analysis
of ˆqα
Assumption 3 (Realizability of soft Q-function). Suppose q⋆
α ∈Q and ∥q∥∞≤BQ ∀q ∈
Q.
Assumption 4 (Realizability of Lagrange multiplier). Suppose l⋆
α ∈L and ∥l∥∞≤BL ∀l ∈
L.
It is natural to set BQ = (1 −γ)−1Rmax and BL = (1 −γ)−1Rmax∥dπ∗α,Pb/Pb∥∞, but
letting these be arbitrary offers further ﬂexibility to our results.
Theorem 1 (L2-convergence of soft Q-estimators). Suppose Assumptions 1, 2, 3, and 4
hold. Then, with probability 1 −δ, the L2-error ∥ˆqα −q⋆
α∥2 is upper-bounded by
c
 B2
Q + BQBL{α + ln(|A|)}
1/2 (ln(|Q||L|/δ)/n)1/4 .
Our result is signiﬁcant as it relies on realizability-type conditions rather than Bellman
closedness. Since the majority of existing works focus on non-regularized Q-functions, we
postpone the comparison to these existing works to the next section. Note when Q and
L are inﬁnite, we can easily replace |Q|, |L| with their L∞-covering numbers following
Uehara et al. (2021). Details are given in the appendix.
4.3
L2-convergence Rate for Q⋆-functions
Next, we give analogous ﬁnite-sample error analysis of ˆq0 leveraging the same reasoning.
Assumption 5 (Realizability of Q⋆-functions). Suppose q⋆∈Q and ∥q∥∞≤BQ ∀q ∈Q.
Next, we deﬁne the Lagrange multiplier:
{P ⋆}⊤: H ∋f 7→
Z
P(· | s, a)π⋆(· | ·)f(s, a)dµ(s, a) ∈H,
l⋆:= {(I −γ{P ⋆}⊤)−1(q⋆Pπb)}/Pπb.
While l⋆involves the density ratio, this is always well-deﬁned as long as ∥dπ⋆,Pb/Pb∥∞<
∞.
Then, it can be similarly established that (q⋆, l⋆) is a saddle point of L0(q, l) over
q ∈H, l ∈H as we show in Lemma 2. We lastly require its realizability.
Assumption 6 (Realizability of Lagrange multiplier). Suppose ∥dπ⋆,Pb/Pb∥∞< ∞and
l⋆∈L. Further suppose ∥l∥∞≤BL ∀l ∈L.
Theorem 2 (L2-convergence of Q-estimators). Suppose Assumptions 5 and 6 hold. Then,
with probability 1 −δ, the L2-error ∥ˆq0 −q⋆∥2 is upper-bounded by
c
 B2
Q + BLBQ
1/2 (ln(|Q||L|/δ)/n)1/4.
10

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
To the best of our knowledge, this is the ﬁrst guarantee on L2 errors for learning q∗using
general function approximation without relying on Bellman completeness. This is highly
nontrivial, and we have carefully crafted our algorithm to obtain this guarantee. Existing
results are often speciﬁc to particular models, such as linear models (Shi et al., 2022a), or
they require Bellman completeness (Chen and Jiang, 2019; Chen and Qi, 2022), or they are
limited to ofﬂine policy evaluation scenarios (Huang and Jiang, 2022) (i.e., cases involving
linear Bellman operators, but nonlinear Bellman operators). Actually, it seems that even
under the assumption of Bellman completeness, obtaining an L2 guarantee without strong
coverage assumptions remains unclear. A detailed comparison among these different ap-
proaches is presented in Section A.
5
Finite Sample Guarantee of MSQP
In this section, we present our primary sample complexity guarantee for our MSQP algo-
rithm under the assumptions of realizability of q⋆
α and l⋆
α and partial coverage. We ﬁrst
show the learned policy ˆπα can compete with π⋆
α. Finally we show ˆπα can compete with π⋆
by selecting α properly.
We ﬁrst introduce the ﬂattened behavior policy π⋄
b, which is uniform on the support
of πb. We use it as a technical device to deﬁne a model-free concentrability coefﬁcient
following Xie et al. (2021).
Deﬁnition 1 (Model-free concentrability coefﬁcient). Deﬁne
CQ,dπ⋆α,µ0 := sup
q∈Q
Es∼dπ⋆α,µ0,a∼π⋄
b (a|s)[∥q(s, a) −q⋆
α(s, a)∥2
2]
E(s,a)∼Pb[∥q(s, a) −q⋆α(s, a)∥2
2]
where π⋄
b(· | s) =
(
0
πb(· | s) = 0
1/|{a ∈A | πb(a | s) > 0}|
πb(· | s) > 0 is the ﬂattened behavior
policy.
Clearly, CQ,dπ⋆α,µ0 is smaller than density-ratio-based concentrability coefﬁcient, in other
words,
CQ,dπ⋆α,µ0 ≤max
(s,a)
dπ⋆α,µ0(s)π⋄
b(a | s)
Pb(s)πb(a | s)
.
Here, we always have ∥π⋄
b/πb∥< ∞even if πb(a | s) is 0 for some (s, a). In the special
case where πb(a | s) ≥1/C′ for any (s, a), we have CQ,dπ⋆α,µ0 ≤C′∥dπ⋆α,µ0/Pb∥∞. The
coefﬁcient CQ,dπ⋆α,µ0 is is a reﬁned concentrability coefﬁcient, which adapts to a function
class Q. For example, in linear MDPs, it reduces to a relative condition number as follows.
Similar properties are obtained in related works (Xie et al., 2021; Uehara and Sun, 2021).
Example 1 (Linear MDPs). A linear MDP is one such that, for a known feature vector
φ : S × A →Rd, the true density satisﬁes P(s′ | s, a) = ⟨µ⋆(s′), φ(s, a)⟩for some
µ⋆: S →Rd and the reward function satisﬁes E[r | s, a] = ⟨θr, φ(s, a)⟩for some θr ∈Rd.
11

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
In linear MDPs, q⋆
α is clearly linear in φ(s, a). Hence, the natural function class is
Q = {⟨θ, φ(s, a)⟩| ∥θ∥≤B} for a certain B ∈R+. Then, we have
CQ,dπ⋆α,µ0 = sup
x̸=0
x⊤Es∼dπ⋆α,µ0,a∼π⋄
b (a|s)[φ(s, a)φ(s, a)⊤]x
x⊤E(s,a)∼Pb[φ(s, a)φ(s, a)⊤]x
.
We are now prepared to present our main result, which states that given the realizability
of the soft Q-function q⋆
α and Lagrange multiplier l⋆
α, it is possible to compete with π⋆
α under
the coverage condition CQ,dπ⋆α,µ0 < ∞, ∥dπ⋆α,Pb/Pb∥∞< ∞.
Theorem 3 (ˆπα can compete with π⋆
α). Fix α > 0. Suppose Assumptions 1, 2, 3, and 4 hold.
With probability 1 −δ, the regret J(π⋆
α) −J(ˆπα) is upper-bounded by
n−1/4Poly

|A|, BQ, BL, CQ,dπ⋆α,µ0, ln
|Q||L|
δ

,
1
1 −γ , Rmax

The proof mainly consists of two steps: (1) obtaining L2-errors of ˆqα as previously
demonstrated in Theorem 1, (2) translating this error into the error of ˆπα. In the second
step, the Lipshitz continuity of the softmax function plays a crucial role. If there is no
regularization (α = 0) and the greedy policy of q⋆
0 is utilized, the second step does not
proceed (without any further additional assumptions).
Our ultimate goal is to compete with π⋆. Theorem 3 serves as the primary foundation
for this goal. The remaining task is to analyze the approximation error J(π⋆) −J(π⋆
α).
Fortunately, this term can be controlled through α and the density ratio between π⋆and πb.
Then, by properly controlling α, we can obtain the following sample complexity result.
Theorem 4 (PAC guarantee of ˆπα). Fix any ǫ > 0. Suppose Assumptions 1, 2, 3, and 4
hold for α = c/n1/8 and ∥π⋆
0/πb∥∞≤C0, CQ,dπ⋆α,µ0 < ∞. Then, if n is at least
ǫ−8Poly(|A|, BQ, BL, CQ,dπ⋆α,µ0, ln(|Q||L|/δ), (1 −γ)−1, ln(C0), Rmax),
with probability at least 1 −δ, we can ensure J(π⋆) −J(ˆπα) ≤ǫ.
In summary, the realiazability of q⋆
α, l⋆
α, per-step coverage ∥π⋆
0/πb∥∞< ∞and partial
coverage CQ,dπ⋆α,µ0 < ∞, ∥dπ⋆α,Pb/Pb∥∞< ∞are sufﬁcient to compete with π⋆. This is
a novel and attractive result. Firstly, if we solely use the na¨ıve FQI or Bellman residual
minimization, existing PAC results require the global coverage ∥dπ,µ0/Pb∥∞< ∞for any
possible policy π (Munos and Szepesv´ari, 2008; Antos et al., 2008). Our result only re-
quires coverage under a single policy π⋆
α (near-optimal policy). Secondly, we only require
the realizability of two functions, and we do not necessitate realizability-type conditions for
all policies in the policy class or Bellman completeness, unlike existing works with partial
coverage (Xie et al., 2021; Jiang and Huang, 2020).
The most similar result is Zhan et al. (2022). However, our guarantee possesses a cer-
tain advantage over their guarantee as follows. They demonstrate the realizability of certain
12

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
functions ˜w⋆
α, v⋆
α and partial coverage ∥d˜πα,µ0/Pb∥< ∞are sufﬁcient conditions in ofﬂine
RL, where ˜w⋆
α = d˜πα,µ0/Pb (˜πα is a certain regularized optimal policy, but fundamentally
distinct from π⋆
α) and v⋆
α is a near-optimal regularized value function parameterized by α.
Here, we have ˜w⋆
0 = w⋆, v⋆
0 = v⋆. Our guarantee has a similar ﬂavor in the sense that
it roughly illustrates realizability and partial coverage are sufﬁcient conditions. However,
the meanings of realizability and partial coverage are signiﬁcantly different. In particular,
by employing our algorithm, we can ensure PAC guarantees under the boundedness of the
reﬁned concentrability coefﬁcient CQ,dπ⋆α,µ0 < ∞(and ∥dπ⋆α,Pb/Pb∥∞through BL). As a re-
sult, the L∞-norm of the density-ratio-based concentrability coefﬁcient ∥dπ⋆α,µ0/Pb∥∞can
even be inﬁnite. More speciﬁcally, we can permit situations where maxs µ0(s)/Pb(s) = ∞
as we will see the practical example soon. Conversely, Zhan et al. (2022) excludes this
possibility since the algorithm explicitly estimates the density ratio ˜w⋆
α.
Example 2 (Contextual bandit under external validity). We consider the contextual bandit
setting where we want to optimize J(π) = Es∼µ0,a∼π(s),r∼Pr(s,a)[r] using ofﬂine data s ∼
Pb, a ∼πb(s), r ∼P(s, a). This is the simplest RL setting with γ = 0. Here, note µ0 could
be different from Pb. This case often happens in practice as discussed in the literature on
causal inference related to external validity (Pearl and Bareinboim, 2014; Dahabreh et al.,
2019; Uehara et al., 2020), which refers to the shift between the target population and the
ofﬂine data. Here, our PAC guarantee does not require that µ0(s) is covered by Pb(s) in
terms of the density ratio as long as the relative condition number is upper-bounded when
we use linear models. On the other hand, Zhan et al. (2022) excludes this possibility.
Despite the aforementioned advantage of our approach, unfortunately, our sample com-
plexity of O(1/ǫ8) is slower compared to that of O(1/ǫ6) in Zhan et al. (2022). In the
following, we demonstrate that MQP, which is a special version of MSQP when α →0,
can achieve a faster rate of O(1/ǫ2).
6
Finite Sample Guarantee of MQP
In this section, building upon the convergence result of ˆq0, we demonstrate the ﬁnite sample
guarantee of our MQP algorithm under partial coverage. We ﬁrst introduce the soft margin.
Assumption 7 (Soft margin). For any a′ ∈A, there exists t0 ∈R+, β ∈(0, ∞] such that
Ps∼dπ⋆,µ0(0 < |q⋆(s, π⋆(s)) −q⋆(s, a′)| < t) ≤(t/t0)β
for any t > 0. Here, we use the convention x∞= 0 if 0 < x < 1 and x∞= ∞if x > 1.
In the extreme case, if there exists a gap in q⋆(also known as a hard margin) so that
the best action is always better than the second-best by some lower bounded amount, then
the soft margin is satisﬁed with β = ∞. Thus, the soft margin is more general than the
gap condition used in Simchowitz and Jamieson (2019); Wu et al. (2022). Crucially, a gap
13

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
generally does not exist in continuous state spaces unless Q-functions are discontinuous or
one action is always option, or a gap involves a large t0 constant in discrete state spaces
with bad dependence on the number of states. In contrast, a soft margin with some β > 0
generally holds (see, e.g., lemma 4 in Hu et al., 2021). The soft margin is widely used
in the literature on classiﬁcation, decision making, and RL (Audibert and Tsybakov, 2007;
Perchet and Rigollet, 2013; Luedtke and Chambaz, 2020; Hu et al., 2021, 2022).
Theorem 5 (PAC guarantee of ˆπ0). Suppose Assumptions 5, 6, and 7 hold and ∥π⋆/πb∥∞≤
C0. Fix any ǫ > 0. Then, if n is at least
{ |A|
ǫ }
4+2β
β Poly

t−1
0 , |A|, BQ, BL, CQ,dπ⋆,µ0, ln

|Q||L|
δ

, (1 −γ)−1, ln(C0), Rmax

with probability at least 1 −δ, we can ensure J(π⋆) −J(ˆπ0) ≤ǫ.
The proof mainly consists of two steps: (1) obtaining L2-errors of ˆq0 as demonstrated in
Theorem 2, (2) translating this error into the error of ˆπ0. In the second step, the soft margin
plays a crucial role.
These theorems indicate that the realizability of the Q-function q⋆and Lagrange mul-
tiplier l⋆, and the soft margin are sufﬁcient for the PAC guarantee under partial cover-
age CQ,dπ⋆,µ0 < ∞, ∥dπ⋆,Pb/Pb∥∞< ∞. Our algorithm is agnostic to β and oper-
ates under any value of β. In particular, when there is a gap (β = ∞), we can achieve
sample complexity of O(1/ǫ2) 3.
In comparison to Theorem 3, although we addition-
ally use the soft margin, the realizability in Theorem 5 is more appealing since it is im-
posed on the standard Q-function q⋆. The closest guarantee to our work can be found in
Chen and Jiang (2022), which demonstrates that the existence of the gap in q⋆, the realiz-
ability of q⋆, w⋆(:= dπ⋆,µ0/Pπb), and partial coverage ∥w⋆∥∞< ∞are sufﬁcient conditions.
A similar comparison is made in Ozdaglar et al. (2023). In comparison to their work, we
use the soft margin, which is signiﬁcantly less stringent.
7
Conclusions
We propose two value-based algorithms, MSQP and MQP, that operate under realizabil-
ity of certain functions and partial coverage (i.e., single-policy-coverage). Notably, our
guarantee does not require Bellman completeness and uniform-type realizability over the
policy class. While guarantees with similar ﬂavors are obtained in Zhan et al. (2022);
Chen and Jiang (2022), MSQP can potentially relax the density-ratio-based partial cov-
erage regarding the initial distribution as opposed to Zhan et al. (2022), and MQP can
operate under the soft-margin, which is less stringent than the hard margin imposed in
Chen and Jiang (2022). Moreover, both algorithms work on Q-functions, which are more
commonly used in practice.
3Similar to the ﬁndings in Wang et al. (2022), in general ofﬂine RL, we may potentially achieve a result
of O(1/ǫ). We leave room for further enhancements in future research.
14

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
References
Andr´as Antos, Csaba Szepesv´ari, and R´emi Munos. Learning near-optimal policies with
bellman-residual minimization based ﬁtted policy iteration and a single sample path. Ma-
chine Learning, 71(1):89–129, 2008.
Jean-Yves Audibert and Alexandre B Tsybakov. Fast learning rates for plug-in classiﬁers.
The Annals of statistics, 35(2):608–633, 2007.
Chenjia Bai, Lingxiao Wang, Zhuoran Yang, Zhihong Deng, Animesh Garg, Peng Liu, and
Zhaoran Wang. Pessimistic bootstrapping for uncertainty-driven ofﬂine reinforcement
learning. arXiv preprint arXiv:2202.11566, 2022.
Dimitri Bertsekas. Convex optimization theory, volume 1. Athena Scientiﬁc, 2009.
Jonathan Chang, Masatoshi Uehara, Dhruv Sreenivas, Rahul Kidambi, and Wen Sun. Mit-
igating covariate shift in imitation learning via ofﬂine data with partial coverage. Ad-
vances in Neural Information Processing Systems, 34:965–979, 2021.
Jinglin Chen and Nan Jiang. Information-theoretic considerations in batch reinforcement
learning. In International Conference on Machine Learning, pages 1042–1051. PMLR,
2019.
Jinglin Chen and Nan Jiang. Ofﬂine reinforcement learning under value and density-ratio
realizability: the power of gaps. arXiv preprint arXiv:2203.13935, 2022.
Xiaohong Chen and Zhengling Qi.
On well-posedness and minimax optimal rates
of nonparametric q-function estimation in off-policy evaluation.
arXiv preprint
arXiv:2201.06169, 2022.
Stephen R Cole and Elizabeth A Stuart. Generalizing evidence from randomized clinical
trials to target populations: the actg 320 trial. American journal of epidemiology, 172(1):
107–115, 2010.
Issa J Dahabreh, Sarah E Robertson, Eric J Tchetgen, Elizabeth A Stuart, and Miguel A
Hern´an. Generalizing causal inferences from individuals in randomized trials to all trial-
eligible individuals. Biometrics, 75(2):685–694, 2019.
Rasool Fakoor, Jonas W Mueller, Kavosh Asadi, Pratik Chaudhari, and Alexander J Smola.
Continuous doubly constrained batch reinforcement learning. Advances in Neural Infor-
mation Processing Systems, 34:11260–11273, 2021.
Roy Fox, Ari Pakman, and Naftali Tishby. Taming the noise in reinforcement learning via
soft updates. arXiv preprint arXiv:1512.08562, 2015.
Bolin Gao and Lacra Pavel. On the properties of the softmax function with application in
game theory and reinforcement learning. arXiv preprint arXiv:1704.00805, 2017.
15

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
Matthieu Geist, Bruno Scherrer, and Olivier Pietquin. A theory of regularized markov
decision processes.
In International Conference on Machine Learning, pages 2160–
2169. PMLR, 2019.
Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-
policy maximum entropy deep reinforcement learning with a stochastic actor. In Inter-
national conference on machine learning, pages 1861–1870. PMLR, 2018.
Yichun Hu, Nathan Kallus, and Masatoshi Uehara.
Fast rates for the regret of ofﬂine
reinforcement learning. arXiv preprint arXiv:2102.00479, 2021.
Yichun Hu, Nathan Kallus, and Xiaojie Mao. Fast rates for contextual linear optimization.
Management Science, 68(6):4236–4245, 2022.
Audrey Huang and Nan Jiang. Beyond the return: Off-policy function estimation under
user-speciﬁed error-measuring distributions. In Neurips, 2022.
Nan Jiang and Jiawei Huang. Minimax value interval for off-policy evaluation and policy
optimization. Advances in Neural Information Processing Systems, 33:2747–2758, 2020.
Ying Jin, Zhuoran Yang, and Zhaoran Wang. Is pessimism provably efﬁcient for ofﬂine rl?
arXiv preprint arXiv:2012.15085, 2020.
Rahul Kidambi, Aravind Rajeswaran, Praneeth Netrapalli, and Thorsten Joachims. Morel:
Model-based ofﬂine reinforcement learning. In Advances in Neural Information Process-
ing Systems, volume 33, pages 21810–21823. Curran Associates, Inc., 2020.
Sergey Levine, Aviral Kumar, George Tucker, and Justin Fu.
Ofﬂine reinforcement
learning:
Tutorial, review, and perspectives on open problems.
arXiv preprint
arXiv:2005.01643, 2020.
Gene Li, Cong Ma, and Nathan Srebro. Pessimism for ofﬂine linear contextual bandits
using lp conﬁdence sets. arXiv preprint arXiv:2205.10671, 2022.
Alex Luedtke and Antoine Chambaz.
Performance guarantees for policy learning.
In
Annales de l’IHP Probabilites et statistiques, volume 56, page 2162. NIH Public Access,
2020.
R´emi Munos and Csaba Szepesv´ari. Finite-time bounds for ﬁtted value iteration. Journal
of Machine Learning Research, 9(5), 2008.
Oﬁr Nachum and Bo Dai. Reinforcement learning via fenchel-rockafellar duality. arXiv
preprint arXiv:2001.01866, 2020.
Gergely Neu, Anders Jonsson, and Vicenc¸ G´omez. A uniﬁed view of entropy-regularized
markov decision processes. arXiv preprint arXiv:1705.07798, 2017.
16

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
Thanh Nguyen-Tang, Ming Yin, Sunil Gupta, Svetha Venkatesh, and Raman Arora. On
instance-dependent bounds for ofﬂine reinforcement learning with linear function ap-
proximation. arXiv preprint arXiv:2211.13208, 2022.
Asuman E Ozdaglar, Sarath Pattathil, Jiawei Zhang, and Kaiqing Zhang. Revisiting the
linear-programming framework for ofﬂine rl with general function approximation. In
International Conference on Machine Learning, pages 26769–26791. PMLR, 2023.
Judea Pearl and Elias Bareinboim. External validity: From do-calculus to transportability
across populations. In Statistical Science, pages 451–482. 2014.
Vianney Perchet and Philippe Rigollet. The multi-armed bandit problem with covariates.
The Annals of Statistics, 41(2):693–721, 2013.
Paria Rashidinejad, Banghua Zhu, Cong Ma, Jiantao Jiao, and Stuart Russell. Bridging of-
ﬂine reinforcement learning and imitation learning: A tale of pessimism. arXiv preprint
arXiv:2103.12021, 2021.
Paria Rashidinejad, Hanlin Zhu, Kunhe Yang, Stuart Russell, and Jiantao Jiao. Optimal
conservative ofﬂine rl with general function approximation via augmented lagrangian.
arXiv preprint arXiv:2211.00716, 2022.
John Schulman, Xi Chen, and Pieter Abbeel. Equivalence between policy gradients and
soft q-learning. arXiv preprint arXiv:1704.06440, 2017.
Chengchun Shi, Sheng Zhang, Wenbin Lu, and Rui Song. Statistical inference of the value
function for reinforcement learning in inﬁnite-horizon settings. Journal of the Royal
Statistical Society Series B: Statistical Methodology, 84(3):765–793, 2022a.
Laixi Shi, Gen Li, Yuting Wei, Yuxin Chen, and Yuejie Chi. Pessimistic q-learning for
ofﬂine reinforcement learning: Towards optimal sample complexity.
arXiv preprint
arXiv:2202.13890, 2022b.
Max Simchowitz and Kevin G Jamieson. Non-asymptotic gap-dependent regret bounds for
tabular mdps. Advances in Neural Information Processing Systems, 32, 2019.
Masatoshi Uehara and Wen Sun. Pessimistic model-based ofﬂine reinforcement learning
under partial coverage. ICLR 2022, 2021.
Masatoshi Uehara, Masahiro Kato, and Shota Yasui. Off-policy evaluation and learning
for external validity under a covariate shift. Advances in Neural Information Processing
Systems, 33:49–61, 2020.
Masatoshi Uehara, Masaaki Imaizumi, Nan Jiang, Nathan Kallus, Wen Sun, and Tengyang
Xie. Finite sample analysis of minimax ofﬂine reinforcement learning: Completeness,
fast rates and ﬁrst-order efﬁciency. arXiv preprint arXiv:2102.02981, 2021.
17

````

## PDF page 18

Technical extraction; compare with original PDF page 18.

````text
Xinqi Wang, Qiwen Cui, and Simon S Du. On gap-dependent bounds for ofﬂine reinforce-
ment learning. Advances in Neural Information Processing Systems, 35:14865–14877,
2022.
Jingfeng Wu, Vladimir Braverman, and Lin Yang. Gap-dependent unsupervised explo-
ration for reinforcement learning. In International Conference on Artiﬁcial Intelligence
and Statistics, pages 4109–4131. PMLR, 2022.
Yifan Wu, George Tucker, and Oﬁr Nachum. Behavior regularized ofﬂine reinforcement
learning. arXiv preprint arXiv:1911.11361, 2019.
Tengyang Xie and Nan Jiang. Q* approximation schemes for batch reinforcement learning:
A theoretical comparison. In Conference on Uncertainty in Artiﬁcial Intelligence, pages
550–559. PMLR, 2020.
Tengyang Xie, Ching-An Cheng, Nan Jiang, Paul Mineiro, and Alekh Agarwal. Bellman-
consistent pessimism for ofﬂine reinforcement learning. Advances in neural information
processing systems, 34:6683–6694, 2021.
Mengjiao Yang, Oﬁr Nachum, Bo Dai, Lihong Li, and Dale Schuurmans. Off-policy evalua-
tion via the regularized lagrangian. Advances in Neural Information Processing Systems,
33:6551–6561, 2020.
Ming Yin and Yu-Xiang Wang. Towards instance-optimal ofﬂine reinforcement learning
with pessimism. Advances in neural information processing systems, 34:4065–4078,
2021.
Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Y Zou, Sergey Levine,
Chelsea Finn, and Tengyu Ma. Mopo: Model-based ofﬂine policy optimization. In
Advances in Neural Information Processing Systems, volume 33, pages 14129–14142,
2020.
Andrea Zanette and Martin J Wainwright. Bellman residual orthogonalization for ofﬂine
reinforcement learning. arXiv preprint arXiv:2203.12786, 2022.
Wenhao Zhan, Baihe Huang, Audrey Huang, Nan Jiang, and Jason Lee.
Ofﬂine rein-
forcement learning with realizability and single-policy concentrability. In Conference
on Learning Theory, pages 2730–2775. PMLR, 2022.
Xuezhou Zhang, Yiding Chen, Xiaojin Zhu, and Wen Sun. Corruption-robust ofﬂine rein-
forcement learning. In International Conference on Artiﬁcial Intelligence and Statistics,
pages 5757–5773. PMLR, 2022.
Hanlin Zhu, Paria Rashidinejad, and Jiantao Jiao. Importance weighted actor-critic for
optimal conservative ofﬂine reinforcement learning. arXiv preprint arXiv:2301.12714,
2023.
18

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
Brian D Ziebart, Andrew L Maas, J Andrew Bagnell, Anind K Dey, et al.
Maximum
entropy inverse reinforcement learning. In Aaai, volume 8, pages 1433–1438. Chicago,
IL, USA, 2008.
Brian D Ziebart, J Andrew Bagnell, and Anind K Dey. Modeling interaction via the princi-
ple of maximum causal entropy. In ICML, 2010.
A
More Related Works
We elaborate on the challenge and novelty of our guarantees in comparison to previous
related works.
Existing L2-guarantees for ofﬂine RL (Shi et al., 2022a).
Shi et al. (2022a) derived the
L2 convergence rate for learning the optimal Q⋆-function. However, their result is restricted
to linear models. While linear models allow for converting Bellman residual errors into L2-
errors under mild assumptions regarding the non-singularity of the covariance matrix, this
guarantee can be achieved through various methods such as modiﬁed BRM (Antos et al.,
2008). However, it remains unclear how to extend this guarantee to general function ap-
proximation settings.
Existing L2-guarantees for off-policy evaluation (Huang and Jiang, 2022; Zhan et al.,
2022).
According to Huang and Jiang (2022), L2-rates were obtained in the context of
ofﬂine policy evaluation, while Zhan et al. (2022) obtained the L2-rate for the (regularized)
optimal marginal density ratio function. While our approach builds upon these works, it is
still considered novel due to the nonlinear constraints we consider, which provide an addi-
tional challenge in the analysis. In contrast, the constraints considered by Huang and Jiang
(2022); Zhan et al. (2022) were linear.
In order to grasp the difﬁculty at a high level, suppose that the state space is tabular 4.
Recall our estimator is motivated by the constrained optimization problem (3). Although
the left-hand side of (3) is convex in q, the constraint induced by the equality is generally
not convex. As a result, this problem is not a convex optimization problem. Therefore, it
is not straightforward whether the saddle point exists when we consider the minimax form.
This differs from previous works (Huang and Jiang, 2022; Zhan et al., 2022), where the
constraint from the linear equality remains convex.
The key insight for addressing this issue is the realization that the equality constraint (=)
in (3) can be relaxed to an inequality constraint (≤) in (3). This relaxation is surprisingly
valid in our problem. As a result, the resulting optimization problem is convex, and a saddle
point exists. For further discussion, see Section B.
4Note our theory still proceeds in the non-tabular case.
19

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
Bellman residual minimization (Antos et al., 2008; Chen and Jiang, 2019; Chen and Qi,
2022).
Chen and Jiang (2022) derived convergence rates for Q-functions in terms of Bell-
man residual errors: E(s,a)∼Pb[(B⋆q −q)2(s, a)] where B⋆is a Bellman operator. While the
convergence of the L2-error implies that of the Bellman residual error since we have
E(s,a)∼Pb[(B⋆q −q)2(s, a)] ≤(1 + γ2E(s,a)∼Pb[(π⋆/πb)2(s, a)])∥q −q⋆∥2
2,
the reverse direction does not generally hold. Although Chen and Qi (2022) demonstrated
the reverse direction by postulating several potentially stringent conditions 5 of ofﬂine data
regarding OPE, it does not generally hold in the absence of these assumptions. Furthermore,
we consider the more challenging setting, ofﬂine policy optimization where the Bellman
operator is nonlinear. Thus, it is imperative to utilize our specialized objective function to
ensure a stronger guarantee in terms of L2-errors.
B
Intuition of Why Saddle Points Exist
In this section, in the tabular setting, we explain how the original optimization problem is
reduced to a convex optimization problem in detail. Note proofs in our theorems do not
directly use the facts in this Section B. Hence, they hold even in the non-tabular setting.
B.1
Q⋆-functions
We consider the optimization problem:
arg min
q∈Q⋆′
0.5E(s,a)∼Pb[q2(s, a)]
where Q⋆′ is a space that consists of q ∈([S × A] →R) that satisﬁes
∀(s, a) ∈(S × A)b; Es′∼P (·|s,a)[γ max
a′∈A q(s′, a′) + r −q(s, a) | s, a] = 0.
The solution (on the ofﬂine data) is clearly q⋆
0. However, this optimization problem is not a
convex optimization problem. Hence, the associated minimax optimization might not have
a saddle point.
Here, we want to claim the following:
q⋆
0(s, a) = arg min
q∈Q⋆′
0.5E(s,a)∼Pb[q2(s, a)](∀(s, a) ∈(S × A)b)
(9)
where Q⋆′ is a space that consists of q ∈([S × A] →R) that satisﬁes
∀(s, a) ∈(S × A)b; Es′∼P (·|s,a)[γ max
a′∈A q(s′, a′) + r −q(s, a) | s, a] ≤0.
This is a convex optimization problem. Hence, we can expect the associated minimax
optimization would have a saddle point. In fact, this is proved as follows.
5These conditions would implicitly impose restriction of the coverage of the ofﬂine data.
20

````

## PDF page 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
Lemma 4. The equation (9) holds.
Proof. Suppose q(s, a; c) is a minimum L2-norm solution that satisﬁes
∀(s, a) ∈(S × A)b; Es′∼P (·|s,a)[γ max
a′∈A q(s′, a′) + r −q(s, a) | s, a] = −c(s, a)
and c(s, a) ≥0.
Suppose c(s, a)̸ = 0 on some (s, a) ∈(S × A)b. Then, we obtain
∀(s, a) ∈(S × A)b; q(s, a; c) = Eπ⋆(c)[rt + c(st, at) | (s0, a0) = (s, a)]
where π⋆(c) is the optimal policy when the reward is ˜r(s, a) + c(s, a). This is derived by a
contraction mapping theorem on the L∞-space on (S × A)b. Here, recall
∀(s, a) ∈(S × A)b; q⋆(s, a) = q(s, a; 0) ≥0
Furthermore, ∀(s, a) ∈(S × A)b; q(s, a; 0) ≤q(s, a; c) clearly holds, and, especially, the
strict inequality holds on some point in (S × A)b. This is because if q(s, a; 0) = q(s, a; c),
we get the contradiction:
∀(s, a) ∈(S × A)b; 0 = Es′∼P (·|s,a)[γ max
a′∈A q(s′, a′) + r −q(s, a) | s, a] = c(s, a).
However, in this situation, we have
E(s,a)∼Pb[q2(s, a; 0)] < E(s,a)∼Pb[q2(s, a; c)].
Thus, it contradicts q2(s, a; c) takes a least L2-norm. Therefore, it is concldued c(s, a) = 0
for any (s, a) ∈(S × A)b. Thus, using the contraction mapping theorem, this implies the
least L2-norm solution is unique and q⋆(s, a) on (s, a) ∈(S × A)b.
B.2
Soft Q-functions
We consider the optimization problem:
arg min
q∈Q′
0.5E(s,a)∼Pb[q2(s, a)]
(10)
where Q′ is a space that consists of q ∈([S × A] →R) that satisﬁes
∀(s, a) ∈(S × A)b; Es′∼P (·|s,a)[γα log
X
a′
{exp(q(s′, a′)/α)πb(a′ | s′)} + r −q(s, a) | s, a] ≤0.
(11)
Lemma 5. Suppose α log ∥π⋆/πb∥∞≤Rmin. Then, the solution to (10) is q⋆
α.
21

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
Proof. Suppose qα(s, a; c) is a minimum L2-norm solution that satisﬁes
∀(s, a) ∈(S × A)b; Es′∼P (·|s,a)[γα log(
X
a′
exp(q(s′, a′)/α)πb(a′ | s′) + r −q(s, a) | s, a] = −c(s, a)
and c(s, a) ≥0.
Suppose c(s, a)̸ = 0 on some (s, a) ∈(S × A)b. Then, we obtain
∀(s, a) ∈(S × A)b; qα(s, a; c) = Eπ⋆α(c)[rt + c(st, at) | (s0, a0) = (s, a)]
where π⋆
α(c) is the optimal policy when the reward is ˜r(s, a) + c(s, a). This is derived by a
contraction mapping theorem on the L∞-space on (S × A)b 6.Here, recall
∀(s, a) ∈(S × A)b; q⋆
α(s, a) = qα(s, a; 0) ≥0
The proof is performed as in the ﬁrst step of the proof of Lemma 2. We use the assumption
in this step.
Furthermore, ∀(s, a) ∈(S ×A)b; qα(s, a; 0) ≤qα(s, a; c) clearly holds, and, especially,
the strict inequality holds on some point in (S × A)b. This is because if qα(s, a; 0) =
qα(s, a; c), we get the contradiction:
∀(s, a) ∈(S × A)b; 0 = Es′∼P (·|s,a)[γα log(
X
a′
exp(q(s′, a′)/α)πb(a′ | s′) + r −q(s, a) | s, a] = c(s, a).
However, in this situation, we have
E(s,a)∼Pb[q2
α(s, a; 0)] < E(s,a)∼Pb[q2
α(s, a; c)].
Thus, it contradicts q2
α(s, a; c) takes a least L2-norm. Therefore, it is concluded c(s, a) = 0
for any (s, a) ∈(S × A)b. Thus, using the contraction mapping theorem, this implies the
least L2-norm solution is unique and q⋆
α(s, a) on (s, a) ∈(S × A)b.
C
Proof in Section 4.1
C.1
Proof of Lemma 1
We deﬁne an L2-space H′ with no weight on the support of (S × A)b. In other words, we
deﬁne
⟨q1, q2⟩H′ :=
Z
q1(s, a)q2(s, a)I(Pb(s, a) > 0)d(s, a).
6Recall the soft Bellman operator is a contraction mapping in L∞-space.
22

````

## PDF page 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
Then, we have
⟨l⋆
α, (I −γP ⋆
α)q⟩H = ⟨Pbl⋆
α, (I −γP ⋆
α)q⟩H′
= ⟨(I −γ{P ⋆
α}⊤)−1(Pbq⋆
α), (I −γP ⋆
α)q⟩H′
= ⟨(I −γ{P ⋆
α}⊤)(I −γ{P ⋆
α}⊤)−1(Pbq⋆
α), q⟩H′
= ⟨Pbq⋆
α, q⟩H′ = ⟨q⋆
α, q⟩H.
Here, letting P ⋆
α(s′, a′ | s, a) = P(s′ | s, a)π⋆(a′ | s′) we use
⟨g1, P ⋆
αg2⟩H′
=
Z
g1(s, a)g2(s′, a′)P ⋆
α(s′, a′ | s, a)I(Pb(s, a) > 0)dµ(s, a, s′, a′)
(Deﬁnition)
=
Z
g1(s, a)g2(s′, a′)P ⋆
α(s′, a′ | s, a)I(Pb(s, a) > 0)I(Pb(s′, a′) > 0)dµ(s, a, s′, a′)
(Recall we assume ∥π⋆/πb∥≤∞.)
= ⟨{P ⋆
α}⊤g1, g2⟩H′.
Note ⟨g1, P ⋆
αg2⟩H = ⟨{P ⋆
α}⊤g1, g2⟩H does not generally hold.
C.2
Proof of Lemma 2
It is obvious that
∀l ∈H; Lα(q⋆
α, l⋆
α) = Lα(q⋆
α, l).
Hence, we show
∀q ∈H; Lα(q, l⋆
α) ≥Lα(q⋆
α, l⋆
α)
To achieve this goal, we show
0.5E(s,a)∼Pb[(q −q⋆
α)(s, a)2] ≤Lα(q, l⋆
α) −Lα(q⋆
α, l⋆
α).
(12)
Using Lemma 1, a function l⋆
α satisﬁes a key adjoint property:
E(s,a,s′)∼Pb,a′∼π⋆α(s′)[l⋆
α(s, a){γq(s′, a′) −q(s, a)}] = −E(s,a,s′)∼Pb,a′∼π⋆α(s′)[q⋆
α(s, a)q(s, a)].
(13)
for any q ∈H.
23

````

## PDF page 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
First Step: Show l⋆
α(s, a) ≥0 and q⋆
α(s, a) ≥0 for any (s, a) ∈S × A.
Recall
q⋆
α(s, a) = Eπ⋆α[r0 +
∞
X
t=1
{γtrt −αγt log π⋆
α(at | st)/πb(at | st)} | s0 = s, a0 = a]
where the inside of the expectation is taken under a policy π⋆
α. Hence,
q⋆
α(s, a) ≥γ(1 −γ)−1(Rmin −α log(∥π⋆
α/πb∥∞)).
(14)
Therefore, using Assumption 2, we have
q⋆
α(s, a) ≥0
for any (s, a) ∈S × A. Finally, from the deﬁnition of l⋆
α, we obtain
l⋆
α(s, a) ≥0
for any (s, a) ∈S × A.
Second Step: Show 0.5E(s,a)∼Pb[(q −q⋆
α)(s, a)2] ≤Lα(q, l⋆
α) −Lα(q⋆
α, l⋆
α) for any q ∈H.
Then, for any q ∈H, we have
Lα(q, l⋆
α) −Lα(q⋆
α, l⋆
α)
= 0.5E(s,a)∼Pb[q2(s, a) −q⋆
α(s, a)2]+
+ E(s,a,s′)∼Pb[l⋆
α(s, a){γα log
X
a′
{exp(q(s′, a′)/α)πb(a′ | s′)} −q(s, a)}]
−E(s,a,s′)∼Pb[l⋆
α(s, a){γα log
X
a′
{exp(q⋆
α(s′, a′)/α)πb(a′ | s′)} −q⋆
α(s, a)}]
≥0.5E(s,a)∼Pb[q2(s, a) −q⋆
α(s, a)2]+
+ E(s,a,s′)∼Pb

l⋆
α(s, a)γ
P
a′ exp(q⋆
α(s′, a′)/α)πb(a′ | s′){q(s′, a′) −q⋆
α(s′, a′)}
P
a′ exp(q⋆α(s′, a′)/α)πb(a′ | s′)

(Convexity)
+ E(s,a)∼Pb[−l⋆
α(s, a)q(s, a) + l⋆
α(s, a)q⋆
α(s, a)]
= 0.5E(s,a)∼Pb[q2(s, a) −q⋆
α(s, a)2]+
+ E(s,a,s′)∼Pb,a′∼π⋆α(s′)[l⋆
α(s, a){γq(s′, a′) −q(s, a) −γq⋆
α(s′, a′) + q⋆
α(s, a)}].
In the convexity part, what we use is
f(x) −f(y) ≥
|A|
X
i=1
∂f
∂yi
(xi −yi),
f(x) = α log(
|A|
X
i=1
exp(xi/α)).
and
∀(s, a) ∈(S × A)b; l⋆
α(s, a) ≥0.
24

````

## PDF page 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
Finally, by using an adjoint propety of l⋆
α in (13),
Lα(q, l⋆
α) −Lα(q⋆
α, l⋆
α)
≥0.5E(s,a)∼Pb[q2(s, a) −q⋆
α(s, a)2] −E(s,a)∼Pb[q⋆
α(s, a){q(s, a) −q⋆
α(s, a)}]
= 0.5E(s,a)∼Pb[{q(s, a) −q⋆
α(s, a)}2].
Then, (12) is concluded.
C.3
Proof of Lemma 3
We denote the solution of arg minq∈Q supl∈L Lα(q, l) by ˆq. Let
ˆl(q) = arg max
l∈L
Lα(q, l),
ˆl = ˆl(ˆq).
Then, we have
Lα(ˆq, l⋆
α) −Lα(q⋆
α, l⋆
α)
= −Lα(q⋆
α, l⋆
α) + Lα(q⋆
α, ˆl(q⋆
α))
|
{z
}
(a)
−Lα(q⋆
α, ˆl(q⋆
α)) + Lα(ˆq, ˆl)
|
{z
}
(c)
−Lα(ˆq, ˆl) + Lα(ˆq, l⋆
α)
|
{z
}
(d)
≤0.
In (a), we use the property of the saddle point in Lemma 2. In (c) and (e), we use the
deﬁnition of estimators. Hence,
0 ≤0.5E(s,a)∼Pb[{q(s, a) −q⋆
α(s, a)}2]
≤Lα(ˆq, l⋆
α) −Lα(q⋆
α, l⋆
α)
(Recall (12))
≤0.
This concludes the statement.
C.4
Proof of Theorem 1
In this proof, the expectation is taken with respect to the ofﬂine data. We deﬁne
ˆLα(q, w) = En[0.5q2(s, a) + l(s, a){r + αγ log(
X
a′
exp(q(s′, a′)/α)πb(a′ | s′)) −q(s, a)}],
ˆl(q) = arg max
l∈L
En[0.5q2(s, a) + l(s, a){r + αγ log(
X
a′
exp(q(s′, a′)/α)πb(a′ | s′)) −q(s, a)}],
ˆl = ˆl(ˆqα).
25

````

## PDF page 26

FORMULA CHECK REQUIRED: original PDF page 26.

````text
We use the following decomposition:
Lα(ˆqα, l⋆
α) = −Lα(q⋆
α, l⋆
α) + L(q⋆
α, ˆl(q⋆
α))
|
{z
}
(a)
−Lα(q⋆
α, ˆl(q⋆
α)) + ˆLα(q⋆
α, ˆl(q⋆
α))
|
{z
}
(b)
−ˆLα(q⋆
α, ˆl(q⋆
α)) + ˆLα(ˆqα, ˆl)
|
{z
}
(c)
−ˆLα(ˆqα, ˆl) + ˆLα(ˆqα, l⋆
α)
|
{z
}
(d)
−ˆLα(ˆqα, l⋆
α) + Lα(ˆqα, l⋆
α)
|
{z
}
(e)
.
Here, terms (a) is than 0 using the saddle point property in Lemma 2. Term (c) and (d) are
less than 0 using the construction of estimators. Besides, using Hoeffding’s inequality, with
probability 1 −δ, terms (b) and (e) are less than
c
 B2
Q + BQBL + γBL{α + α ln(|A|)}

r
ln(|Q||L|/δ)
n
.
Hereafter, we condition on this event. Here, we use
|0.5q2(s, a) + l(s, a){r + αγ log(
X
a′
exp(q(s′, a′)/α)πb(a′ | s′)) −q(s, a)}|
≤|αl(s, a)γ log(
X
a′
exp(q(s′, a′)/α)πb(a′ | s′))| + |0.5q2(s, a) + l(s, a){r −q(s, a)}|
≤0.5B2
Q + BL{Rmax + BQ} + γBLα max
a′ (BQ/α + πb(a′ | s′)) + γBL ln(|A|)
(Use Lemma 7 and l(s, a) ≥0 for any (s, a).)
≲B2
Q + BLBQ + γBL{α + α ln(|A|)}.
Therefore,
0.5E(s,a)∼Pb[{ˆqα(s, a) −q⋆
α(s, a)}2]
≤L(l⋆
α, ˆqα) −L(l⋆
α, q⋆
α)
(Recall (12))
≤c
 B2
Q + BLBQ + BLγ{α + α ln(|A|)}

r
ln(|Q||L|/δ)
n
.
In the ﬁrst inequality, we use (12).
C.5
Proof of Theorem 2
In this proof, the expectation is taken w.r.t. the ofﬂine data. We deﬁne
L0(q, l) = E[0.5q2(s, a) + l(s, a){r + γ max
a′ (q(s′, a′) −q(s, a)}],
ˆL0(q, l) = En[0.5q2(s, a) + l(s, a){r + γ max
a′
q(s′, a′) −q(s, a)}],
ˆl(q) = arg max
l
En[0.5q2(s, a) + l(s, a){r + max
a′
q(s′, a′) −q(s, a)}],
ˆl = ˆl(ˆq0).
26

````

## PDF page 27

FORMULA CHECK REQUIRED: original PDF page 27.

````text
Part1: Show l⋆(s, a) ≥0 for any (s, a) ∈S × A.
First, since Rmin ≥0, we have
q⋆(s, a) ≥0. Then, recalling the deﬁnition:
l⋆:= {(I −γ{P ⋆}⊤)−1(q⋆Pπb)}/Pπb,
we obtain l⋆(s, a) ≥0 for any (s, a) ∈S × A.
Part 2: Showing 0.5E(s,a)∼Pb[(q −q⋆)(s, a)2] ≤L0(q, l⋆) −L0(q⋆, l⋆).
Note l⋆(s, a)
satisﬁes
E(s,a,s′)∼Pb,a′∼π⋆(s′)[l⋆(s, a){γq(s′, a′) −q(s, a)}] = −E(s,a,s′)∼Pb,a′∼π⋆(s′)[q⋆(s, a)q(s, a)].
(15)
for any q(s, a) ∈Q.
Then, for any q ∈Q, we have
L0(q, l⋆) −L0(q⋆, l⋆)
= 0.5E(s,a)∼Pb[q2(s, a) −q⋆(s, a)2] + E(s,a,s′)∼Pb[l⋆(s, a){γ max
a′
q(s′, a′) −q(s, a)}]
−E(s,a,s′)∼Pb[l⋆(s, a){γ max
a′
q⋆(s′, a′) −q⋆(s, a)}]
≥0.5vE(s,a)∼Pb[q2(s, a) −q⋆(s, a)2] + E(s,a,s′)∼Pb[l⋆(s, a){γq(s′, π⋆(s)) −γq⋆(s′, π⋆(s))}]
(Convexity)
+ E(s,a)∼Pb[−l⋆(s, a)q(s, a) + l⋆(s, a)q⋆(s, a)]
= 0.5E(s,a)∼Pb[q2(s, a) −q⋆(s, a)2]+
+ E(s,a,s′)∼Pb,a′∼π⋆(s′)[l⋆(s, a){γq(s′, a′) −q(s, a) −γq⋆(s′, a′) + q⋆(s, a)}].
In the convexity part, what we use is
max
i {f(xi)} −max
i {f(yi)} ≥f(xarg maxi{f(yi)}) −max
i {f(yi)}
and
∀(s, a) ∈(S × A)b; l∗(s, a) ≥0.
Finally, by using the adjoint property (15),
L0(q, l⋆) −L0(q⋆, l⋆)
≥0.5E(s,a)∼Pb[q2(s, a) −q⋆(s, a)2] −E(s,a)∼Pb[q⋆(s, a){q(s, a) −q⋆(s, a)}]
= 0.5E(s,a)∼Pb[{q(s, a) −q⋆(s, a)}2].
27

````

## PDF page 28

FORMULA CHECK REQUIRED: original PDF page 28.

````text
Part 3: Showing the ﬁnal bound.
We use the following decomposition:
L0(ˆq0, l⋆) = −L(q⋆, l⋆) + L0(q⋆, ˆl(q⋆))
|
{z
}
(a)
−L0(q⋆, ˆl(q⋆)) + ˆL0(q⋆, ˆl(q⋆))
|
{z
}
(b)
−ˆL0(q⋆, ˆl(q⋆)) + ˆL0(ˆq0, ˆl)
|
{z
}
(c)
−ˆL0(ˆq0, ˆl) + ˆL0(ˆq0, l⋆)
|
{z
}
(d)
−ˆL0(ˆq0, l⋆) + L0(ˆq0, l⋆)
|
{z
}
(e)
.
Here, (a) is equal to 0 since q⋆satisﬁes the Bellman equation. Besides, using Hoeffd-
ing’s inequality, with probability 1 −δ, terms (b) and (e) are less than
c
 B2
Q + BLBQ

r
ln(|Q||L|/δ)
n
.
Terms (c) and (d) are greater than 0 using the construction of estimators. This implies
0.5E(s,a)∼Pb[{ˆq0(s, a) −q⋆(s, a)}2] ≤L0(ˆq0, l⋆) −L0(q⋆, l⋆)
(Second step.)
≤c
 B2
Q + BLBQ

r
ln(|Q||L|/δ)
n
.
D
Proof in Section 5
D.1
Proof of Theorem 3
Using Theorem 1, with probability 1 −δ, the following holds
E(s,a)∼Pb[{ˆqα(s, a) −q⋆
α(s, a)}2] ≲Error,
(16)
Error =
 B2
Q + BQBL + BLγ{α + α ln(|A|)}

r
ln(|Q||L|/δ)
n
.
Hereafter, we condition on this event. Then, letting ˆπα(a | s) = softmax(ˆqα/α + log πb),
we have
J(π⋆
α) −J(ˆπα) ≤(1 −γ)−1RmaxEs∼dπ⋆α[
X
a
|π⋆
α(a | s) −ˆπα(a | s)|]
(Performance difference lemma in Lemma 6)
≤(1 −γ)−1RmaxEs∼dπ⋆α

p
|A|
 X
a
{π⋆
α(a | s) −ˆπα(a | s)}2
!1/2

(CS inequality)
= (1 −γ)−1RmaxEs∼dπ⋆α


p
|A|


X
a:πb(a|s)>0
{π⋆
α(a | s) −ˆπα(a | s)}2


1/2
.
28

````

## PDF page 29

FORMULA CHECK REQUIRED: original PDF page 29.

````text
From the second line to the third line, we use a relation that π⋆
α, ˆπα, and πb have the same
support.
Now, we want to connect this bound with L2-error of Q-functions. This is possible since
the softmax function with Lipschitz constant 1/α is Lipschitz continuous with constant 1/α
in Gao and Pavel (2017, Proposition 4). Hence, the right hand side is upper-bounded by
(1 −γ)−1p
|A|/αRmaxEs∼dπ⋆α





X
a:πb(a|s)>0
{ˆqα(s, a) −q⋆
α(s, a)}2



1/2
.
From Jensen’s inequality, this is further upper-bounded by
(1 −γ)−1p
|A|/αRmaxEs∼dπ⋆α


X
a:πb(a|s)>0
{ˆqα(s, a) −q⋆
α(s, a)}2


1/2
.
Then, using the deﬁnition of π⋄
b, this is upper-bounded by
(1 −γ)−1|A|/αRmaxEs∼dπ⋆α,a∼π⋄
b (·|s)

{ˆqα(s, a) −q⋆
α(s, a)}21/2
Finally, by combining this result with (16), we get the ﬁnal guarantee.
D.2
Proof of Theorem 4
We have
J(π) −Jα(π) = Rmaxα(1 −γ)−1Es∼dπ,a∼π(s)[log π(a | s)/πb(a | s)] ≥0
(17)
for any π. Then,
J(π⋆) −J(π⋆
α) = J(π⋆) −Jα(π⋆) + Jα(π⋆) −Jα(π⋆
α)
|
{z
}
(a)
+ Jα(π⋆
α) −J(π⋆
α)
|
{z
}
(b)
≤J(π⋆) −Jα(π⋆).
Note the term (a) is less than 0 since π⋆
α is the optimal softmax policy and the term (b) is
less than 0 using (17). Furthermore,
J(π⋆) −Jα(π⋆) = (1 −γ)−1αRmaxEs∼dπ⋆,a∼π⋆(s)[log π⋆(a | s)/πb(a | s)]
≤(1 −γ)−1αRmax log C0.
Therefore, by combining with Theorem 3, we have
J(π⋆) −J(ˆπα) ≤cRmax
|A|C1/2
Q,dπ⋆α,µ0{BQ + γBL{BQα + ln(|A|)}}1/2{ln(|Q||L|/δ)}1/4
(1 −γ)αn1/4
+ cRmaxα log C0
1 −γ
.
The sample complexity is easily obtained from this result.
29

````

## PDF page 30

FORMULA CHECK REQUIRED: original PDF page 30.

````text
E
Proof in Section 6
From Section D, with probability 1 −δ, the following holds
E(s,a)∼Pb[{ˆq(s, a) −q⋆(s, a)}2] ≲Error,
(18)
Error =
 B2
Q + γBLBQ

r
ln(|Q||L|/δ)
n
.
Hereafter, we condition on this event. Then, letting
ˆπ(a | s) =
arg max
a∈A:πb(a|s)>0
ˆq(s, a),
we have
(1 −γ)2R−1
max{J(π⋆) −J(ˆπ)}
≤Es∼dπ⋆[I(π⋆(s)̸ = ˆπ(s))]
(Performance difference lemma in Lemma 6)
≤Es∼dπ⋆


X
a′:a′∼πb(a|s)>0
I(ˆq(s, a′) −ˆq(s, π⋆(s)) ≥0 & q⋆(s, a′) −q⋆(s, π⋆(s)) < 0)

.
Hence, we have
Es∼dπ⋆


X
a′:a′∼πb(a|s)>0
I(ˆq(s, a′) −ˆq(s, π⋆(s)) ≥0 & q⋆(s, a′) −q⋆(s, π⋆(s)) < 0)


≤Es∼dπ⋆


X
a′:a′∼πb(a|s)>0
I(0 > q⋆(s, a′) −q⋆(s, π⋆(s)) ≥−t)

+
+ Es∼dπ⋆


X
a′:a′∼πb(a|s)>0
I(ˆq(s, a′) −ˆq(s, π⋆(s)) −q⋆(s, a′) + q⋆(s, π⋆(s)) ≥t)


In the ﬁrst term, we can use a margin assumption:
Es∼dπ⋆


X
a′:a′∼πb(a|s)>0
I(0 > q⋆(s, a′) −q⋆(s, π⋆(s)) ≥−t)

≤c|A|(t/t0)β.
30

````

## PDF page 31

FORMULA CHECK REQUIRED: original PDF page 31.

````text
In the second term, we can use
Es∼dπ⋆


X
a′:a′∼πb(a|s)>0
t2I(ˆq(s, a′) −ˆq(s, π⋆(s)) −q⋆(s, a′) + q⋆(s, π⋆(s)) ≥t)


≤Es∼dπ⋆


X
a′:a′∼πb(a|s)>0
|ˆq(s, a′) −ˆq(s, π⋆(s)) −q⋆(s, a′) + q⋆(s, π⋆(s))|2


≤2Es∼dπ⋆


X
a′:a′∼πb(a|s)>0
|ˆq(s, a′) −q⋆(s, a′)|2
2 + |ˆq(s, π⋆(s)) −q⋆(s, π⋆(s))|2


≤2|A|Es∼dπ⋆,a∼π⋄
b (s)[|ˆq(s, a′) −q⋆(s, a′)|2] + 2|A|Es∼dπ⋆,a∼π⋆(s)[|ˆq(s, a) −q⋆(s, a)|2].
Therefore,
(1 −γ)2R−1
max{J(π⋆) −J(ˆπ)}
≤c2{|A|(t/t0)β + t−2{2|A|Es∼dπ⋆,a∼π⋄
b (s)[|ˆq(s, a′) −q⋆(s, a′)|2]
+ 2|A|Es∼dπ⋆,a∼π⋆(s)[|ˆq(s, a) −q⋆(s, a)|2]}}
≤c3{|A|t−2β/(2+β)
0
{Es∼dπ⋆,a∼π⋄
b (s)[|ˆq(s, a′) −q⋆(s, a′)|2]β/(2+β)
+ Es∼dπ⋆,a∼π⋆(s)[|ˆq(s, a) −q⋆(s, a)|2]β/(2+β)}}.
Hence,
(1 −γ)2R−1
max{J(π⋆) −J(ˆπ)} ≤c|A|t−2β/(2+β)
0

CQ,dπ⋆
0,µ0C0
 B2
Q + γBLBQ

{ln(|Q||L/δ)/n}1/2β/(2+β)
.
This concludes the statement by some algebra.
F
Auxiliary Lemmas
We prove two auxiliary lemmas used in the proof.
Lemma 6 (Performance Difference Lemma ).
J(π) −J(π′) = (1 −γ)−1Es∼dπ[⟨π(· | s) −π′(· | s), Qπ′(s, ·)⟩]
≤(1 −γ)−2RmaxEs∼dπ[∥π(· | s) −π′(· | s)∥1].
Lemma 7 (LogSumExp Inequality).
max{x1, · · · , x|A|} ≤log(
|A|
X
i=1
exp(xi)) ≤max{x1, · · · , x|A|} + ln(|A|).
31

````

