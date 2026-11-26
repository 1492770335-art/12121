# Censoring-adjusted tree-based policy learning for estimating dynamic treatment regimes with censored outcomes

Original PDF: [original.pdf](original.pdf). SHA256: `db95d176baa4189dda4aeb426c7d76383e09aed24ddc3b2f2b6a05c0995c38e9`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
Censoring-Aware Tree-Based Reinforcement Learning for Estimating Dynamic Treatment 
Regimes with Censored Outcomes 
 
Animesh Kumar Paul1,2, Russell Greiner1,2,3 
 
​
1Department of Computing Science, University of Alberta, Edmonton, AB, Canada 
​
2Alberta Machine Intelligence Institute, Edmonton, Canada 
​
3Department of Psychiatry, University of Alberta, Edmonton, AB, Canada. 
 
 
Abstract 
Dynamic Treatment Regimes (DTRs) provide a systematic approach for making sequential 
treatment decisions that adapt to individual patient characteristics, particularly in clinical 
contexts where survival outcomes are of interest. Censoring-Aware Tree-Based Reinforcement 
Learning (CA-TRL) is a novel framework to address the complexities associated with censored 
data when estimating optimal DTRs. We explore ways to learn effective DTRs, from 
observational data. By enhancing traditional tree-based reinforcement learning methods with 
augmented inverse probability weighting (AIPW) and censoring-aware modifications, CA-TRL 
delivers robust and interpretable treatment strategies. We demonstrate its effectiveness through 
extensive simulations and real-world applications using the SANAD epilepsy dataset, where it 
outperformed the recently proposed ASCL method in key metrics such as restricted mean 
survival time (RMST) and decision-making accuracy. This work represents a step forward in 
advancing personalized and data-driven treatment strategies across diverse healthcare settings. 
Introduction 
Dynamic Treatment Regimes (DTRs) offer a systematic approach to optimizing sequential 
treatment decisions by tailoring interventions based on individual patient characteristics and 
evolving clinical histories 1,2. Widely applicable in managing chronic and progressive diseases, 
such as cancer and diabetes, DTRs consist of stage-specific decision rules that guide treatment 
allocation to maximize long-term patient outcomes 3,4. We consider ways to learn DTRs from 
observational data. Grounded in causal inference 5 (described in the Notation and Assumptions 
section under the Methods section below), the primary goal of learning is to produce a DTR 
model that can personalize treatment strategies by accounting for the heterogeneity in treatment 
responses, thereby enhancing both individual and population-level health outcomes. 
Here, we measure the effectiveness (reward) of a policy based on the survival time of the 
individual. For datasets with only uncensored information – that is, where survival outcomes are 
fully observed for all individuals – various statistical and machine learning techniques have been 
proposed to estimate optimal DTRs. Traditional methods – such as Q-learning 6–8 and A-learning 
1 

````

## PDF page 2

Technical extraction; compare with original PDF page 2.

````text
9,10 – rely on regression-based models to iteratively estimate stage-specific decision rules. While 
effective, these methods often require strong parametric assumptions and can struggle with 
scalability in high-dimensional settings. To overcome these limitations, tree-based methods 
have emerged as a robust alternative due to their flexibility and interpretability. Among these, 
the Tree-Based Reinforcement Learning (T-RL) algorithm, introduced by Tao et al. 11, embeds 
augmented inverse probability weighting (AIPW) 12 into the tree structure to estimate optimal 
treatment rules across multiple stages. T-RL has demonstrated excellent performance on 
complete datasets, particularly due to its ability to handle complex interactions between 
covariates and treatments while producing interpretable decision rules, leveraging the inherent 
transparency and simplicity of decision tree structures. 
In the context of censored data, methods often integrate survival analysis techniques to address 
incomplete observations – in particular, situations where we want to know when a training 
individual will die, but know only that this patient is still alive 2 years later after a specific 
baseline time point (eg, the start of the study), meaning that patient lived at least 2 years. 
Approaches 
such 
as 
inverse 
probability 
censoring 
weighting 
(IPCW) 
13–16 
and 
pseudo-value-based methods 17 have been developed to adjust for such censoring in survival 
outcomes. Pseudo-value methods, for example, replace censored survival quantities with 
derived pseudo-observations to allow us to apply standard machine learning techniques to such 
datasets with censored individuals. These pseudo-observations approximate the target quantity, 
such as restricted mean survival time, for both censored and uncensored individuals, using 
information derived from survival models like the Cox proportional hazard model. Despite 
advancements in handling censored data, no tree-based methods have yet been extended to 
incorporate censoring directly into the estimation framework for DTRs. 
To address this gap, we propose Censoring-Aware Tree-Based Reinforcement Learning 
(CA-TRL), an extension of the T-RL method tailored for right-censored data, where the exact 
timing of an event is unknown but is known to occur after a certain observed time point. Building 
on the robustness and interpretability of T-RL, CA-TRL introduces censoring adjustments 
through a modified AIPW estimator that incorporates survival and censoring probabilities into 
the tree-building process. This ensures unbiased estimation of counterfactual outcomes while 
retaining the flexibility of tree-based methods. By leveraging T-RL's strengths and addressing its 
limitations in handling incomplete data, CA-TRL provides a scalable and interpretable solution 
for optimizing multi-stage, multi-treatment decision-making under censoring conditions. 
The remainder of this paper is organized as follows. The Methods section details the notation 
and assumptions underlying the CA-TRL framework, and its methodology, including the 
modified purity measures and recursive estimation process. The Results section evaluates the 
performance of CA-TRL through simulation studies and a real-world dataset, comparing it to 
baseline models including fixed treatment policies (uniform treatment assignment), random 
treatment assignment policies, and a recent advanced DTR method, demonstrating its utility in 
clinical decision-making under censored data conditions. Finally, the Discussion section 
concludes with a discussion of the method's implications and potential extensions for future 
research. 
2 

````

## PDF page 3

Technical extraction; compare with original PDF page 3.

````text
Results 
 
To thoroughly assess the performance of the proposed method, we performed extensive 
experiments, of our method, baseline models including fixed treatment policies (uniform 
treatment assignment), random treatment assignment policies, and a recent advanced DTR 
method, ASCL17, on a semi-synthetic and real-world datasets, using four distinct evaluation 
metrics, as described in the Methods subsection. Given the absence of a true reward function or 
true policy in existing survival datasets, we generated semi-synthetic datasets by integrating 
real-world data with simulated censoring mechanisms. Importantly, the survival models only 
utilize the observed censored times for the subjects affected by those simulated censoring 
mechanisms. The true underlying information, including the given reward function and true 
policy  used for generating the semi-synthetic data, was exclusively used during the evaluation 
phase to assess the learned policy's effectiveness and was not incorporated during the training 
process. 
i.​
Semi-Synthetic Data Study 
Given the challenges of directly validating learned policies due to the absence of true reward 
functions and corresponding optimal policies in real-world survival datasets, we created a 
semi-synthetic dataset. This dataset preserved the structure and characteristics of real-world 
data, including realistic covariate distributions and censoring percentages, while incorporating 
simulated outcomes and treatment assignments to ensure a controlled yet practical evaluation 
environment. 
 
For this study, we utilized the MIMIC-IV v2.0 dataset as the primary source 18. Coronary artery 
disease (CAD) was selected as the focus due to its prevalence and significance as a leading 
cause of hospitalization and mortality worldwide. The dataset provided comprehensive clinical 
information, including demographics, laboratory measurements, and outcomes from hospital 
admissions. To refine the analysis, we focused on non-ICU admissions, treating each hospital 
admission as an independent patient record to capture diverse clinical trajectories.  
 
A 48-hour observation window was defined, divided into two 24-hour intervals. For the 
experimental purpose, we have considered the first interval as the baseline covariates for 
Stage 1 (renal and anemia management), while the second interval as time-dependent 
changes for Stage 2 (glycemic management). The features included in the analysis were Age, 
Creatinine, Hemoglobin, Potassium, Sodium, Glucose, Platelet Count, Hematocrit, and White 
Blood Cell Count. Survival time was measured from admission to death or discharge, with 
approximately 62.18% of CAD patients exhibiting censored survival times. This censoring rate 
was replicated in the semi-synthetic dataset to maintain realistic evaluation conditions. For the 
initial preprocessing, we employed the recently published data processing pipeline for 
MIMIC-IV by Mehak et al. 19.  After preprocessing, a total of 65,486 patient records were 
available for analysis. 
3 

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Data Generation 
 
The processed data were used to simulate a two-stage DTR problem. Stage 1 focused on 
renal and anemia management using baseline covariates, while Stage 2 addressed glycemic 
control. The primary goal was to identify treatment policies that maximize survival outcomes. 
While we aimed to align the reward function, true policy, and other simulation-defined functions 
with clinical reasoning, we acknowledge that these may not fully represent the complexities of 
individual CAD treatment. Hence, the following functions should not be considered as ground 
truth for clinical decision-making.  
At Stage 1, the treatment indicator 
 was assigned using a multinomial distribution. For binary (
𝐴1
) and three-categorical (
 ) treatment options, the treatment probability vector was 
𝑀= 2
𝑀= 3
defined as follows: for binary treatments, the reference treatment probability 
was set to 1, 
(π10) 
and the alternative treatment probability 
 was modeled as 
