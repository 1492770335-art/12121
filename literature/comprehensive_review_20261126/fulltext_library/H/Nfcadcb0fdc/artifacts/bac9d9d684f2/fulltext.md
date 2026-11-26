# A Path‐Specific Effect Approach to Mediation Analysis With Time‐Varying Mediators and Time‐to‐Event Outcomes Accounting for Competing Risks

Original PDF: [original.pdf](original.pdf). SHA256: `bac9d9d684f2bc1b8ee39a6cbb6c900eb869a4cb8ac193785c72d7c44574d16c`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
A path-specific effect approach to mediation analysis with time-varying mediators and 
time-to-event outcomes accounting for competing risks 
 
Arce Domingo-Relloso,1,2 Yuchen Zhang,1 Ziqing Wang,1 Astrid M Suchy-Dicey,3 Dedra S 
Buchwald,4 Ana Navas-Acien,2 Joel Schwartz,5 Kiros Berhane,1 Brent A. Coull,6 Linda Valeri1,7 
 
1 Department of Biostatistics, Columbia University Mailman School of Public Health, New York, 
NY 
2 Department of Environmental Health Sciences, Columbia University Mailman School of Public 
Health, New York, NY 
3 Huntington Medical Research Institutes, Pasadena, CA 
4 Neurosciences Institute, Department of Neurological Surgery, University of Washington, 
Seattle, WA 
5 Department of Environmental Health Sciences, Harvard TH Chan School of Public Health, 
Cambridge, MA 
6 Department of Biostatistics, Harvard TH Chan School of Public Health, Boston, MA 
7 Department of Epidemiology, Harvard TH Chan School of Public Health, Boston, MA 
 
 
 
 
 

````

## PDF page 2

Technical extraction; compare with original PDF page 2.

````text
Abstract 
Not accounting for competing events in survival analysis can lead to biased estimates, as 
individuals who die from other causes do not have the opportunity to develop the event of 
interest. Formal definitions and considerations for causal effects in the presence of competing 
risks have been published, but not for the mediation analysis setting. We propose, for the first 
time, an approach based on the path-specific effects framework to account for competing risks in 
longitudinal mediation analysis with time-to-event outcomes. We do so by considering the 
pathway through the competing event as another mediator, which is nested within our 
longitudinal mediator of interest. We provide a theoretical formulation and related definitions of 
the effects of interest based on the mediational g-formula, as well as a detailed description of the 
algorithm. We also present an application of our algorithm to data from the Strong Heart Study, a 
prospective cohort of American Indian adults. In this application, we evaluated the mediating 
role of the blood pressure trajectory (measured during three visits) on the association between 
arsenic and cadmium, in separate models, with time to cardiovascular disease, accounting for 
competing risks by death. Identifying the effects through different paths enables us to evaluate 
the impact of metals on the outcome of interest, as well as through competing risks, more 
transparently. 
 
Keywords: mediation analysis, longitudinal data, competing risks, g-formula, survival analysis, 
path-specific effects 
 

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
1. Introduction 
In survival settings, competing events refer to any event that makes it impossible for the event of 
interest to occur. For example, death is a competing event for any other event, as when an 
individual dies, he/she cannot experience any further events. Not accounting for competing 
events in survival analysis can lead to biases caused by the fact that individuals that die from 
other causes do not have the opportunity to develop the event of interest (1). This has been 
clearly shown, for example, in the context of aging-related diseases, such as dementia. As 
reported in Rojas-Saunero et al. (2), counterintuitive findings have been observed when factors 
such as smoking (3) or cancer history (3) showed protective effects against dementia when 
ignoring death. This does not mean that those factors are protective of the dementia disease but 
because smokers and cancer patients tend to die earlier, this premature mortality makes them less 
likely to develop dementia. There is urgent need to develop new frameworks to effectively 
acknowledge competing risks, and to report causal effects that would take their potential impact 
into account. 
Various statistical estimands have been proposed for competing risks in failure-time 
settings including marginal cumulative incidence, cause-specific cumulative incidence, marginal 
hazard, sub-distribution hazard and cause-specific hazard (4). However, Young et al. (5) was the 
first paper to present a formal definition of causal effects in the presence of competing risks 
using counterfactuals. In this paper, the authors describe two different estimands that can be 
considered in the presence of competing risks: the direct effect, defined as the risk under 
elimination of competing events, and the total effect, defined as the risk without elimination of 
competing events. Martinussen and Stensrud (6) propose to address the issue of competing 

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
events by considering a hypothetical scenario in which we have two separable treatments, the 
first only affects the event of interest and the second only affects the competing event. 
In this work, we propose a framework for the causal mediation setting in presence of 
mediators measured repeatedly over time. We do this by considering the competing event as an 
additional mediator that is affected by past values of the mediator of interest (i.e. is nested with 
our mediator of interest), and in turn affects future values of both the mediator of interest and the 
outcome deterministically. This path specific effect structure has previously been described in 
the literature in the context of nested mediators (i.e. not in the context of competing risks) (7), 
but the authors did not consider time-varying nested mediators in that work. One of the key 
differences between our approach and previously considered approaches to deal with competing 
events is that we do not consider the framework in which causal effects are calculated under 
elimination of the competing event nor a framework in which the exposure can be separated into 
components that only affect the terminal event, as these scenarios are not realistic in many 
settings in which competing events by death simply cannot be eliminated or separated.  
The paper is organized as follows: in section 2, we introduce the data structure and notation 
related to our causal setting. In section 3, we introduce the counterfactual estimands of causal 
mediation analysis in the presence of competing events. In section 4, we describe the 
identifiability assumptions. Section 5 describes the estimation of the effects. Section 6 is a full 
description of our algorithm. Section 7 includes an application of the approach to the analysis of 
the Strong Heart Study, a prospective cohort study of American Indian adults. This analysis 
evaluated the potential mediated effect of blood pressure on the association between metals and 

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
cardiovascular disease incidence, accounting for competing events by death. Last, section 8 
includes discussion. 
2. Data structure and notation 
Consider 𝑖 = 1,… , 𝑛 individuals exposed to different levels of a continuous exposure 𝐴 at 
baseline. Individuals are assumed to be independent and identically distributed. Let 
Mi1,…,MiK denote longitudinal measurements of a mediator for the 𝑖-th individual at visits 
1,… ,𝐾. For simplicity, we denote this vector as M1,…,MK hereinafter. In addition, let 𝐿0 
represent a vector of baseline covariates, and 𝑌𝑘, 𝐷𝑘 and 𝑆𝑘 denote indicators of the event of 
interest (e.g., cardiovascular disease), a competing event (e.g., death from all causes) and 
survival by time interval 𝑘, respectively. Our causal framework is depicted in the directed 
acyclic graph shown in Figure 1, provided for 𝐾= 3 even though it could easily be extended to 
allow for more visits. By definition, 𝐷0 ≡ 𝑌0 ≡ 0 and 𝑆0 ≡ 1, because the study population is 
restricted to those who have not yet experienced the event of interest or the competing event at 
baseline. We assume, without loss of generality, the temporal ordering (𝐴, 𝑀𝑘, 𝐷𝑘, 𝑆𝑘, 𝑌𝑘) within 
each follow-up visit 𝑘 > 0. For simplicity, we also assume that all variables are measured 
without error. 
Figure 1. Directed Acyclic Graph for 𝐾= 3. 

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
 
𝐴 represents the exposure, 𝐿0 represents a vector of baseline confounders, 𝑀 is the mediator measured at 
three time points (𝑀1, 𝑀2, 𝑀3), 𝐷 is the competing risk indicator measured at three time points 
(𝐷1, 𝐷2, 𝐷3) and 𝑌 is the time-to-event outcome. Please note there is no arrow from 𝑀1 and 𝑀2 to 𝐷3, 
from 𝑀1 to 𝑀3, from 𝑀1 to 𝐷2 and from 𝐷1 to 𝐷3 because we assume that our process is Markovian and 
therefore each longitudinal value of 𝑀 and 𝐷 is only affected by immediately prior values of 𝑀 and 𝐷. 
This assumption can be relaxed within the proposed approach. 
 
