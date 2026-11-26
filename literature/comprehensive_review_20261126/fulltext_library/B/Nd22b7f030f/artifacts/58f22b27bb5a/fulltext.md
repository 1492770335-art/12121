# Ambiguous Dynamic Treatment Regimes: A Reinforcement Learning Approach

Original PDF: [original.pdf](original.pdf). SHA256: `58f22b27bb5a98975531975bf48395e8c6e7f0f236edd2122aa3b3c784975c99`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1; PDF label 1

FORMULA CHECK REQUIRED: original PDF page 1.

````text
Submitted to
manuscript
Ambiguous Dynamic Treatment Regimes:
A Reinforcement Learning Approach
Soroush Saghafian
Harvard Kennedy School, Harvard University, Cambridge, MA
A main research goal in various studies is to use an observational data set and provide a new set of coun-
terfactual guidelines that can yield causal improvements. Dynamic Treatment Regimes (DTRs) are widely
studied to formalize this process and enable researchers to find guidelines that are both personalized and
dynamic. However, available methods in finding optimal DTRs often rely on assumptions that are violated
in real-world applications (e.g., medical decision-making or public policy), especially when (a) the existence
of unobserved confounders cannot be ignored, and (b) the unobserved confounders are time-varying (e.g.,
affected by previous actions). When such assumptions are violated, one often faces ambiguity regarding
the underlying causal model that is needed to be assumed to obtain an optimal DTR. This ambiguity is
inevitable, since the dynamics of unobserved confounders and their causal impact on the observed part
of the data cannot be understood from the observed data. Motivated by a case study of finding superior
treatment regimes for patients that underwent transplantation in our partner hospital (Mayo Clinic) and
faced a medical condition known as New Onset Diabetes After Transplantation (NODAT), we extend DTRs
to a new class termed Ambiguous Dynamic Treatment Regimes (ADTRs), in which the causal impact of
treatment regimes is evaluated based on a “cloud” of potential causal models. We then connect ADTRs
to Ambiguous Partially Observable Mark Decision Processes (APOMDPs) proposed by Saghafian (2018),
and consider unobserved confounders as latent variables but with ambiguous dynamics and causal effects on
observed variables. Using this connection, we develop two Reinforcement Learning methods termed Direct
Augmented V-Learning (DAV-Learning) and Safe Augmented V-Learning (SAV-Learning), which enable
using the observed data to effectively learn an optimal treatment regime. We establish theoretical results
for these learning methods, including (weak) consistency and asymptotic normality. We further evaluate
the performance of these learning methods both in our case study (using clinical data) and in simulation
experiments (using synthetic data). We find promising results for our proposed approaches, showing that
they perform well even compared to an imaginary oracle who knows both the true causal model (of the
data generating process) and the optimal regime under that model. Finally, we highlight that our approach
enables a two-way personalization: obtained treatment regimes can be personalized based on both patients’
characteristics and physicians’ preferences.*
Key words : Observational Data; Dynamic Treatment Regimes; Unobserved Confounders; APOMDPs,
Reinforcement Learning; Precision Medicine
History : Version: June 6, 2023, Forthcoming at Management Science.
1. Introduction
In a variety of applications in public policy, governance, medicine, economics, education, energy,
and e-commerce, a main goal is to make better decisions that are both personalized and dynamic.
This requires learning from a data set which actions to choose and when to apply them given the
dynamic conditions of each subject (e.g., an individual). One of the main factors that makes this
learning process challenging is that one needs to estimate the impact of an alternative sequence of
actions that could have been used in order to improve outcomes. This requires causal reasoning, as
the estimand—the effect of an alternative sequence of actions—is a counterfactual quantity (see,
e.g., Murphy et al. 2001, Murphy 2003, Namkoong et al. 2020).
* The author is grateful to Susan Murphy (Harvard), Richard Zeckhauser (Harvard), and Guido Imbens (Stanford)
for their valuable suggestions and comments.
1
arXiv:2112.04571v4  [cs.LG]  5 Jun 2023

````

## PDF page 2; PDF label 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
2
Article submitted to ; manuscript no.
Dynamic Treatment Regimes (DTRs) have been widely studied for this goal, enabling finding
effective alternative policies from observational data (Robins 1986, 1997, Murphy et al. 2001,
Murphy 2003, Robins 2004, Zhao et al. 2015, Zhang et al. 2018, Wang et al. 2018, Tsiatis et al.
2019, Kosorok and Laber 2019, Luckett et al. 2020, Nie et al. 2021, Leqi and Kennedy 2021). A
DTR is, in essence, a set of rules that prescribe individualized sequence of actions by mapping a
subject’s history to a series of recommended treatments (Murphy 2003, Chakraborty and Murphy
2014, Tsiatis et al. 2019, Luckett et al. 2020, Xu et al. 2020).
Using available results in finding effective DTRs, however, requires making strong assumptions
that might not hold in real-world applications, especially when the data in hand is observa-
tional. Notably, one needs to assume sequential ignorability1 (Robins 1986, 1997, Murphy et al.
2001, Murphy 2003, Robins 2004), meaning that the data is rich enough, and hence, unob-
served/latent/unmeasured confounding variables either do not exist or their effects can be ignored.
When using observational data sets, this assumption is often violated in many real-world appli-
cations. Even in some secondary analyses of experimental data sets (e.g., those obtained under
Micro-Randomized Trials (MRTs) in some mobile health studies where the goal is to study the
effect of users following a treatment regime and not just being assigned to it), various practical chal-
lenges (e.g., user habituation, user engagement, and/or user compliance) may lead to unobserved
confounding; see, e.g., Saghafian and Murphy (2021) for some discussions on scientific challenges in
mobile health applications. Furthermore, unobserved confounders are time-varying in most appli-
cations: they are themselves affected by the previous actions taken. Adjusting for them, thus, is a
perplexing task, making standard approaches for adjustment of confounding erroneous (see, e.g.,
Robins et al. 2000).
Correctly adjusting for unobserved time-varying confounding can be managed, if one assumes a
specific causal model for the data generating process.2 Assuming such a model can allow estimating
a distribution for potential trajectories under any alternative decision-making policy (i.e., treatment
regime), which is central to estimating its effect. However, since time-varying confounders are often
unobserved, estimating and assuming any such model is subject to significant misspecifications
(a.k.a., model ambiguity). We address this challenge by extending the analyses of DTRs to a
new class termed Ambiguous DTRs (ADTRs), in which the impact of any sequence of actions
is evaluated based on a “cloud” of potential data generating models as opposed to a single one.
Specifically, we allow for non-probabilistic ambiguity (a.k.a., Knightian uncertainty) about the
true data generating model, while (similar to the literature on DTRs) we assume that under any
1 This assumption has also appeared in the literature under other names such as “sequential randomization” (Tsiatis
et al. 2019) and “sequential backdoor criterion” (Pearl and Robins 1995).
2 For example, this can be done under an assumed model for the dynamics of unobserved confounders (e.g., how
they are affected by actions taken) and their relationship to observed values (e.g., how unobserved time-varying
confounders affect the actions under which data is generated).

````

## PDF page 3; PDF label 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
3
given potential model, there is a certain probabilistic understanding of how data is generated (see,
e.g., Saghafian (2018) and Chapter 11 of Manski (2007) for further discussions, Stoy (2011) for
an axiomatic treatment of statistical decision-making under these conditions, and Saghafian and
Tomlin (2016) for an information entropy view of data-driven decision-making under ambiguity).3
This allows for (a) directly taking into account potential model misspecifications when estimating
causal impacts, and (b) distinguishing between ambiguity (lack of knowledge about the true model)
and risk (probabilistic consequences of decisions under a known model).4
In extending DRTs to ADTRs, we are particularly motivated by our various collaborations with
our partner hospital, the Mayo Clinic. In various studies (see, e.g., Boloori et al. 2015, 2020, Munshi
et al. 2020a,b, 2021), we have collected data sets from our partner hospital and have examined
clinical decisions for patients who undergo a solid organ transplantation and develop what is
known as New Onset Diabetes After Transplantation (NODAT). In practice, physicians often use
an intensive amount of an immunosuppressive drug (e.g., tacrolimus) to reduce the risk of organ
rejection post-transplant (see, e.g., Boloori et al. 2015, 2020). Due to a well-established effect known
as the diabetogenic effect, this can increase the risk of NODAT, which prompts physicians to use a
glucose control drug (e.g., insulin). Learning better ways to prescribe these drugs (e.g., tacrolimus
and insulin) in both a personalized and dynamic way to jointly control risks of NODAT and organ
rejection is not an easy endeavor; the available data sets are only observational, the main health
states are hidden (see, e.g., Boloori et al. 2020), and the existence of unobserved confounders that
are time-varying disallow using existing methods.
Our approach in extending DTRs to ADTRs and analyzing them involves the following three
main steps. (1) We make use of a utility function that is appropriate under model ambiguity
(instead of the expected value of outcomes widely used in the literature). (2) We generalize tradi-
tional importance sampling methods to accommodate model ambiguity. (3) We connect ADTRs
to Ambiguous Partially Observable Mark Decision Processes (APOMDPs) proposed by Saghafian
(2018) by showing that ADTRs can be studied via APOMDPs, which in turn enables us to develop
Reinforcement Learning (RL) algorithms capable of learning optimal treatment regimes from the
observed data in effective ways.
The utility function we use is based on a generalization of the traditional maximin expected utility
(MEU) theory (a.k.a., Wald’s or robust optimization criterion). The MEU theory assumes that
outcomes should be obtained by maximizing utility with respect to the worst possible member of
3 This view of data-driven decision-making under ambiguity has also been shown useful in various applications,
including in designing and optimizing queueing systems under model ambiguity (Bren and Saghafian 2019) and
medical decision-making (Boloori et al. 2020).
4 This view is also aligned with that of Arrow (1951) who stated: “There are two types of uncertainty: one as to the
hypothesis, which is expressed by saying that the hypothesis is known to belong to a certain class or model, and one
as to the future events or observations given the hypothesis, which is expressed by a probability distribution.”.

````

## PDF page 4; PDF label 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
4
Article submitted to ; manuscript no.
the ambiguity set (cloud of potential causal models in our setting). In most applications, using the
MEU approach yields overly conservative decisions (for related discussions, see, e.g., Saghafian 2018,
and the references therein), and furthermore, does not allow for representing meaningful human
choices such as those of ambiguity seeking individuals established in some behavioral studies (see,
e.g., Bhid´e 2000, Heath and Tversky 1991, Ahn et al. 2014). This was also recognized in the seminal
work of Savage (1951) who wrote that this criterion is “ultrapessimisitic” and “can lead to absurd
conclusion[s]”. The generalization we use is known as α-maximin expected utility (α-MEU), which
allows for both optimistic and pessimistic views of the world (Arrow and Hurwicz 1977, Hurwicz
1951a,b, Ghiradato et al. 2004, Saghafian 2018). Unlike studies that use the MEU criterion, using
the α-MEU criterion avoids overly conservative decisions by allowing for a controllable pessimism
level (denoted by the parameter α) that can take values in [0, 1].
Within the utility theory literature, early studies (see, e.g., Arrow and Hurwicz 1977, Hurwicz
1951a,b) provided four axioms that a choice operator must satisfy. These axioms allowed such
studies to show that, under complete ignorance, one can focus merely on two extreme cases: the
best-case and the worst-case. Later studies (see, e.g., Ghiradato et al. 2004, Marinacci 2002) further
axiomatized preferences under the α-MEU criterion and also highlighted another importance of
using the α-MEU criterion in decision-making: it allows for differentiating between the inherent
ambiguity (a property related to the true causal model) and ambiguity attitude (a property related
to the decision-maker). In our study, using the α-MEU criterion not only allows us to provide
an alternative for the expectation operator—the conventional measure of performance used in the
literature surrounding DTRs5—but also allows finding treatment regimes that are tailored to the
preferences and attitudes of the decision-maker.
Importantly, this means that our work enables a two-way personalization: treatment regimes
can be personalized based on both the subject’s and the decision-maker’s characteristics. This
is important in various domains such as medicine, where not only the treatment plan needs to
be customized for each patient, but also the physician in charge should be given the ability to
include his/her preferences in providing the best course of treatment. Incorporating a physician’s
preferences is important for many reasons, including the fact that several behavioral challenges
often make it difficult for the physician to follow treatment decisions that are personalized to
the patient but not him/her (see, e.g., Frank and Zeckhauser 2007). When using our framework,
the physician’s preferences in dealing with ambiguous outcomes can be incorporated in various
5 For studies in this literature that consider other measure instead of the expected value of outcomes, we refer to Linn
et al. (2017) and Wang et al. (2018) (quantile performance) and Leqi and Kennedy (2021) (median performance).
These studies, however, do not consider model ambiguity, existence of unobserved confounders, or other challenges
we aim to address. While by using the α-MEU criterion we primarily generalize the expected value of outcomes, it
should be noted that our results can also be used to study generalizations of other measures such as the quantile or
median measures.

````

## PDF page 5; PDF label 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
5
ways. For example, questionnaires similar to those used in preference elicitation methods6 can be
designed to first understand the preferences and attitudes of the physician towards ambiguous
outcomes, thereby obtaining a small interval (if not a specific value) for α. Using these values of
α, a small set of corresponding optimal treatment regimes can be presented to the physician for
further consideration. Alternatively, when it is crucial for the physician to follow the treatment
regime that provides the maximum robustness and/or efficacy, one can use our framework to find
the best treatment regime across all values of α in [0,1]. Finally, when other factors beside efficacy
or robustness (e.g., cost, availability, or patient consent) need to be considered, one can simply
present the set of all treatment regimes that are optimal as α ranges in [0,1], allowing the provider
to inspect a broader set of treatment regimes.
We start our analyses by showing how a generalization of importance sampling methods (a.k.a.,
inverse-probability-weighting) widely used in the literature (see, e.g., Robins et al. 2000, Precup
et al. 2000, Murphy 2005, Tsiatis et al. 2019) can be utilized to find optimal regimes for ADTRs
without requiring the dynamics of observed or unobserved variables to be memoryless (i.e., sat-
isfy the Markov property).7 Specifically, we start by generalizing importance sampling methods
by allowing sampling across a cloud of potential data generating models (a.k.a., ambiguity set).
We show that under some conditions the resulted method, which we term Generalized Sequential
Importance Sampling (GSIS), provides a baseline for estimating the causal impact of any dynamic
treatment regime, and hence, finding the optimal one.
When the dynamics of variables satisfy the Markov property, we connect ADTRs to APOMDPs
recently introduced by Saghafian (2018). APOMDPs generalize traditional POMDPs by allowing
model ambiguity. APOMDPs, however, were proposed without any causal inference application
in mind. In this paper, for the first time, we make use of them through a causal inference lens.
Notably, by connecting ADTRs to APOMDPs, we consider time-varying unobserved confounders
as dynamic latent states and form dynamic belief distributions over them while allowing ambiguity
regarding the true (data generating) causal model.8 We then make use of known structural results
for APODMPs (e.g., piecewise linearity and continuity of the value function) established in the
literature (Saghafian 2018), and develop two RL approaches that can provide effective treatment
regimes. In developing these RL approaches, as is common, we view the problem of finding an effec-
6 Several studies consider finding treatment regimes that allow shared decision-making between physicians and
patients when there are multiple risky (probabilistic)—as opposed to ambiguous (non-probabilistic)—outcomes. Some
available methods include set-valued treatment regimes (Laber et al. 2014, Lizotte and Laber 2016), inverse-preference
elicitation (Lizotte et al. 2012), constrained estimation (Linn et al. 2015), and use of item response theory (Butler
et al. 2018).
7 See also Zhang and Bareinboim (2019) for more discussions related to fining the optimal treatment regime under
model ambiguity without a Markovian structure.
8 Since APOMDPs generalize POMPDs, our results can also be viewed as generalizations of those in the literature
that use a POMDP setting to perform off-policy evaluation (see, e.g., Tennenholtz et al. 2020, Xu et al. 2020, Bennett
and Kallus 2021, Hu and Wager 2021, Thomas and Brunskill 2016, and the references therein).

````