π11
. For three-categorical treatments, the reference 
𝑒𝑥𝑝⁡(0. 2 * 𝐶𝑟𝑒𝑎𝑡𝑖𝑛𝑖𝑛𝑒1 + 0. 2 * 𝐻𝑒𝑚𝑜𝑔𝑙𝑜𝑏𝑖𝑛1)
treatment probability remained 1, while the additional treatment probabilities 
​ and 
 were 
(π11
π12)
modeled as 
 and 
𝑒𝑥𝑝⁡(0. 2 * 𝐶𝑟𝑒𝑎𝑡𝑖𝑛𝑖𝑛𝑒1 + 0. 1 * 𝑃𝑜𝑡𝑎𝑠𝑠𝑖𝑢𝑚1)
, respectively. In both binary and three-categorical 
𝑒𝑥𝑝⁡(0. 2 * 𝐻𝑒𝑚𝑜𝑔𝑙𝑜𝑏𝑖𝑛1 −0. 02 * 𝐴𝑔𝑒)
cases, these probabilities were then normalized to ensure they sum to 1 and used to simulate 
treatment assignments for each subject. Importantly, these represent treatment propensity 
models and do not correspond to censoring probabilities, which are separately modeled and 
incorporated into the data generation process. The optimal treatment rule at Stage 1, 
​, was 
𝑔1
𝑜𝑝𝑡
determined using clinically relevant covariates. For binary treatments, the optimal treatment rule 
was 
    
   
, 
𝑔1
𝑜𝑝𝑡=
𝐼(𝐶𝑟𝑒𝑎𝑡𝑖𝑛𝑖𝑛𝑒1 > 1. 5) * 𝐼(𝐻𝑒𝑚𝑜𝑔𝑙𝑜𝑏𝑖𝑛1 ≤ 12)    ∈ {0, 1}
while for three-categorical treatments, it was  
    
     ∈ {0,1,2}.  
𝑔1
𝑜𝑝𝑡=𝐼(𝐶𝑟𝑒𝑎𝑡𝑖𝑛𝑖𝑛𝑒1 > 1. 5) * (1 + 𝐼(𝐻𝑒𝑚𝑜𝑔𝑙𝑜𝑏𝑖𝑛1≤ 10) )
For our simulation, we generated the Stage 1 outcome 
 (which was the time until the next 
𝑇1
decision point, which could be either another treatment stage or terminating the process 
—perhaps due to an event like kidney failure, or death) using the equation 
, where  ~ Exp( λ 
𝑒𝑥𝑝⁡(1. 5 + 0. 3 * 𝑃𝑜𝑡𝑎𝑠𝑠𝑖𝑢𝑚1 −∣1. 5 * 𝐶𝑟𝑒𝑎𝑡𝑖𝑛𝑖𝑛𝑒1 −2∣* (𝐴1 −𝑔1
𝑜𝑝𝑡)
2 + ε)
ε
) represents a noise term added to capture variability in survival times. 
 
4 

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
In Stage 2, treatment assignments (
) were generated based on updated covariates, including 
𝐴2
the first-stage outcome (
). 
 was assigned using a multinomial distribution. For binary 
𝑇1
𝐴2
treatments, the reference treatment (unnormalized) probability 
 remained fixed at 1, while 
(π20) 
the alternative treatment unnormalized probability was 
. For three-categorical treatments, the unnormalized 
π21 = 𝑒𝑥𝑝⁡(0. 002 * 𝐺𝑙𝑢𝑐𝑜𝑠𝑒2 + 0. 005 * 𝑇1)
probabilities were 
 and 
π21 = 𝑒𝑥𝑝⁡(0. 002 * 𝐺𝑙𝑢𝑐𝑜𝑠𝑒2 + 0. 002 * 𝑆𝑜𝑑𝑖𝑢𝑚2)
. The optimal treatment rule at the second 
π22 = 𝑒𝑥𝑝⁡(0. 005 * 𝑃𝑙𝑎𝑡𝑒𝑙𝑒𝑡 𝐶𝑜𝑢𝑛𝑡2 + 0. 005 * 𝑇1)
stage (
​) was defined similarly. For binary treatments, the optimal treatment rule was  
𝑔2
𝑜𝑝𝑡
 = 
,  
𝑔2
𝑜𝑝𝑡
𝐼(𝐺𝑙𝑢𝑐𝑜𝑠𝑒2 > 140) + 𝐼(𝑇1 < 3)
while for three-categorical treatments, it was  
.  
𝑔2
𝑜𝑝𝑡= 𝐼(𝐺𝑙𝑢𝑐𝑜𝑠𝑒2 > 140) * ( 𝐼(𝑇1 > 0. 5) + 𝐼(𝑇1 > 3) )
The second-stage outcome (
) was generated using the function 
𝑇2
. 
𝑇2 = 𝑒𝑥𝑝⁡(1. 18 + 0. 2 * 𝑇1 −∣0. 5 * 𝐺𝑙𝑢𝑐𝑜𝑠𝑒2 + 2∣* (𝐴2 −𝑔2
𝑜𝑝𝑡)
2 + ε)
The methodology for defining treatment probabilities, optimal treatment assignment, and 
outcome functions follows recent works on synthetic data generation for evaluating DTR models 
11,17, ensuring consistency with state-of-the-art approaches. For the optimal treatment rule and 
outcome (or reward) function, we selected key features based on their well-established clinical 
relevance. For Stage 1, Creatinine (>1.5 mg/dL) was chosen because elevated levels indicate 
significant renal impairment and are strongly linked to increased cardiovascular risk20, while low 
Hemoglobin is a marker for anemia, which adversely affects cardiac outcomes21–23. For Stage 2, 
we use a Glucose threshold of >140 mg/dL to identify hyperglycemia that necessitates more 
aggressive glycemic management24. In addition, routinely measured features such as Age, 
Potassium, Sodium, Platelet Count, Hematocrit, and White Blood Cell Count are included to 
capture a comprehensive cardiovascular risk profile25–30. 
In our survival outcome function, the exponential transformation is employed to ensure that the 
predicted survival times remain strictly positive—a fundamental requirement in time-to-event 
analyses. This transformation is standard practice in survival analysis, as seen in both the Cox 
proportional hazards model and accelerated failure time models, where exponential forms are 
used to capture the multiplicative effect of covariates on the baseline hazard31,32. Moreover, the 
quadratic penalty term 
 is incorporated to measure the deviation of the actual 
(𝐴−𝑔
𝑜𝑝𝑡)
2
treatment  from the optimal treatment 
. Squaring this difference ensures that the penalty is 
𝐴
𝑔
𝑜𝑝𝑡
symmetric and increases nonlinearly with larger deviations, reflecting the intuition that 
5 

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
departures from the optimal decision should incur disproportionately higher costs. This 
approach is well supported by literature in DTRs for generating the synthetic data11,17. 
Censoring mechanisms were incorporated into the data generation process to mimic real-world 
survival datasets, where complete observation of survival times is often unavailable. The 
censoring times ( ) were generated using three distinct distributions to reflect varying levels of 
𝐶
censoring: 
1.​ Exponential Censoring: Censoring times were drawn from an exponential distribution, 
, where 
 was chosen appropriately to achieve the desired censoring rate. 
𝐶 ~ 𝐸𝑥𝑝(𝑐0)
𝑐0
2.​ Conditional Exponential Censoring: To introduce covariate dependency, censoring 
times followed 
. 
𝐶~ 𝑐0 * 𝑒𝑥𝑝(0. 3 ⋅ 𝐶𝑟𝑒𝑎𝑡𝑖𝑛𝑖𝑛𝑒1 + 0. 2 ⋅ |𝑃𝑜𝑡𝑎𝑠𝑠𝑖𝑢𝑚1 − 4. 0|)
3.​ Uniform Censoring: Censoring times were generated from a uniform distribution, 
, where  and  define the lower and upper bounds, respectively, and were 
𝐶∼𝑈𝑛𝑖𝑓(𝑎, 𝑏)
𝑎
𝑏
chosen appropriately to achieve the desired censoring rate. 
These distributions were calibrated to achieve a censoring rate of around 62%, consistent with 
the MIMIC CAD population. 
To determine whether a subject proceeds to the second stage, the binary indicator variable 
 was used, where 
 indicates that the first-stage outcome (
​) is less than 
η = 𝐼(𝑇1 < 𝐶)
η = 1
𝑇1
the censoring time (C), allowing progression to the second stage, and 
 signifies 
η = 0
censoring after the first stage. The total survival time (
) was defined as: 
𝑇
𝑢𝑛𝑜𝑏
,  
𝑇
𝑢𝑛𝑜𝑏= 𝑇1 + η * 𝑇2
where ​ represents the second-stage outcome. 
𝑇2
The observed total survival time 
 is the minimum of the total survival time (
𝑇= 𝑚𝑖𝑛(𝑇
𝑢𝑛𝑜𝑏, 𝐶)
) and the censoring time (C). The observed outcomes for each stage were defined as 
𝑇
𝑢𝑛𝑜𝑏
follows: 
1.​ For the second stage, the observed outcome (
) was calculated as:​
𝑅2
 if 
, else NaN 
𝑅2 = (𝑇−𝑇1) * 𝐼(𝑇≥𝑇1)
η = 1
            Here if the patient does not enter stage 2, 
 is set as undefined (NaN). 