Following the notation used in Young et al. (5), we denote the history of a random variable 
using overbars, e.g., 𝑀̅𝑘= (𝑀1,… , 𝑀𝑘) is the history of the mediator of interest through interval 
𝑘. Note that, if an individual is known to experience the competing event by visit 𝑘 > 0 without 
having experienced the event of interest (𝑌𝑘−1 = 0,𝐷𝑘 = 1), then all future indicators of the 
event of interest will be observed and will be deterministically zero because, by definition, 
individuals that experience the competing event cannot experience the event of interest. 
Following Figure 1, the competing event indicator at a certain time point 𝑘 (𝐷𝑘) can be 
considered as another mediator which is nested within the vector of mediators 𝑀, in the sense 
that it is influenced by past values of the mediator of interest and in turn influences future values 
of the mediator of interest (in a deterministic way, because if an individual dies, the mediator is 
death-truncated). 

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
3. Counterfactual estimands of causal mediation analysis in presence of competing 
events 
We used the Lin-Ying additive hazards model (8), a special case of the Aalen additive hazards 
model with time-invariant coefficients, to model our time-to-event outcome. This model allows 
us to define our counterfactual outcome in terms of absolute attributable risks, but also in terms 
of survival probability. The additive hazards model has been described in the context of 
mediation analysis in previous work (9). For times 𝑘= 0,… , 𝐾, consider the counterfactual 
history of the mediator of interest 𝑀̅𝑘+1(𝑎, 𝑆̅𝑘(𝑎)), which refers to the value the history of the 
mediator would take had the individual, possibly contrary to fact, been exposed to 𝐴= 𝑎 and to 
the survival status 𝑆̅𝑘(𝑎). Consider also the counterfactual history of the survival status 
𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎)), and the counterfactual outcomes 𝛾(𝑎, 𝑀̅𝑘+1(𝑎, 𝑆̅𝑘(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))), which 
refers to the number of cases attributable to the exposure per a number of person-years (typically 
set to 10,000 or 100,000) at time 𝑘; and 𝑃(𝑌𝑘+1 (𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎,𝑀̅𝑘(𝑎))) = 0), which 
refers to the probability of being free of the outcome at time 𝑘+ 1. 
We propose to decompose our causal mediation effects of interest in a path-specific 
effects approach to account for competing risks. Therefore, we define, for certain levels 𝑎 and 𝑎∗ 
of the exposure of interest, the following path-specific effects on the rate difference, as well as 
survival probability difference, scales: 
 
1) Direct effect of the exposure on the outcome (DE): effect that operates neither through 
mortality nor through the longitudinal mediator of interest 𝑀 (see Supplementary Figure 
1). 

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
𝛾(𝑎∗, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))) −𝛾(𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))), 
being 𝛾 the rate obtained from an additive hazards model, and 
𝑃(𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))) = 0)
−𝑃(𝑌𝑘+1 (𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))) = 0), 
 
2) Indirect effect through the history of the mediator of interest (IEM), when the death 
process behaves under the reference level of exposure (Supplementary Figure 2). 
𝛾(𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎∗))) −𝛾(𝑎∗,𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))), or 
𝑃(𝑌𝑘+1 (𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎∗))) = 0)
−𝑃(𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))) = 0) 
 
This is the effect that operates by impacting the mediator of interest directly, which in turn might 
impact the outcome (i) directly or (ii) via the mortality process. Please note that separating (i) 
and (ii) is impossible unless we make additional modeling (parametric) assumptions (see 
Discussion section). 
 
3) Indirect effect through the history of the competing event (IED): effect that operates by 
impacting the death process directly, which has a deterministic relationship with the 
mediator of interest and the outcome, in the sense that the mediator is unobserved, and 
the outcome does not happen, if death happens before (Supplementary Figure 3). 
𝛾(𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))) −𝛾(𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎∗))), or 
𝑃(𝑌𝑘+1 (𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))) = 0)
−𝑃(𝑌𝑘+1 (𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎∗))) = 0) 

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
 
4) Total effect (TE): 
𝛾(𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))) −𝛾(𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎,𝑀̅𝑘(𝑎))), or 
𝑃(𝑌𝑘+1 (𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))) = 0)
−𝑃(𝑌𝑘+1 (𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))) = 0) 
 
Sum of direct effect and indirect effect through the mediator of interest (Supplementary Figure 
4): 
 
𝛾(𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎∗))) −𝛾(𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))), or 
𝑃(𝑌𝑘+1 (𝑎∗,𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎∗))) = 0)
−𝑃(𝑌𝑘+1 (𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)), 𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))) = 0) 
Please note that the sum of the three path-specific effects leads to the total effect: 
𝑇𝐸= 𝐷𝐸+ 𝐼𝐸𝑀+ 𝐼𝐸𝐷 
For the rate difference, the effects can be identified using the estimated coefficients of the 
additive hazards model. The survival probability is calculated using the predict() function of the 
timereg R package, fixing a certain time point.  
Also note that our definition of the total effect, 𝔼(𝑌𝑘+1(𝑎∗, 𝑆̅𝑘(𝑎∗))) − 𝔼(𝑌𝑘+1(𝑎, 𝑆̅𝑘(𝑎))), is 
different than the definition of the total effect in traditional analysis that considers death as a 
censoring event, 𝔼(𝑌𝑘+1(𝑎∗)|𝑆̅𝑘= 1) − 𝔼(𝑌𝑘+1(𝑎)|𝑆̅𝑘= 1), in the sense that the traditional total 
effect calculates the effect conditioning on survival up to time 𝑘, whereas the total effect 
accounting for competing risks calculates the effect when setting survival to the level it would 
take at the level of exposure 𝑎 versus 𝑎∗. Conversely, the sum of the direct effect and the indirect 

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
effect through M, 𝔼(𝑌𝑘+1(𝑎∗, 𝑆̅𝑘(𝑎)) −𝔼(𝑌𝑘+1(𝑎, 𝑆̅𝑘(𝑎)), does not condition on survival, but sets 
survival to the level it would take under the reference level of exposure. The differences between 
these effects are also illustrated in our analysis of the Strong Heart Study data in section 8. 
 
4. Identifiability assumptions 
The following assumptions need to be fulfilled for the effects described in the previous section to 
be identifiable. 
4.1. 
Exchangeability 
4.1.1. No unmeasured confounding of the relationship between the exposure and the history 
of the outcome:   𝑌̅𝑘+1(𝑎, 𝑚̅, 𝑠̅ = 1) ⊥𝐴|𝐿0. 
4.1.2. No unmeasured confounding of the relationship between the history of the mediator 
and both the outcome and the survival status at time 𝑘+ 1:   (𝑌𝑘+1(𝑎∗,𝑠̅𝑘=
1,𝑚̅𝑘), 𝑆̅𝑘(𝑎∗, 𝑚̅𝑘)) ⊥𝑀̅𝑘|𝐴, 𝐶, 𝐿0. 
4.1.3. No unmeasured confounding of the relationship between the mediator of interest and 
the survival status at each time point: 𝑆̅𝑘+1(𝑎, 𝑚̅) ⊥𝑀̅𝑘+1(𝑎, 𝑠̅ = 1)|𝐴= 𝑎, 𝑀̅𝑘=
𝑚̅𝑘, 𝑌̅𝑘= 0,𝑆̅𝑘= 1,𝐿0. 
4.1.4. No unmeasured confounding of the relationship between the history of the mediator 
and the exposure: 𝑀̅𝑘+1(𝑎, 𝑠̅ = 1) ⊥𝐴| 𝐿0,𝑌̅𝑘= 0, 𝑆̅𝑘= 1. 
4.1.5. No unmeasured confounding of the relationship between the history of the competing 
event and the exposure: 𝑆̅𝑘+1(𝑎, 𝑚̅) ⊥𝐴| 𝐿0,𝑌̅𝑘= 0, 𝑆̅𝑘= 1. 

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
4.1.6. Cross-world assumption: no confounders of the mediators-outcome relationship 
affected by the exposure.   𝑌𝑘+1(𝑎, 𝑚̅, 𝑠̅ = 1) ⊥(𝑀̅𝑘(𝑎∗,𝑠̅ = 1),𝑆̅𝑘(𝑎∗, 𝑚̅))|𝑌̅𝑘=
0,𝑆̅𝑘−1 = 1, 𝐴= 𝑎, 𝐿0. 
Please note that the cross-world assumption would be violated if time-varying confounders 
exist. However, our approach can be extended to the setting in which we can consider time-
varying confounders by adding an additional path to the path specific effects involving the time-
varying confounder (see the discussion section). 
 
4.2. 
Positivity: 𝑃(𝐴= 𝑎|𝐿0 = 𝑙0) > 0, and 
𝑃(𝑀̅𝑘+1 = 𝑚̅𝑘+1, 𝑆̅𝑘+1 = 𝑠̅𝑘+1|𝐴= 𝑎, 𝐿0 = 𝑙0, 𝑌̅𝑘= 0, 𝑆̅𝑘= 1) > 0, ∀𝑘= 1,… , 𝐾. 
4.3. 
Consistency: If 𝐴= 𝑎 and 𝑆𝑘= 1, then, 𝑀̅𝑘+1 = 𝑀̅𝑘+1(𝑎, 𝑠̅ = 1), 𝑆𝑘+1 =
𝑆̅𝑘+1(𝑎, 𝑚̅),  𝑌̅𝑘+1 = 𝑌̅𝑘+1(𝑎, 𝑚̅, 𝑠̅ = 1). 
We additionally assume the stable unit treatment value assumption, i.e., that there is no 
interference across units. 
Under these identifiability conditions, the expected value of the outcome at time 𝑘+ 1, 
𝔼[𝑌𝑘+1(𝑎, 𝑀̅𝑘, 𝑆̅𝑘)] is identified by the following function of the observed data: 
𝜙(𝑎, 𝑎, 𝑎) = ∫𝔼(𝑌𝑘+1|𝐴= 𝑎, 𝑆̅𝑘= 1,𝑀̅𝑘= 𝑚̅𝑘, 𝐶= 𝑐)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1,𝐶= 𝑐)𝑑𝑚̅𝑘 
 
This expression is called the mediational g-formula (10–12). 
 
 

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
5. Effect estimation 
Our path-specific effects, as described in section 3, can be computed using the mediational g-
formula: 
1) Direct effect of the exposure on the outcome: 
𝜙(𝑎∗, 𝑎, 𝑎) − 𝜙(𝑎, 𝑎, 𝑎)
= ∫𝔼(𝑌𝑘+1|𝐴= 𝑎∗, 𝑆̅𝑘= 1,𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐) 𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1| 𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐶= 𝑐) 𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1, 𝐶= 𝑐)𝑑𝑚̅𝑘
−∫𝔼(𝑌𝑘+1|𝐴= 𝑎, 𝑆̅𝑘= 1,𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐶= 𝑐)𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1, 𝐶= 𝑐)𝑑𝑚̅𝑘 
 