## PDF page 6; PDF label 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
6
Article submitted to ; manuscript no.
tive treatment regime as an off-policy RL problem. However, in contrast to main RL methods such
as Q-Learning (an approximate dynamic programming approach that uses regression to learn the
“quality” function) and A-Learning (which tries to learn the “advantage” function) our approaches
try to learn the value function directly. Thus, roughly speaking they are within the V-Learning
methods (see, e.g., Luckett et al. 2020, Xu et al. 2020). We term our proposed learning algorithms
Direct Augmented V-Learning (DAV-Learning) and Safe Augmented V-Learning (SAV-Learning)
as they augment the V-Learning methods by (a) making use of the structural properties of the
value function, and (b) incorporating model ambiguity (in a direct and safe way, respectively).9
For our proposed learning approaches, we establish important theoretical results, including weak
consistency and asymptotic normality of both the estimated optimal treatment regime and the
associate overall gain. To establish these results, we require specific but relatively common “regular-
ity” conditions, including conditions on (a) basic “complexity” properties of the class of allowable
policies (measured by entropy-based versions of the Donsker theorems with bracketing integrals),
and (b) absolute regularity of the underlying empirical processes.
We also examine the performance of our proposed approaches by applying them to a clinical data
set of over 63,000 observations made of patients who underwent kidney transplantation in our part-
ner hospital and faced NODAT. We find promising results, indicating that using DAV-Learning and
SAV-Learning yields notable improvements over the treatment regime used in practice; depending
on the decision-maker’s pessimism level, these improvements are in the ranges (10%, 42%) and
(10%, 32%) for DAV-Learning and SAV-Learning, respectively. Furthermore, we observe that the
performance of the SAV-Learning regime is much more robust to the value of the pessimism level
(parameter α) than that of DAV-Learning, and hence, a decisions-maker who uses SAV-Learning
does not need to be worried about the value of α s/he uses in obtaining an optimal treatment
regime. We further investigate the performance of our proposed approaches using simulations
experiments (synthetic data). Our results show that DAV-Learning and SAV-Learning can improve
the observed regime by an amount that ranges in (1%, 37%) and (1%, 8%), respectively. Further-
more, we make use of our simulation experiments to quantify the robustness of our approaches to
model ambiguity, and find that DAV-Learning and the SAV-Learning are able to strongly shield
against model ambiguity: the gain loss under these approaches compared to an imaginary oracle
who knows both the true data generating model and the optimal treatment regime under that
model is very low (below 0.6%), regardless of the value of α. Thus, a decision-maker who is facing
model ambiguity can make use of our proposed approaches and obtain a treatment policy that
has a similar performance to that of an imaginary decision-maker who knows both the true data
9 The fact that the structural properties of the value function in APOMDPs is known (see Saghafian 2018) is a main
reason we make use of V-Learning as opposed to other RL methods (e.g., Q-Learning or A-Learning). Furthermore,
as we will see, a data transformation approach allows using a weight-adjusted version of the Bellman equation, and
thereby directly estimating the value function from observed data.

````

## PDF page 7; PDF label 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
7
generating model and the optimal policy under that model. Finally, our results show that the gain
loss compared to such an imaginary decision-maker has a U-shape curve in the pessimism level:
the minimum loss for both DAV-Learning and SAV-Learning are obtained at a mid-value of α.
This implies that (a) using extreme cases of α = 0 (a maximax view) or α = 1 (a maximin view) is
almost never robustness-maximizing, and (b) by viewing α as a tuning parameter (when needed) in
our proposed approaches, one can obtain a treatment regime that performs best across all possible
pessimism levels.
In closing this section, we note that our work in incorporating model ambiguity a priori in the
analyses not only provides robustness to potential misspecifications, but more broadly, can bridge
the gap between two philosophical views of decision-making using causal inference: model-based and
model-free. The former postulates that any sensible causal reasoning for decision-making needs to
be based on a specific model and set of assumptions in addition to data, while the latter advocates
that it needs to rely only on data. We hope that our work in taking a middle ground and considering
a cloud of models can serve as a step for future research in trying to further bridge the gap between
the two. The importance of doing so has its roots in seminal work in Statistical Decision Theory
(see, e.g., Wald 1939, 1945, 1950), but has also been highlighted in various more recent studies.
For example, Manski (2021) emphasizes that “models can at most approximate actualities” and
highlights that statistical inference for decision-making needs to be performed across all feasible
models. Similarly, referring to the famous quote from Box (1979), Watson and Holmes (2016) state
that “statisticians are taught from an early stage that essentially all models are wrong, but some
are useful,” and stress that decision-making needs to rely on a set of models that are misspecified
(hence “wrong”) but useful in that they can be “helpful for aiding actions (taking decisions).”
2. The Framework
Throughout the paper, the notation “ ≜” is used to differentiate between definitions and equations.
For a set T ≜{1,2,3,··· ,T}, the notations (Xt)t∈T and T≤t are used to represent the vector
(X1,X2,··· ,XT) and the set T \ {t + 1,t + 2,··· ,T}, respectively. All vectors are consider to be
in the column format (e.g., (Xt)t∈T is |T | × 1). For any finite set Ξ ⊂R, we let ∆Ξ denote the
probability simplex induced by Ξ. The notations
p→and
d→denote convergence in probability and
distribution, respectively. The set I represents the interval [0,1].
We let the observed data be a collection of n ∈N i.i.d. realizations (called trajectories) of the
vector of variables (Ot,At)t∈T . For a realized trajectory, (ot,at)t∈T , ot ∈O is the observation made
about a subject (e.g., a patient’s observed covariates or an observed health state serving as a
summary of them) at time t ∈T , and At ∈A denotes the action/treatment assigned at time

````

## PDF page 8; PDF label 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
8
Article submitted to ; manuscript no.
t ∈T , where T is the set of time periods (e.g., patients’ visits/follow-ups).10 For example, in our
study of NODAT patients, observations made about each patient (Ot) include various test results,
demographic information, and other observed risk factors such as diabetes history, body mass
index, blood pressure, triglyceride, uric acid, and lipoprotein information (see Table 1). Actions
taken (At) include low dose (non-aggressive) or high-dose (aggressive) tacrolimus prescriptions as
well as information on whether insulin has been used (see Table 3), Finally, T ≜{1,2,3,··· ,12},
since patient follow-ups are monthly for a year after transplantation.
Besides the observed data, there are often unobserved variables that might have affected what
is observed in the data. Let St denote a summary of them at time t, and let S be the support of
St. For example, in mHealth applications, St might include information relating to the patient’s
habituation level (see, e.g., Saghafian and Murphy 2021) and/or patient true health state, both
of which are often unobserved. In our case study of NODAT patients, St is a nine-level variable
that summarizes the unobserved health state of the patient in terms of both transplantation and
diabetes conditions (see Table 2). We denote the observable history up to each time t ∈T by
Ho
t ≜(O1,A1,O2,A2,··· ,Ot) and let H o
t be the support of Ho
t. Similarly, we denote the (partially)
unobservable history up to each time t ∈T by Hu
t ≜(S1,O1,A1,S2,O2,A2,··· ,St,Ot) and let H u
t
be the support of Hu
t . It is important to note that in general both variables St and Ot depend on
the previous treatments. However, for notational simplicity, we suppress the dependency of St and
Ot on the vector (at)t∈T≤t−1 ≜(a1,a2,··· ,at−1).
We assume the latent state summaries (St)t∈T are such that the immediate gain in each decision
epoch depends on the history only through them. This can always be achieved with appropriate
definition of variables (St)t∈T (see, e.g., Xu et al. 2020). For example, in our case study, the
immediate gains are based on predefined Quality of Life (QoL) scores that depend only on patient
summaries defined by St (see Table 4). Thus, we denote the immediate gain at time t through
Gt ≜g(St,At) ∈R, where g is a known function.11 The set of all possible immediate gains can be
denoted by G ≜{ga ∈R|S | : a ∈A }, where ga ≜(g(s,a))s∈S .
A treatment regime (hereafter also “policy” for simplicity) λ ≜(λt)t∈T in this setting is a vector
of time-dependent mappings from the available history at each time t to the probability simplex
induced by actions, ∆A . It defines the probability of assigning each action/treatment at each
decision epoch given the available history up to that point. Policies are compared using the overall
gain they generate. The overall gain of a policy λ is defined by the discounted sum of immediate
10 We do not assume that time points are evenly distributed or homogenous across patient trajectories. Importantly,
in some applications, the treatment times are random. For simplicity, we assume treatment times are fixed. However,
extending our results to scenarios with random treatment times is relatively straightforward.
11 It should be noted that St, in general, depends on the history up to time t. Thus, Gt ≜g(St,At) also depends on
the history. But this dependence is only through St, which as noted earlier, can always be achieved with appropriate
definition of summary variables (St)t∈T (see, e.g., Xu et al. 2020).

````

## PDF page 9; PDF label 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
9
gains it generates, which we denote by
ΓT(λ) ≜
X
t∈T
βt−1Gλ
t ,
(1)
where β ∈I \ {1} is a discount factor. Similarly, the long-run impact of λ can be analyzed using
Γ∞(λ) ≜limT →∞ΓT(λ).12 Here, we shall note that Gλ
t , and hence ΓT(λ), should be viewed with
a potential outcomes lens (for more discussions, see, e.g., Robins 1986, Rubin 1986, Angrist et al.
1996, Robins 1997, Murphy et al. 2001); equivalently, in the language of do calculus, Gλ
t and ΓT(λ)
should be viewed as Gt|do(λ) and ΓT|do(λ), respectively (see, e.g., Pearl 2009). In addition to
this, which is implicit in our notation, our notation also implicitly implies consistency13, which is a
standard assumption in the causal inference literature with time-varying variables (see, e.g., Robins
1997, Murphy et al. 2001) and holds in our motivating study of NODAT patients. In settings we
consider, however, the distribution of ΓT(λ) cannot be solely identified from the observed data
alone. In fact, there are often a variety of plausible data generating models all agreeing with the
observed part of the data, but with different implications about the distribution of ΓT(λ). We let
M denote the set of all such models (a.k.a., an ambiguity set).14 In this view, each given model
m ∈M can be viewed as a rule that, given λ, imposes a specific probability distribution over the
full history Hu
T. Thus, each given model m ∈M implies a distribution for ΓT(λ), which we denote
by fm ∈F, where F ≜{fm : m ∈M }.
Finally, since the distribution of ΓT(λ) varies across the models in M , we define a utility function
that allows us to compare the performance of different policies. To this end, we make use of α-MEU,
which is suitable for decision-making under ambiguity (see, e.g., Ghiradato et al. 2004, Marinacci
2002, Saghafian 2018). Specifically, by considering Y (λ) ≜ΓT(λ) or Y (λ) ≜Γ∞(λ) as our main
outcome variable of interest, we make use of
MEUα[Y (λ)] ≜α
inf
fm∈F Efm[Y (λ)] + (1 −α) sup
fm∈F
Efm[Y (λ)]
α ∈I ,
(2)
as the utility of Y (λ), where α represents the pessimism level and Efm denotes the expectation
operator with respect to the distribution f m. For example, at α = 1, (100% pessimism level),
policies are compared with respect to their worst-case performance. At α = 0 (0% pessimism level),
on the other hand, policies are compared with respect to their best case performance. Of note,
12 While we focus on discounted sum of immediate gains, we note that many of our results readily extend to the
average overall gains ¯Γ(λ) ≜1
T
P
t∈T Gλ
t , and in particular, to its long-run counterpart liminfT →∞¯Γ(λ). This is
because under some mild conditions limT →∞¯Γ(λ) = limT →∞limβ→1
ΓT (λ)
1−β .
13 This assumption links the counterfactual data with the factual one (Robins 1997), and can be violated if treatment
of a subject impacts another subject’s variables (e.g., vaccinating a group of individuals may decrease exposure of
others to a disease).
14 We defer discussions on how the space of models can be constructed to the numerical experiments section (see, e.g.,
the discussion under “Other Details” in the case study). As described there, there are various ways of constructing
the set M , and our analysis does not rely on any specific method or assumption in this regard.

````

## PDF page 10; PDF label 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
10
Article submitted to ; manuscript no.
when |M | = 1, MEUα[Y (λ)] returns the expected value of Y (λ), and hence, the utility function
in (2) provides a generalization for the traditional expectation operator that is widely used in the
causal inference literature.
We say that the effect of treatment policy λ is “α-MEU identifiable,” if
MEUα[Y (λ)]
 < ∞and
MEUα[Y (λ)] can be identified given M . Since a main goal is to learn the optimal policy, we next
define the following notion of optimality in ADTRs, which is a generalization of the traditional
notion of optimality used in analyzing DTRs.
Definition 1 (Optimality). Let Λ be the set of all α-MEU identifiable policies. We say that a
policy λ∗∈Λ is optimal, if with Y (λ) ≜ΓT(λ), we have
MEUα[Y (λ∗)] ≥MEUα[Y (λ)]
∀λ ∈Λ.
(3)
Remark 1 (Fairness). When performance is evaluated under the traditional expectation opera-
tor, it is known that (under some assumptions) the optimal policy assigns treatment (when |A |=2)
only to those subjects who benefit from it: optimizing mean treatment and conditional mean treat-
ment are equivalent. However, when using some other measures such as median, this no longer holds:
the treatment decision for a given group might depend on outcomes from a different group, creating
a “across-group fairness” concern (see, e.g., Leqi and Kennedy 2021). This concern is relatively
mitigated when using the notion of optimality defined above. This is clear when |M | = 1, since
MEUα[Y (λ)] returns the expected value of Y (λ). More broadly, it can be seen that, under some
conditions, the optimal policy λ∗∈Λ defined in Definition 1 also optimizes MEUα[Y (λ)] after con-
ditioning on subject specific observed variables. For example, if we let m(λ∗) ≜inffm∈F Efm[Y (λ∗)]
and m(λ∗) ≜supfm∈F Efm[Y (λ∗)], assume that both of these models are in M , impose similar
conditions to those needed when evaluating the mean treatment effect, and evaluate the condi-
tional MEUα value after fixing these models (as the worse-case and best-case model, respectively),
we can see that λ∗satisfies a version of “across-group fairness.” Specifically, λ∗treats only those
subjects who benefit from it in terms of the conditional MEUα value, regardless of the outcomes of
the other subjects. In addition, when needed, one can further restrict the set of allowable policies
Λ to those that satisfy some desirable fairness attributes. However, studying fairness and what
should be considered as “fair” is outside the scope of this work, especially since measuring fairness
under ambiguity is more complex than that under risk; see the discussion in the Introduction that
highlights the difference between the two as well as more in-depth discussions in prior work (see,
e.g., Saghafian and Tomlin 2016, Saghafian 2018). In what follows, we simply focus on data-driven
ways of findings a policy λ∗∈Λ that is optimal based on Definition 1.
To perform our analyses, it is useful to differentiate between the policy under which the data have
been generated (hereafter, the “behavior policy”) and the policy that we would like to evaluate and
recommend (hereafter, the “evaluation policy”). The behavior policy denoted by λb ≜(λb
t)t∈T is a

````

## PDF page 11; PDF label 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
11
vector of time-dependent mappings λb
t : H u
t →∆A whereas the evaluation policy denoted by λe ≜
(λe
t)t∈T is a vector of time-dependent mappings λe
t : H o
t →∆A . An important difference between
the evaluation and the behavior policies relates to a condition known as sequential ignitability15
(see, e.g., Robins 1986, 1997, Murphy et al. 2001, Murphy 2003, Robins 2004), which we define
next.
Definition 2 (Sequential Ignorability). For
any
policy
λ ≜(λt)t∈T ,
let
Ho,m
t
(λ) ≜
(Om,λ
1
,Am,λ
1
,Om,λ
2
,Am,λ
2
,··· ,Om,λ
t
) denote the observable history up to time t ∈T , generated under
λ and model m ∈M . We say that λ satisfies sequential ignorability under model m ∈M , if
for all t ∈T , the action generated by λt is independent of the collection of potential outcomes
(Gm,λ′
t
,Om,λ′
t+1 ,Gm,λ′
t+1 ,Om,λ′
t+2 ,··· ,Gm,λ′
T
)λ′∈Λ conditional on Ho,m
t
(λ).
In essence, this definition requires, for each time t ∈T and given Ho,m
t
(λ), the action generated by
λt to be independent of (Gm
t ,Om
t+1,Gm
t+1,Om
t+2,··· ,Gm
T ) values that can be obtained when following
any feasible sequence of actions (at)t∈T . Both by this definition and naturally, any evaluation policy
λe ≜(λe
t)t∈T (where λe
t : H o
t →∆A ) satisfies sequential ignorability under any model m ∈M ,
because it is only a function of the observed history and possible exogenous randomness (it maps
H o
t to ∆A by definition). In contrast, a behavior policy λb ≜(λb
t)t∈T (where λb
t : H u →∆A ) may
or may not satisfy this condition, since it might depend on unobservable confounders (variables in
(St)t∈T that affect both the gain and the actions selected by λb). In fully randomized experiments
(e.g., Micro Randomized Trials), the behavior policy may satisfy sequential ignorability. However,
when the data are observational, it is often impossible to test whether the behavior policy satisfies
this assumption, and in addition, it is highly likely that this assumption does not hold. Finally, we
note that while the behavior policy is often known in randomized experiments, it might need to be
estimated when using observational data (unless specific known treatment protocols or standard
are fully followed).
2.1. Analyzing ADTRs via Generalized Sequential Importance Sampling (GSIS)
We now show that, under some conditions, an optimal policy for an ADRT can be found using
a generalized version of sequential importance sampling, which we term Generalized Sequential
Importance Sampling (GSIS). While allowing for ambiguity (not risk, which is the focus of the
existing literature), GSIS assigns weights under each model and sequentially adjusts the trajectory
probabilities that occur under a given evaluation policy compared to those observed in the data set.
Of note, we use GSIS in this section to study ADTRs that do not satisfy any Markovian (a.k.a.,
memoryless) property regarding the dynamics of the underlying variables. In the next section,
we show how the analyses of ADTRs can be simplified when such dynamics satisfy a Markovian
15 See also the sequential backdoor criterion (Pearl and Robins 1995).