𝑅2
2.​ For the first stage, the observed outcome 
 is defined as:​
𝑅1
  
𝑅1 = 𝑇* 𝐼(𝑇< 𝑇1)  +  𝑇1 * 𝐼(𝑇 ≥𝑇1)
6 

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
To facilitate understanding of the notations used in results, we summarize key notations in Table 
1. This framework for censoring and outcome generation ensures that the simulated data aligns 
with the complexities of survival analysis in multi-stage decision-making contexts. By integrating 
realistic censoring percentage and structured definitions of observed outcomes, this approach 
facilitates robust evaluation of the proposed method under various censoring scenarios. Note 
the learning algorithms will see only the observed information – here 
 and 
– but not 
𝑇, 𝑅1,
𝑅2
. As we have large enough samples, we split the data into 5 folds, using one fold for 
𝑇1 𝑎𝑛𝑑 𝑇2
training and the other 4 for evaluation each time to ensure reliable performance estimation. This 
choice of using a single fold for training allows us to simulate a more challenging scenario, 
where the model is trained on limited data. Such an approach is particularly valuable in dynamic 
treatment regime optimization, as it helps evaluate the model's robustness and generalizability 
when applied to unseen data. Additionally, reserving a larger portion of the data for evaluation 
provides a more precise estimate of the model's performance by minimizing the variability in test 
results across folds. 
Table 1: Key notations for semi-synthetic data generation process.  
Notation 
Description 
 
𝐴1
Stage 1 treatment 
 was assigned using a multinomial distribution. 
𝐴1
 
𝐴2
Stage 2 treatment 
 was assigned using a multinomial distribution. 
𝐴2
 
𝑔1
𝑜𝑝𝑡
Stage 1 optimal treatment. 
 
𝑔2
𝑜𝑝𝑡
Stage 2 optimal treatment. 
 
𝑇1
Time spent in Stage 1 if no censoring happens. 
 
𝑇2
Time at Stage 2 if no censoring happens. 
 
𝑇
𝑢𝑛𝑜𝑏
Total survival time if no censoring happens (
). 
𝑇1 + 𝑇2
C 
Censoring time: The time at which a patient's survival is no longer observed. 
 
𝑇
Observed total survival time due to censoring: 
. 
𝑚𝑖𝑛(𝑇
𝑢𝑛𝑜𝑏, 𝐶)
 
𝑅1
Survival time at Stage 1 after adjusting for censoring. 
 
𝑅2
Survival time at Stage 2 after adjusting for censoring. 
7 

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
 
η
: Equals 1 if the patient enters Stage 2, otherwise 0. 
 𝐼(𝑇1 < 𝐶)
 
Models for comparison 
To evaluate the proposed CA-TRL method, we compared its performance against several 
approaches in both binary and multi-category treatment settings. Baseline models included fixed 
treatment policies, where treatments were uniformly assigned to all individuals (e.g., for g=0, 
assign treatment 0 to all patients; similarly for g=1, assign treatment 1, and so on as used in 
Table 2). A random treatment assignment policy, where treatments were allocated without 
considering individual covariates, was also included as a simplistic benchmark. 
 
In addition to these baselines, we compared CA-TRL with the ASCL method 17, a recent 
advanced approach in dynamic treatment regime optimization. The ASCL method leverages a 
contrast-learning framework, which is based on the idea of the doubly-robust weighted 
classification approach. By incorporating pseudo-value approaches to address censoring in 
survival data, ASCL used penalized support vector machines. ASCL has demonstrated superior 
performance over earlier standard methods and is recognized for its adaptability and robustness 
in handling survival data. We selected ASCL as a benchmark because it is one of the most 
recent methods developed for censored dynamic treatment regimes and has a publicly available 
implementation, ensuring reproducibility and ease of comparison. We have used the publicly 
available implementation of ASCL. 
 
The evaluation metrics included Restricted Mean Survival Time (RMST), which captures the 
average survival time up to a specified truncation point , making it well-suited for censored 
τ
data. Correct Decision Rate at the First Stage (CDR1) measured the accuracy of treatment 
assignments at the initial stage, while Average Correct Decision Rate (ACDR) provided an 
overall assessment of decision accuracy across all stages 17. Counterfactual outcomes were 
also analyzed to estimate the survival benefits that would have if individuals followed the 
treatments recommended by each method 11. 
 
 
Analysis Results 
The evaluation results, presented in Table 2, demonstrate the superior performance of the 
proposed CA-TRL method across various evaluation metrics, including 
-restricted mean 
τ
survival time ( -RMST), CDR1, ACDR, and expected survival outcomes. These metrics were 
τ
computed under different treatment options, propensity models, and censoring types. 
8 

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
For binary treatments, CA-TRL consistently outperformed all comparison methods, including 
random treatment assignment and the ASCL algorithm. Under exponential censoring with a true 
propensity model, CA-TRL achieved a -RMST of 46.37 ± 0.28 compared to 34.50 ± 3.15 for 
τ
ASCL. Additionally, CA-TRL achieved a CDR1 of 93.17 ± 5.90 and an ACDR of 89.13 ± 2.40, 
both significantly higher than those obtained by ASCL, which recorded 70.80 ± 9.88 and 52.09 ± 
7.36, respectively. Similar trends were observed for other censoring and propensity model 
types, with CA-TRL consistently demonstrating higher -RMST, CDR1, and ACDR values. 
τ
For three categorical treatment options, the results were equally compelling. Under conditional 
censoring with a false propensity model, CA-TRL achieved a -RMST of 26.11 ± 0.19, a CDR1 
τ
of 80.28 ± 4.25, and an ACDR of 77.28 ± 4.73. In contrast, ASCL showed significantly lower 
values with a -RMST of 14.35 ± 2.89, a CDR1 of 66.64 ± 13.6, and an ACDR of 20.09 ± 11.62. 
τ
Similar trends were observed for other scenarios. These findings highlight the robustness and 
adaptability of the proposed method in complex multi-treatment scenarios. 
CA-TRL's effectiveness is further validated by its ability to achieve higher survival outcomes 
across all scenarios. The expected survival outcomes under CA-TRL consistently outperformed 
those of other methods. For instance, under uniform censoring with a true propensity model for 
binary treatments, CA-TRL recorded an expected survival outcome of 92.45 ± 1.90 compared to 
77.52 ± 1.77 for ASCL. 
Overall, these results underline the strength of CA-TRL in accurately estimating dynamic 
treatment regimes and maximizing survival outcomes, regardless of treatment complexity, 
censoring type, or propensity model specifications. The consistent outperformance across 
various metrics establishes CA-TRL as a reliable method for personalized treatment planning. 
 
Table 2: Performance of several DTR algorithms. The table reports the τ
-restricted survival time, correct decision rate at the first stage (CDR1), average correct decision 
across all stages (ACDR), and Expected Survival outcome. For each scenario, the best model is 
highlighted in bold. 
 
Treatm
ent 
Option
s 
Prope
nsity 
Model 
Type 
Censor
ing 
Type 
Method 
 τ
-RMST 
τ
CDR1 
ACDR 
Expected 
Survival 
outcome 
 
𝐸[𝑇
*|𝑔]
2 
True 
Expon
ential  
g=0 
52 
16.16±0.12 
80.14±0.06 
66.19±0.04 
24.25±0.05 
g=1 
2.86±0.01 
19.86±0.06 
5.01±0.04 
3.24±0.0 
Random 
9.34± 0.02 
17.33±0.06 
3.01±0.07 
12.41±0.07 
9 

````

## PDF page 10

Technical extraction; compare with original PDF page 10.

````text
ASCL 
34.50±3.15 
70.80±9.88 
52.09±7.36 
62.12±8.43 
CA-TRL 
46.37±0.28 
93.17±5.90 
89.13±2.40 
93.98±1.93 
Conditi
onal  
g=0 
62 
14.70±0.05 
80.14±0.05 
68.53±0.09 
24.21±0.04 
g=1 
2.75±0.01 
19.86±0.05 
3.91±0.02 
3.24±0.00 
Random 
9.29±0.09 
17.43±0.05 
2.90±0.04 
12.37±0.05 
ASCL 
40.80±3.06 
68.11±9.38 
54.60±6.67 
57.25±4.24 
CA-TRL 
57.62±0.17 
91.38±3.38 
92.01±2.50 
93.25±1.16 
Unifor
m 
g=0 
13 
9.30±0.01 
80.14±0.02 
66.71±0.05 
24.21±0.04 
g=1 
2.82±0.0 
19.86±0.02 
4.80±0.2 
3.24±0.0 
Random 
6.30±0.01 
17.39±0.01 
2.99±0.03 
12.41±0.03 
ASCL 
12.62±0.01 
86.03±1.44 
78.72±3.10 
77.52±1.77 
CA-TRL 
12.84±0.03 
89.96±2.14 
90.33±1.95 
92.45±1.90 
False 
Expon
ential  
g=0 
52 
16.19±0.09 
80.14±0.03 
66.22±0.05 
24.21±0.05 
g=1 
2.86±0.01 
19.86±0.03 
4.99±0.04 
3.24±0.0 
Random 
9.32±0.03 
17.42±0.08 
3.08±0.06 
12.37±0.05 
ASCL 
33.51±1.81 
67.86±8.94 
48.44±4.91 
59.94±5.01 
CA-TRL 
46.87±0.35 
95.77±3.60 
93.34±2.89 
95.79±1.53 
Conditi
onal  
g=0 
62 
14.67±0.04 
80.16±0.05 
68.48±0.09 
24.20±0.05 
g=1 
2.76±0.01 
19.84±0.05 
3.92±0.02 
3.24±.01 
Random 
9.25±0.11 
17.41±0.05 
2.87±0.02 
12.37±0.07 
ASCL 
41.23±3.75 
71.33±10.4
7 
54.57±7.42 
58.63±5.11 
CA-TRL 
57.58±0.21 
90.07±4.02 
91.02±2.97 
92.69±1.32 
Unifor
m 
g=0 
13 
9.31±0.01 
80.14±0.02 
66.71±0.05 
24.21±0.04 
g=1 
2.82±0.0 
19.86±0.02 
4.80±0.02 
3.24±.0.0 
Random 
6.30±0.01 
17.40±0.01 
2.99±0.03 
12.41±0.03 
ASCL 
12.67±0.01 
87.71±0.73 
80.27±2.95 
79.13±1.75 
10 