2) Indirect effect through the history of the mediator of interest: 
𝜙(𝑎∗, 𝑎∗, 𝑎∗) − 𝜙(𝑎∗, 𝑎∗,𝑎)
= ∫𝔼(𝑌𝑘+1|𝐴= 𝑎∗, 𝑆̅𝑘= 1, 𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎∗, 𝑆̅𝑘−1 = 1, 𝐶= 𝑐)𝑑𝑚̅𝑘
−∫𝔼(𝑌𝑘+1|𝐴= 𝑎∗, 𝑆̅𝑘= 1,𝑀̅𝑘= 𝑚̅𝑘, 𝐶= 𝑐)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1,𝐶= 𝑐)𝑑𝑚̅𝑘 
 
3) Indirect effect through the history of the competing event: 

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
𝜙(𝑎∗, 𝑎∗,𝑎) − 𝜙(𝑎∗, 𝑎, 𝑎)
= ∫𝔼(𝑌𝑘+1|𝐴= 𝑎∗, 𝑆̅𝑘= 1, 𝑀̅𝑘= 𝑚̅𝑘, 𝐶= 𝑐)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐶= 𝑐)𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎,𝑆̅𝑘−1 = 1, 𝐶= 𝑐)𝑑𝑚̅𝑘
−∫𝔼(𝑌𝑘+1|𝐴= 𝑎∗,𝑆̅𝑘= 1, 𝑀̅𝑘= 𝑚̅𝑘, 𝐶= 𝑐)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1,𝐶= 𝑐)𝑑𝑚̅𝑘 
 
4) Total effect: 
𝜙(𝑎∗, 𝑎∗, 𝑎∗) − 𝜙(𝑎, 𝑎, 𝑎)
= ∫𝔼(𝑌𝑘+1|𝐴= 𝑎∗, 𝑆̅𝑘= 1, 𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎∗, 𝑆̅𝑘−1 = 1, 𝐶= 𝑐)𝑑𝑚̅𝑘
−∫𝔼(𝑌𝑘+1|𝐴= 𝑎, 𝑆̅𝑘= 1, 𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐶= 𝑐)𝑓(𝑀̅𝑘= 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1,𝐶= 𝑐)𝑑𝑚̅𝑘 
 
The proofs of these expressions are presented in the Supplementary Material. 
 
6. Mediational g-formula algorithm with time-varying mediators and competing risks 
by death 
Based on the DAG presented in Figure 1, our mediational g-formula algorithm proceeds as 
follows: 
1. Choose two exposure values 𝑎 and 𝑎∗ (for example, percentiles 25th and 75th) 
2. Fit sequential parametric linear and logistic regression models, respectively, for each time 
point 𝑘= 1, … ,𝐾 for both 𝑀 and 𝐷: 𝑀𝑘 ~ 𝑀𝑘−1 + 𝐴+ 𝐿0,  𝐷𝑘 ~ 𝑀𝑘+ 𝐴+ 𝐿0. 

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
3. Fit a parametric time-to-event additive hazards model for the outcome 𝑌 using a counting 
process format (13) to adjust for 𝑀 in all time points: 𝑌 ~ 𝑀+ 𝐴+ 𝐿0. We use the 
tmerge function from the survival R package to transform the database to a counting 
process format, and the timereg R package to fit a Lin-Ying additive hazards model. 
4. Predict the counterfactual values of 𝑀𝑘 and 𝐷𝑘 for each iteration and each time point 𝑘: 
𝑀𝑘(𝑎) = 𝑀𝑘(𝑎, 𝑀𝑘−1(𝑎),𝐷𝑘−1(𝑎)); 𝑀𝑘(𝑎∗) = 𝑀𝑘(𝑎∗,𝑀𝑘−1(𝑎∗),𝐷𝑘−1(𝑎∗)); 
𝑀𝑘(𝑎, 𝑎∗) = 𝑀𝑘(𝑎, 𝑀𝑘−1(𝑎),𝐷𝑘−1(𝑎∗)), and 𝐷𝑘(𝑎) = 𝐷𝑘(𝑎,𝑀𝑘(𝑎), 𝐷𝑘−1(𝑎)); 
 𝐷𝑘(𝑎∗) = 𝑀𝑘(𝑎∗, 𝑀𝑘(𝑎∗),𝐷𝑘−1(𝑎∗)); 𝐷𝑘(𝑎∗, 𝑎) = 𝐷𝑘(𝑎∗, 𝑀𝑘−1(𝑎),𝐷𝑘−1(𝑎∗)). 
The death status of each participant is predicted by generating random values from a 
binomial distribution with the predicted probabilities of the logistic regression model. 
Thus, different individuals will be predicted to die/survive for different counterfactual 
scenarios. 
5. Predict the counterfactual values of the outcome 𝑌: 
• 𝑌(𝑎) = 𝑌(𝑎, 𝑀̅(𝑎, 𝐷̅(𝑎)),𝐷̅(𝑎, 𝑀̅(𝑎))) 
• 𝑌(𝑎∗) = 𝑌(𝑎∗, 𝑀̅(𝑎∗,𝐷̅(𝑎∗)), 𝐷̅(𝑎∗, 𝑀̅(𝑎∗))) 
• 𝑌(𝑎∗, 𝑀̅(𝑎),𝐷̅(𝑎)) = 𝑌(𝑎∗, 𝑀̅(𝑎, 𝐷̅(𝑎)),𝐷̅(𝑎, 𝑀̅(𝑎))) 
• 𝑌(𝑎∗, 𝑀̅(𝑎, 𝑎∗), 𝐷̅(𝑎∗,𝑎)) = 𝑌(𝑎∗, 𝑀̅(𝑎,𝐷̅(𝑎∗)), 𝐷̅(𝑎∗, 𝑀̅(𝑎))). 
6. Calculate the effects of interest for each iteration: 
• Direct effect: 𝔼[𝑌(𝑎∗, 𝑀(𝑎), 𝐷(𝑎))] − 𝔼[𝑌(𝑎)]. 
• Indirect effect through M: 𝔼[𝑌(𝑎∗)] −𝔼[𝑌(𝑎∗, 𝑀(𝑎,𝑎∗),𝐷(𝑎∗, 𝑎))]. 
• Indirect effect through D: 𝔼[𝑌(𝑎∗,𝑀(𝑎, 𝑎∗), 𝐷(𝑎∗, 𝑎))] −𝔼[𝑌(𝑎∗, 𝑀(𝑎), 𝐷(𝑎))]. 

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
• Total effect: 𝔼[𝑌(𝑎∗)] −𝔼[𝑌(𝑎)]. 
 
7. Use a quantile bootstrap procedure to calculate confidence intervals. Take the 50th 
percentile as the effect of interest, and the 2.5th and 97.5th percentiles as the 95 % lower 
and upper confidence intervals. 
 
Please note that we make a Markovian assumption and only adjust each model for the mediator 
in the preceding time point to avoid multicollinearity. These assumptions can be relaxed, if 
needed. Our models allow for exposure-mediator interactions and for non-linear effects. 
 
7. Application: metals, blood pressure and cardiovascular disease in the Strong Heart 
Study 
We evaluated the potential mediating role of the systolic blood pressure trajectory on the 
association between arsenic and cadmium (in separate models) and incident CVD, accounting for 
competing risks by death. Both arsenic and cadmium have shown to be associated with elevated 
blood pressure (14,15) and with incident CVD (16,17) in the SHS. 
 
Study population: the Strong Heart Study 
A total of 4,549 men and women aged 45-74 years were recruited for the SHS from 13 American 
Indian tribes across three study centers in South Dakota, North Dakota, Oklahoma and Arizona 
with baseline visits occurring between 1989 and 1991 (18). In 2016, one tribal community 
(N=1,033) withdrew consent to use their data for research, leaving 3,516 participants. Among the 
remaining participants, baseline urine samples were analyzed for participants who had sufficient 

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
urine samples for analysis and who were free of diabetes and cardiovascular disease at baseline. 
After removing missing values in all covariates, 2,925 participants were included in this analysis. 
 