````

## PDF page 12; PDF label 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
12
Article submitted to ; manuscript no.
structure. Notably, the results presented in this section provide a building block for the algorithms
and the theoretical findings established in the next sections.
To present GSIS, we first suppress the dependencies to the underlying model by assuming the
model is fixed. Consider an evaluation policy λe, and let Ho
t(λe) be the history that will be observed
under λe up to time t. Also, denote by λe
t(At|Ho
t(λe)) the probability that actions At is chosen
under λe when the observed history is Ho
t(λe). Furthermore, while the behavior policy is not known
(e.g., due to its potential dependency on unobserved variables), we can observe the marginalized
probabilities of action selection under the behavior policy, which we denote by λb
t(At|Ho
t(λb)).
These allow us to define importance sampling weights
wt(λe) ≜λe
t(At|Ho
t(λe))
λb
t(At|Ho
t(λb))
∀t ∈T .
(4)
Proposition 1 establishes that, under some conditions, the optimal policy for an ADTR governed
by a set of models M can be found via GSIS. Specifically, an MEUα–unbiased estimator of ΓT(λe)
is obtained in Proposition 1, where the notion of MEUα–unbiased estimation is defined below.
Definition 3 (MEUα–Unbiasedness). An estimator ˆY of an outcome variable of interest Y is
said to be MEUα–unbiased if, and only if, MEUα[ ˆY ] = MEUα[Y ] for any α ∈I .
To establish an MEUα–unbiased estimator of ΓT(λe), we also need to make sure that the evalua-
tion and the behavior policies sufficiently overlap. Specifically, we need to ensure that these policies
overlap almost surely (defined below).
Definition 4 (Almost Sure Overlap). We say that the evaluation and the behavior policy
almost surely overlap, if λb
t(at|Ho
t(λb)) > 0 whenever λe
t(at|Ho
t(λe)) > 0 a.s. over Ho
t(λb) and Ho
t(λe)
for all t ∈T and at ∈A .
Intuitively, the evaluation and the behavior policy need to overlap to ensure that trajectories
obtained under the behavior policy are to some extent informative about the trajectories under
the evaluation policy. When the evaluation and the behavior policy almost surely overlap, the
importance sampling weights defined in (4) are well-defined for all t ∈T (except perhaps on
histories that might happen with probability zero).
Proposition 1 (Generalized Sequential Importance Sampling (GSIS)). Suppose that the
evaluation and behavior policies (a) satisfy sequential ignorability under all models m ∈M , and
(b) almost surely overlap. Then, for any α ∈I , we have
MEUα

ΓT(λe)

= MEUα

ΓT(λb)
Y
t∈T
wt(λe)

,
(5)
and hence, ˆΓT(λe) ≜ΓT(λb)Q
t∈T wt(λe) is an MEUα–unbiased estimator of ΓT(λe).

````

## PDF page 13; PDF label 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
13
The proof of Proposition 1 is developed by understanding how the impact of an evaluation policy
can be first analyzed for any given (a) sequence of actions, and (b) model m ∈M under which the
data might be generated (see Lemma ?? in Appendix A).
Of note, Proposition 1 also provides a partial way of characterizing the optimal evaluation policy,
since it provides a way of estimating MEUα

ΓT(λe)

under any given evaluation policy. That is,
using this proposition and optimizing MEUα

ΓT(λe)

over a given set of policies (which for use
in practice might be restricted to those satisfying desirable attributes such as fairness or inter-
pretability) can shed light on the optimal evaluation policy. However, Proposition 1 provides only
a partial way of characterizing the optimal evaluation policy, because analyzing ADTRs often
requires considering a behavior policy that might not satisfy sequential ignorability (at least under
some models in M ). Therefore, we next study scenarios in which the behavioral policy does not
fully satisfy sequential ignorability, but satisfies it to some extent. This entails limiting the impact
of unobserved confounders (which make the probability of observing certain trajectories in the
observed data biased compared to what would have happen if we could observe unobservables) on
the behavior policy under each model. In limiting the impact of unobserved confounders on the
behavior policy, we are mainly motivated by extending the analyses of confounding in causal infer-
ence (see, e.g., Rosenbaum 2002) from a traditional setting in which |T | = 1, the treatment variable
is binary |A | = 2, and there is no model ambiguity |M | = 1, to ADTRs in which these restrictions
are all relaxed. Two notable challenges in doing so are: (1) since future actions depend on the
history, a confounding decision/treatment in any period can make future decisions confounding as
well; (2) since the trajectory probabilities depend on the underlying model, the impact of unob-
served confounding depends on the underlying model. We next introduce the notion of bounded
unobservable confoundedness, which we define using the likelihood ratios of treatment propensities
(functions ℓ(·) in the following definition). This, in turn, allows us to provide a version of GSIS
under bounded unobservable confoundedness (Proposition 2).
Definition 5 (Bounded Unobservable Confounding (BUC)). We say that the behavioral
policy satisfies Bounded Unobserved Confounding (BUC) under a model m ∈M , if there exist
constants ηm
t ∈[1,∞) such that
(ηm
t )−1 ≤ℓ(at,a′
t,Ho,m
t
,Sm
t = s)
ℓ(at,a′
t,Ho,m
t
,Sm
t = s′) ≤ηm
t
(6)
a.s. over observable history Ho,m
t
, for all t ∈T , at,a′
t ∈A , s,s′ ∈S (T ), where Sm
t ≜(Sm
t )t∈T≤t and
ℓ(at,a′
t,Ho,m
t
,Sm
t = s) ≜λb
t(at|Ho,m
t
,Sm
t = s)
λb
t(a′
t|Ho,m
t
,Sm
t = s).

````

## PDF page 14; PDF label 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
14
Article submitted to ; manuscript no.
The above definition bounds the impact of the vector of the unobservable confounder variables,
Sm
t , in each period. In Lemma ?? (Appendix B) we show that this definition results in
(ηm
t )−1 ≤λb
t(at|Hu,m
t
)
λb
t(at|Ho,m
t
) ≤ηm
t
a.s.
(7)
over Ho,m
t
and Hu,m
t
= (Ho,m
t
,Sm
t ) for all t ∈T and a ∈A . Thus, benefiting from the observed
history (as opposed to the unobserved one) and making use of marginalized propensities λb
t(at|Ho,m
t
)
as an estimate of the true treatment propensities λb
t(at|Hu,m
t
) will not be unboundedly misleading.
The results provided in the following proposition are analogous to design sensitivity analyses (see,
e.g., Rosenbaum 2010) in static (i.e., T = 1) settings, where the idea is to examine how much
propensity odds need to vary so that the gained causal understanding becomes invalid (see, also,
Kallus and Zhou 2020, 2021). This proposition can also be viewed as a generalization of some of
the available bounds in the literature of DRTs (see, e.g., Lemma 2 of Namkoong et al. 2020), since
such bounds can be obtained from our results under the special case of |M | = 1. Furthermore, we
note that while these bounds can be conservative (hence, not useful) for the purpose of estimating
the mean performance, they are relatively suitable for estimating the MEUα value of it (see part
(ii) of Proposition 2 as well as the learning approaches discussed in Section 6).
Proposition 2 (GSIS under Bounded Unobservable Confounding). Suppose the behavior
policy satisfies BUC under all models m ∈M . If the evaluation policy satisfies sequential ignora-
bility under all models m ∈M , and it overlaps with the behavior policy almost surely, then:
(i)
Under each model m ∈M we have:
Em
ΓT(λb)
Y
t∈T
wm
t (λe)

≤Em
ΓT(λe)

≤Em
ΓT(λb)
Y
t∈T
wm
t (λe)

,
where
wm
t (λe) ≜wt(λe)

(ηm
t )−1 11{ΓT (λb)>0} + ηm
t 11{ΓT (λb)<0}

,
and
wm
t (λe) ≜wt(λe)

(ηm
t )−1 11{ΓT (λb)<0} + ηm
t 11{ΓT (λb)>0}

.
(ii) For any α ∈I , there exists ˜α ∈I such that MEUα

ΓT(λe)

= f(˜α), where f(˜α) ≜
˜αMEUα

ΓT(λb)Q
t∈T wm
t (λe)

+ (1 −˜α)MEUα

ΓT(λb)Q
t∈T wm
t (λe)

.
Similar to Proposition 1, part (ii) of Proposition 2 provides a way of finding the optimal eval-
uation policy, since it characterizes the causal impact of any such policy. Whereas Proposition 1
requires the behavior policy to satisfy sequential ignorability—an unrealistic assumption in most
applications—Proposition 2 only requires the unobserved variables to have a bounded impact.
Importantly, however, Proposition 1 directly provides an α-MEU unbiased estimator, but Propo-
sition 2 does so subject to a tuning parameter ˜α. Specifically, in part (ii) of Proposition 2, the

````

## PDF page 15; PDF label 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
15
function f can be computed using only observed data. This, in turn, resolves the issue that the
outcome of interest under the evaluation policy as well as the time-varying confounders needed to
estimate it are unobservable. However, to use Proposition 2 part (ii), one needs to tune the param-
eter ˜α. Since f is a decreasing function and ˜α ∈I , tuning ˜α can be done in an structured way. For
example, in practice, one is often interested in evaluating policies that are known to be better than
the behavior policy. Thus, we have f(˜α) ≥MEUα

ΓT(λb)

, implying that one can start tuning ˜α
using the threshold value ˜α∗≜min

f (−1)
MEUα

ΓT(λb)

,1

and only consider values of ˜α that
are in [0, ˜α∗]. More importantly, it should be noted that the parameters (ηm
t )t∈T ,m∈M are design
sensitivity parameters. Specifically, for any ϵ > 0, they can be chosen so that f(0) −f(˜α∗) < ϵ.
Since f(0) −f(˜α∗) ≥0, this allows one to use any ˜α in [0, ˜α∗] and obtain an approximate unbiased
MEUα estimator for ΓT(λe) with a guaranteed approximation error of ϵ. While this provides an
approximation method, two limitations are noteworthy: (1) obtaining an exact value for ˜α (and
hence, an exact unbiased MEUα estimator for ΓT(λe)) can be challenging, and (2) the bounds in
part (i) of Proposition 2 can be conservative, since in general they may diverge exponentially in
T. Nonetheless, as described above, one can obtain an ϵ-approximate unbiased MEUα estimator
for ΓT(λe).
Finally, we note that one can extend Propositions 1 and 2 to provide doubly robust estimators16
to account for the fact that, under each given model m ∈M , the variance of an importance
sampling based estimator can be high. Such an extension is, however, not that useful in our work,
because we are (a) directly allowing for a cloud of models, and (b) using MEUα of the outcome
variable as opposed to its expected value (the criterion used in the studies related to doubly robust
estimation). Instead, we next develop two RL methods based on our results, and establish that
they have suitable asymptotic behavior, including consistency and asymptotic normality. We also
test their performance directly using both a clinical data set and simulation experiments, and
find that our proposed learning methods provide strong robustness to model ambiguity (see, e.g.,
Section 7.3).
3. Analyzing ADTRs via APOMDPs
In this section, we show that a tractable way of analyzing ADTRs is via APOMDPs. Specifically,
analyzing ADTRs via APOMDPs enables (a) considering unobserved variables as latent time-
varying states while allowing for model ambiguity, and (b) developing effective RL methods.17
An APOMDP (Saghafian 2018) can be represented via the Directed Acyclic Graph (DAG)
depicted in Figure 1. The ambiguous mechanisms in this figure represent causal relationships that
16 For related studies on doubly robust estimators, we refer to Bang and Robins (2021), Jiang and Li (2016), Thomas
and Brunskill (2016), Kallus and Uehara (2020), Athey and Wager (2021), and the references therein.
17 For other approaches in modeling confounders as hidden states see, e.g., Bennett et al. (2021), Xu et al. (2020),
and the references therein.

````

## PDF page 16; PDF label 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
16
Article submitted to ; manuscript no.
 
 
 
 
 
 
 
 St 
Gt 
t+2 
 
St+1 
Gt+1 
Ot 
At 
Ot+1 
At+1 
t-1 
𝜆𝜆𝑡𝑡
𝑒𝑒, 𝜆𝜆𝑡𝑡
𝑏𝑏 
𝜆𝜆𝑡𝑡
𝑏𝑏 
𝜆𝜆𝑡𝑡+1
𝑒𝑒
, 𝜆𝜆𝑡𝑡+1
𝑏𝑏
𝜆𝜆𝑡𝑡+1
𝑏𝑏
 
t 
t+1 
Figure 1
DAG representation of APOMDPs. Circles: observable variables; Rectangles: unobservable variables; Solid
arrows: unambiguous causal mechanisms; Dashed arrows: ambiguous causal mechanisms. [Note: using πt ≜
νt(ho
t)—a belief distribution over the latent states—allows working with an equivalent DAG representation where
πt becomes the observed state at time t.]
cannot be quantified from the data alone. The main assumption needed to represent an ADTR via
an APOMDP is that the dynamics of the variables is Markovian. In various applications, it is often
possible to transform data so that this assumption holds (see, e.g., Xu et al. 2020). Specifically,
while the observed history Ho
t grows over time, we can assume that there are summary functions
νt : H o
t →∆S such that πt ≜νt(ho
t) (a belief distribution over the latent states) is a sufficient
statistics.18
Using the belief distribution πt, we can work with transformed policies: we can consider µe ≜
 µe
t(πt)

t∈T and µb ≜
 µb
t(πt)

t∈T as the evaluation and behavior policies, respectively, where
µe
t,µb
t : ∆S →∆A . We denote the probability that an action at is applied at time t (when the
belief distribution is πt) under these transformed evaluation and behavior policies by µe
t(at|πt) and
µb
t(at|πt), respectively. In what follows, we first define the class of APOMDPs and then develop
two RL algorithms that enable finding the optimal policy by effectively learning the causal impact
of any given evaluation policy.
As defined in Saghafian (2018), a time-homogenous APOMDP is an extension of the classical
POMDPs, and can be defined by the tuple (α, β, S , O, A , G , P, Q). The notation used in
the first part of this tuple is as introduced earlier. P and Q are the sets of possible transition
probability matrices with respect to (latent) states and observations, respectively (Saghafian 2018).
These sets define the ambiguous causal mechanisms depicted in Figure 1.
To simplify the analyses, we can index members of the set P ×Q using M so that each m ∈M
represents a specific (unambiguous) POMDP model. In particular, associated with each m ∈M is
a set of the form Pm × Qm with Pm ∈P and Qm ∈Q denoting the set of state and observation
18 For typical POMDPs and APOMDPs, it is known that the belief distribution over latent states can serve as a
sufficient statistics (see, e.g., Saghafian 2018, Boloori et al. 2020, Saghafian and Rasouli 2019, and the references
therein). In Remark 2 and Section 6, we further discuss handling cases where this might not hold. We also refer
interested readers to Assumption 1 in Tennenholtz et al. (2020), which establishes the existence of a sufficient statistics
as one sufficient condition for unbiasedness of importance sampling in POMDPs, but highlight that our focus is on
APOMDPs as opposed to POMDPs.

````

## PDF page 17; PDF label 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
17
transition probabilities under model m, respectively (Saghafian 2018). In this setting, (a) Pm ≜
{P a
m : a ∈A }, where for each a ∈A , P a
m ≜[pa
ij(m)]i,j∈S is an |S | × |S | matrix with pa
ij(m) ≜
Pr{j|i,a,m} denoting the probability that the (latent) state moves to j from i under action a and
model m, and (b) Qm ≜{Qa
m : a ∈A }, where for each a ∈A , Qa
m ≜[qa
jo(m)]j∈S ,o∈O is an |S |×|O|
matrix with qa
jo(m) ≜Pr{o|j,a,m} denoting the probability of observing o under action a and
model m when the (latent) state is j (Saghafian 2018).
If M was a singleton with its only member being m, the optimal gain and policy for any t ∈T
and π ∈∆S could be obtained by a traditional POMDP Bellman equation (along with the terminal
condition V m
0 (π) ≜0):
V m
t (π) = max
a∈A
n
π′ga + β
X
o∈O
Pr{o|π,a,m}V m
t−1(T(π,a,o,m))
o
,
(8)
where V m
t (π) denotes the value function under model m when the belief distribution is π and there
are t periods to go, “ ′ ” represents the transpose operator, Pr{o|π,a,m} = P
i
P
j πipa
ij(m)qa
jo(m),
and the belief updating operator T : ∆S ×A ×O ×M →∆S is defined by the Bayes’ rule (in the
matrix form):
T(π,a,o,m) =
 π′P a