````

## PDF page 11

Technical extraction; compare with original PDF page 11.

````text
CA-TRL 
12.84±0.03 
89.87±2.20 
90.25±1.78 
92.42±1.90 
3 
 
True 
Expon
ential  
g=0 
23 
7.98±0.04 
80.14±0.03 
62.01±0.09 
8.45±0.01 
g=1 
5.97±0.08 
7.74±0.03 
0.00±0.0 
12.35±0.02 
g=2 
1.38±0.0 
12.12±0.04 
4.78±0.03 
1.60±0.0 
Random 
7.60±0.10 
17.54±0.07 
3.32±0.07 
12.32±0.06 
ASCL 
13.29±0.97 
75.12±4.76 
21.17±11.90 
28.91±8.54 
CA-TRL 
20.19±0.14 
79.33±3.45 
80.18±4.10 
80.15±2.30 
Conditi
onal  
g=0 
26 
7.56±0.01 
80.18±0.05 
63.44±0.06 
8.45±0.0 
g=1 
4.56±0.02 
7.72±0.03 
0.0±0.0 
12.36±0.06 
g=2 
1.32±0.02 
12.10±0.03 
4.28±0.03 
1.59±0.0 
Random 
7.69±0.11 
17.48±0.08 
3.34±0.08 
12.36±0.05 
ASCL 
14.67±3.44 
63.25±16.9
4 
26.93±18.97 31.22±13.04 
CA-TRL 
24.82±0.42 
82.77±2.70 
83.03±2.36 
80.95±1.70 
Unifor
m 
g=0 
5 
4.15±0.0 
80.11±0.03 
62.35±0.07 
8.45±0.01 
g=1 
2.69±0.0 
7.77±0.03 
0.0±0.0 
12.36±0.05 
g=3 
0.95±0.0 
12.12±0.02 
4.80±0.02 
1.60±0.0 
Random 
3.28±0.01 
17.46±0.07 
3.43±0.2 
12.39±0.08 
ASCL 
4.28±0.0 
80.11±0.03 
0.0±0.0 
12.44±0.01 
CA-TRL 
4.93±0.04 
87.24±3.16 
69.22±7.31 
76.55±7.04 
False 
Expon
ential  
g=0 
23 
8.02±0.03 
80.13±0.04 
62.01±0.11 
8.45±0.0 
g=1 
6.00±0.09 
7.74±0.04 
0.0±0.0 
12.35±0.03 
g=2 
1.38±0.01 
12.13±0.04 
4.78±0.03 
1.60±0.0 
Random 
7.60±0.13 
17.60±0.02 
3.34±0.09 
12.31±0.07 
ASCL 
13.5±1.23 
74.20±5.93 
23.91±15.02 30.42±10.89 
CA-TRL 
19.96±0.69 
85.41±4.02 
79.06±8.57 
80.22±6.20 
Conditi
onal  
g=0 
28 
7.47±0.04 
80.14±0.05 
63.44±0.08 
8.45±0.01 
11 

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
g=1 
4.44±0.04 
7.74±0.04 
0.0±0.0 
12.35±0.02 
g=2 
1.31±0.02 
12.12±0.03 
4.33±0.03 
1.60±0.0 
Random 
7.67±0.06 
17.48±0.07 
3.22±0.05 
12.41±0.04 
ASCL 
14.35±2.89 
66.64±13.6
5 
20.09±11.62 
27.44±8.21 
CA-TRL 
26.11±0.19 
80.28±4.25 
77.28±4.73 
79.01±2.51 
Unifor
m 
g=0 
5 
4.15±0.0 
80.14±0.04 
62.40±0.07 
8.45±0.01 
g=1 
2.68±0.01 
7.74±0.03 
0.0±0.0 
12.35±0.04 
g=2 
0.95±0.0 
12.12±0.02 
4.8±0.01 
1.60±0.0 
Random 
3.28±0.0 
17.45±0.05 
3.40±0.04 
12.37±0.06 
ASCL 
4.33±0.05 
80.88±0.77 
6.69±6.69 
17.43±4.99 
CA-TRL 
4.99±0.0 
91.55±1.98 
75.91±2.43 
88.41±2.39 
Observational studies 
The proposed method was applied to the SANAD dataset 33 to illustrate its utility in estimating 
DTRs in a real-world clinical setting. The SANAD study, a randomized controlled trial, evaluated 
the effectiveness of two antiepileptic drugs—carbamazepine (CBZ) and lamotrigine (LTG)—for 
patients with partial epilepsy. Treatment failure, defined as the withdrawal of the randomized 
drug due to unacceptable adverse effects (UAE) or inadequate seizure control (ISC), served as 
the primary outcome. The dataset includes both longitudinal and survival data for 605 patients, 
randomly assigned to CBZ (
) or LTG (
). 
𝐴1 = 1
𝐴1 = 2
 
Our decision to use this dataset and the preprocessing steps were inspired by a study by Speth 
et al. work 15, which employed this data to explore DTR estimation. While the original SANAD 
study 33 is a randomized trial, the rate of drug titration—encompassing initial doses and 
subsequent dose adjustments—was determined by clinicians based on their judgment, 
effectively making it observational in nature. Speth et al. 15 highlighted that this setup provides a 
realistic scenario for evaluating DTRs, as the dosing adjustments introduce variability reflective 
of clinical practice. 
 
Following Speth et al.'s approach, we focused on the first two visits, where clinicians could 
adjust the dose based on patient outcomes. At each visit (
), the clinician could decrease (
𝑘> 1
), maintain (
), or increase (
) the dose. Patients were followed up regularly at 
𝐴𝑘= 1
𝐴𝑘= 2
𝐴𝑘= 3
intervals determined by clinical judgment, leading to variability in follow-up schedules. Due to 
the limited number of observed events beyond the third visit, the analysis was restricted to the 
first two visits to ensure a reliable estimation of optimal treatment regimes. The preprocessing 
12 

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
involved excluding 31 patients who did not receive treatment (zero initial and subsequent doses) 
from the analysis. This left 574 patients, with an event rate of approximately 33%.  
 
Baseline covariates included age, gender, and the presence of a learning disability (recorded as 
“Yes” or “No”). Longitudinal data encompassed the calibrated dose of medication at each visit, 
along with the start and end times of treatment intervals.  For stage 1 treatment prediction, we 
utilized age, gender, the start time of the dose interval, and the presence of a learning disability 
as input features. For stage 2 treatment prediction, we incorporated all stage 1 features along 
with the end time of the stage 1 interval and the corresponding dose amount. 
 
Analysis Results 
 
To evaluate the performance of the proposed model on this dataset, we employed 10-fold 
cross-validation due to the limited sample size. The proposed CA-TRL model demonstrated 
superior performance, achieving a restricted mean survival time (RMST) of 1742.67 with a 
standard error of 75.23, compared to ASCL, which achieved an RMST of 1509.12 with a 
standard error of 70.78. This difference is statistically significant (p < 0.05). Additionally, patients 
whose actual treatments aligned with the estimated optimal treatments recommended by 
CA-TRL exhibited significantly better survival outcomes than those whose treatments did not 
align with the recommendations (p < 0.05). At the initial visit, the estimated DTRs by CA-TRL 
suggest prescribing LTG to a greater number of individuals compared to the current treatment 
strategy. This observation aligns with prior findings 15,34, which highlight LTG's advantage over 
CBZ in reducing treatment failures, despite CBZ being the long-standing standard treatment. 
Discussion and Future Scope 
This work presents CA-TRL, a censoring-aware extension of tree-based reinforcement learning 
(T-RL), which addresses the critical need for robust estimation of dynamic treatment regimes 
(DTRs) in survival analysis. By integrating censoring adjustments and leveraging augmented 
inverse probability weighting (AIPW), CA-TRL successfully navigates challenges associated 
with incomplete data. The model’s performance was validated through rigorous simulations and 
real-world application, particularly on the SANAD dataset, where it outperformed 
state-of-the-art methods such as ASCL in key metrics like -restricted mean survival time (
τ
τ
-RMST) and decision accuracy. These results affirm CA-TRL’s potential to guide personalized 
treatment strategies in clinical practice. 
 