Demographic and lifestyle assessment: Baseline sociodemographic, lifestyle and anthropometric 
information were obtained through interview and physical examination. The standardized in-
person questionnaire included sociodemographic data (age, sex, BMI) and smoking status (never, 
current, former). Estimated glomerular filtration rate (eGFR), which measures kidney function 
and might be associated with urinary metal concentrations, was estimated from recalibrated 
plasma creatinine, age, and sex using the Chronic Kidney Disease – Epidemiology Collaboration 
formula (19). 
 
Arsenic and cadmium measurements: Metal concentrations were determined using spot urine 
samples collected at the SHS baseline visit (1989-1991). Metals were measured by inductively 
coupled plasma mass spectrometry (ICP-MS) at the Trace Element Laboratory of University of 
Graz, Austria. Inorganic arsenic, monomethylarsonate, dimethylarsinate and arsenobetaine and 
other arsenic cations were also measured by coupling high performance liquid chromatography 
(HPLC) and ICP-MS. Arsenic exposure refers to the sum of inorganic and methylated As 
species. Metal concentrations were corrected by creatinine and log-transformed for analyses. 
 
Cardiovascular disease incidence follow-up: The endpoints of this study are fatal and non-fatal 
CVD, which were assessed during the follow-up by annual mortality and morbidity surveillance 
of medical records. Medical records were reviewed and a central adjudication system with two or 
more physicians was used to classify any potential cardiovascular event (20). Mortality 

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
surveillance examined death certificates from state health departments, records from the Indian 
Health Service, autopsy and coroner’s reports, and interviews with physicians or family 
members. Incident CVD was defined as the first occurrence of fatal or nonfatal coronary heart 
disease, stroke or congestive heart failure, or other nonfatal CVD. CVD mortality was defined as 
any fatal CVD. The follow-up time was calculated as the time from urinary sample collection 
(1989-1991) to the time for CVD events (through 2009, as metal exposure in the tribes changed 
after the implementation of the EPA Final Arsenic Rule (21)). For participants who did not 
develop incident CVD, follow-up was censored at the time of occurrence of non-CVD death, loss 
to follow-up, or the last day of follow-up.  
 
Blood pressure measurements: Participants fasted for 12 hours or more before the physical 
examination. Brachial artery blood pressure (first and fifth Korotkoff sounds) was measured 
three consecutive times on seated participants after they had rested 5 minutes with the use of a 
mercury sphygmomanometer (WA Baum Co) (22). An appropriately sized cuff was placed on the 
right arm, pulse occlusion pressure was determined, and the cuff was inflated to 20 mm Hg 
above that pressure. The mean of the last two of these measurements was used for estimation of 
blood pressure. Systolic blood pressure was measured at three time points: visit 1 (1989-1991), 
visit 2 (1993-1995) and visit 3 (1998-1999). 
 
Statistical Analysis 
We used MICE imputation (23) to impute 605 missing values in systolic blood pressure in the 
second visit and 890 missing values in the third visit, based on the values of the other visits. We 
ran the mediational g-formula algorithm to evaluate the potential mediating role of blood 

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
pressure (measured in three visits) on the association between both cadmium and arsenic (in 
separate models) and incident CVD, accounting for competing risks by death introducing death 
as another mediator. To do so, we created a death indicator for each visit (between baseline and 
the second visit, between the second and the third visit, and between the third visit and the end of 
follow-up), which we used as the outcome to fit parametric logistic models. From those models, 
we obtained the probability of dying by that visit using random sampling from the binomial 
distribution. All models were adjusted for the metal of interest, age, sex, smoking status, BMI 
and estimated glomerular filtration rate. Thus, we had two sets of mediator models: 
 
1. Models of the mediator of interest (blood pressure) in each visit. These models were 
adjusted for blood pressure in the previous visit. 
2. Models of the competing risk indicator (death) in each visit. These models were adjusted 
for blood pressure in the same visit. 
 
To fit the outcome model, we used the counting process format (24), in which each individual 
contributes several rows to the database (one row per time interval, until the event happens). This 
format can be used in survival analysis without additional specifications and appropriately 
adjusts for time-varying confounders (25). We used a semi-parametric additive hazards model 
with CVD incidence as the outcome, adjusted for the metal of interest, blood pressure (in all 
visits), age, sex, smoking status, BMI and estimated glomerular filtration rate. 
We ran the mediational g-formula algorithm with 1000 bootstrap iterations, comparing 
the metals’ 75th percentile to their 25th percentile. We thus have four effects of interest: 

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
• Total effect: number of CVD cases per 100,000 person-years, or probability of not 
developing CVD after 20 years, attributable to an IQR change in each metal 
concentration. 
• Direct effect: number of CVD cases per 100,000 person-years, or probability of not 
developing CVD after 20 years, attributable to an IQR change in each metal 
concentration not operating through the blood pressure or death pathways. 
• Indirect effect through blood pressure (the mediator of interest): number of CVD 
cases per 100,000 person-years, or probability of not developing CVD after 20 years, 
attributable to an IQR change in each metal concentration that occur through the 
blood pressure trajectory either causing CVD or causing death (which would make it 
impossible for CVD to occur). Please note that this pathway can operate through 
death only through changes in the mediator of interest, not through direct changes in 
death resulting from changes in the exposure. 
• Indirect effect through death (the competing event): number of CVD cases per 
100,000 person-years, or probability of not developing CVD after 20 years, 
attributable to an IQR change in each metal concentration avoided by the fact that the 
individual died before the CVD event happening. Please note that this pathway can 
operate through death only through changes in the exposure, not through changes in 
the mediator of interest. 
 
For comparative purposes, we are also interested in the following effects: 
• Sum of the direct effect and the indirect effect through blood pressure: number of CVD 
cases per 100,000 person-years, or probability of not developing CVD after 20 years, 

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
attributable to an IQR change in each metal concentration that occur through the blood 
pressure trajectory fixing the survival status to the value it would take under the reference 
level of the exposure (25th percentile). 
• Direct, indirect and total effects conditional on survival: effects that are traditionally 
calculated in mediation analysis, not accounting for competing risks. 
 
Results 
Participant characteristics are shown in Table. There were 977 CVD cases. Participants who had 
a CVD event were older, more likely to be current smokers, had higher SBP levels and both 
urinary arsenic and cadmium concentrations. Table 2 shows the results of the longitudinal 
mediation analysis for arsenic, both without accounting for competing risks (i.e., not taking into 
account the pathway through death for other causes different to CVD) and accounting for 
competing risks. Results are presented both in differences in hazards and survival probability 
differences. Of 345 CVD cases attributable to an interquartile range increase in log-arsenic 
exposure, 45 would happen through the blood pressure trajectory, and 26 CVD cases would be 
avoided by the participant dying from other causes before having the chance to develop CVD per 
100,000 person-years. For the difference in hazards, the indirect effect through blood pressure is 
statistically significant when not accounting for competing risks, but it is not when accounting 
for competing risks, as the confidence intervals become much wider. It is, however, statistically 
significant in the survival probability difference scale. The total effect is statistically significant 
but attenuated when accounting for competing risks, as this estimator takes into account the 
CVD cases that are not allowed to happen given that the individual dies before, and is not, 
therefore, in the risk set. 

````

## PDF page 21

Technical extraction; compare with original PDF page 21.

````text
Table 3 shows the results for cadmium. Of 137 CVD cases attributable to a interquartile 
range increase in log-cadmium exposure, of which, 14 would happen through the blood pressure 
trajectory, and 22 CVD cases would be avoided by the participant dying before having the 
chance to develop CVD. We see no statistically significant indirect effect in the hazard difference 
scale, regardless of accounting or not for competing risks. For the survival probability difference 
scale, the indirect effect is not statistically significant after accounting for competing risks. The 
total effect is not statistically significant and is attenuated when accounting for competing risks. 
The indirect effect through death has an impact on the total effect but is not statistically 
significant for either cadmium or arsenic. 
 
 

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
8. Discussion 
In this work, we developed an extension of the mediational g-formula which can deal with 
competing events. This is, to our knowledge, the first method that incorporates competing events 
to the mediation analysis setting using the path-specific effects framework. Our algorithm reports 
effects in terms of attributable cases per a number of person-years, which is a measure of public 
health impact, and also in the survival probability difference scale, which has a causal 
interpretation. 
 
Traditional Cox proportional hazards models censor people that die as if they had 
dropped out of the study, and therefore consider they could develop the disease at the same rate 
as those who remain in the study, leading to potential biases of the associations. Other 
approaches for competing risks in mediation analysis include the survivor average causal effect 
(26) and the separable effects framework (27) These methods, however, are focused on a 
population that is either unrealistic (all survivors), or not observed (those who would survive no 
matter the exposure level). Also, effects cannot be separable in all settings. For example, in this 
setting, we have intertwined mediators, thus, we would not be able to consider separate non-
intertwined paths for the mediator of interest and the competing event. Instead, the indirect effect 
through the mediator of interest can also operate through the death pathway, provided that the 
death trajectory changes because of changes in the mediator of interest, and not because of direct 
changes in the exposure. Our method decomposes the contribution of each pathway to the 
association between an exposure and a health outcome while accounting for people that die 
during follow-up. This provides a better opportunity to investigate different pathways involved in 
the adverse health effects of elevated urinary metal levels. 

````

## PDF page 23