mQa
m(o)
′
Pr{o|π,a,m} ,
(9)
with Qa
m(o) ≜diag(qa
1o(m),qa
2o(m),...,qa
no(m)) denoting the diagonal matrix made of the oth col-
umn of Qa
m (Saghafian 2018).
Unlike POMDPs, in AMPOMDs M is not a singleton. However, it is shown in Saghafian (2018)
that the APOMDP value function, a model independent function which we denote by Vt(π), can
still be obtained using dynamic programming. Furthermore, the underlying Bellman operator in
the APOMDP is a contraction mapping with modulus β on a complete metric space (under some
mild conditions), which in turn allows analyzing the APOMDP value function in infinite-horizon
settings as the limit of its finite-horizon version. More importantly, Saghafian (2018) establishes
some structural properties for the value function of the APOMDP (e.g, piecewise linearity and
continuity in π). In the next section, we make use of these structural properties to develop effective
RL approaches (termed Augmented V-Learning). We start our analyses by first developing suitable
algorithms for learning the value function in POMDPs (i.e., when |M | = 1), and then show how
they can be extended to learn the APOMDP value function.
4. Augmented V-Learning for POMDPs and APOMDPs
4.1. Augmented V-Learning for POMDPs
To develop our results, we require that the behavior policy, µb, satisfies positivity defined below.
Definition 6 (Positivity). We say that a policy µ ≜(µt)t∈T satisfies positivity, if there exists a
constant c0 > 0 such that µt(at|πt) ≥co for all t ∈T , πt ∈∆S , and at ∈A .

````

## PDF page 18; PDF label 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
18
Article submitted to ; manuscript no.
Positivity implies that all actions have a positive chance of being selected (appear in the observed
data) regardless of the belief. The behavior policy, µb, automatically satisfies positivity when the
data are collected based on a randomized trial. When using observational data this assumption is
sensible, because inference involving treatment patterns (using action at when the belief is πt) that
cannot occur in the observational study requires further knowledge and assumptions (Murphy et al.
2001). If the behavior satisfies positivity, we can establish the following result (see also Lemma 4.1
of Murphy et al. (2001) and Lemma 2.1 of Luckett et al. (2020) for related results in settings with
fully observable states).
Proposition 3 (Weight-Adjusted Bellman Equation). Suppose |M | = 1 and denote the
only member of M by m. If µb satisfies positivity and sequential ignorability, then for any policy
µe, the finite-horizon value function satisfies the weight-adjusted Bellman equation
V m,µe
T −t+1(πt) = Em
µe
t(At|Πm
t )
µb
t(At|Πm
t )
h
Gt + β V m,µe
T −t (T(Πm
t ,At,Ot,m))
iΠm
t = πt

,
(10)
for all t ∈T and πt ∈∆S , where πt is considered as a realization (of a model dependent random
variable denoted by Πm
t ) and V m,µe
0
(π) ≜0. Therefore, for any function ϕ defined on ∆S , and for
all t ∈T , we have:
Em
µe
t(At|Πm
t )
µb
t(At|Πm
t )
h
Gt + β V m,µe
T −t (T(Πm
t ,At,Ot,m)) −V m,µe
T −t+1(Πm
t )
i
ϕ(Πm
t )

= 0.
(11)
The importance of Proposition 3 (which is built on the importance sampling results of the
previous section) is that it allows us to empirically estimate the value function under any evaluation
policy, and hence, learn the optimal policy. Specifically, using the data, we can make use of the
sample-average version of (11):
EP
" X
t∈T
µe
t(At|Πm
t )
µb
t(At|Πm
t )
h
Gt + β V m,µe
T −t (T(Πm
t ,At,Ot,m)) −V m,µe
T −t+1(Πm
t )
i
ϕ(Πm
t )
#
= 0,
(12)
where EP denotes average with respect to the empirical probability measure.19 It is important to
note that while we are using sample-average in (12), the result still depends on the assumed m,
because while the sequence {(At,Ot)}t∈T is observable to us, to form the sequence {Πm
t }t∈T , we
need to have an assumed model. That is, due to the existence of unobserved variables, the empirical
measure alone is insufficient for our goal.
Remark 2 (Weight Adjustment under BUC). The
weight-adjusted
results
(10)-(12)
is
obtained assuming that µb satisfies sequential ignorability. It should be noted that this assumption
is milder than assuming that the original behavior policy satisfies sequential ignorability. This is
19 For a random variable X with n observed values denoted by x1,x2,··· ,xn, EP[X] ≜n−1 Pn
i=1 xi. Similarly, for a
function f, EP[f(X)] ≜n−1 Pn
i=1 f(xi).

````

## PDF page 19; PDF label 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
19
especially the case, because µb ≜
 µb
t(πt)

t∈T is a transformed policy that takes advantage of the
availability of information about the unobserved variables summarized in (πt)t∈T . In particular,
since in APOMDPs (Saghafian 2018) we have access to (πm
t )t∈T under each model m ∈M , we
might be able to make use of it to ensure that µb satisfies sequential ignorability. For example,
in many medical decision-making applications, including the case study with our partner hospital
discussed in Section 7.1, the immediate gain depends on hidden states (confounders) only through
(πm
t )t∈T . This occurs, for example, when the gain in each period t is simply (πm
t )′ ga
t , where
ga
t ≜(g(st,at))st∈S ; that is, when the gain in each period t is considered to be the average value of
ga
t considering the belief distribution πm
t .20 (See Boloori et al. (2020) for more discussions about
the immediate gain values in our medical decision-making application, and Xu et al. (2020) for a
similar assumption made in analyzing latent-state models.) However, µb might not satisfy sequen-
tial ignorability in some other applications; see, e.g., Saghafian and Murphy (2021) for related
challenges in mHealth applications. Thus, in Section 6, we provide an extension of Proposition 3 by
making use of the BUC results presented in Proposition 2. However, in what follows, we first focus
on understanding and analyzing the cases where µb satisfies sequential ignorability, as it provides
a foundation for the extensions discussed in Section 6.
Remark 3 (Effective Approximation). In using the results of Proposition 3, we only require
an approximate solution to (12). Thus, how the solution to (12) is obtained is not that restrictive.
Indeed, there are many ways to obtain an approximate solution to (12). In what follows, however,
we provide an effective way of estimating the optimal policy and optimal value function using (12).
We do so by taking advantage of important structural properties of the optimal value function
of POMDPs and APOMDPs. Specifically, the optimal value function of POMDPs is known to
be piecewise linear and convex in π under some mild conditions (Smallwood and Sondik 1973).
Saghafian (2018) shows that in general the convexity does not hold in APOMDPs, and some
additional conditions are needed (see Proposition 2 of Saghafian (2018)). To be consistent, for both
POMDP and APOMDP settings, we only assume piecewise linearity and continuity, but do not
impose any assumption on convexity. This, in turn, helps us in another way: while piecewise linear
and continuous functions can be effectively learned from data, learning a function that is both
piecewise linear and convex (i.e., is point-wise maximum of a set of linear functions) is much harder
(see, e.g., Magnani and Boyd 2009, and the references therein).
Let V denote the set of real-valued piecewise linear and continuous bounded functions defined
on ∆S , and assume V m,µe
t
∈V . To learn V m,µe
t
∈V using (12), we consider the parametric version
of the value function: V m,µe
t
(π;ψt) ≜
 b(π))′ ψt, where b(π) ≜
 b1(π),b2(π),··· ,bdt(π)
′ is a
predefined basis function that allows us to ensure that the learned function is in V , and ψt ∈Ψt ⊆
20 This is the case in how the value function in traditional POMDPs is often constructed; see, e.g., Eq. (8).

````

## PDF page 20; PDF label 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
20
Article submitted to ; manuscript no.
Rdt is the parameter.21 This also enables us to set ϕ(π) ≜b(π) in (12), since b(π) can be thought
of as the gradient of V m,µe
t
(π;ψt) with respect to its parameter, which only depends on π (and
not the parameter) and is almost everywhere defined.
Furthermore, since ψt can be high-dimensional in some applications (especially when t is large),
we estimate it using a regularized approach as follows (to avoid overfitting). Starting with V m
0 (π) =
0 and moving backwards iteratively, having an estimation of T −t periods to go value function in
hand ( ˆV m,µe
T −t ), we define
φm,µe(ψt) ≜EP
µe
t(At|Πm
t )
µb
t(At|Πm
t )
h
Gt + β ˆV m,µe
T −t (T(Πm
t ,At,Ot,m)) −V m,µe
T −t+1(Πm
t ;ψt)
i
b(Πm
t )

.
(13)
We then obtain the estimate
ˆψ
µe
t
= arg min
ψt∈Ψt
 φm,µe(ψt)
′ Ωφm,µe(ψt) + θtP(ψt)

,
(14)
where Ωis an arbitrary positive definite matrix, P(·) is a penalty function, and θt is a tuning
parameter.22 Consequently, we plug in ˆψ
µe
t
in V m,µe
T −t+1(πt;ψt) and thereby obtain an estimate for the
value function V m,µe
T −t+1(πt), and move to the next period (backward). This procedure, under a given
model m ∈M , yields an estimator for the gain under µe. That is, ˆΓm
T (µe) ≜
R ˆV m,µe
T
(π)dF(π) can
be used as an estimator for Γm
T (µe) =
R
V m,µe
T
(π)dF(π), where dF(π) is a given distribution on
(starting) belief values. Since we have an estimator for the gain under any policy µe, we can obtain
ˆµe∗≜argmaxµe∈Υ ˆΓm
T (µe) as an estimate for the optimal policy under model m, where Υ is a given
set of policies.23 Finally, an estimate of the gain under the optimal policy is ˆΓm
T (ˆµe∗).
In an infinite-horizon setting, the procedure above simplifies. This is because in homogenous
POMDPs (and APOMDPs) the value function with t periods to go converges to a stationary value
function as t →∞(see, e.g., Proposition 1 of Saghafian 2018). Therefore, in (12) we can replace both
V m,µe
T −t (·) and V m,µe
T −t+1(·) with the same function. This removes the need for recursive calculations
and allows us to follow a “one-shot” method. We discuss this further in the next sections, and also
study the asymptotic behavior of our proposed approach.
4.2. Augmented V-Learning for APOMDPs
Motivated by the results in the previous section, we now extend our approach to APOMDPs,
where the condition |M | = 1 does not hold. We propose two approaches termed Direct Augmented
21 Allowing the dimensionality of the parameter space, dt, to depend on t can enable us increase flexibility as t grows
(e.g., by introducing more knots). The special case where dt does not depend on t is still useful in some settings,
including those where the goal is to learn the long-run impact of a policy (see, e.g., Algorithms 1 and 2 in the next
sections).
22 In our case study, simulations experiments, and theoretical results, we make use of the squared Euclidean norm as
the penalty function, and hence, assume P(ψt) = ψ′
tψt.
23 We use the “max” operator instead of “sup,” because in most real-world applications, Υ is first identified by a set
of domain experts and is such that maximum is obtained. We later make this assumption more implicit (see, e.g.,
Condition (C4) in Section 5. Furthermore, in various practical applications, Υ is often restricted to the set of policies
that satisfy specific attributes such as fairness or interpretability.

````

## PDF page 21; PDF label 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
21
V-Learning (DAV-Learning) and Safe Augmented V-Learning (SAV-Learning). As we will see, in
DAV-Learning, we directly extend the approach presented in the previous section for POMDPs by
first obtaining a value function separately for each POMDP model in M . These values are then
combined at the end of the horizon to provide an estimate of the value function for the APOMDP.
In SAV-Learning, however, we make use of a safe estimation approach upfront that takes into
account ambiguity and removes the need to obtain a value function separately for each POMDP
model in M .
4.2.1. Direct Augmented V-Learning (DAV-Learning).
Recall that for each evaluation
policy µe and each given m ∈M , we can use the approach proposed for POMDPs in Section 4.1
to obtain an estimate for the value function V m,µe
T
(·), which we denote by ˆV m,µe
T
(·). Thus, we can
first obtain an estimate for the APOMDP value function:
ˆV µe
T (π) = MEUα
 ˆV m,µe
T
(π)

≜α inf
m∈M
ˆV m,µe
T
(π) + (1 −α) sup
m∈M
ˆV m,µe
T
(π).
(15)
Next, to estimate the optimal policy, we note that for any policy µe, the estimator of the gain
is ˆΓT(µe) =
R ˆV µe
T (π)dF(π), where dF(π) is a given distribution on (starting) belief values. This
means that we can obtain an estimate of the optimal policy as ˆµe∗≜argmaxµe∈Υ ˆΓT(µe). Finally,
the estimated optimal gain is ˆΓT(ˆµe∗).
This DAV-Learning approach for APOMDPs in the infinite-horizon case is presented in Algo-
rithm 1. In presenting this algorithm, as is often the case, we assume that the data only includes
a finite number of periods for each subject, but the goal is to estimate the long-run performance
of policies (see, e.g., Luckett et al. 2020, Xu et al. 2020). We also use subscript n to highlight the
dependency of our estimators to the number of trajectories in the data set, which in turn allows
us to investigate the behavior of our proposed learning algorithm as n →∞(see Section 5). Our
estimation equations for the infinite-horizon gain are
φm,µe
n
(ψ) ≜EP
" X
t∈T
µe(At|Πm
t )
µb(At|Πm
t )
h
Gt + β V m,µe
∞
(T(Πm
t ,At,Ot,m)) −V m,µe
∞
(Πm
t )
i
b(Πm
t )
#
(16)
and
ˆψ
m,µe
n
= argmin
ψ∈Ψ
 φm,µe
n
(ψ)
′ Ωφm,µe
n
(ψ) + θnP(ψ)

,
(17)
where Ψ ⊆Rd. Similar to before, we make use of the piecewise linearity and continuity of the
value function (i.e., the fact that V m,µe
∞
∈V ) for all m ∈M . This allows us to use predefined
basis function to ensure that the learned function remains in V when we use the parametric form
V m,µe
∞
(π,ψ) ≜
 b(π))′ ψ.
Using (17), we then set ˆV m,µe
∞
(π) ≜V m,µe
∞
(π; ˆψ
m,µe
n
). In addition, denoting the infinite-horizon
gain under any policy µe and m ∈M by Γm
∞(µe) ≜
R
V m,µe
∞
(π)dF(π), we consider ˆΓm
∞(µe) ≜
R ˆV m,µe
∞
(π)dF(π) as an estimator for Γm
∞(µe). With estimated values under each model m in

````

## PDF page 22; PDF label 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
22
Article submitted to ; manuscript no.
Algorithm 1: DAV-Learning
1 for each observed trajectory and model m ∈M do
2
Initialize πm
0 using a random draw from F(π);
3
set t=1;
4
while t + 1 ∈T do
5
πm
t+1 ←T(πm
t ,at,ot,m);
6 for any given µe ∈Υ and m ∈M do
7
φm,µe
n
(ψ) ←EP
"
P
t∈T

µe(At|Πm
t )
µb(At|Πm
t )
h
Gt + β V m,µe
∞
(T(Πm
t ,At,Ot,m)) −V m,µe
∞
(Πm
t )
i
b(Πm
t )
#
;
8
ˆψ
m,µe
n
←argminψ∈Ψ
 φm,µe
n
(ψ)
′ Ωφm,µe
n
(ψ) + θnP(ψ)

;
9
ˆV m,µe
∞
(π) ←
 b(π))′ ˆψ
m,µe
n
;
10
ˆΓm
∞(µe) ←
R ˆV m,µe
∞
(π)dF(π);
11 for any given µe ∈Υ do
12
ˆΓ∞(µe) ←αinfm∈M ˆΓm
∞(µe) + (1 −α)supm∈M ˆΓm
∞(µe);
13 ˆµe∗←argmaxµe∈Υ ˆΓ∞(µe);
14 ˆΓ∞(ˆµe∗) ←maxµe∈Υ ˆΓ∞(µe);
hand, we next define the estimated overall gain (a model independent value) as ˆΓ∞(µe) ≜
αinfm∈M ˆΓm
∞(µe) + (1 −α)supm∈M ˆΓm
∞(µe), which provides an estimation for the overall gain
Γ∞(µe) ≜αinfm∈M Γm
∞(µe) + (1 −α)supm∈M Γm
∞(µe).
Finally, the estimated optimal policy and its infinite-horizon value for the APOMDP are obtained
as ˆµe∗≜argmaxµe∈Υ ˆΓ∞(µe) and ˆΓ∞(ˆµe∗) = maxµe∈Υ ˆΓ∞(µe), respectively, where the latter pro-
vides an estimate for Γ∞(µe∗) ≜maxµe∈Υ Γ∞(µe∗). Similarly, under each model m, we denote
the estimated optimal policy and its infinite-horizon value as ˆµe∗,m ≜argmaxµe∈Υ ˆΓm
∞(µe), and
ˆΓm
∞(ˆµe∗,m) = maxµe∈Υ ˆΓm
∞(µe), respectively, where the latter provides an estimate for Γm
∞(µe∗,m) ≜
maxµe∈Υ Γm
∞(µe∗,m).
4.2.2. Safe Augmented V-Learning (SAV-Learning).
The DAV-Learning algorithm pre-
sented in the previous section is a direct extension of the approach proposed for POMDPs (Section
4.1) in which “the curse of ambiguity” (Saghafian 2018) is overcome at the end. In contrast, in
SAV-Learning, this curse is overcome upfront via a “safe method” for estimating the underlying
parameter ψt, and hence, the value function. To develop the SAV-Learning algorithm, similar
to before, we first denote the APOMDP value function with t periods to go under policy µe (a
model independent function) with V µe
t
, assume that V µe
t
∈V , and parameterize it via V µe
t
(π;ψt) ≜
 b(π)