Despite its strengths, CA-TRL has certain limitations that warrant further research. First, the 
framework currently supports discrete treatment options, limiting its applicability to settings 
where treatments can be categorized into distinct groups. However, many real-world scenarios, 
such as drug dosage optimization, involve continuous treatment variables. Second, treatment 
selection bias remains a challenge, particularly in observational datasets where treatment 
assignments may reflect underlying clinician preferences. While CA-TRL incorporates 
13 

````

## PDF page 14

Technical extraction; compare with original PDF page 14.

````text
propensity score adjustments to mitigate confounding, residual bias could influence the 
estimated treatment regimes. Incorporating more sophisticated causal inference techniques 
could further strengthen the model’s robustness and reliability. Third, it employs a greedy 
approach when selecting splits, focusing solely on the purity improvement at the current node. 
While this strategy simplifies the tree construction process, it may not always lead to the global 
optimum in terms of overall decision rule performance. An alternative approach to enhance the 
performance of this method is to incorporate a "lookahead" mechanism 35. By evaluating 
potential future splits and their impact on downstream nodes, this method can identify splits 
that optimize the tree structure more holistically, potentially leading to better overall treatment 
decisions. Finally, while the method demonstrated promising results on the SANAD dataset, 
additional validation across diverse clinical conditions is necessary to generalize its 
applicability. Future studies could explore CA-TRL’s performance in domains such as 
cardiovascular diseases, and diabetes management, refining the methodology for specific 
clinical settings. 
Conclusions 
CA-TRL offers a robust and interpretable solution for estimating dynamic treatment regimes in 
settings with censored survival outcomes. By integrating censoring-aware adjustments and 
leveraging the strengths of tree-based methodologies, it provides an effective framework for 
personalized medicine. The model's superior performance in both simulated and real-world 
datasets highlights its potential to improve clinical decision-making. However, addressing 
limitations related to continuous treatments, and treatment selection bias will be critical for 
broader adoption. By pursuing these advancements and validating the approach across diverse 
medical domains, CA-TRL can serve as a transformative tool in precision medicine, fostering 
improved patient outcomes and personalized care strategies. 
Methods 
a.​Notation and assumptions 
We use the context of coronary artery disease (CAD) as a motivating example to illustrate the 
dynamic treatment regimes (DTR) framework. CAD is a leading cause of hospitalization and 
mortality worldwide, presenting a complex clinical challenge that necessitates personalized and 
adaptive treatment strategies to optimize survival outcomes. We focus on CAD in this study due 
to its clinical significance, high prevalence, and the availability of detailed patient data in the 
MIMIC-IV dataset 18. In our study, we assume treatment decisions are made over two stages to 
maximize the long-term outcome (the patient’s overall survival time): Stage 1, focusing on renal 
and anemia management, followed by stage 2, focusing on glycemic management. These 
stages reflect two critical aspects of CAD management that affect long-term outcomes. The 
event of interest is defined as a critical clinical endpoint (e.g., mortality) that could terminate 
14 

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
follow-up. It is important to note that this example is designed solely for experimental purposes, 
and actual treatment stages and options may differ in real-life clinical scenarios. 
 
We assume that data from 
 individuals are available. The data from the individuals are 
𝑁
independent, identically distributed (iid) copies of covariates (
), treatments (
), and outcomes 
𝑋𝑘
𝐴𝑘
(
) for all individuals, at each stage 
. In the CAD context, X includes patient clinical 
𝑅𝑘
𝑘
measurements such as age, creatinine, hemoglobin, potassium, sodium, glucose, platelet 
count, hematocrit, and white blood cell count. The treatment indicator 
 can represent a 
𝐴𝑘
multi-categorical or ordinal treatment, with observed values 
, where |
 | = 
𝑎𝑘∈ 𝐴𝑘
𝑜𝑝𝑡𝑖𝑜𝑛𝑠
𝐴𝑘
𝑜𝑝𝑡𝑖𝑜𝑛𝑠
 denotes the number of available treatment options at the stage . For instance, in the 
𝑀𝑘≥ 2
𝑘
CAD context, stage 1 focuses on renal and anemia management, with treatment options 
including conservative monitoring (observation without intervention), moderate support 
(medications or dietary adjustments for mild dysfunction), and aggressive intervention 
(treatment for severe anemia or renal dysfunction). If this stage finishes, the patient moves to 
Stage 2, which addresses glycemic management, with several treatment options: conservative 
glycemic management (dietary and lifestyle interventions), pharmacological intervention 
(glucose-lowering medications), versus aggressive glycemic control (intensive management 
using insulin or combination therapies). In this framework,  represents the overall observed 
𝑅
survival time, defined as 
, where 
 denotes the observed survival time at the stage  
𝑅=
𝑘=1
𝐾
∑𝑅𝑘
𝑅𝑘
𝑘
until the next stage or the event of interest. This serves as a quantitative measure for evaluating 
the effectiveness of treatment policies across the two stages. 
 
Individual data are represented as sequences of covariates, treatments, and outcomes [ [
, organized by stages, with each stage indicated by the subscript 
𝑋1, 𝐴1, 𝑅1], ..., [𝑋𝐾  , 𝐴𝐾  , 𝑅𝐾 ] ]
. Here, stages refer to distinct points in the treatment process where decisions are made about 
𝑘
interventions. Let individuals be identified with a superscript 
 , although this 
𝑖 ∈ {1, ..., 𝑁}
subscript is often omitted for simplicity.  For example, instead of explicitly writing [
 
𝑋𝑘
𝑖, 𝐴𝑘
𝑖, 𝑅𝑘
𝑖]
for the covariates, treatments, and outcomes of the individual  at the stage , we often simplify 
𝑖
𝑘
notation by using 
​, implicitly assuming that the data are indexed by  when referring 
[𝑋𝑘, 𝐴𝑘, 𝑅𝑘 ]
𝑖
to a single individual. 
 
The policy can use the values of the covariates 
 as they are known at the start of stage , to 
𝑋𝑘
𝑘
decide which treatment 
 to administer. This means the treatment options for the second stage 
𝐴𝑘
can be influenced by the treatment given in the first stage, as those second-stage covariates  
are determined by the treatment 
, covariates 
, and outcome observed during the first stage 
𝐴1
𝑋1
. 
𝑅1
 
15 

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
Let 
 represent the histories, which include (a function of) covariates, previous treatments, and 
ℎ𝑘
previous outcomes available at the start of the stage , used to guide the treatment decision for 
𝑘
that stage. For instance, 
 could be 
, where 
 is a 
ℎ𝑘
ℎ𝑘= 𝑓𝑘(𝑋1, 𝐴1, 𝑅1, ..., 𝑋𝑘−1, 𝐴𝑘−1, 𝑅𝑘−1, 𝑋𝑘)
𝑓𝑘( .)
function summarizing past information at stage . For example, perhaps 
 for the first 
𝑘
ℎ1 = 𝑋1
stage and 
 for the second stage, etc. In this paper, we specifically assume 
ℎ2 = (𝑋1, 𝐴1, 𝑅1, 𝑋2)
 to be the identity function, such that 
 for all . This means that the history 
 
𝑓𝑘(.)
𝑓𝑘(𝑄) = 𝑄
𝑘
ℎ𝑘
directly incorporates all covariates, treatments, and outcomes from prior stages up to stage , 
𝑘
without any transformation or aggregation. 
 
In the CAD context, at stage 1, the patient’s history 
 includes baseline covariates such as age, 
ℎ1
and laboratory values like creatinine and hemoglobin levels. Based on this history, the policy 
makes a treatment decision 
, such as prescribing a specific renal management strategy. The 
𝐴1
observed survival time during stage 1 is denoted by 
 representing the time until the next 
𝑇1 ∈ ℜ
decision point, which could be either another treatment stage or terminating the process 
(perhaps due to an event like kidney failure, or death). If there is no terminal event during stage 
1, the policy then always advances to stage 2. Here, the details of that next decision point are 
influenced by the patient's clinical progression and the effectiveness of the current treatment. 
For example, this waiting period for CAD patients could be clinically determined based on the 
patient's response to the initial treatment, the stability of their renal function, and other indicators 
such as hemoglobin levels. At this point, the policy uses the updated history 
, which 
ℎ2
incorporates the treatment from stage 1 
, the elapsed time 
 during stage 1, and additional 
𝐴1
𝑇1
covariates 
 such as glucose levels at the end of stage 1 (before the start of stage 2).  It can 
𝑋2
then use this 
 to decide on the next treatment action – e.g., to help guide decisions for 
ℎ2
glycemic management. Finally, we can have the observed stage-2 survival time 
,  
𝑇2 ∈ ℜ
representing the time until terminating the process (perhaps due to an event like kidney failure). 
The overall survival time for an individual is then defined as 
.  
𝑇= 𝑇1 + 𝑇2
 
However, not all patients experience the event of interest within the observation period 
, 
τ > 0
resulting in censored outcomes. Censoring can occur, for example, when the study concludes 
before a patient experiences the event (e.g., when 
) or when a patient is lost to follow-up, 
𝑇> τ
etc. When 
, no information on survival is available beyond the study length  in the 
𝑇> τ
τ
observed data, meaning the outcome of interest is truncated by . The overall censoring time  
τ
𝐶
marks the point when the observation of an individual's survival time stops without the event of 
interest occurring. If the censoring happens during an earlier stage, the patient does not 
progress to the next stage, which is another way the survival time  may be censored for some 
𝑇
CAD patients. 
 