Technical extraction; compare with original PDF page 23.

````text
 
Both exposure-mediator interactions and non-linear effects can be considered in our 
algorithm. The algorithm can be extended to include time-varying confounders by considering an 
additional path-specific effect that evaluates the effect of the exposure on the outcome through 
those time-varying confounders, nested with the path through the mediator of interest and 
through the competing event. In addition, we currently model the trajectory of the mediator of 
interest by adjusting the mediator models at each time point for the immediate previous time 
point of the mediator, i.e., we do not adjust for all the previous mediator measurements to avoid 
multi-collinearity. This modelling approach could potentially be modified to include more 
specific measures of the longitudinal trajectory of the mediator such as the rate of change. 
 
Using our mediational g-formula algorithm, we identified a statistically significant 
indirect effect of the trajectory of blood pressure over time on the association between arsenic 
and CVD, but not cadmium, and CVD. Our results also show the importance of taking 
competing risks into account for cadmium, as many people typically die from other causes 
attributable to cadmium before being able to develop CVD. The wider confidence intervals in 
both the indirect and total effects show that the statistical uncertainty is greater when accounting 
for competing risks. The total effect not accounting for competing risks does not consider any 
variation in the survival status, as it is conditional on survival. Conversely, in our algorithm, we 
account for the difference in the survival trajectory under the two exposure scenarios, which 
makes this approach likely to enable modeling of a more realistic scenario. The effects were 
more statistically significant when using the survival probability difference in 20 years, which 
has a causal interpretation, as compared to using differences in hazards. 
 
This work has several limitations. First, we consider discrete time points for death 
indicators, rather than modeling death as time-to-event, which might potentially lead to some 

````

## PDF page 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
measurement errors due to not being able to incorporate the exact time in which the event 
happened. An extension to multi-state models (28), in which our primary event of interest (CVD, 
in this case) and death could be considered as a composite event, represents relevant future work. 
Another limitation is the parametric modeling approach. It would be of interest to extend this 
work to the machine learning setting, to be able to consider several exposures simultaneously, for 
example. In addition, the no unmeasured confounding assumption is not verifiable in practice in 
observational studies (29). Thus, the results of this study need to be interpreted with caution. The 
development of sensitivity analyses that evaluate how strong an unmeasured confounder would 
need to be to bias the estimated effects is left for future work.  
 
In conclusion, this work shows the importance of considering competing events in 
mediation analysis with survival outcomes. The fact of being able to identify the effects through 
different paths sheds light on the impact of metals on the outcome of interest, as well as through 
competing risks, more transparently.  
 
 
 
 
 
 
 

````