′ ψt. We then estimate its parameter as
ˆψ
µe
t
≜MEUα
ˆψ
m,µe
t

≜α ˆψ
m,µe
t
+ (1 −α) ˆψ
m,µe
t
,
(18)

````

## PDF page 23; PDF label 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
23
Algorithm 2: SAV-Learning
1 for each observed trajectory and model m ∈M do
2
Initialize πm
0 using a random draw from F(π);
3
set t=1;
4
while t + 1 ∈T do
5
πm
t+1 ←T(πm
t ,at,ot,m);
6 for any given µe ∈Υ and m ∈M do
7
φm,µe
n
(ψ) ←EP
"
P
t∈T

µe(At|Πm
t )
µb(At|Πm
t )
h
Gt + β V m,µe
∞
(T(Πm
t ,At,Ot,m)) −V m,µe
∞
(Πm
t )
i
b(Πm
t )
#
;
8
ˆψ
m,µe
n
←argminψ∈Ψ
 φm,µe
n
(ψ)
′ Ωφm,µe
n
(ψ) + θnP(ψ)

;
9 for any given µe ∈Υ do
10
m ←arginfm∈M || ˆψ
m,µe
n
||;
11
m ←argsupm∈M || ˆψ
m,µe
n
||;
12
ˆψ
µe
n ←α ˆψ
m,µe
n
+ (1 −α) ˆψ
m,µe
n
;
13
ˆV µe
∞(π) ←
 b(π))′ ˆψ
µe
n ;
14
ˆΓ∞(µe) ←
R ˆV µe
∞(π)dF(π);
15 ˆµe∗←argmaxµe∈Υ ˆΓ∞(µe);
16 ˆΓ∞(ˆµe∗) ←maxµe∈Υ ˆΓ∞(µe);
where
α ∈I
can
be
viewed
as
a
tuning
parameter,
m ≜arginfm∈M ||ˆψ
m,µe
t
||,
m ≜
argsupm∈M ||ˆψ
m,µe
t
||,24 and
ˆψ
m,µe
t
= arg min
ψt∈Ψt
 φm,µe(ψt)
′ Ωφm,µe(ψt) + θtP(ψt)

,
(19)
where φm,µe(ψt) is defined in (13). Consequently, we plug ˆψ
µe
t
obtained in (18) in V µe
T −t+1(πt;ψt),
which yields an estimate for the APOMDP value function V µe
T −t+1(πt), and move to the next period
(backwards) as before. This yields an estimated value function ˆV µe
T (π). Denoting the gain under
any policy µe by ΓT(µe) ≜
R
V µe
T (π)dF(π), we use ˆΓT(µe) ≜
R ˆV µe
T (π)dF(π) as an estimator for
ΓT(µe).
Finally, optimization over µe ∈Υ will provide the estimated optimal policy of the APOMDP
under the SAV-Learning approach: ˆµe∗≜argmaxµe∈Υ ˆΓT(µe) = argmaxµe∈Υ
R ˆV µe
T (π)dF(π). The
estimated optimal gain under this approach is ˆΓT(ˆµe∗) = maxµe∈Υ
R ˆV µe
T (π)dF(π), which provides
an estimate for ΓT(µe∗) ≜maxµe∈Υ
R
V µe
T (π)dF(π). Similar to before, this procedure can also be
used for the infinite-horizon case by noting that since both VT −t(·) and VT −t+1(·) become V∞(·)
the calculations simplifies. The SAV-Learning approach for infinite-horizon case is presented in
Algorithm 2. Besides their benefit in analyzing the long-run impact of different treatment regimes,
both Algorithms 1 and 2 can also be used as approximations for learning policies that work well
over a finite but long horizon.
24 We assume M is such that infm∈M ||ψm,µe
t
|| and supm∈M ||ψm,µe
t
|| are both finite, and m and m are both in M .

````

## PDF page 24; PDF label 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
24
Article submitted to ; manuscript no.
5. Performance Analyses: Theoretical Results
We now establish some theoretical results for the performance of our proposed approaches. Specif-
ically, we demonstrate the asymptotic properties of the estimators under our main proposed algo-
rithm, DAV-Learning (Algorithm 1). With some minor modifications, one can then also estab-
lish similar results for the estimators under the second proposed approach, SAV-Learning (Algo-
rithm 2).25
The main results of this section are as follows. Under some conditions discussed below, we first
establish weak consistency and asymptotic normality of the estimators under any policy µe ∈Υ
(Theorem 1). We then move to the estimators related to the optimal policy, and establish weak
consistency and asymptotic normality of both the estimated optimal policy and its estimated value
(Theorem 2). To establish our results, we make use of arguments in empirical processes (specifically
for stationary process as opposed to i.i.d. ones; see, e.g., Dedecker and Louhichi (2002), Kosorok
(2008)), and think of each realization of the underlying stochastic process as a function in ℓ∞(Υ)
(i.e., the set of real-valued bounded functions indexed by µe ∈Υ).
We assume Ωin (17) is an arbitrary positive-definite matrix, P(·) is the squared norm penalty
function, and θn is a tuning parameter satisfying θn = op(n−1/2). We also assume that Em
||b(Πt)||2
and Em
G2
t

are both finite for all m ∈M and t ∈T . Some other technical conditions are needed,
mainly because of two broad set of challenges in our setting which make establishing asymptotic
results more involved: (1) the underlying process is not i.i.d over time, and (2) there is model
ambiguity (|M |̸ = 1). Specifically, we need the following “regularity” conditions on the parameter
space, trajectories space, policy space, and model space:
(C1) For every µe ∈Υ and m ∈M there exists a unique solution to φm,µe(ψ) = 0 denoted by
ψm,µe
⋄
∈Ψ ⊆Rd, where supµe∈Υ ||ψm,µe
⋄
|| < ∞, ψm,µe
⋄
is an interior point of Ψ, and Ψ is
compact subset of Rd.
(C2) There exists a 2 < ρ < ∞such that for all m ∈M :
(C2a) The class of policies (Υ) is either finite, or its bracketing integral satisfies
J[](∞,Υ,Lρ(P m)) < ∞, where P m is the marginal stationary distribution of the
sequence {(Πm
t ,At)}t≥1.26
(C2b) The sequence {(Πm
t ,At)}t≥1 is an absolutely regular stationary process with its
β-mixing coefficients ζm(t) satisfying P∞
t=1 k2/(ρ−2)ζm(t) < ∞.27
25 For general results related to the asymptotic properties of V-Learning algorithms when all variables are observable
and there is no model ambiguity, we refer interested readers to Luckett et al. (2020).
26 For the definition of the bracketing integral, J[](∞,Υ,Lρ(P m)), see, e.g., Kosorok (2008).
27 For the definition of an absolutely regular stationary process and its β-mixing coefficients, see, e.g., Dedecker and
Louhichi (2002), Kosorok (2008), and the references therein.

````

## PDF page 25; PDF label 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
25
(C3) There exists a constant c1 > 0 such that for all m ∈M , t ∈T , µe ∈Υ, and c ∈Rd:
c′ Em
"
µe(At|Πm
t )
µb(At|Πm
t ) b(Πm
t )

b(Πm
t ) −β b(T(Πm
t ,At,Ot,m))
′#
c ≥c1||c||2.
(20)
(C4) µe∗is a unique and well septated maximizer of Γ∞(µe) and µe∗is in the interior Υ.
(C5) For every µe ∈Υ: |infm∈M Γm
∞(µe)| < ∞, |supm∈M Γm
∞(µe)| < ∞, and M contains both
arginfm∈M Γm
∞(µe) and argsupm∈M Γm
∞(µe).
Assumptions related to these conditions are relatively common in the Z-estimation and M-
estimation theories (see, e.g., Kosorok 2008). Some of these conditions are also assumed to hold in
the Generalized Method of Moments (GMM) (for asymptotic properties of GMM, see, e.g., Hansen
1982). These conditions hold both in our case study of NODAT patients (Section 7.1) and in
our simulation experiments (Section 7.2). (C1) is a regularity condition on the parameter space,
and ensures that the solutions obtained by solving φm,µe(ψ) = 0 are “well-behaved.” (C2a) is a
regularity condition on the policy space, and requires that the set of policies under consideration
satisfy a minimum level of “complexity” (measured by an appropriate entropy-based metric). This
condition clearly allows working with any finite set of policies, but also holds for many infinite sets
of policies (see, e.g., the parametric class of policies in Luckett et al. 2020). (C2b) is a regulatory
condition on the space of trajectories and allows viewing their formation as a suitable stationary
process. The β-mixing coefficients ζm(t) quantify dependency of the observed values in the process t
steps removed, and are zero when there is no such dependency. (C3) ensures that the matrix Cm(µe)
defined in Theorem 1 below is positive-definite, and hence, invertible. One can empirically check
whether (C3) holds by creating certain matrixes using data and testing whether they are positive-
definite. (C4) is needed to establish that the sequence of estimated optimal policies converges to
the true optimal policy, which is a stronger result than just the gain of these policies converging
to each other. (C5) is a regularity condition on the space of models, M , which holds in most
real-wrold applications, because any set of models can be represented/approximated with a finite
set (with any required level of accuracy).
We first establish the asymptotic behavior of our estimators under any given policy µe ∈Υ by
only requiring (C1)-(C3). The proof is based on some additional results provided in Appendix B
(see Lemmas ?? and ??), which establish Donsker properties and asymptotic normality in ℓ∞(Υ)
for the underlying absolutely regular stationary process in our setting .
Theorem 1 (Asymptotic Behavior: Fixed Policy and its Value). Suppose (C1)-(C3) hold
and the behavior policy satisfies positivity. Then under DAV-Learning (Algorithm 1), for any µe ∈Υ
and m ∈M , we have:
(i)
ˆψ
m,µe
n
p→ψm,µe
⋄
.

````

## PDF page 26; PDF label 26

FORMULA CHECK REQUIRED: original PDF page 26.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
26
Article submitted to ; manuscript no.
(ii) √n
ˆψ
m,µe
n
−ψm,µe
⋄
 d→G(µ) in ℓ∞(Υ), where G(µ) is a zero-mean and tight Gaussian process
indexed by µ ∈Υ with the covariance function given by
E
h
G(µ)G(˜µ)
i
=

Cm(µe)
−1 ˜Cm(µe, ˜µe)
 Cm(µe)
−1′
∀µ, ˜µ ∈Υ,
(21)
where
Cm(µe) ≜Em
"
µe(At|Πm
t )
µb(At|Πm
t ) b(Πm
t )

b(Πm
t ) −β b(T(Πm
t ,At,Ot,m))
′#
,
(22)
˜Cm(µe, ˜µe) ≜Em
"
µe(At|Πm
t )˜µe(At|Πm
t )
µb(At|Πm
t )µb(At|Πm
t ) ϑ(Πm
t ,ψµe
⋄)ϑ(Πm
t ,ψ ˜µe
⋄)b(Πm
t )

b(Πm
t )
′#
, (23)
and
ϑ(Πm
t ,ψµe
⋄) ≜Gt +
h
β b(T(Πm
t ,At,Ot,m)) −b(Πm
t )
i
ψµe
⋄.
(24)
(iii) ˆΓm
∞(µe)
p→Γm
∞(µe).
(iv) ˆΓ∞(µe)
p→Γ∞(µe) assuming (C5) holds.
We next establish the asymptotic properties of the optimal policy and the gain under it. The
proof of the following theorem is based on an additional result provided in Appendix B (see Lemma
??), which in turn relies on results from the M-estimation theory.
Theorem 2 (Asymptotic Behavior: Optimal Policy and its Value). Suppose
(C1)-(C5)
hold and the behavior policy satisfies positivity. Then, considering a metric space (Υ,dΥ), under
DAV-Learning (Algorithm 1) we have:
(i)
dΥ(ˆµe∗,m,µe∗,m)
p→0 for all m ∈M .
(ii) dΥ(ˆµe∗,µe∗)
p→0.
(ii) ˆΓm
∞(ˆµe∗,m)
p→Γm
∞(µe∗,m).
(iv) ˆΓ∞(ˆµe∗)
p→Γ∞(µe∗).
6. Extension: Learning Under Bounded Unobservable Confounding (BUC)
As discussed in Remark 2, in various applications, one might be able to ensure that µb satisfies
sequential ignorability, because it takes advantage of the availability of information about the
unobserved variables (confounders) summarized in (πt)t∈T . The DAV-Learning and SAV-Learning
approaches introduced earlier are based on the results of Proposition 3, which assumes µb satisfies
sequential ignorability. In this section, we show how such results can be extended to cases where µb
does not satisfy sequential ignorability, but satisfies BUC conditions introduced earlier (see, e.g.,
Definition 5). This, in turn, allows us to extend DAV-Learning and SAV-Learning, and introduce
their BUC counterparts, which we term DAV-Learning-BUC and SAV-Learning-BUC, respectively.
Similar to (7), which is based on Lemma ?? (Appendix B), assume for each model m ∈M there
exist constants ηm
t ∈[1, ∞) such that:
(ηm
t )−1 ≤µb
t(at|Πm
t ,Sm
t )
µb
t(at|Πm
t )
≤ηm
t
a.s.
(25)

````

## PDF page 27; PDF label 27

FORMULA CHECK REQUIRED: original PDF page 27.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
27
over Πm
t and Sm
t for all t ∈T and a ∈A . If ηm
t = 1, µb
t satisfies sequential ignorability. Further-
more, with ηm
t = 1, (25) implies that benefiting from Πm
t
under each model m and making use
of marginalized treatment propensities µb
t(at|Πm
t ) is enough for the goal of estimating the true
treatment propensities µb
t(at|Πm
t ,Sm
t ). More broadly, however, (25) ensures that this estimation
exercise is not unboundedly misleading. Of note, since µb
t(at|Πm
t ) = Em
Sm
t

µb
t(at|Πm
t ,Sm
t )

, one can
also view (25) as bounded variations compared to the average (under each model).
Assuming that (25) holds, we next extend Proposition 3 by relaxin the assumption that µb
satisfies sequential ignorability. To this end, we introduce the following weight modifiers:
κm
t ≜

(ηm
t )−1 11
{V µb
T
(π)≥0} + ηm
t 11
{V µb
T
(π)<0}

(26)
and
κm
t ≜

(ηm
t )−1 11
{V µb
T
(π)<0} + ηm
t 11
{V µb
T
(π)≥0}

,
(27)
and make use of the BUC results presented in Proposition 2.28
Proposition 4 (Weight-Adjusted Bellman Equation Under BUC). Suppose µb satisfies
both the BUC condition (25) and positivity. For any policy µe, define the upper and lower bound
value functions via the modified weight-adjusted Bellman equations:
V
m,µe
T −t+1(πt) ≜Em

κm
t
µe
t(At|Πm
t )
µb
t(At|Πm
t )
h
Gt + β V
m,µe
T −t (T(Πm
t ,At,Ot,m))
iΠm
t = πt

,
(28)
and
V m,µe
T −t+1(πt) ≜Em

κm
t
µe
t(At|Πm
t )
µb
t(At|Πm
t )
h
Gt + β V m,µe
T −t (T(Πm
t ,At,Ot,m))
iΠm
t = πt

,
(29)
along with V
m,µe
0
(π) ≜0 and V m,µe
0
(π) ≜0. Then:
(i)
For any function ϕ defined on ∆S , and for all t ∈T and m ∈M , we have:
Em

κm
t
µe
t(At|Πm
t )
µb
t(At|Πm
t )
h
Gt + β V
m,µe
T −t (T(Πm
t ,At,Ot,m)) −V
m,µe
T −t+1(Πm
t )
i
ϕ(Πm
t )

= 0,
(30)
and
Em

κm
t
µe
t(At|Πm
t )
µb
t(At|Πm
t )
h
Gt + β V m,µe
T −t (T(Πm
t ,At,Ot,m)) −V m,µe
T −t+1(Πm
t )
i
ϕ(Πm
t )

= 0.
(31)
(ii) For all m ∈M and π ∈∆S we have: V m,µe
T
(π) ≤V m,µe
T
(π) ≤V
m,µe
T
(π).
(iii) For any α ∈I , there exists ˜α ∈I such that V µe
T (π) ≜MEUα

V m,µe
T
(π)

= f(˜α,π), where
f(˜α,π) ≜˜αMEUα

V m,µe
T
(π)

+(1−˜α)MEUα

V
m,µe
T
(π)

. Hence, ΓT(µe) =
R
f(˜α,π)dF(π),
where ΓT(µe) ≜
R
V µe
T (π)dF(π).
28 These weight modifiers may depend on π in general (based on (26)-(27)). Such dependency is suppressed here for
the ease of notation.

````

## PDF page 28; PDF label 28