Formally, let ηk be a random variable that equals 1 if an individual is known to enter stage k and 
0 otherwise, with the condition that η1 = 1 for all individuals (as we assume that no individual 
16 

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
can be censored before entering stage 1). Additionally, If 
, then for any future stage 
η𝑘= 0
𝑗> 𝑘
, 
. The duration of survival during each stage  is represented by 
, defined as the time 
η𝑗= 0
𝑘
𝑇𝑘
interval from the time the individual entered stage k until they either progress to stage 
 or 
𝑘+ 1
experience a terminating event such as failure or death, whichever occurs first. For an 
individual, this process generates a sequence of covariates, treatments, and outcomes [ [
, where the observed survival outcome is 
, and 
𝑋1, 𝐴1, 𝑅1], ..., [𝑋𝐾  , 𝐴𝐾  , 𝑅𝐾 ]  ]
𝑅𝑘= 𝑚𝑖𝑛(𝑇𝑘, 𝐶𝑘)
 represents the remaining censoring time at the stage , calculated based on the individual's 
𝐶𝑘
𝑘
overall censoring time  and their progression through the stages. Specifically, 
​ is defined as 
𝐶
𝐶𝑘
, where 
 represents the cumulative survival time up to stage 
. 
𝐶𝑘= 𝐶−
𝑗=1
𝑘−1
∑η𝑗+1𝑇𝑗
𝑗=1
𝑘−1
∑η𝑗+1𝑇𝑗
𝑘−1
The censoring indicator δk = I(Tk ≤ Ck) specifies whether the event occurred without censoring 
before the end of the stage 
. If censoring occurs at a given stage, no further outcomes, 
𝑘
treatments, or covariates are observed for subsequent stages – ie, this process just terminates. 
The observed outcome is defined as the overall survival time, which is the sum of the survival 
times across all stages, 
.  
𝑇=
𝑘=1
𝐾
∑η𝑘𝑅𝑘 
 
A 
Dynamic 
Treatment 
Regime 
(DTR) 
consists 
of 
a 
series 
of 
decision 
rules 
, where G represents the set of all possible treatment regimes. Each 
𝑔= [𝑔1(ℎ1),..., 𝑔𝐾(ℎ𝐾)] ∈𝐺
policy 
 comprises stage-specific decision rule functions 
. At each stage , the 
𝑔
[𝑔1, 𝑔2,..., 𝑔𝐾]
𝑘
decision rule 
 is a function that maps the history 
to a treatment, where 
 represents 
𝑔𝑘(.) ∈𝐺𝑘
ℎ𝑘 
𝐺𝑘
the set of all possible decision rules at the stage . This means that 
 provides a treatment 
𝑘
𝑔𝑘(ℎ𝑘)
recommendation based on the history up to stage .   
𝑘
 
The goal of an optimal DTR is to maximize the expected patient outcomes over the entire 
treatment course. To define this mathematically, we adopt a counterfactual framework. While  
𝑇
captures the observed survival through all K stages, 
 represents the potential (counterfactual) 
𝑇
*
survival outcome under another tuple of hypothetical treatment assignments. At the final stage 
K, let 
 represent the counterfactual outcome for a patient who received the 
𝑇
*(𝑎1,..., 𝑎𝐾)
treatments 
. For a specific treatment rule 
 , the counterfactual outcome 
 is given 
𝑎1,..., 𝑎𝐾
𝑔𝐾
𝑇
*(𝑔𝐾)
by:  
 
 
𝑇
*(𝑔𝐾) =
𝑎𝐾=1
𝑀𝐾
∑𝑇
*(𝑎𝑘) × 𝐼{𝑔𝐾(𝐻𝐾) == 𝑎𝐾}
 
where 
 is an indicator function that equals 1 if the treatment prescribed by 
𝐼{𝑔𝐾(𝐻𝐾) == 𝑎𝐾}
 matches 
. The performance of a treatment regime 
 is measured by the value 
𝑔𝐾(𝐻𝐾)
𝑎𝐾
𝑔
17 

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
function, 
, which represents the expected counterfactual outcome for all 
𝑉(𝑔) = 𝐸[𝑇
*(𝑔)]
individuals if they followed the regime . The optimal regime, denoted by 
, is the one that 
𝑔
𝑔
𝑜𝑝𝑡
maximizes this value function:  
. For example, in the case of the 
𝑉(𝑔
𝑜𝑝𝑡) ≥𝑉(𝑔), ∀𝑔 ∈𝐺 
aforementioned CAD example, the value function, 
, represents the expected survival time if 
𝑉(𝑔)
all patients follow a specific regime . The optimal regime, 
, maximizes 
, ensuring the 
𝑔
𝑔
𝑜𝑝𝑡
𝑉(𝑔)
longest expected survival across the population. 
 
Since only one of the counterfactual outcomes is observed for each individual, estimating the 
full counterfactual distribution requires specific assumptions. To address this challenge, we rely 
on the below key assumptions 11,15: 
 
●​ Positivity: This condition, 
), ensures that all 
𝑃(𝐴𝑘= 𝑎𝑘|𝐻𝑘= ℎ𝑘) > 0, ∀𝑎𝑘 ∈𝐴𝑘, ∀ℎ𝑘
individuals have a chance of receiving each treatment. In practice, violations commonly 
arise in the empirical sample when certain treatments are never (or almost never) 
prescribed to individuals with specific characteristics (e.g., sicker patients rarely receive a 
more intensive therapy). This can lead to regions of the covariate space where one 
treatment is effectively unavailable, making estimation of counterfactuals infeasible. 
●​ Consistency: The observed outcome for an individual under a given treatment matches 
the counterfactual outcome predicted under that treatment. 
●​ No unmeasured confounding: It ensures that, given the observed covariates, the 
treatment assignment is independent of the potential outcomes, or stated another way, 
the outcome of a treatment depends on the observed covariates, but NOT on the 
decision of which treatment to apply. For instance, for stage 1, 
, for stage 
𝑅1
*(𝑎1) ⊥ 𝐴1|𝐻1
2, 
, and so on, where 
 and 
 represent the potential 
𝑅2
*(𝑎1, 𝑎2) ⊥ 𝐴2|𝐻2
𝑅1
*(𝑎1)
𝑅2
*(𝑎1, 𝑎2)
outcomes corresponding to the respective treatment actions. This assumption enables 
valid causal inferences and is sometimes referred to as ‘strongly ignorable treatment 
assignment’ or ‘exchangeability’. For the longitudinal setting, this assumption requires 
that the treatment assignment at a given stage cannot depend on future covariates and 
treatment history. It is also called ‘sequential randomization’. This assumption is 
frequently the biggest challenge in observational data, where there may be variables 
related to both treatment decisions and outcomes that are not measured (unmeasured 
confounders). Violations can lead to biased estimates of causal effects. 
•​ No inference assumption: The outcome for any individual should not be influenced by the 
treatment assignment of another individual. It is also called ‘Stable unit treatment value’. It 
can be difficult to maintain in real-world clinical settings where doctors’ decisions for one 
patient often influence subsequent treatments and outcomes. 
18 

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
By adhering to these assumptions, the observed data can be linked to the counterfactual 
framework, allowing for valid causal inference and identification of optimal DTRs. 
Under these assumptions, the optimal decision rule 
 ​ at any stage k is derived recursively, 
𝑔𝑘
𝑜𝑝𝑡
starting from the final stage and moving backward. This is defined as: 
Final Stage : The optimal rule 
 ​ at the last stage K is 
𝐾
𝑔𝐾
𝑜𝑝𝑡
 
𝑔𝐾
𝑜𝑝𝑡= arg
𝑔𝐾∈𝐺𝐾
max 𝐸[
𝑎𝐾=1
𝑀𝑇
∑𝐸(𝑇|𝐴𝐾= 𝑎𝐾, 𝐻𝐾)𝐼(𝑔𝐾(𝐻𝐾) == 𝑎𝐾)]
Intermediate Stages 
:  For earlier stages, the optimal rule 
​ is defined 
( 𝑘 = 1 , … , 𝐾 − 1)
𝑔𝑘
𝑜𝑝𝑡
recursively, 
incorporating 
the 
expected 
outcomes 
of 
future 
stages. 
We 
consider 
, which represents the counterfactual outcome if a patient 
𝑇
*(𝐴1,..., 𝐴𝑘−1, 𝑔𝑘, 𝑔𝑘+1
𝑜𝑝𝑡,..., 𝑔𝐾
𝑜𝑝𝑡)
follows the decision rule 
​ at stage k, assuming that all future stages 
  are 
𝑔𝑘
(𝑘+ 1,..., 𝐾)
governed by the optimal rules 
​, given the treatments 
​ up to stage 
. 
𝑔𝑘+1
𝑜𝑝𝑡,..., 𝑔𝐾
𝑜𝑝𝑡
𝐴1,..., 𝐴𝑘−1
𝑘−1
At any intermediate stage , the optimal decision rule is given by: 
𝑘
​
𝑔𝑘
𝑜𝑝𝑡= arg
𝑔𝑘∈𝐺𝑘
max 𝐸[𝑇
*(𝐴1,..., 𝐴𝑘−1, 𝑔𝑘, 𝑔𝑘+1
𝑜𝑝𝑡,..., 𝑔𝐾
𝑜𝑝𝑡)]
 