## PDF page 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
References 
1.  
Andersen PK, Geskus RB, De witte T, et al. Competing risks in epidemiology: possibilities 
and pitfalls. Int J Epidemiol [electronic article]. 2012;41(3):861. 
(/pmc/articles/PMC3396320/). (Accessed December 7, 2023) 
2.  
Rojas-Saunero LP, Young JG, Didelez V, et al. Considering Questions Before Methods in 
Dementia Research With Competing Events and Causal Goals. Am J Epidemiol [electronic 
article]. 2023;192(8):1415. (/pmc/articles/PMC10403306/). (Accessed November 14, 
2023) 
3.  
Driver JA. Inverse association between cancer and neurodegenerative disease: review of 
the epidemiologic and biological evidence. Biogerontology [electronic article]. 
2014;15(6):547–557. (https://pubmed.ncbi.nlm.nih.gov/25113739/). (Accessed 
December 10, 2023) 
4.  
Data Analysis with Competing Risks and Intermediate States - Ronald B. Geskus - Google 
Books. 
(https://books.google.com/books?hl=en&lr=&id=sswdCgAAQBAJ&oi=fnd&pg=PP1&ots=b
rp6Xz6xWr&sig=gHbUPA4fxH6N2rETG3XtQWfJCFs#v=onepage&q&f=false). (Accessed 
November 14, 2023) 
5.  
Young JG, Stensrud MJ, Tchetgen Tchetgen EJ, et al. A causal framework for classical 
statistical estimands in failure-time settings with competing events. Stat Med [electronic 
article]. 2020;39(8):1199–1236. 
(https://onlinelibrary.wiley.com/doi/full/10.1002/sim.8471). (Accessed November 15, 
2023) 
6.  
Martinussen T, Stensrud MJ. Estimation of separable direct and indirect effects in 
continuous time. Biometrics [electronic article]. 2023;79(1):127–139. 
(https://onlinelibrary.wiley.com/doi/full/10.1111/biom.13559). (Accessed January 8, 
2024) 
7.  
Huanga YT, Yangc HI. Causal mediation analysis of survival outcome with multiple 
mediators. Epidemiology. 2017;28(3):370–378.  
8.  
Lin DY, Ying Z. Semiparametric Analysis of the Additive Risk Model. Biometrika. 
1994;81(1):61.  
9.  
Lange T, Hansen J V. Direct and Indirect Effects in a Survival Context. Epidemiology 
[electronic article]. 2011;22(4):575–581. 
(http://content.wkhealth.com/linkback/openurl?sid=WKPTLP:landingpage&an=00001648
-201107000-00024). (Accessed April 22, 2020) 
10.  
Lin S-H, Young J, Logan R, et al. Parametric mediational g-formula approach to mediation 
analysis with time-varying exposures, mediators, and confounders. Epidemiology 
[electronic article]. 2017;28(2):266–274. 
(http://www.hsph.harvard.edu/causal/software/.). (Accessed December 7, 2023) 
11.  
Tai A-S, Lin S-H, Chu Y-C, et al. Causal mediation analysis with multiple time-varying 
mediators.  
12.  
Lin SH, Young JG, Logan R, et al. Mediation analysis for a survival outcome with time-
varying exposures, mediators, and confounders. Stat Med [electronic article]. 
2017;36(26):4153. (/pmc/articles/PMC6242332/). (Accessed December 7, 2023) 

````

## PDF page 26

FORMULA CHECK REQUIRED: original PDF page 26.

````text
13.  
Zhang Z, Reinikainen J, Adeleke KA, et al. Time-varying covariates and coefficients in Cox 
regression models. Ann Transl Med [electronic article]. 2018;6(7):121–121. 
(/pmc/articles/PMC6015946/). (Accessed December 10, 2023) 
14.  
Franceschini N, Fry RC, Balakrishnan P, et al. Cadmium body burden and increased blood 
pressure in middle-aged American Indians: the Strong Heart Study. J Hum Hypertens 
[electronic article]. 2017;31(3):225. (/pmc/articles/PMC5299034/). (Accessed April 23, 
2024) 
15.  
Kaufman JA, Mattison C, Fretts AM, et al. Arsenic, blood pressure, and hypertension in 
the Strong Heart Family Study. Environ Res [electronic article]. 2021;195. 
(https://pubmed.ncbi.nlm.nih.gov/33581093/). (Accessed April 23, 2024) 
16.  
Moon KA, Guallar E, Umans JG, et al. Association Between Exposure to Low to Moderate 
Arsenic Levels and Incident Cardiovascular Disease. Ann Intern Med [electronic article]. 
2013;159(10):649. (/pmc/articles/PMC4157936/?report=abstract). (Accessed July 3, 
2020) 
17.  
Tellez-Plaza M, Guallar E, Howard B V., et al. Cadmium Exposure and Incident 
Cardiovascular Disease. Epidemiology [electronic article]. 2013;24(3):421. 
(/pmc/articles/PMC4142588/). (Accessed June 9, 2023) 
18.  
Lee ET, Welty TK, Fabsitz R, et al. The Strong Heart Study. A study of cardiovascular 
disease in American Indians: design and methods. Am J Epidemiol [electronic article]. 
1990;132(6):1141–55. (http://www.ncbi.nlm.nih.gov/pubmed/2260546). (Accessed 
March 13, 2019) 
19.  
Levey AS, Stevens LA, Schmid CH, et al. A new equation to estimate glomerular filtration 
rate. Ann Intern Med [electronic article]. 2009;150(9):604–12. 
(http://www.ncbi.nlm.nih.gov/pubmed/19414839). (Accessed January 29, 2018) 
20.  
Lee ET, Welty TK, Fabsitz R, et al. The Strong Heart Study. A study of cardiovascular 
disease in American Indians: design and methods. Am J Epidemiol. 1990;132(6):1141–55.  
21.  
Nigra AE, Sanchez TR, Nachman KE, et al. The effect of the Environmental Protection 
Agency maximum contaminant level on arsenic exposure in the USA from 2003 to 2014: 
an analysis of the National Health and Nutrition Examination Survey (NHANES). Lancet 
Public Health [electronic article]. 2017;2(11):e513–e521. 
(https://pubmed.ncbi.nlm.nih.gov/29250608/). (Accessed July 6, 2020) 
22.  
Howard B V., Lee ET, Yeh JL, et al. Hypertension in adult American Indians: The strong 
heart study. Hypertension. 1996;28(2):256–264.  
23.  
Azur MJ, Stuart EA, Frangakis C, et al. Multiple imputation by chained equations: what is 
it and how does it work? Int J Methods Psychiatr Res [electronic article]. 2011;20(1):40. 
(/pmc/articles/PMC3074241/). (Accessed January 22, 2024) 
24.  
Zhang Z, Reinikainen J, Adeleke KA, et al. Time-varying covariates and coefficients in Cox 
regression models. Ann Transl Med [electronic article]. 2018;6(7):121–121. 
(/pmc/articles/PMC6015946/). (Accessed January 8, 2024) 
25.  
Madadizadeh F, Ghanbarnejad A, Ghavami V, et al. Applying Additive Hazards Models for 
Analyzing Survival in Patients with Colorectal Cancer in Fars Province, Southern Iran. 
Asian Pac J Cancer Prev [electronic article]. 2017;18(4):1077. 
(/pmc/articles/PMC5494219/). (Accessed January 8, 2024) 

````

## PDF page 27

FORMULA CHECK REQUIRED: original PDF page 27.

````text
26.  
Tchetgen Tchetgen EJ. Identification and estimation of survivor average causal effects. 
Stat Med [electronic article]. 2014;33(21):3601. (/pmc/articles/PMC4131726/). (Accessed 
October 9, 2024) 
27.  
Stensrud MJ, Hernán MA, Tchetgen Tchetgen EJ, et al. A generalized theory of separable 
effects in competing event settings. Lifetime Data Anal [electronic article]. 
2021;27(4):588. (/pmc/articles/PMC8536652/). (Accessed October 9, 2024) 
28.  
Valeri L, Proust-Lima C, Fan W, et al. A multistate approach for the study of interventions 
on an intermediate time-to-event in health disparities research. 
https://doi.org/10.1177/09622802231163331 [electronic article]. 2023;32(8):1445–1460. 
(https://journals.sagepub.com/doi/10.1177/09622802231163331). (Accessed April 5, 
2024) 
29.  
Valente MJ, Pelham WE, Smyth H, et al. Confounding in Statistical Mediation Analysis: 
What It Is and How to Address It. J Couns Psychol [electronic article]. 2017;64(6):659. 
(/pmc/articles/PMC5726285/). (Accessed April 5, 2024) 
  
 
 

````

## PDF page 28

FORMULA CHECK REQUIRED: original PDF page 28.

````text
Table 1. Participant characteristics by cardiovascular disease status. 
 
Overall (N=2,932) 
Non-cases (N=1,955) 
Cardiovascular disease 
cases (N=977) 
Age (years) 
55.3 (49.3, 62.6) 
54.1 (48.6, 61.4) 
57.4 (51.2, 64.5) 
Sex (%) 
 
 
 
     Female 
1698 (57.9) 
1151 (58.9) 
547 (56) 
     Male 
1234 (42.1) 
804 (41.1) 
430 (44) 
Study center (%) 
 
 
 
     AZ 
397 (13.5) 
294 (15) 
103 (10.5) 
     OK 
1275 (43.5) 
891 (45.6) 
384 (39.3) 
     ND/SD 
1260 (43) 
770 (39.4) 
490 (50.2) 
Smoking (%) 
 
 
 
     Never 
851 (29) 
593 (30.3) 
258 (26.4) 
     Former 
979 (33.4) 
656 (33.6) 
323 (33.1) 
     Current 
1102 (37.6) 
706 (36.1) 
396 (40.5) 
BMI (kg/m2) 
29.71 (26.38, 33.77) 
29.38 (25.9, 33.46) 
30.25 (27.12, 34.23) 
eGFR (mL/min/1.73m2) 
99.98 (90.58, 107.3) 
100.72 (91.64, 107.89) 
98.2 (89.19, 105.79) 
SBP (visit 1) 
124 (113, 136.12) 
122 (111, 134) 
128 (118, 141) 
SBP (visit 2) 
126 (114, 140) 
124 (113, 136) 
131 (119, 144) 
SBP (visit 3) 
129 (118, 142) 
128 (117, 141) 
132 (120, 146) 
Arsenic µg/g 
8.41 (5.12, 14.27) 
8.36 (4.99, 13.9) 
8.56 (5.36, 14.78) 
Cadmium µg/g 
0.97 (0.62, 1.5) 
0.95 (0.61, 1.47) 
1 (0.64, 1.55) 
 
Median (interquartile range) for continuous variables, percentages for categorical variables  

````

## PDF page 29

Technical extraction; compare with original PDF page 29.

````text
Table 2. Direct, indirect, and total effects of one interquartile range increase in urinary arsenic on incident CVD through the systolic 
blood pressure trajectory and death. 
 
Without accounting for competing risks 
Accounting for competing risks 
 
Hazard differencea 
Difference in survival 
probability in 20 years (%) 
Hazard differencea 
Difference in survival 
probability in 20 years (%) 
Direct effect 
330.6 (39.7, 617.9) 
-2.6 (-2.6, -2.6) 
330.6 (36.2, 627.4) 
-2.59 (-2.60, -2.58) 
Indirect effect through the 
blood pressure trajectory 
44.9 (9.6, 86.3) 
-0.4 (-0.4, -0.3) 
46.5 (7.5, 90.4) 
-0.34 (-0.70, -0.02) 
Indirect effect through the 
death process 
- 
- 
-8.9 (-22.5, 4.5) 
0.22 (-0.07, 0.49) 
Total effect 
375.8 (85.9, 666.1) 
-2.91 (-2.93, -2.90) 
368.6 (72.1, 668.4) 
-2.73 (-2.99, -2.36) 
Sum of direct effect and 
indirect effect through 
blood pressure 
 
375.6 (49.3, 704.2) 
 
-2.91 (-2.93, -2.89) 
 
377.1 (43.7, 717.8) 
 
-2.93 (-3.30, -2.60) 
 
a The hazard difference is reported in number of cases per 100,000 person-years. 
Models adjusted for age, sex, study center (Arizona, Oklahoma, or North Dakota and South Dakota), estimated glomerular filtration 
rate, BMI and smoking status (never, former, or current smoking). 
 
 
 
 

````

## PDF page 30

Technical extraction; compare with original PDF page 30.

````text
Table 3. Direct, indirect, and total effects of one interquartile range increase in urinary cadmium on incident CVD through the systolic 
blood pressure trajectory and death. 
 
Without accounting for competing risks 
Accounting for competing risks 
 
Hazard differencea 
Difference in survival 
probability in 20 years (%) 
Hazard differencea 
Difference in survival 
probability in 20 years (%) 
Direct effect 
149.4 (-80.7, 374.4) 
-1.68 (-1.70, -1.67) 
146.2 (-83.2, 374.9) 
-1.69 (-1.71, -1.67) 
Indirect effect through the 
blood pressure trajectory 
13.1 (-17.7, 46.1) 
-0.152 (-0.153, -0.150) 
13.8 (-19.8, 49.1) 
-0.16 (-0.32, -0.02) 
Indirect effect through the 
death process 
- 
- 
-8.8 (-22.6, 4.7) 
0.1 (-0.04, 0.23) 
Total effect 
161.8 (-72.1, 387.8) 
-1.83 (-1.85, -1.81) 
152.2 (-80.2, 382.9) 
-1.76 (-1.9, -1.63) 
Sum of direct effect and 
indirect effect through 
blood pressure 
 
162.5 (-98.4, 420.5) 
 
-1.83 (-1.85, -1.82) 
 
160.0 (-103.0, 424.0) 
 
-1.85 (-2.03, -1.69) 
 
a The hazard difference is reported in number of cases per 100,000 person-years. 
Models adjusted for age, sex, study center (Arizona, Oklahoma, or North Dakota and South Dakota), estimated glomerular filtration 
rate, BMI and smoking status (never, former, or current smoking).  
 
 

````

## PDF page 31

Technical extraction; compare with original PDF page 31.

````text
SUPPLEMENTARY MATERIAL 
A path-specific effect approach to mediation analysis with time-varying mediators and time-to-event outcomes accounting for 
competing risks 
 
Supplementary Figure 1. Directed acyclic graph for the direct effect of the exposure on the outcome. 
 
 
Supplementary Figure 2. Directed acyclic graph for the indirect effect through the mediator of interest. 

````

## PDF page 32

Technical extraction; compare with original PDF page 32.

````text
 
Supplementary Figure 3. Directed acyclic graph for the indirect effect through death/competing event. 

````

## PDF page 33

Technical extraction; compare with original PDF page 33.

````text
 
 
Supplementary Figure 4. Directed acyclic graph for the sum of the direct effect and the indirect effect through the mediator of 
interest  
 

````

## PDF page 34

Technical extraction; compare with original PDF page 34. NO TEXT LAYER: no OCR or invented transcription supplied.

````text
 
 
 

````

## PDF page 35

FORMULA CHECK REQUIRED: original PDF page 35.

````text
Supplementary Methods 
Proof of the calculation of the total effect using the mediational g-formula. 
𝜙(𝑎∗, 𝑎∗, 𝑎∗) ≡E (𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))) |𝐿0 = 𝑙0)
= E (𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗))) |𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗)) = 1, 𝐿0 = 𝑙0) 𝑃(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))
= 1|𝐿0 = 𝑙0)
+ E (𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗))) |𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗)) = 0, 𝐿0 = 𝑙0) 𝑃(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))
= 0|𝐿0 = 𝑙0) 
∵𝐭𝐡𝐞𝐨𝐫𝐞𝐦 𝐨𝐟 𝐭𝐡𝐞 𝐭𝐨𝐭𝐚𝐥 𝐩𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐭𝐲 
= E(𝑌𝑘+1(𝑎∗,𝑠̅𝑘= 1, 𝑀̅𝑘(𝑎∗,𝑠̅𝑘−1 = 1))|𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗)) = 1, 𝐿0 = 𝑙0)𝑃(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗)) =
1|𝐿0 = 𝑙0)   
 (∵𝒀(𝑺̅𝒌(𝒂∗, 𝑴̅𝒌(𝒂∗)) = 𝟎) = 𝟎) 