FORMULA CHECK REQUIRED: original PDF page 28.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
28
Article submitted to ; manuscript no.
When the behavior policy µb satisfies sequential ignorability, we have κm
t = κm
t = 1, and hence,
the above results boil down to those in Proposition 3. Proposition 4, however, generalizes Propo-
sition 3 by highlighting the role of weight modifiers κm
t and κm
t in analyzing scenarios in which µb
violates sequential ignorability, but satisfies it to some extent. In particular, after incorporating
these modifiers, one can make use of the same procedures as in the previous section using Propo-
sition 4. That is, the sample-average version of (30) and (31) together with regularized learning
can be used to learn the upper and lower bound value functions in a parametric way, respectively.
Once these functions are learned, part (ii) of Proposition 4 guarantees that they can be used to
bound the actual value function under each model. More specifically, part (iii) of Proposition 4
states that f(˜α,π) and
R
f(˜α,π)dF(π) can be used to estimate the APOMDP value function and
the overall performance, respectively. It should be noted that (1) the function f(·,·) is calculable
using only observed part of the data. This resolves the issue that the outcome of interest under the
evaluation policy as well as the time-varying confounders needed to estimate it are unobservable.
(2) A similar procedure to that discussed after Proposition 2 can be used to tune parameter ˜α.
Specifically, as discussed there, noting that the parameters (ηm
t )t∈T ,m∈M can be viewed as design
sensitivity parameters, one can choose them and approximate ˜α so as to obtain an approximate
unbiased MEUα estimator for ΓT(µe) with any desired approximation error ϵ > 0.
Finally, the above results allow us to extend DAV-Learning and SAV-Learning, and intro-
duce their BUC counterparts. These extensions, which we term DAV-Learning-BUC and
SAV-Learning-BUC, are presented in Algorithms 3 and 4, respectively (see Online Appendix C).
The main difference between these extensions and their original version is that they benefit from
weight modifiers (26)-(27) to first obtain estimators for the upper and lower bound value functions
(as opposed to the main value function itself).
7. Performance Analyses: Numerical Results
To gain further insights into the performance of our purposed algorithms, we now perform two sets
of numerical experiments. The first is a case study of a medical decision-making problem faced by
physicians at our partner hospital, and involves using a clinical data set of patients with a kidney
transplant operation. In the second set, we make use of synthetic data in which we simulate patient
trajectories under different models while controlling the true data generating model.
7.1. Case Study: New Onset Diabetes After Transplantation (NODAT)
In this section, we apply our proposed algorithms on a clinical data set that contains over 63,000
data points pertaining 407 patients who had a kidney transplant operation during a seven year
period at our partner hospital. Details about the data set can be found in the author’s previous
publications (Boloori et al. 2015, 2020, Munshi et al. 2020b, 2021).

````

## PDF page 29; PDF label 29

FORMULA CHECK REQUIRED: original PDF page 29.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
29
Patients who undergo transplantation often face a significant risk of organ rejection. To miti-
gate this risk, physicians typically use an intensive amount of an immunosuppressive drug (e.g.,
tacrolimus). Immunosuppressive drugs, however, have a well-established effect known as the dia-
betogenic effect, and thus, can elevate the risk of New Onset Diabetes After Transplantation
(NODAT). NODAT refers to incidence of diabetes in a patient with no history of diabetes prior
to transplantation (see, e.g., Chakkera et al. 2009, Boloori et al. 2015, 2020, and the references
therein). To control the risk of NODAT, physicians have to decide whether or not to put the patient
on insulin.29
Table 1 describes the observed patient covariates (observations) and their levels. As the table
shows, some of these observations are time-varying. Furthermore, most of them are dichotomized
to high versus low level values. However, the medical tests used to measure the blood glucose
(FPG and Hb1Ac) and the lowest concentration of tacrolimus in the patient’s body—a quantity
known as trough level or C0—have three levels. These levels are defined based on both the medical
literature and the practice at our partner hospital. Tables 2 and 3 show the patients’ latent states
and physicians’ actions/prescriptions during each visit post-transplant, respectively. Latent states
described in Table 2 are summary variables that describe the main condition of the patient in
terms of decision-making related to use of an immunosuppressive drug (e.g., tacrolimus) and insulin
therapy (i.e., the actions in Table 3). These patient summary variables are, however, hidden to
physicians, since physicians can only rely on medical tests, which have a wide range of false-positive
and false-negative errors. In particular, blood glucose levels are measured by two medical tests
Fasting Plasma Glucose (FPG) and Hemoglobin A1c (HbA1c), which are subject to false-positive
and false-negative errors. Similarly, the concentration of immunosuppressive drugs is measured
through tests such as Abbott Architect and Magnetic Immunoassay, which are error-prone.
Data Pre-processing Steps. Our data set includes information related to patients’ follow-up
visits during months 1, 4, and 12 post transplantation. However, for the goals of this study, we
make use of the same data preprocessing steps as those in (Boloori et al. 2020). In particular, we
use imputation to replace missing values (see also Munshi et al. 2021) and also make use of cubic
spline interpolation to create a test bed with clinical history of patients for months 1 to 12 after
transplant. That is, for the purpose of this study, we consider monthly visits that occur for a year
post-transplant. Thus, we let T ≜12 and T ≜{1,2,··· ,12}. The imputed data includes the 13
29 Of note, similar to this study, Boloori et al. (2020) also address simultaneous management of immunosuppressive
drugs and insulin for NODAT patients. However, the study of Boloori et al. (2020) is not concerned with the main
aspects of this work. Namely, it does not deal with (a) causal inference, or (b) Reinforcement Learning. The main
ideas we use in this work are also not used in Boloori et al. (2020). For example, we make use of Importance Sampling
ideas along with weight-adjusted versions of the Bellman equation, but in Boloori et al. (2020) the approach is vastly
different: an APOMDP model is directly fitted to the data, and the optimal policy of this APOMDP is established
using its Bellman equation (without weight adjustment) based on the theoretical results known for APOMDPs
(Saghafian 2018). We believe both the approach used in Boloori et al. (2020) and in this study are novel. However,
they are not directly comparable in a ceteris paribus manner due to the above-mentioned differences.

````

## PDF page 30; PDF label 30

FORMULA CHECK REQUIRED: original PDF page 30.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
30
Article submitted to ; manuscript no.
Table 1
Observed Covariates (Observations)
Var. No.
Risk Factor (Abbr.)
Unit
Low Level
Mid Level
High Level
Time-Varying
1
Glucose test† (FPG, HbA1c)
mg/dL, %
Healthy
Pre-Diabetic
Diabetic
Yes
2
Trough level test‡ (C0)
mg/dL
[4,8)
[8,10)
[10,14]
Yes
3
Age
Years
<50
—
≥50
No
4
Gender
—
Female
—
Male
No
5
Race
—
White
—
non-White
No
6
Diabetes history (Diab Hist)
—
No
—
Yes
No
7
Body mass index (BMI)
kg/m2
<30 (non-obese)
—
≥30 (obese)
Yes
8
Blood pressure (BP)
—
Normal♯
—
Hypertension
Yes
9
Total cholesterol (Chol)
mg/dL
<200
—
≥200
Yes
10
High-density lipoportein (HDL)
mg/dL
≥40
—
<40
Yes
11
Low-density lipoportein (LDL)
mg/dL
<130
—
≥130
Yes
12
Triglyceride (TG)
mg/dL
<150
—
≥150
Yes
13
Uric acid (UA)
mg/dL
<7.3
—
≥7.3
Yes
†A patient with FPG≥126 (100 ≤FPG< 126) mg/dL or HbA1c≥6.5% (5.7 ≤HbA1c<6.5%) is labeled as diabetic (pre-diabetic),
and a patient with FPG<100 mg/dL or HbA1c<5.7% is labeled as healthy (see, e.g., ADA 2012).
‡C0 ∈[4,8), [8,10), [10,14] mg/dL is label as “low,” “medium,” and “high,” respectively (see, e.g., Boloori et al. 2020).
♯Normal Blood Pressure (BP) is defined as systolic (diastolic) BP less than 120 (80) mmHg (see, e.g., Whelton et al. 2017).
Note: All variables with three levels are coded as 1,2, 3 (low, mid, high). All variables with two levels are coded as 1, 2 (low, high).
variables listed in Table 1 for each of the 407 patients and every month during a year of follow-up
post-transplant (a total of 13 × 407 × 12 = 63,492 data points).
Behavior Policy. We estimate the behavior policy based on the actions we observe in our data.
These actions are mainly based on the the clinical protocols followed at our partner hospital.
A detailed summary of the main immunosuppression protocol can be found in (Munshi et al.
2021), which includes induction therapy with either rabbit anti-thymocyte, immunoglobulin, or
basiliximab, as well as a tapering course of glucocorticoids. However, here our focus is on the use
of tacrulimus, and we observe that patients are often put on high (i.e., aggressive) dose tacrolimus
during the first months post-transplant, and in later months, depending on the observations made
about the patient patients, they might be transferred to a low (i.e., non-aggressive) dose. This is
consistent with the fact that patients in most medical practices are consistently kept on high levels
of tacrolimus in early stages post-transplant (see, e.g., Ghisdal et al. 2012, Boloori et al. 2020).
Furthermore, with respect to the use of insulin, patients are primarily put on insulin when their
Hb1Ac and FPG tests indicates that they are not diabetic free (see definitions of pre-diabetic and
diabetic in Table 1). Using the observed actions in our data set as well as the estimated belief
vectors {πm
t }t∈T for each patient (for further details, see the “Other Details” paragraph below),
we next estimate µb(At|Πm
t ) by training a multi-class multiple logistic regression classifier. This
classifier is endowed with an ℓ2-norm penalty, which is tuned to ensure that each action is selected
with an estimated probability of 0.05 or higher across all observations (see, e.g., Murphy et al.
2016).
Immediate Gain Variable. To calculate the immediate gains, we use a similar approach to our
previous work (see, e.g., Boloori et al. 2020). In particular, we make use of Quality of Life (QoL)
scores, which take values in [0,1]. This allows us to differentiate between the Quality of Life of
being in a diabetic, prediabetic, or healthy state and also having different concentration of the

````

## PDF page 31; PDF label 31

FORMULA CHECK REQUIRED: original PDF page 31.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
31
Table 2
Latent Health States
State
Transplant Condition
Diabetes Condition
(Tacrolimus C0)
1
Low
Diabetes (type II)
2
Medium
3
High
4
Low
Pre-diabetes
5
Medium
6
High
7
Low
Healthy
8
Medium
9
High
immunosuppressive in the body, which are in turn associated with differing risks of organ rejection.
Table 4 shows the yearly-based QoL scores associated with each state, which are divided by 12 to
represent the fact that patients’ visits are monthly.3031
Other Details. The belief state space in our setting, ∆S , is a 8-simplex, since there are 9 latent
states (Table 2). The vector of basis functions b(π) maps this 8-simplex to R13, which allows us
to include enough cut points (while making sure that the value function is piecewise linear and
continuous). Thus, both the belief space and the parameter space in our setting are continuous
and relatively high-dimensional. To perform our analyses, we use a discount factor of β = 0.95. We
also tune a penalty parameter θt = θ. To create the set of models M , we make use of the algorithm
in Table 3 of our earlier work (Boloori et al. 2020). Specifically, first the Baum–Welch algorithm
is used to obtain point estimations for state transition and observation probability matrices. Next,
an entropy ball is constructed (using the Kullback–Leibler divergence criterion) around these point
estimate matrices. For tractability, we set |M | = 4 in this case study. However, our framework is
general and can be used for any number of estimated models. In Section 7.2, for example, we change
30 In addition to immediate gains, our framework allows including lump-sum gains (i.e., gains at the end of the horizon
to reflect the Quality of Life associated with the remaining years). For the purposes of this study, however, we simply
set V0(π) ≜0.
31 Given πm
t
in each period t under each model m, the obtained immediate gain in each period t under each model
m is considered be the weighted average of immediate gain values shown in Table 4, where weights are given by πm
t
(see also Remark 2).
Table 3
Actions
Action
Prescription
Prescription
(Tacrolimus dose)
(Insulin use)
1
Low (Non-Aggressive)
No
2
High (Aggressive)
3
Low (Non-Aggressive)
Yes
4
High (Aggressive)

````

## PDF page 32; PDF label 32

FORMULA CHECK REQUIRED: original PDF page 32.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
32
Article submitted to ; manuscript no.
Table 4
Immediate Gain Values
State
Transplant Condition
Diabetes Condition
Immediate Gain Value†
(Tacrolimus C0)
1
Low
Diabetes (type II)
0.68/12
2
Medium
0.72/12
3
High
0.76/12
4
Low
Pre-diabetes
0.82/12
5
Medium
0.87/12
6
High
0.89/12
7
Low
Healthy
0.90/12
8
Medium
0.92/12
9
High
0.95/12
†Immediate gains are average values approximated based on QoL scores reported in other studies and include combined
disutility of (a) being in a diabetic state, and (b) having high risk of organ rejection. Yearly-based values are divided by
12 to represent monthly measures.
our assumption on the number of models and consider |M | = 10 different models. Our framework
is also not restricted to any specific way of estimating the underlying models. For example, in
Section 7.2, we make use of a different way of constructing the set M .32 Finally, we consider the
distribution F(π) to be uniform. That is, we use a uniform prior belief at time zero, and implement
the Bayesian belief updating operator (see Eq. (9)) to create a sequence of belief vectors {πm
t }t ∈T
for each patient under each model m ∈M (see, e.g., steps 1-5 in Algorithms 1, 2, 3, and 4).
Results. The performance of the three treatment regimes (DAV-Learning, SAV-Learning, and
observed) are compared in Table 5. Average and standard deviations in these tables are calculated
using Monte Carlo replications.33 We focus on the performance of DAV-Learning, SAV-Learning
as opposed to their BUC extensions (DAV-Learning-BUC, SAV-Learning-BUC), because as dis-
cussed in Remark 2, the results of Proposition 3 hold in this application. In the next section,
we run experiments using DAV-Learning and SAV-Learning as well as DAV-Learning-BUC and
SAV-Learning-BUC.
As can be seen from the results in Table 5, DAV-Learning outperforms SAV-Learning in terms
of the mean performance for most values of the pessimism level, α. As both Table 5 and Figure 2
show, however, both DAV-Learning and SAV-Learning approaches significantly outperform the
observed regime. In particular, as Figure 2 shows, the improvements over the observed regime when
using DAV-Learning and SAV-Learning are in the ranges (10%,42%) and (10%,32%), respectively,
depending the value of α. Of note, these ranges also imply that the mean performance of the
SAV-Learning regime is much more robust to the value of α than that of DAV-Learning. This is due
to the fact that SAV-Learning uses a “safe estimation” of the underlying parameter of the value
32 It should be also noted that any continuous set of models can be approximated via finite sets with any required
precision. That is, even if M is not finite, one can always consider a finite set M as a close approximation to the
continuous one.
33 The number of these replications is chosen so that the confidence intervals are tight enough, while maintaining
reasonable computational times.

````

## PDF page 33; PDF label 33

FORMULA CHECK REQUIRED: original PDF page 33.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
33
Table 5
Estimated Total Discounted Gain Under Observed and Proposed Regimes (Case Study with β = 0.95)
Pessimism Level (α)
Observed Regime†
DAV-Learning†
SAV-Learning†
0.00
1.472 (1.455, 1.489)
2.085 (2.061, 2.108)
1.949 (1.770, 2.128)
0.25
1.468 (1.456, 1.480)
1.939 (1.920, 1.958)
1.888 (1.566, 2.210)
0.50
1.464 (1.457, 1.471)
1.794 (1.779, 1.808)
1.786 (1.534, 2.039)
0.75
1.460 (1.458, 1.462)
1.648 (1.638, 1.658)
1.682 (1.658, 1.706)
1.00
1.455 (1.452, 1.458)
1.609 (1.560, 1.657)
1.606 (1.585, 1.627)
†Values in parenthesis represent 95% confidence intervals. Values in bold font represent the best performance.
For all values, only the first three decimal places are shown.
DAV-Learning
SAV-Learning
maximax values
maximin values
0.0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
100
α
Improvement (%)
Figure 2
Percentage improvement over the observed regime (case study with β = 0.95). Gray areas represent error bands
with the curve at the center of each error band representing the mean value.
function (see, e.g., step 12 of Algorithm 2). This allows SAV-Learning to guard against ambiguity
up-front (i.e., in parameter estimation) in contrast to DAV-Learning which combines policy values
at the end. Thus, a decisions-maker who uses SAV-Learning does not need to be that concerned
about the value of α s/he uses (or try to tune it).
Finally, as can be seen from both Table 5 and Figure 2, the performance of DAV-Learning
and SAV-Learning regimes degrades as the pessimism level α increases. This is fully expected,
since as we move from a maximax view to a maximin one DAV-Learning and SAV-Learning tend
to put more weight on the worst-case scenario, and hence, perform more conservatively. More
conservativeness, however, does not necessarily mean more robustness to model ambiguity. We
further investigate this issue in Section 7.3, and generate important insights into the values of α
that can provide the highest level of robustness to model ambiguity.
7.2. Synthetic Data Analyses
We now use similar assumptions to those described in the case study, but instead of using actual
patient traceries, simulate random patient trajectories for 100 patients with 10 follow-up periods,
and use (|M | = 10) different models. These yield randomly generated belief data of the form
(πm
t )t∈T under each m ∈M . We keep the other assumptions (e.g., the action space, the number of
hidden states, the parameter space, basis functions, etc.) the same as those in the previous section.