= arg
𝑔𝑘∈𝐺𝑘
max 𝐸[
𝑎𝑘=1
𝑀𝑘
∑𝐸[𝑅𝑘|𝐴𝑘+1 = 𝑎𝑘, 𝐻𝑘)𝐼{𝑔𝐾(𝐻𝑘) == 𝑎𝑘}]] 
where, 
is the pseudo outcome at stage 
, representing an intermediate estimate of the 
𝑅𝑘
𝑘
counterfactual outcome based on observed data and accounting for the optimal decisions at 
future stages. 
b.​Censoring-Aware 
Tree-Based 
Reinforcement 
Learning 
(CA-TRL) 
Censoring-aware tree-based reinforcement learning builds on the foundational principles of 
decision trees and is inspired by the work of Tao et al. 11, who extended traditional tree-based 
methods to optimize counterfactual outcomes in dynamic treatment regimes (DTRs). Tao et al.'s 
framework focuses on complete datasets without censoring, where all outcomes are fully 
observed. In contrast, CA-TRL adapts this approach to address the complexities of 
right-censored survival data, making it applicable in settings where incomplete observations are 
prevalent. 
19 

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
Tree-Based Learning Framework 
The construction of decision trees in CA-TRL follows the idea of recursively partitioning the 
covariate space to create regions that maximize homogeneity based on a "purity" criterion. 
Unlike standard decision tree methods, such as Classification and Regression Trees (CART) 36, 
which rely on directly observed outcomes, CA-TRL focuses on counterfactual mean outcomes. 
These represent the expected results under hypothetical treatment assignments and serve as 
the foundation for assessing purity. 
At each stage of the tree-growing process, CA-TRL evaluates possible splits by calculating the 
counterfactual mean outcomes for the resulting child nodes. The purity improvement from a split 
is determined by comparing the counterfactual outcomes of the child nodes to the parent node. 
The split that maximizes this improvement is selected, ensuring that the tree partitions the 
covariate space in a way that optimizes treatment assignment. 
Recursive Partitioning for Counterfactual Optimization 
To guide the tree-growing process, CA-TRL employs a recursive partitioning framework. Let  
ϕ
denote a parent node and 
 a potential split at that node. The counterfactual purity measure 
ω
evaluates the counterfactual mean outcome for the split and without splitting. The optimal split 
 is selected to maximize the purity improvement. This recursive process continues until 
ω *
predefined stopping criteria are met, resulting in a tree structure that optimally partitions the 
covariate space to guide treatment decisions. 
Counterfactual Framework and Recursive Optimization 
The recursive optimization framework of CA-TRL ensures that decisions at each stage account 
for their impact on future outcomes. At stage , the counterfactual outcome is expressed as: 
𝑘
 
𝑇
*(𝐴1 , ···, 𝐴𝑘−1, 𝑔𝑘, 𝑔
𝑜𝑝𝑡
𝑘+1 , ···, 𝑔𝑇
𝑜𝑝𝑡​) 
representing the expected outcome for an individual following the decision rule 
​ at stage , 
𝑔𝑘
𝑘
assuming optimal decision rules are applied at all subsequent stages. This recursive structure 
aligns with Bellman’s principle of optimality and provides a framework for dynamically refining 
treatment rules based on evolving patient histories. 
CA-TRL incorporates pseudo-outcomes 
 at each stage to estimate counterfactual outcomes, 
𝑅𝑘
particularly in the presence of censoring. These pseudo-outcomes are adjusted to account for 
incomplete data and serve as substitutes for the unobserved counterfactual outcomes. By 
integrating these censoring-aware adjustments, as described in the later section on CA-TRL 
estimation for stage ,  CA-TRL ensures accurate and robust optimization of treatment rules. 
𝑘
 
20 

````

## PDF page 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
Stopping Rules to Prevent Overfitting 
CA-TRL employs stopping rules to prevent overfitting, following the framework of Tao et al.11, 
These rules include: 
1.​ Minimum Node Size: Nodes with fewer than 
 number of observations are not split, 
2𝑛0
where 
 denotes the minimum node size. 
𝑛0
2.​ Purity Improvement Threshold: Splits resulting in a minimal improvement in purity 
(below a threshold ) are disallowed. 
λ
3.​ Maximum Tree Depth: The tree-growing process is capped at a user-defined maximum 
depth. 
4.​ Child Node Size: Splits that create child nodes smaller than 
 observations are not 
𝑛0
performed. 
If none of these stopping rules are triggered, the node is split, and the tree continues to grow 
until the criteria are satisfied. 
CA-TRL estimation for the final stage  
𝐾
To address the causal objective of optimal DTR estimation at the final stage , we propose a 
𝐾
modified augmented inverse probability weighting estimator, specifically adapted for censored 
data. This approach builds upon the work of Tao et al. 11 and extends it to handle incomplete 
observations, ensuring robustness and accuracy in estimating counterfactual outcomes. The 
estimator for the counterfactual mean outcome at the final stage is given by 
 
 
 
µ
^𝐶𝐴𝐼𝑃𝑊
𝐾,𝑎𝐾
(𝐻𝐾) =
𝐼(𝐴==𝑎𝐾)δ𝐾
π
^
𝑎𝐾
(𝐻𝐾)𝑆𝐶
^ (𝑇|𝐻𝐾) 𝑇+ (1 −
𝐼(𝐴==𝑎𝐾)
π
^
𝑎𝐾
(𝐻𝐾) )µ
^
𝐾,𝑎𝐾
(𝐻𝐾)
where: 
●​
​ is the censoring indicator, 
δ𝐾
●​
 is the estimated propensity score for treatment 
​, 
π
^
𝑎𝐾
(𝐻𝐾)
𝑎𝐾
●​
 is the censoring survival probability conditional on the history 
​, 
𝑆𝐶(𝑇|𝐻𝐾)
𝐻𝐾
●​
 represents the conditional mean outcome, 
µ
^
𝐾,𝑎𝐾
(𝐻𝐾)
●​
 is the observed outcome (the overall survival time across all stages). 
𝑇
 
This estimator exhibits double robustness, meaning it remains consistent if either the propensity 
model 
 or the conditional mean model 
 is correctly specified. The censoring 
π
^
𝑎𝑘
(𝐻𝐾)
µ
^
𝐾,𝑎𝐾
(𝐻𝐾)
21 

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
survival probability 
 in the first term adjusts for the incomplete nature of the observed 
𝑆𝐶(𝑇|𝐻𝐾)
outcomes T, ensuring unbiased estimation. The second term does not require this adjustment, 
as the conditional mean model, such as random survival forests, directly accounts for censoring 
within its estimation. 
CA-TRL estimation for stages 
 
1,..., 𝐾−1
For intermediate stages 
, the estimation of dynamic treatment regimes 
(𝐾−1 ≥ 𝑘 ≥ 1)
involves a recursive process that propagates information from future stages back to earlier 
stages. This process relies on pseudo-outcomes that capture the cumulative effects of treatment 
decisions. 
We employ an adjusted version of pseudo-outcomes to mitigate the cumulative bias arising from 
the conditional mean models, as described by Huang et al. 37. For complete data, rather than 
relying solely on model-derived values under optimal future treatments (
), we 
µ
^
𝑘+1,𝑔
𝑜𝑝𝑡
𝑘+1
(𝐻𝑘+1)
incorporate observed outcomes along with the anticipated loss resulting from suboptimal 
treatments. In the case of censored data, the estimation is based exclusively on 
.  
µ
^
𝑘+1,𝑔
𝑜𝑝𝑡
𝑘+1
(𝐻𝑘+1)
The pseudo-outcome  
​ at stage  is defined as: 
𝑅𝑘
𝑘
 
 𝑅𝑘= δ𝑘+1( 𝑅𝑘+1 + µ
^
𝑘+1,𝑔
𝑜𝑝𝑡
𝑘+1
(𝐻𝑘+1) −µ
^
𝑘+1,𝐴𝑘+1
(𝐻𝑘+1)) + (1 −δ𝑘+1)µ
^
𝑘+1,𝑔
𝑜𝑝𝑡
𝑘+1
(𝐻𝑘+1)
where: 
●​
: Censoring indicator for stage 
 (
=1 if uncensored, 0 otherwise), 
δ𝑘+1
𝑘+ 1 δ𝑘+1
●​
​: Pseudo-outcome at the stage 
, 
𝑅𝑘
𝑘+ 1
●​
 : Expected outcome under the optimal treatment rule at the stage 
µ
^
𝑘+1,𝑔
𝑜𝑝𝑡
𝑘+1
(𝐻𝑘+1)
𝑘+ 1
, 
●​
: Expected outcome under the observed treatment 
  at the stage 
µ
^
𝑘+1,𝐴𝑘+1
(𝐻𝑘+1)
𝐴𝑘+1
. 
𝑘+ 1
The estimator for the counterfactual mean outcome at the stage is given by 
𝑘 
 
 
µ
^𝐶𝐴𝐼𝑃𝑊
𝑘,𝑎𝑘
(𝐻𝑘) =
𝐼(𝐴==𝑎𝑘)δ𝑘
π
^
𝑎𝑘
(𝐻𝑘)𝑆𝐶
^ (𝑅𝑘|𝐻𝑘) 𝑅𝑘+ (1 −
𝐼(𝐴==𝑎𝑘)
π
^
𝑎𝑘
(𝐻𝑘) )µ
^
𝑘,𝑎𝑘
(𝐻𝑘)
 