= E(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗)) 𝑌𝑘+1(𝑎∗, 𝑠̅𝑘= 1,𝑀̅𝑘(𝑎∗, 𝑠̅𝑘−1 = 1))|𝐿0 = 𝑙0) 
 (∵𝐁𝐢𝐬𝐛𝐢𝐧𝐚𝐫𝐲⇒𝑬(𝑩𝒀) = 𝑬(𝒀|𝑩= 𝟏)𝑷(𝑩= 𝟏)) 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝑀̅𝑘(𝑎∗,𝑠̅𝑘−1 = 1) = 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗,𝑠̅𝑘−1 = 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝑀̅𝑘(𝑎∗,𝑠̅𝑘−1 = 1) = 𝑚̅𝑘,𝐴= 𝑎∗, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗, 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌) ⊥𝑨 |𝑳𝟎    and   𝑺̅𝒌(𝒂∗, 𝒎̅𝒌) ⊥𝑨 |𝑳𝟎 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝐴= 𝑎∗, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗, 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
∵ (𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌), 𝑺̅𝒌(𝒂∗, 𝒎̅𝒌)) ⊥𝑴̅𝒌 |𝑨, 𝑳𝟎 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0) 𝑓(𝑀̅𝑘(𝑎∗,1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
∵ 𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌) ⊥𝑴̅𝒌|𝑨,𝑺̅𝒌−𝟏= 𝟏, 𝑳𝟎   and   𝑺̅𝒌(𝒂∗, 𝒎̅𝒌) ⊥𝑴̅𝒌|𝑨,𝑳𝟎 

````

## PDF page 36

FORMULA CHECK REQUIRED: original PDF page 36.

````text
= ∫E(𝑆̅𝑘𝑌𝑘+1(𝑎∗, 1,𝑚̅𝑘)|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗,1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒄𝒐𝒏𝒔𝒊𝒔𝒕𝒆𝒏𝒄𝒚 
 
= ∫E(𝑌𝑘+1(𝑎∗, 1,𝑚̅𝑘)|𝑆̅𝑘= 1,𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗,𝑀̅𝑘= 𝑚̅𝑘,𝐶= 𝑐)𝑓(𝑀̅𝑘(𝑎∗,1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
= ∫E(𝑌𝑘+1(𝑎∗,1,𝑚̅𝑘)|𝑆̅𝑘= 1,𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0) 𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1| 𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0) 𝑓(𝑀̅𝑘(𝑎∗,1)
= 𝑚̅𝑘| 𝐴= 𝑎∗, 𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
∵ 𝑴̅𝒌(𝒂∗, 𝒔̅𝒌−𝟏= 𝟏) ⊥𝑨 |𝑺̅𝒌−𝟏= 𝟏, 𝑳𝟎 
= ∫E(𝑌𝑘+1|𝐴= 𝑎∗, 𝑆̅𝑘= 1, 𝑀̅𝑘= 𝑚̅𝑘,𝐿0 = 𝑙0) 𝑓(𝑆̅𝑘= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0) 𝑓(𝑀̅𝑘
𝑚̅𝑘
= 𝑚̅𝑘|𝐴= 𝑎∗, 𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒄𝒐𝒏𝒔𝒊𝒔𝒕𝒆𝒏𝒄𝒚 
 
On the other hand: 
𝜙(𝑎, 𝑎,𝑎) ≡E (𝑌𝑘+1 (𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎)))|𝐿0 = 𝑙0)
= E (𝑌𝑘+1 (𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎,𝑀̅𝑘(𝑎))) |𝑆̅𝑘(𝑎,𝑀̅𝑘(𝑎)) = 1,𝐿0 = 𝑙0) 𝑃(𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))
= 1|𝐿0 = 𝑙0)
+ E (𝑌𝑘+1 (𝑎, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎)),𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))) |𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎)) = 0,𝐿0 = 𝑙0) 𝑃(𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎))
= 0|𝐿0 = 𝑙0) 
∵𝐭𝐡𝐞𝐨𝐫𝐞𝐦 𝐨𝐟 𝐭𝐡𝐞 𝐭𝐨𝐭𝐚𝐥 𝐩𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐭𝐲 
= E(𝑌𝑘+1(𝑎, 𝑠̅𝑘= 1,𝑀̅𝑘(𝑎,𝑠̅𝑘−1 = 1))|𝑆̅𝑘(𝑎,𝑀̅𝑘(𝑎)) = 1,𝐿0 = 𝑙0)𝑃(𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎)) =
1|𝐿0 = 𝑙0)   
 (∵𝒀(𝑺̅𝒌(𝒂, 𝑴̅𝒌(𝒂)) = 𝟎) = 𝟎) 
= E(𝑆̅𝑘(𝑎, 𝑀̅𝑘(𝑎)) 𝑌𝑘+1(𝑎,𝑠̅𝑘= 1, 𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1))|𝐿0 = 𝑙0) 
 (∵𝐁𝐢𝐬𝐛𝐢𝐧𝐚𝐫𝐲⇒𝑬(𝑩𝒀) = 𝑬(𝒀|𝑩= 𝟏)𝑷(𝑩= 𝟏)) 

````

## PDF page 37

FORMULA CHECK REQUIRED: original PDF page 37.

````text
= ∫E(𝑆̅𝑘(𝑎,𝑚̅𝑘) 𝑌𝑘+1(𝑎,1, 𝑚̅𝑘)|𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1) = 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
= ∫E(𝑆̅𝑘(𝑎,𝑚̅𝑘) 𝑌𝑘+1(𝑎,1, 𝑚̅𝑘)|𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1) = 𝑚̅𝑘,𝐴= 𝑎, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒀𝒌+𝟏(𝒂, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌) ⊥𝑨 |𝑳𝟎    and   𝑺̅𝒌(𝒂, 𝒎̅𝒌) ⊥𝑨 |𝑳𝟎 
= ∫E(𝑆̅𝑘(𝑎,𝑚̅𝑘) 𝑌𝑘+1(𝑎,1, 𝑚̅𝑘)|𝐴= 𝑎, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎,1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0) 𝑑𝑚̅𝑘
𝑚̅𝑘
 
∵ (𝒀𝒌+𝟏(𝒂, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌), 𝑺̅𝒌(𝒂, 𝒎̅𝒌)) ⊥𝑴̅𝒌 |𝑨, 𝑳𝟎 
= ∫E(𝑆̅𝑘(𝑎,𝑚̅𝑘) 𝑌𝑘+1(𝑎,1, 𝑚̅𝑘)|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
∵ 𝒀𝒌+𝟏(𝒂, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌) ⊥𝑴̅𝒌|𝑨,𝑺̅𝒌−𝟏= 𝟏, 𝑳𝟎   and   𝑺̅𝒌(𝒂, 𝒎̅𝒌) ⊥𝑴̅𝒌|𝑨,𝑳𝟎 
= ∫E(𝑆̅𝑘𝑌𝑘+1(𝑎,1, 𝑚̅𝑘)|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘
𝑚̅𝑘
 
∵ 𝒄𝒐𝒏𝒔𝒊𝒔𝒕𝒆𝒏𝒄𝒚 
= ∫E(𝑌𝑘+1(𝑎, 1,𝑚̅𝑘)|𝑆̅𝑘= 1, 𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
= ∫E(𝑌𝑘+1(𝑎, 1,𝑚̅𝑘)|𝑆̅𝑘= 1, 𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1) = 𝑚̅𝑘|𝐴= 𝑎,𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝑴̅𝒌(𝒂, 𝒔̅𝒌−𝟏= 𝟏) ⊥𝑨 |𝑺̅𝒌−𝟏= 𝟏, 𝑳𝟎 
= ∫E(𝑌𝑘+1|𝐴= 𝑎, 𝑆̅𝑘= 1,𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘= 1|𝐴= 𝑎, 𝑀̅𝑘= 𝑚̅𝑘,𝐿0 = 𝑙0) 𝑓(𝑀̅𝑘
𝑚̅𝑘
= 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒄𝒐𝒏𝒔𝒊𝒔𝒕𝒆𝒏𝒄𝒚 
 
 

````

## PDF page 38

FORMULA CHECK REQUIRED: original PDF page 38.

````text
Proof of the calculation of the indirect through the mediator of interest using the mediational g-
formula. 
𝜙(𝑎∗, 𝑎∗, 𝑎) ≡E (𝑌𝑘+1 (𝑎∗,𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎)))|𝐿0 = 𝑙0)
= E (𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎))) |𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎)) = 1, 𝐿0 = 𝑙0) 𝑃(𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎))
= 1|𝐿0 = 𝑙0)
+ E (𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎, 𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎))) |𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎)) = 0, 𝐿0 = 𝑙0) 𝑃(𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎))
= 0|𝐿0 = 𝑙0) 
∵𝐭𝐡𝐞𝐨𝐫𝐞𝐦 𝐨𝐟 𝐭𝐡𝐞 𝐭𝐨𝐭𝐚𝐥 𝐩𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐭𝐲 
= E(𝑌𝑘+1(𝑎∗,𝑠̅𝑘= 1, 𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1))|𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎)) = 1,𝐿0 = 𝑙0)𝑃(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎)) =
1|𝐿0 = 𝑙0)   
 (∵𝒀(𝑺̅𝒌(𝒂∗, 𝑴̅𝒌(𝒂)) = 𝟎) = 𝟎) 