````

## PDF page 34; PDF label 34

FORMULA CHECK REQUIRED: original PDF page 34.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
34
Article submitted to ; manuscript no.
Table 6
Estimated Total Discounted Gain Under Observed and Proposed Regimes (Synthetic Data Analyses
with β = 0.95)
Pessimism Level (α)
Observed Regime†
DAV-Learning†
SAV-Learning†
0.00
1.441 (1.440, 1.442)
1.973 (1.969, 1.977)
1.442 (1.441, 1.442)
0.25
1.415 (1.415, 1.416)
1.815 (1.811, 1.818)
1.434 (1.433, 1.434)
0.50
1.389 (1.389, 1.390)
1.656 (1.654, 1.659)
1.428 (1.428, 1.429)
0.75
1.364 (1.364, 1.364)
1.498 (1.496, 1.499)
1.434 (1.434, 1.434)
1.00
1.338 (1.338, 1.339)
1.348 (1.348, 1.348)
1.444 (1.444, 1.444)
†Values in parenthesis represent 95% confidence intervals. Values in bold font represent the best performance.
For all values, only the first three decimal places are shown.
We assume patient trajectories are such that for each m ∈M the belief vector (πm
t )t∈T is gener-
ated via a Dirichlet distribution with the vector of parameters (pm
i )i∈{1,2··· ,9}. All of these models are
misspecified, and hence, for each model, we randomly draw each pm
i from a Uniform(0,1) distribu-
tion. We assume the true model is such that all pi values are equal to 0.5. Furthermore, we specify
the behavior policy as follows. For actions a = 1,2,3, we set µb(A = a|Π = π) =
exp(π′ ϱa)
1+P3
a=1 exp(π′ ϱa) and
for action a = 4 we set µb(A = a|Π = π) =
1
1+P3
a=1 exp(π′ ϱa), where ϱ1, ϱ2, and ϱ3 are 9-dimensional
predefined vectors. To perform our analyses, we choose each ϱa (a = 1,2,3) as a vector with all
elements equal to 0.1, except the a-th element, which is set to −1.
Table 6 and Figure EC.1 (Online Appendix D) present our results using the DAV-Learning
and SAV-Learning approaches under the same immediate gain values as those in the case study
(see Table 4). Similar results for the BUC version of these approaches, DAV-Learning-BUC and
SAV-Learning-BUC, are presented in Table 7 and Figure EC.2 (Online Appendix D). Similar to
the case study, we observe from these results that all of our proposed algorithms outperform the
observed regime. Furthermore, the percentage improvement of DAV-Learning an SAV-Learning
over the observe regime ranges in (1%,37%) and (1%,8%), respectively, depending on the value of
α. These improvement ranges for DAV-Learning-BUC an SAV-Learning-BUC are (0.7%,4.9%) and
(0.07%,7.9%), respectively. In addition, similar to our observation in the case study, DAV-Learning
outperforms SAV-Learning for most vales of α (Figure EC.1), and a similar result can be seen
for the BUC regimes (Figure EC.2). Furthermore, similar to the case study, the performance of
SAV-Learning is much more robust to the value of α compared to DAV-Learning, but in the BUC
regimes, DAV-Learning-BUC shows relatively more robustness than SAV-Learning-BUC. In the next
section, we further investigate the robustness of our proposed approaches to model ambiguity, and
generate insights into the best value of α that a decision-maker can use to achieve the highest level
of robustness.
7.3. Robustness to Model Ambiguity
We now compare our proposed approaches in terms of their percentage gain loss (a.k.a., regret).
That is, we first consider an oracle who knows both the true data generating model and the optimal
policy under it, and then compare the performance of a decision-maker who is blind to the true data
generating model (is facing model ambiguity) but uses either DAV-Learning or SAV-Learning (or

````

## PDF page 35; PDF label 35

FORMULA CHECK REQUIRED: original PDF page 35.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
35
Table 7
Estimated Total Discounted Gain Under Observed and Proposed BUC Regimes (Synthetic Data
Analyses with β = 0.95)
Pessimism Level (α)
Observed Regime†
DAV-Learning-BUC†‡
SAV-Learning-BUC†‡
0.00
1.441 (1.440, 1.442)
1.511 (1.506, 1.517)
1.448 (1.442, 1.447)
0.25
1.415 (1.415, 1.416)
1.468 (1.464, 1.472)
1.429 (1.428, 1.429)
0.50
1.389 (1.389, 1.390)
1.425 (1.422, 1.428)
1.419 (1.418, 1.420)
0.75
1.364 (1.364, 1.364)
1.382 (1.380, 1.384)
1.418 (1.416, 1.420)
1.00
1.338 (1.338, 1.339)
1.344 (1.344, 1.345)
1.444 (1.441, 1.447)
†Values in parenthesis represent 95% confidence intervals. Values in bold font represent the best performance.
For all values, only the first three decimal places are shown.
‡Algorithm is run by assuming ηm
t = 1.02 for all t ∈T and m ∈M . Results are based on ϵ-approximations
for a small ϵ (see the discussion in Section 6).
their BUC version, DAV-Learning or SAV-Learning). How much robustness to model ambiguity
using these proposed approaches provide? What is the maximum gain loss of these approaches? For
what value of α the gain loss is minimized? Importantly, in order to minimize the gain loss, should
the decision-maker use an extreme value of α (e.g., α = 0,1) or a mid level value (e.g., α = 0.5)?
And does the answer depend on which learning approach is used?
To answer these questions, we make use of a similar setup to the one discussed in Section 7.2.
The results are shown in Figure EC.3 (Online Appendix D), which depicts the percentage gain
loss of DAV-Learning and SAV-Learning compared to the imaginary oracle. Similar results for
the BUC version of these approaches (DAV-Learning-BUC or SAV-Learning-BUC) are provided in
in Figure EC.4 (Online Appendix D). From these figure, we make three main observations: (1)
Gain loss has a U-shape curve as α varies. Importantly, the minimum loss for all four approaches
(DAV-Learning, SAV-Learning DAV-Learning, SAV-Learning) are obtained at a mid value of α
(approximately α = 0.25), which implies that using extreme cases of α = 0.0 (a maximax view) or
α = 1.0 (a maximin view) does not provide the highest level of robustness to model ambiguity. That
is, neither the maximax view nor the maximin view is robustness-maximizing. (2) The gain loss
under SAV-Learning (SAV-Learning-BUC) is more robust to the changes in value of α compared to
DAV-Learning (DAV-Learning-BUC). (3) All four proposed approaches are able to strongly shield
against model ambiguity, regardless of the value of α used. Specifically, the gain loss under these
approaches (compared to the imaginary oracle) is very low (below 0.6%). This implies that a
decision-maker who is facing model ambiguity can use these approaches and obtain policies that
have similar performance to the very best policy that could be used, if the true data generating
was known (i.e., if there was no ambiguity regarding the underlying causal model).34
Remark 4 (Dimensionality and Computations). The proposed algorithms DAV-Learning
and SAV-Learning as well as their BUC extensions, DAV-Learning-BUC and SAV-Learning-BUC,
do not require their main parameter spaces to have low dimensionality. That is, they can safely
34 These findings hold in the context of our numerical experiments. However, we avoid making general conclusions,
since doing so will require a more extensive set of experiments. Our results, however, provide a proof of concept that
can be further explored by future research.

````

## PDF page 36; PDF label 36

FORMULA CHECK REQUIRED: original PDF page 36.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
36
Article submitted to ; manuscript no.
be used in high-dimensions, especially because they make use of regularization to avoid overfit-
ting in high-dimensional settings. In particular, both our theoretical and numerical performance
results (Sections 5 and 7) indicate that these algorithms have suitable convergence results and are
relatively tractable for use in real-world applications. For example, while the results in Section 5
indicate that only some typical “regularity” conditions are needed to ensure that they have suitable
asymptotic convergence behavior, numerical experiments in Section 7 suggest that they are indeed
tractable in real-world applications. However, it should be noted that our numerical experiments
are motivated by a specific medical decision-making application in which the belief state space,
∆S , is a 8-simplex (since there are 9 latent states), the vector of basis functions b(π) maps this
8-simplex to R13, and the main parameter needed to estimate the value function has a reasonable
dimensionality (belongs to R13). Furthermore, the set of models and the policies needed in this
application are not extremely large. If, in an application, the cardinality of these underlying spaces
is significantly higher than those in our experiments, the proposed algorithms may lose compu-
tational tractability. In such scenarios, further care (e.g., discretization, approximation, etc.) is
needed to speed up these algorithms. Finally, it should be noted that the proposed algorithms
are suitable for scenarios in which the observed history provides at least some information about
latent confounders. In APOMDPs, some models might be naturally more informative than oth-
ers; see Definition 2 and Lemma 2 of Saghafian (2018) for the notion of model informativeness in
APOMDPs, which is based on the Blackwell–Sherman–Stein sufficiency theorem. However, if none
of the models are informative, then the Bayesian operator that is used in these algorithms might
fail to update the belief distributions under all models, and hence, the value function cannot be
learned from data for different values of π. Intuitively, if the observed data does not provide any
information about the dynamic latent confounders, then one should not hope for using observed
variables to effectively adjust for the effect of dynamic unobserved confounders.
8. Conclusion
We propose a mathematical framework as well as learning algorithms for finding an effective
dynamic treatment regime under model ambiguity. Incorporating model ambiguity a priori in the
analyses not only provides robustness to inevitable misspecifications (e.g., caused by hidden con-
founders with unknown dynamics and/or impact on the observed variables), but more broadly can
bridge the gap between two philosophical views of causal inference: model-based and model-free.
Our work also tries to close the gap between RL techniques and dynamic causal inference meth-
ods. Specifically, as is common, we view the problem of finding an effective treatment regime as an
“off-policy” RL problem. However, unlike the existing work, we allow the learning to occur across
a “cloud” of potential data generating models. This is specifically useful when data are observa-
tional, the behavior policy is unknown, and the existence of time-varying unmeasured confounders

````

## PDF page 37; PDF label 37

FORMULA CHECK REQUIRED: original PDF page 37.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
37
(which are themselves affected by previous actions) make the task of learning the causal impact of
an evaluation policy challenging.
Unlike the available RL techniques, or the methods related to causal inference in dynamic set-
tings, our work also allows for a two-way personalization: the obtained treatment policies are not
only personalized based on the subject’s variables (e.g., a patient’s covariates), but also based on
the ambiguity attitude and preferences of the decision-maker (e.g., the physician). Given the impor-
tance of this two-way personalization in a variety of applications (e.g., medical decision-making
or public policy), we hope that future research can develop further data-driven methods to learn
policies that are personalized in both ways.
We also hope that the future research can test and implement our prosed learning algorithms
in a variety of other applications. In this study, we investigate the performance of these learning
algorithms in three ways. First, we analytically establish their asymptotic behavior, including
(weak) consistency and asymptotic normality. Second, we examine them in a case study using
clinical data related to NODAT patients. Third, we make use of simulation experiments (synthetic
data), in which we control the true data generating model and compare the performance of our
proposed methods with that of an imaginary oracle who knows both the true data generating model
and the optimal policy under that model. All these investigations reveal promising results. However,
further research is needed to more broadly investigate the performance of our proposed methods in
other applications and domains. With the increasing availability of sensor-based devices that are
connected via Internet of Things (IoT) and benefit from data fusion (see, e.g., Saghafian et al. 2022),
future research can also investigate augmenting our approaches to work with data obtained from
multiple connected streams. Finally, future research can examine the interpretability of the policies
that are obtained via DAV-Learning, SAV-Learning, DAV-Learning-BUC, and SAV-Learning-BUC,
and propose adjustments (if needed) to ensure that they can be effectively used in practice.
References
ADA(2012). 2012. Standards of medical care in diabetes. Diabetes Care 35 S11–S63.
Ahn, D., S. Choi, D. Gale, S. Kariv. 2014. Estimating ambiguity aversion in a portfolio choice experiment. Quantitative
Economics 5(2) 195–223.
Angrist, J.D., G.W. Imbens, D.B. Rubin. 1996. Identification of causal effects using instrumental variables. Journal
of the American Statistical Association 91 434––471.
Arrow, K. J., L. Hurwicz. 1977. An optimality criterion for decision making under ignorance. K. J. Arrow, L. Hurwicz,
eds., Studies in Resource Allocation Processes. Cambridge University Press.
Arrow, K.J. 1951.
Alternative approaches to the theory of choice in risk-taking situations. Econometrica 19(4)
404–437.
Athey, S., S. Wager. 2021. Policy learning with observational data. Econometrica 89(1) 133–161.
Bang, H., J.M. Robins. 2021. Doubly robust estimation in missing data and causal inference models. Biometrics
61(4) 962–972.
Bennett, A., N. Kallus. 2021. Proximal reinforcement learning: Efficient off-policy evaluation in partially observed
Markov decision processes. arXiv preprint arXiv:2110.15332 .
Bennett, A., N. Kallus, L. Li, A. Mousavi. 2021.
Off-policy evaluation in infinite-horizon reinforcement learning
with latent confounders. Proceedings of the 24th International Conference on Artificial Intelligence and Statistics.
1999–2007.

````

## PDF page 38; PDF label 38

FORMULA CHECK REQUIRED: original PDF page 38.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
38
Article submitted to ; manuscript no.
Bhid´e, A.V. 2000. The Origin and Evolution of New Business. Oxford University Press, Oxford.
Boloori, A., S. Saghafian, H.A. Chakkera, C.B. Cook. 2015. Characterization of remitting and relapsing hyperglycemia
in post-renal-transplant recipients. PLOS ONE 10(11) 1–16.
Boloori, A., S. Saghafian, H.A. Chakkera, C.B. Cook. 2020. Data-driven management of post-transplant medica-
tions: An ambiguous partially observable Markov decision process approach. Manufacturing and Service Operations
Management 22(5) 1066–1087.
Box, G. 1979. Robustness in the strategy of scientific model building. R. Launer, G. Wilkinson, eds., Robustness in
Statistics. Academic Press, NY, 201–236.
Bren, A., S. Saghafian. 2019.
Data-driven percentile optimization for Multi-Class queueing systems with model
ambiguity: Theory and application. INFORMS Journal on Optimization 1(4) 267–287.
Butler, Emily L, Eric B Laber, Sonia M Davis, Michael R Kosorok. 2018. Incorporating patient preferences into
estimation of optimal individualized treatment rules. Biometrics 74(1) 18–26.
Chakkera, H. A., E. J. Weil, J. Castro, R. L. Heilman, K. S. Reddy, M. J. Mazur, K. Hamawi, D. C. Mulligan,
A. A. Moss, K. L. Mekeel, F. G. Cosio, C. B. Cook. 2009. Hyperglycemia during the immediate period after kidney
transplantation. Clinical Journal of the American Society of Nephrology 4 853–859.
Chakraborty, B., S.A. Murphy. 2014. Dynamic treatment regimes. Annual Review of Statistics and Its Application
1(1) 447–464.
Dedecker, J., S. Louhichi. 2002. Maximal inequalities and empirical central limit theorems. T. Mikosch, M. Sørensen,
eds., Empirical Process Techniques for Dependent Data. Birkh¨auser, Boston, 137–159.
Frank, R.G., R.J. Zeckhauser. 2007. Custom-made versus ready-to-wear treatments: Behavioral propensities in physi-
cians’ choices. Journal of Health Economics 26(6) 1101–1127.
Ghiradato, P, F Maccheroni, M Marinacci. 2004.
Differentiating ambiguity and ambiguity attitude.
Journal of
Economic Theory 118 133–173.
Ghisdal, L., S. Van Laecke, M.J. Abramowicz, R. Vanholder, D. Abramowicz. 2012. New-onset diabetes after renal
transplantation risk assessment and management. Diabetes Care 35(1) 181–188.
Hansen, L.P. 1982.
Large sample properties of generalized method of moments estimators.
Econometrica 50(4)
1029–1054.
Heath, C., A. Tversky. 1991. Preference and belief: ambiguity and competence in choice under uncertainty. Journal
of Risk and Uncertainty 4(1) 5–28.
Hu, Y., S. Wager. 2021.
Off-policy evaluation in partially observed Markov decision processes.
arXiv preprint
arXiv:2110.12343 .
Hurwicz, L. 1951a. Optimality criteria for decision making under ignorance. Cowles Commission discussion paper:
Statistics no. 370 .
Hurwicz, L. 1951b. Some specification problems and applications to econometric models. Econometrica 19 343–344.
Jiang, N, L. Li. 2016. Doubly robust off-policy value evaluation for reinforcement learning. Proceedings of the 33rd
International Conference on Machine Learning. 652–661.
Kallus, N., M. Uehara. 2020. Double reinforcement learning for efficient off-policy evaluation in Markov decision
processes. Journal of Machine Learning Research 21 167–1.
Kallus, N., A. Zhou. 2020. Confounding-robust policy evaluation in infinite-horizon reinforcement learning. arXiv
preprint arXiv:2002.04518 .
Kallus, N., A. Zhou. 2021. Minimax-optimal policy learning under unobserved confounding. Management Science
67(5) 2870–2890.
Kosorok, M.R. 2008. Introduction to Empirical Processes and Semiparametric Inference. Springer, New York, NY.
Kosorok, M.R., E.B. Laber. 2019. Precision medicine. Annual Review of Statistics and its Application 6(263–286)
1243–1254.
Laber, Eric B, Daniel J Lizotte, Bradley Ferguson. 2014.
Set-valued dynamic treatment regimes for competing
outcomes. Biometrics 70(1) 53–61.
Leqi, L., E.H. Kennedy. 2021. Median optimal treatment regimes. arXiv preprint arXiv:2103.01802 .
Linn, K.A., E.B. Laber, L.A. Stefanski. 2017. Interactive q-learning for quantiles. Journal of the American Statistical
Association 112(518) 638–649.
Linn, Kristin A, Eric B Laber, Leonard A Stefanski. 2015. Chapter 15: Estimation of dynamic treatment regimes
for complex outcomes: balancing benefits and risks. Adaptive treatment strategies in practice: Planning trials and
analyzing data for personalized medicine. SIAM, 249–262.
Lizotte, Daniel J, Michael Bowling, Susan A Murphy. 2012. Linear fitted-q iteration with multiple reward functions.
The Journal of Machine Learning Research 13(1) 3253–3295.
Lizotte, Daniel J, Eric B Laber. 2016. Multi-objective markov decision processes for data-driven decision support.
The Journal of Machine Learning Research 17(1) 7378–7405.
Luckett, D.J., E.B. Laber, A.R. Kahkoska, D.M. Maahs, E. Mayer-Davis, M.R. Kosorok. 2020. Estimating dynamic
treatment regimes in mobile health using V-Learning. Journal of the American Statistical Association 115(530)
692–706.