22 

````

## PDF page 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
Implementation of CA-TRL 
The implementation of CA-TRL begins with the stage 
, where the observed outcome  is 
𝐾
𝑇
directly used as the pseudo-outcome (
​), and proceeds via backward induction through 
𝑅𝐾= 𝑇
earlier stages. The propensity scores (
 ) are estimated using multinomial logistic 
π
^
𝑎𝑘
(𝐻𝑘)
regression, while the censoring survival probability  
 and the conditional mean outcome 
𝑆𝐶(𝑇|𝐻𝐾)
(
) are estimated using random survival forests. The pseudo-outcomes (
​) are 
µ
^
𝐾,𝑎𝑘
(𝐻𝑘)
𝑅𝑘
updated recursively, incorporating adjustments for censoring and the expected loss from 
suboptimal treatments, ensuring the robustness of the recursive estimation process and 
enabling effective handling of incomplete data. To optimize the performance of the proposed 
CA-TRL 
method, 
grid 
search 
was 
employed 
for 
hyperparameter 
tuning. 
The 
hyperparameters—number of trees, maximum tree depth, regularization parameter (𝜆), and 
minimum split size—were systematically varied. The optimal set of hyperparameters was 
selected based on the highest restricted mean survival time (RMST) value. This approach 
ensured robust and efficient tree-based estimation tailored to the dataset characteristics. 
 
 
 
References 
 
1.​
Murphy, S. A. Optimal dynamic treatment regimes. J. R. Stat. Soc. Series B Stat. Methodol. 
65, 331–355 (2003). 
2.​
Moodie, E. E. M., Richardson, T. S. & Stephens, D. A. Demystifying optimal dynamic 
treatment regimes. Biometrics 63, 447–455 (2007). 
3.​
Chakraborty, B. & Moodie, E. E. M. Statistical Methods for Dynamic Treatment Regimes: 
Reinforcement Learning, Causal Inference, and Personalized Medicine. (Springer Science 
& Business Media, 2013). 
4.​
Tsiatis, A. A., Davidian, M., Holloway, S. T. & Laber, E. B. Dynamic Treatment Regimes: 
Statistical Methods for Precision Medicine. (Productivity Press, New York, NY, 2019). 
doi:10.1201/9780429192692. 
5.​
Robins, J. A new approach to causal inference in mortality studies with a sustained 
exposure period—application to control of the healthy worker survivor effect. Math. Model. 
23 

````

## PDF page 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
7, 1393–1512 (1986). 
6.​
Watkins, C. J. C. H. & Dayan, P. Q-learning. Mach. Learn. 8, 279–292 (1992). 
7.​
Moodie, E. E. M. et al. A cure-rate model for Q-learning: Estimating an adaptive 
immunosuppressant treatment strategy for allogeneic hematopoietic cell transplant patients. 
Biom. J. 61, 442–453 (2019). 
8.​
Oh, S. H., Lee, S. J. & Park, J. Precision medicine for hypertension patients with type 2 
diabetes via reinforcement learning. J. Pers. Med. 12, 87 (2022). 
9.​
Schulte, P. J., Tsiatis, A. A., Laber, E. B. & Davidian, M. Q- and A-learning methods for 
estimating optimal dynamic treatment regimes. Stat. Sci. 29, 640–661 (2014). 
10.​ Clairon, Q., Henderson, R., Young, N. J., Wilson, E. D. & Taylor, C. J. Adaptive treatment 
and robust control. Biometrics 77, 223–236 (2021). 
11.​ Tao, Y., Wang, L. & Almirall, D. Tree-based reinforcement learning for estimating optimal 
dynamic treatment regimes. Ann. Appl. Stat. 12, 1914–1938 (2018). 
12.​ Tao, Y. & Wang, L. Adaptive contrast weighted learning for multi-stage multi-treatment 
decision-making. Biometrics 73, 145–155 (2017). 
13.​ Zhao, Y.-Q., Zhu, R., Chen, G. & Zheng, Y. Constructing dynamic treatment regimes with 
shared parameters for censored data. Stat. Med. 39, 1250–1263 (2020). 
14.​ Simoneau, G., Moodie, E. E. M., Nijjar, J. S., Platt, R. W. & the Scottish Early Rheumatoid 
Arthritis Inception Cohort Investigators. Estimating Optimal Dynamic Treatment Regimes 
With Survival Outcomes. J. Am. Stat. Assoc. 115, 1531–1539 (2020). 
15.​ Zhang, Z., Yi, D. & Fan, Y. Doubly robust estimation of optimal dynamic treatment regimes 
with multicategory treatments and survival outcomes. Stat Med 41, 4903–4923 (2022). 
16.​ Zhao, Y. Q. et al. Doubly Robust Learning for Estimating Individualized Treatment with 
Censored Data. Biometrika 102, 151–168 (2015). 
17.​ Choi, T., Lee, H. & Choi, S. Accountable survival contrast-learning for optimal dynamic 
treatment regimes. Sci. Rep. 13, 2250 (2023). 
24 

````

## PDF page 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
18.​ Johnson, A. E. W. et al. MIMIC-IV, a freely accessible electronic health record dataset. Sci. 
Data 10, 1 (2023). 
19.​ Gupta, M. et al. An extensive data processing pipeline for MIMIC-IV. arXiv [cs.LG] (2022). 
20.​ Go, A. S., Chertow, G. M., Fan, D., McCulloch, C. E. & Hsu, C.-Y. Chronic kidney disease 
and the risks of death, cardiovascular events, and hospitalization. N Engl J Med 351, 
1296–1305 (2004). 
21.​ Pan, J., Liu, M., Huang, J., Chen, L. & Xu, Y. Impact of anemia on clinical outcomes in 
patients with acute heart failure: A systematic review and meta-analysis. Clin Cardiol 47, 
e24228 (2024). 
22.​ Arant, C. B. et al. Hemoglobin level is an independent predictor for adverse cardiovascular 
outcomes in women undergoing evaluation for chest pain: results from the National Heart, 
Lung, and Blood Institute Women’s Ischemia Syndrome Evaluation Study. J Am Coll Cardiol 
43, 2009–2014 (2004). 
23.​ Siddiqui, S. W. et al. Anemia and Heart Failure: A Narrative Review. Cureus 14, e27167 
(2022). 
24.​ Dhatariya, K. & Umpierrez, G. E. Management of Diabetes and Hyperglycemia in 
Hospitalized Patients. in Endotext (eds. Feingold, K. R. et al.) (MDText.com, Inc., South 
Dartmouth (MA), 2024). 
25.​ Wilson, P. W. et al. Prediction of coronary heart disease using risk factor categories. 
Circulation 97, 1837–1847 (1998). 
26.​ O’Gara, P. T. et al. 2013 ACCF/AHA guideline for the management of ST-elevation 
myocardial infarction: a report of the American College of Cardiology Foundation/American 
Heart Association Task Force on Practice Guidelines. Circulation 127, e362–425 (2013). 
27.​ Adrogué, H. J. Hyponatremia in Heart Failure. Methodist Debakey Cardiovasc J 13, 40 
(2017). 
28.​ Vinholt, P. J. et al. Platelet count is associated with cardiovascular disease, cancer and 
25 

````

## PDF page 26

FORMULA CHECK REQUIRED: original PDF page 26.

````text
mortality: A population-based cohort study. Thromb Res 148, 136–142 (2016). 
29.​ Gagnon, D. R., Zhang, T. J., Brand, F. N. & Kannel, W. B. Hematocrit and the risk of 
cardiovascular disease--the Framingham study: a 34-year follow-up. Am Heart J 127, 
674–682 (1994). 
30.​ Madjid, M., Awan, I., Willerson, J. T. & Casscells, S. W. Leukocyte count and coronary heart 
disease: implications for risk assessment. J Am Coll Cardiol 44, 1945–1956 (2004). 
31.​ Kalbfleisch, J. D. & Prentice, R. L. The Statistical Analysis of Failure Time Data. (John 
Wiley & Sons, 2011). 
32.​ Fleming, T. R. & Harrington, D. P. Counting Processes and Survival Analysis. (John Wiley & 
Sons, 2013). 
33.​ Marson, A. G. et al. The SANAD study of effectiveness of carbamazepine, gabapentin, 
lamotrigine, oxcarbazepine, or topiramate for treatment of partial epilepsy: an unblinded 
randomised controlled trial. Lancet 369, 1000–1015 (2007). 
34.​ Williamson, P. R., Kolamunnage-Dona, R., Philipson, P. & Marson, A. G. Joint modelling of 
longitudinal and competing risks data. Stat. Med. 27, 6426–6438 (2008). 
35.​ Murthy, S. & Salzberg, S. Lookahead and pathology in decision tree induction. in 
Proceedings of the 14th international joint conference on Artificial intelligence - Volume 2 
1025–1031 (Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 1995). 
36.​ Breiman, L., Friedman, J. H., Olshen, R. A. & Stone, C. J. Classification And Regression 
Trees. (Routledge, 2017). 
37.​ Huang, X., Choi, S., Wang, L. & Thall, P. F. Optimization of multi-stage dynamic treatment 
regimes utilizing accumulated data. Stat. Med. 34, 3424–3443 (2015). 
 
26 

````