= E(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎)) 𝑌𝑘+1(𝑎∗,𝑠̅𝑘= 1, 𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1))|𝐿0 = 𝑙0) 
 (∵𝐁𝐢𝐬𝐛𝐢𝐧𝐚𝐫𝐲⇒𝑬(𝑩𝒀) = 𝑬(𝒀|𝑩= 𝟏)𝑷(𝑩= 𝟏)) 
= ∫E(𝑆̅𝑘(𝑎∗,𝑚̅𝑘) 𝑌𝑘+1(𝑎∗, 1,𝑚̅𝑘)|𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1) = 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝑀̅𝑘(𝑎, 𝑠̅𝑘−1 = 1) = 𝑚̅𝑘, 𝐴= 𝑎∗, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 𝑠̅𝑘−1
𝑚̅𝑘
= 1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
∵ 𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌) ⊥𝑨 |𝑳𝟎    and   𝑺̅𝒌(𝒂∗, 𝒎̅𝒌) ⊥𝑨 |𝑳𝟎 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝐴= 𝑎∗, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0) 𝑑𝑚̅𝑘
𝑚̅𝑘
 
∵ (𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌), 𝑺̅𝒌(𝒂∗, 𝒎̅𝒌)) ⊥𝑴̅𝒌(𝒂, 𝒔̅𝒌−𝟏= 𝟏) |𝑨, 𝑳𝟎 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎,1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌) ⊥𝑴̅𝒌|𝑨,𝑺̅𝒌−𝟏= 𝟏, 𝑳𝟎   and   𝑺̅𝒌(𝒂∗, 𝒎̅𝒌) ⊥𝑴̅𝒌|𝑨,𝑳𝟎 

````

## PDF page 39

FORMULA CHECK REQUIRED: original PDF page 39.

````text
= ∫E(𝑆̅𝑘𝑌𝑘+1(𝑎∗, 1,𝑚̅𝑘)|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒄𝒐𝒏𝒔𝒊𝒔𝒕𝒆𝒏𝒄𝒚 
 
= ∫E(𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝑆̅𝑘= 1,𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
= ∫E(𝑌𝑘+1(𝑎∗,1,𝑚̅𝑘)|𝑆̅𝑘= 1,𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎, 1) = 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝑴̅𝒌(𝒂, 𝒔̅𝒌−𝟏= 𝟏) ⊥𝑨 |𝑺̅𝒌−𝟏= 𝟏, 𝑳𝟎 
= ∫E(𝑌𝑘+1|𝐴= 𝑎∗,𝑆̅𝑘= 1,𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘
𝑚̅𝑘
= 𝑚̅𝑘|𝐴= 𝑎, 𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒄𝒐𝒏𝒔𝒊𝒔𝒕𝒆𝒏𝒄𝒚 
 
On the other hand: 
𝜙(𝑎∗, 𝑎∗, 𝑎∗) ≡E (𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))) |𝐿0 = 𝑙0)
= E (𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗))) |𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗)) = 1, 𝐿0 = 𝑙0) 𝑃(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))
= 1|𝐿0 = 𝑙0)
+ E (𝑌𝑘+1 (𝑎∗, 𝑀̅𝑘(𝑎∗,𝑆̅𝑘−1(𝑎∗)),𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗))) |𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗)) = 0, 𝐿0 = 𝑙0) 𝑃(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗))
= 0|𝐿0 = 𝑙0) 
∵𝐭𝐡𝐞𝐨𝐫𝐞𝐦 𝐨𝐟 𝐭𝐡𝐞 𝐭𝐨𝐭𝐚𝐥 𝐩𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐭𝐲 
= E(𝑌𝑘+1(𝑎∗,𝑠̅𝑘= 1, 𝑀̅𝑘(𝑎∗,𝑠̅𝑘−1 = 1))|𝑆̅𝑘(𝑎∗, 𝑀̅𝑘(𝑎∗)) = 1, 𝐿0 = 𝑙0)𝑃(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗)) =
1|𝐿0 = 𝑙0)   
 (∵𝒀(𝑺̅𝒌(𝒂∗, 𝑴̅𝒌(𝒂)) = 𝟎) = 𝟎) 
= E(𝑆̅𝑘(𝑎∗,𝑀̅𝑘(𝑎∗)) 𝑌𝑘+1(𝑎∗, 𝑠̅𝑘= 1,𝑀̅𝑘(𝑎∗, 𝑠̅𝑘−1 = 1))|𝐿0 = 𝑙0) 
 (∵𝐁𝐢𝐬𝐛𝐢𝐧𝐚𝐫𝐲⇒𝑬(𝑩𝒀) = 𝑬(𝒀|𝑩= 𝟏)𝑷(𝑩= 𝟏)) 

````

## PDF page 40

FORMULA CHECK REQUIRED: original PDF page 40.

````text
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝑀̅𝑘(𝑎∗,𝑠̅𝑘−1 = 1) = 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗,𝑠̅𝑘−1 = 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝑀̅𝑘(𝑎∗,𝑠̅𝑘−1 = 1) = 𝑚̅𝑘,𝐴= 𝑎∗, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗, 𝑠̅𝑘−1
𝑚̅𝑘
= 1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
∵ 𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌) ⊥𝑨 |𝑳𝟎    and   𝑺̅𝒌(𝒂∗, 𝒎̅𝒌) ⊥𝑨 |𝑳𝟎 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝐴= 𝑎∗, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗, 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0) 𝑑𝑚̅𝑘 
∵ (𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌), 𝑺̅𝒌(𝒂∗, 𝒎̅𝒌)) ⊥𝑴̅𝒌 |𝑳𝟎 
= ∫E(𝑆̅𝑘(𝑎∗, 𝑚̅𝑘) 𝑌𝑘+1(𝑎∗,1, 𝑚̅𝑘)|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗, 1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒀𝒌+𝟏(𝒂∗, 𝒔̅𝒌= 𝟏, 𝒎̅𝒌) ⊥𝑴̅𝒌|𝑨,𝑺̅𝒌−𝟏= 𝟏, 𝑳𝟎   and   𝑺̅𝒌(𝒂∗, 𝒎̅𝒌) ⊥𝑴̅𝒌|𝑨,𝑳𝟎 
= ∫E(𝑆̅𝑘𝑌𝑘+1(𝑎∗, 1,𝑚̅𝑘)|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗,1)
𝑚̅𝑘
= 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝒄𝒐𝒏𝒔𝒊𝒔𝒕𝒆𝒏𝒄𝒚 
= ∫E(𝑌𝑘+1(𝑎∗,1,𝑚̅𝑘)|𝑆̅𝑘= 1,𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗,1) = 𝑚̅𝑘|𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
= ∫E(𝑌𝑘+1(𝑎∗,1,𝑚̅𝑘)|𝑆̅𝑘= 1,𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘
𝑚̅𝑘
= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘,𝐿0 = 𝑙0)𝑓(𝑀̅𝑘(𝑎∗,1)
= 𝑚̅𝑘|𝐴= 𝑎∗, 𝑆̅𝑘−1 = 1,𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ 𝑴̅𝒌(𝒂∗, 𝒔̅𝒌−𝟏= 𝟏) ⊥𝑨 |𝑺̅𝒌−𝟏= 𝟏, 𝑳𝟎 
= ∫E(𝑌𝑘+1|𝐴= 𝑎∗,𝑆̅𝑘= 1,𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑆̅𝑘= 1|𝐴= 𝑎∗, 𝑀̅𝑘= 𝑚̅𝑘, 𝐿0 = 𝑙0)𝑓(𝑀̅𝑘
𝑚̅𝑘
= 𝑚̅𝑘|𝐴= 𝑎∗,𝑆̅𝑘−1 = 1, 𝐿0 = 𝑙0)𝑑𝑚̅𝑘 
∵ \𝒎𝒂𝒕𝒉𝒃𝒊𝒕{𝒄𝒐𝒏𝒔𝒊𝒔𝒕𝒆𝒏𝒄𝒚} 
 

````

## PDF page 41

Technical extraction; compare with original PDF page 41.

````text
Please note that the proof for the direct effect and the indirect effect through death can be 
obtained analogously. 
 
 

````