````

## PDF page 39; PDF label 39

FORMULA CHECK REQUIRED: original PDF page 39.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Article submitted to ; manuscript no.
39
Magnani, A., S.P. Boyd. 2009. Convex piecewise-linear fitting. Optimization and Engineering 10 1–17.
Manski, C.F. 2007. Identification for Prediction and Decision. Harvard Univeristy Press, Cambridge, MA.
Manski, C.F. 2021. Econometrics for decision making: Building foundations sketched by haavelmo and wald. Econo-
metrica 89(6) 2827–2853.
Marinacci, M. 2002. Probabilistic sophistication and multiple priors. Econometrica 70(2) 755––764.
Munshi, V.N., S. Saghafian, C.B. Cook, S. Aradhyula, H.A. Chakkera. 2021. Use of imputation and decision modeling
to improve diagnosis and management of patients at risk for newonset diabetes after transplantation. Annals of
Transplantation 26 1–9.
Munshi, V.N., S. Saghafian, C.B. Cook, D. Steidley, B. Hardaway, H.A. Chakkera. 2020a. Incidence, risk factors, and
trends for post-heart transplantation diabetes mellitus. The American Journal of Cardiology 125(3) 436–440.
Munshi, V.N., S. Saghafian, C.B. Cook, K.T. Werner, H.A. Chakkera. 2020b. Comparison of post-transplantation
diabetes mellitus incidence and risk factors between kidney and liver transplantation patients. PLOS ONE 15(1)
1–12.
Murphy, S.A. 2003. Optimal dynamic treatment regimes. Journal of the Royal Statistical Society: Series B (Statistical
Methodology) 65(2) 331–355.
Murphy, S.A. 2005. An experimental design for the development of adaptive treatment strategies. Satitics in Medicine
24(10) 1455–1481.
Murphy, S.A., Y. Deng, E.B. Laber, H.R Maei, R.S. Sutton, K. Witkiewitz. 2016. A batch, off-policy, actor-critic
algorithm for optimizing the average reward. arXiv preprint arXiv:1607.05047 .
Murphy, S.A., M.J. van der Laan, J.M. Robins, CPPRG. 2001. Marginal mean models for dynamic regimes. Journal
of the American Statistical Association 96(456) 1410–1423.
Namkoong, H., R. Keramati, S. Yadlowsky, E. Brunskill. 2020. Off-policy policy evaluation for sequential decisions
under unobserved confounding. arXiv preprint arXiv:2003.05623 .
Nie, X., E. Brunskill, S. Wager. 2021. Learning when-to-treat policies. Journal of the American Statistical Association
116(533) 392–409.
Pearl, J. 2009. Causality: Models, Reasoning, and Inference. Cambridge University Press.
Pearl, J., J. Robins. 1995. Probabilistic evaluation of sequential plans from causal models with hidden variables.
P. Besnard, S. Hanks, eds., Uncertainty in Artificial Intelligence 11. Morgan Kaufmann, San Francisco, 444––453.
Precup, D., R.S. Sutton, S. Singh. 2000. Eligibility traces for off-policy policy evaluation. Proceedings of the 17th
International Conference on Machine Learning. 759–66.
Robins, J. 1986. A new approach to causal inference in mortality studies with a sustained exposure period—application
to control of the healthy worker survivor effect. Mathematical Modeling 7(9-12) 1393–1512.
Robins, J. 1997.
Causal inference from complex longitudinal data. Latent variable modeling and applications to
causality. Springer, 69–117.
Robins, J. 2004. Optimal structural nested models for optimal sequential decisions. Proceedings of the Second Seattle
Symposium in Biostatistics. Springer, 189–326.
Robins, J., M.A. Hern´an, B. Brumback. 2000.
Marginal structural models and causal inference in epidemiology.
Epidemiology 11(5) 550–560.
Rosenbaum, PR. 2002. Observational Studies. Springer, New York, NY.
Rosenbaum, PR. 2010. Design of Observational Studies. Springer, New York, NY.
Rubin, D.B. 1986. Comment: Which ifs have causal answers. Journal of the American Statistical Association 81
961––962.
Saghafian, S. 2018. Ambiguous partially observable Markov decision processes: Structural results and applications.
Journal of Economic Theory 178 1–35.
Saghafian, S., S.A. Murphy. 2021. Innovative health care delivery: The scientific and regulatory challenges in designing
mHealth interventions. NAM Perspectives. Commentary, National Academy of Medicine, Washington, DC. .
Saghafian, S., M. Rasouli. 2019. Robust partially observable Markov decision processes. Working Paper, Harvard
University .
Saghafian, S., B. Tomlin, S. Biller. 2022. The internet of things and information fusion: Who talks to who? Manu-
facturing & Service Operations Management 24(1) 333–351.
Saghafian, S., B.T. Tomlin. 2016. The newsvendor under demand ambiguity: Combining data with moment and tail
information. Operations Research 64(1) 167–185.
Savage, L. 1951. The theory of statistical decision. Journal of the American Statistical Association 46 55–67.
Smallwood, R., E.J. Sondik. 1973. The optimal control of partially observable Markov processes over a finite horizon.
Operations Research 21(5) 1071–1088.
Stoy, J. 2011. Statistical decisions under ambiguity. Theory and Decision 70(2) 129–148.
Tennenholtz, G., U. Shalit, Sh. Mannor. 2020. Off-policy evaluation in partially observable environments. Proceedings
of the AAAI Conference on Artificial Intelligence, vol. 34. 10276–10283.

````

## PDF page 40; PDF label 40

FORMULA CHECK REQUIRED: original PDF page 40.

````text
Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
40
Article submitted to ; manuscript no.
Thomas, Ph., E. Brunskill. 2016. Data-efficient off-policy policy evaluation for reinforcement learning. Proceedings
of the 33rd International Conference on Machine Learning. 2139–2148.
Tsiatis, A.A., M. Davidian, S.T. Holloway, E.B. Laber, M.R. Kosorok. 2019. Dynamic Treatment Regimes: Statistical
Methods for Precision Medicine. Chapman and Hall/CRC, Boca Raton.
Wald, A. 1939. Contribution to the theory of statistical estimation and testing hypotheses. Annals of Mathematical
Statistics 10 299–326.
Wald, A. 1945. Statistical decision functions which minimize the maximum risk. Annals of Mathematics 46 265–280.
Wald, A. 1950. Statistical Decision Functions. Wiley, New York, NY.
Wang, L., Y. Zhou, R. Song, B. Sherwood. 2018. Quantile-optimal treatment regimes. Journal of the American
Statistical Association 113(523) 1243–1254.
Watson, J., C. Holmes. 2016. Approximate models and robust decisions. Statistical Science 31 465–489.
Whelton, P.K., R.M. Carey, W.S. Aronow, D.E. Casey Jr, K.J. Collins, et al. 2017. Guideline for the prevention,
detection, evaluation, and management of high blood pressure in adults: a report of the American College of Car-
diology/American Heart Association Task Force on clinical practice guidelines. Journal of the American College of
Cardiology 71(19) e127–e248.
Xu, Z., E. Laber, A.M. Staicu, E. Severus. 2020.
Latent-state models for precision medicine.
arXiv preprint
arXiv:2005.13001 .
Zhang, J., E. Bareinboim. 2019. Near-optimal reinforcement learning in dynamic treatment regimes. Advances in
Neural Information Processing Systems, vol. 32.
Zhang, Y., E.B. Laber, M. Davidian, A.A. Tsiatis. 2018. Interpretable dynamic treatment regimes. Journal of the
American Statistical Association 113(524) 1541–1549.
Zhao, Y.Q., D. Zeng, E.B. Laber, M.R. Kosorok. 2015. New statistical learning methods for estimating optimal
dynamic treatment regimes. Journal of the American Statistical Association 110(510) 583–598.

````

## PDF page 41; PDF label ec1

Technical extraction; compare with original PDF page 41.

````text
e-companion to Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
ec1
Online Appendix A: Proofs
Available Upon Request

````

## PDF page 42; PDF label ec2

Technical extraction; compare with original PDF page 42.

````text
ec2
e-companion to Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Online Appendix B: Supplementary Results and Proofs
Available Upon Request

````

## PDF page 43; PDF label ec3

FORMULA CHECK REQUIRED: original PDF page 43.

````text
e-companion to Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
ec3
Online Appendix C: DAV-Learning-BUC and SAV-Learning-BUC
Algorithms
Algorithm 3: DAV-Learning-BUC
1 for each observed trajectory and model m ∈M do
2
Initialize πm
0 using a random draw from F(π);
3
set t=1;
4
while t + 1 ∈T do
5
πm
t+1 ←T(πm
t ,at,ot,m);
6 for any given µe ∈Υ and m ∈M do
7
φm,µe
n
(ψ) ←EP
"
P
t∈T

κm
t
µe(At|Πm
t )
µb(At|Πm
t )
h
Gt + β V
m,µe
∞
(T(Πm
t ,At,Ot,m)) −V
m,µe
∞
(Πm
t )
i
b(Πm
t )
#
;
8
φm,µe
n
(ψ) ←EP
"
P
t∈T

κm
t
µe(At|Πm
t )
µb(At|Πm
t )
h
Gt + β V m,µe
∞
(T(Πm
t ,At,Ot,m)) −V m,µe
∞
(Πm
t )
i
b(Πm
t )
#
;
9
ˆψ
m,µe
n
←argminψ∈Ψ
 φm,µe
n
(ψ)
′ Ωφm,µe
n
(ψ) + θnP(ψ)

;
10
ˆψ
m,µe
n
←argminψ∈Ψ
 φm,µe
n
(ψ)
′ Ωφm,µe
n
(ψ) + θnP(ψ)

;
11
ˆV
m,µe
∞
(π) ←
 b(π))′ ˆψ
m,µe
n
;
12
ˆV
m,µe
∞
(π) ←
 b(π))′ ˆψ
m,µe
n
;
13
ˆΓ
m
∞(µe) ←
R ˆV
m,µe
∞
(π)dF(π);
14
ˆΓ
m
∞(µe) ←
R ˆV
m,µe
∞
(π)dF(π);
15 for any given µe ∈Υ do
16
ˆΓ∞(µe) ←αinfm∈M ˆΓ
m
∞(µe) + (1 −α)supm∈M ˆΓ
m
∞(µe);
17
ˆΓ∞(µe) ←αinfm∈M ˆΓ
m
∞(µe) + (1 −α)supm∈M ˆΓ
m
∞(µe);
18
˜α ←TUNE(α,ϵ);
19
ˆΓ∞(µe) ←˜α ˆΓ∞(µe) + (1 −˜α) ˆΓ∞(µe);
20 ˆµe∗←argmaxµe∈Υ ˆΓ∞(µe);
21 ˆΓ∞(ˆµe∗) ←maxµe∈Υ ˆΓ∞(µe);

````

## PDF page 44; PDF label ec4

FORMULA CHECK REQUIRED: original PDF page 44.

````text
ec4
e-companion to Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
Algorithm 4: SAV-Learning-BUC
1 for each observed trajectory and model m ∈M do
2
Initialize πm
0 using a random draw from F(π);
3
set t=1;
4
while t + 1 ∈T do
5
πm
t+1 ←T(πm
t ,at,ot,m);
6 for any given µe ∈Υ and m ∈M do
7
φm,µe
n
(ψ) ←EP
"
P
t∈T

κm
t
µe(At|Πm
t )
µb(At|Πm
t )
h
Gt + β V
m,µe
∞
(T(Πm
t ,At,Ot,m)) −V
m,µe
∞
(Πm
t )
i
b(Πm
t )
#
;
8
φm,µe
n
(ψ) ←EP
"
P
t∈T

κm
t
µe(At|Πm
t )
µb(At|Πm
t )
h
Gt + β V m,µe
∞
(T(Πm
t ,At,Ot,m)) −V m,µe
∞
(Πm
t )
i
b(Πm
t )
#
;
9
ˆψ
m,µe
n
←argminψ∈Ψ
 φm,µe
n
(ψ)
′ Ωφm,µe
n
(ψ) + θnP(ψ)

;
10
ˆψ
m,µe
n
←argminψ∈Ψ
 φm,µe
n
(ψ)
′ Ωφm,µe
n
(ψ) + θnP(ψ)

;
11 for any given µe ∈Υ do
12
m1 ←arginfm∈M || ˆψ
m,µe
n
||;
13
m1 ←argsupm∈M || ˆψ
m,µe
n
||;
14
m2 ←arginfm∈M || ˆψ
m,µe
n
||;
15
m2 ←argsupm∈M || ˆψ
m,µe
n
||;
16
ˆψ
µe
n ←α ˆψ
m1,µe
n
+ (1 −α) ˆψ
m1,µe
n
;
17
ˆψ
µe
n ←α ˆψ
m2,µe
n
+ (1 −α) ˆψ
m2,µe
n
;
18
ˆV
µe
∞(π) ←
 b(π))′ ˆψ
µe
n ;
19
ˆV
µe
∞(π) ←
 b(π))′ ˆψ
µe
n ;
20
ˆΓ∞(µe) ←
R ˆV
µe
∞(π)dF(π);
21
ˆΓ∞(µe) ←
R ˆV
µe
∞(π)dF(π);
22
˜α ←TUNE(α,ϵ);
23
ˆΓ∞(µe) ←˜α ˆΓ∞(µe) + (1 −˜α) ˆΓ∞(µe);
24 ˆµe∗←argmaxµe∈Υ ˆΓ∞(µe);
25 ˆΓ∞(ˆµe∗) ←maxµe∈Υ ˆΓ∞(µe);
Online Appendix D: Additional Figures
DAV-Learning
SAV-Learning
maximax values
maximin values
0.0
0.2
0.4
0.6
0.8
1.0
0
10
20
30
40
α
Improvement (%)
Figure EC.1
Percentage improvement over the observed regime (synthetic data analyses with β = 0.95). Error bands for
both approaches, and especially for the SAV-Learning approach, are very tight (hence, not depicted).

````

## PDF page 45; PDF label ec5

FORMULA CHECK REQUIRED: original PDF page 45.

````text
e-companion to Soroush Saghafian: Ambiguous Dynamic Treatment Regimes
ec5
DAV-Learning-BUC
SAV-Learning-BUC
maximax values
maximin values
0.0
0.2
0.4
0.6
0.8
1.0
0
2
4
6
8
10
α
Improvement (%)
Figure EC.2
Percentage improvement over the observed regime (synthetic data analyses with β = 0.95 and ηm
t = 1.02 for
all t ∈T and m ∈M ).
DAV-Learning
SAV-Learning
minimum loss
maximax values
maximin values
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.5
1.0
1.5
2.0
α
Gain Loss (%)
Figure EC.3
Percentage Gain Loss of DAV-Learning and SAV-Learning (Synthetic Data Analyses with β = 0.95). Minimum
loss is obtained for a mid level value of the pessimism level (α = 0.25).
DAV-Learning-BUC
SAV-Learning-BUC
maximin values
minmum loss
maximax values
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.5
1.0
1.5
2.0
α
Gain Loss (%)
Figure EC.4
Percentage Gain Loss of DAV-Learning-BUC and SAV-Learning-BUC (Synthetic Data Analyses with β = 0.95
and ηm
t = 1.02 for all t ∈T and m ∈M ). Minimum loss is obtained for a mid level value of the pessimism
level (α = 0.25). Results are based on ϵ-approximations for a small ϵ (see the discussion in Section 6))

````

