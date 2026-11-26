# The optimal conditioning intensity of stem cell transplantation for acute myeloid leukemia in complete remission

Source: [original.xml](original.xml).

PAGINATION UNAVAILABLE: this original JATS XML does not supply a verified PDF page map. Sections and original formula markup are preserved; no PDF pages are invented. TeX-math and MathML blocks below are original XML content, not reconstructed equations. Formula images remain unresolved and are flagged.



This study aimed to identify patient groups in which myeloablative conditioning (MAC) or reduced-intensity conditioning (RIC) regimens induced superior progression-free survival (PFS) in patients with acute myeloid leukemia (AML) in complete remission (CR) using a machine-learning approach. Our study included 3273 patients aged 40–69 with AML in CR. The patients were divided into training (N = 2020) and validation cohorts (N = 1253). We employed a machine learning-based group identification model in the training cohort. Subsequently, in the validation cohort, we estimated the impact of the optimal conditioning group compared with the non-optimal conditioning group on PFS using an inverse probability weight analysis. The developed model was consistent with the eight factors and combinations, and the high score suggested that RIC was more appropriate than MAC. In the validation cohort, 127 patients with high scores and who received RIC and 769 patients with low scores and who received MAC were categorized into the optimal conditioning group (896, 71.5%). The weighted hazard ratio for PFS was 0.73 (95% confidence interval: 0.57–0.94) in the optimal conditioning group compared with the non-optimal conditioning group (P = 0.016). In conclusion, we developed an easy-to-use model that helps the physician choose a patient-specific conditioning regimen for patients with AML in CR.



### Supplementary Information


The online version contains supplementary material available at 10.1007/s00277-026-06881-w.





### Introduction


Acute myeloid leukemia (AML) is a heterogeneous disease characterized by the uncontrolled proliferation of myeloid cells. Notably, most patients with AML achieve complete remission (CR) upon induction chemotherapy; however, the risk of relapse is considerable [1]. Allogeneic hematopoietic stem cell transplantation (HSCT) is one of the curative options for AML with CR to prevent relapse [1]. The conditioning regimen before HSCT is crucial in immunosuppression to facilitate engraftment and eliminate residual AML cells. Conventionally, allogeneic HSCT is limited to younger and fit patients eligible for myeloablative conditioning (MAC). However, improvements in supportive therapy and the introduction of reduced-intensity conditioning (RIC) have recently increased the number of patients eligible for allogeneic HSCT. RIC is generally associated with a higher relapse rate and lower non-relapse mortality than MAC [2–12]. Therefore, striking the appropriate balance between reducing relapse rates and managing non-relapse mortality remains a critical challenge in allogeneic HSCT.

Several retrospective studies have revealed that RIC has a progression-free survival similar to MAC in patients with AML in CR. However, these results raised concerns regarding patient selection bias due to the retrospective nature of the studies [2–4]. Consequently, some randomized controlled trials have evaluated conditioning intensity, yielding inconsistent results [5–12]. This inconsistency may be attributed to differences in patient characteristics. Studies focusing on patients with more favorable disease status found that RIC had similar PFS to MAC [5, 6]. In contrast, a study focusing on patients with poorer disease status found that RIC had an inferior PFS than MAC [7, 8]. These retrospective studies and randomized control trials primarily focused on the average treatment effect for all enrolled patients, potentially overlooking significant heterogeneous treatment effects, which may be present even in comparing comparable patient groups [13–15]. Notably, some studies have delved into specific subgroups, revealing the heterogeneity of the conditioning intensity’s treatment effect [16–19]. However, these analyses have generally considered only one factor at a time rather than a multiple-factor combination that could generate heterogeneity [20, 21]. Therefore, the optimal conditioning intensity for each patient with AML in CR is difficult to establish because of the heterogeneity among the patients. Recently, some machine-learning methods for group identification have been developed to overcome standard comparison-study and subgroup-analysis limitations [13–15]. Therefore, this study aimed to identify groups in which MAC or RIC had a superior PFS in patients with AML in CR using a machine-learning method.




### Materials and methods




### Study patients


Our study included 3273 patients with AML in CR (Fig. 1). All patients were enrolled in the Transplant Registry Unification Management Program 2 (TRUMP 2) of the Japanese Data Center for Hematopoietic Cell Transplantation (JDCHCT) between 2009 and 2019. This study enrolled patients who recieved a well-identified conditioning regimen as cyclophosphamide and total body irradiation (CY/TBI), a myeloablative dose of busulfan and cyclophosphamide (Bu/Cy), fludarabine and a myeloablative dose of busulfan (FB4), fludarabine and a myeloablative dose of busulfan and melphalan (FBM), fludarabine and a non-myeloablative dose of busulfan (FB2), and fludarabine and melphalan (FM). Subsequently, we divided the remaining patients into training and validation cohorts based on when they underwent transplantation (training cohort: 2009–2015; validation cohort: 2016–2019). Fig. 1

Patient Selection Flow. AML, acute myeloid leukemia; Bu/Cy, busulfan and cyclophosphamide; CR, complete remission; CY/TBI, cyclophosphamide and total body irradiation; FB2, fludarabine and a non-myeloablative dose of busulfan; FB4, fludarabine and a myeloablative dose of busulfan; FBM, fludarabine, a myeloablative dose of busulfan and melphalan; FM, fludarabine and melphalan; HLA, human leukocyte antigen; HSCT, hematopoietic stem cell transplantation and TRUMP2; transplant registry unified management program 2. The well-defined conditioning regimens included CY/TBI, Bu/Cy, FB4, FBM, FB2, and FM

[ORIGINAL IMAGE / POSSIBLE FORMULA: 277_2026_6881_Fig1_HTML.jpg; not reconstructed]

Patient consent was obtained before the TRUMP 2 registration. This study was approved by the Data Management Committee of the JDCHCT and the Ethics Committee of Osaka University (approval number: 22143).




### Definitions, handling of missing data, and endpoints


All variables were obtained from the JDCHCT-registry database. The definitions of these conditioning regimens were as follows: CY/TBI, 120 mg/kg cyclophosphamide and > 8 Gy total body irradiation; Bu/Cy, 6.4–12.8 mg/kg busulfan and 120 mg/kg cyclophosphamide; FB4, 120–200 mg/m2 fludarabine and 6.4–12.8 mg/kg busulfan; FBM, 120–200 mg/m2 fludarabine, 6.4–12.8 mg/kg buslfan, and 80–140 mg/m2 melphalan; FB2, 120–200 mg/m2 fludarabine and ≤ 6.4 mg/kg buslfan; and FM, 120–200 mg/m2 fludarabine and < 140 mg/kg melphalan. Based on previous reports, the MAC regimen was defined as CY/TBI, Bu/Cy, FB4, FBM, and RIC as FB2 and FM [22, 23]. The hematopoietic cell transplantation-specific comorbidity index (HCT-CI) was defined as described previously [24]. We imputed the missing values using the “missforest” package in the R software, which used a non-parametric algorithm through a random forest method [25, 26]. The patient characteristics and missing values before and after imputation are shown in Supplemental Tables 1 and Table 1, respectively. We set the primary endpoint as 1-year PFS, the time from allogeneic HSCT to relapse or any cause of death, because conditioning intensity may contribute to short-term outcomes. We also evaluated the cumulative incidence of relapse and non-relapse mortality (NRM) as secondary endpoints. Relapse was defined as the hematological evidence of AML. NRM was defined as death without a relapse. Relapse was considered a competing NRM risk and vice versa.



Table 1

Patient characteristics

CharacteristicOverall, N = 3,2741Training, N = 2,0201Validation, N = 1,2531p-value2Age55 (48, 62)55 (48, 61)56 (48, 62)0.239 Age > 492,272 (69%)1,402 (69%)870 (69%)0.987 Age > 591,110 (34%)685 (34%)425 (34%)0.996 Age > 64395 (12%)218 (11%)177 (14%)0.004Male sex1,802 (55%)1,111 (55%)691 (55%)0.934Performance Status0 (0, 1)0 (0, 1)0 (0, 1)0.352 Performance Status > 1108 (3.3%)65 (3.2%)43 (3.4%)0.739HCT-CI0 (0, 2)0 (0, 2)0 (0, 2)0.085 HCT-CI > 1904 (28%)542 (27%)362 (29%)0.200 HCT-CI > 2539 (16%)311 (15%)228 (18%)0.036 HCT-CI > 3206 (6.3%)114 (5.6%)92 (7.3%)0.052Disease Status< 0.001 1st CR2,468 (75%)1,488 (74%)980 (78%) 2nd CR~805 (25%)532 (26%)273 (22%)0.003Karyotype Risk0.062 Favorite391 (12%)227 (11%)164 (13%) Intermediate2,385 (73%)1,501 (74%)884 (71%) Poor497 (15%)292 (14%)205 (16%)Treatment-related AML146 (4.5%)89 (4.4%)57 (4.5%)0.847Myelodysplastic Related Change725 (22%)431 (21%)294 (23%)0.154Extra bone marrow involvement220 (6.7%)133 (6.6%)87 (6.9%)0.690Donor Source< 0.001 Bone marrow1,718 (52%)1,169 (58%)549 (44%) Peripheral blood511 (16%)261 (13%)250 (20%) Cord blood1,044 (32%)590 (29%)454 (36%)Unrelated donor Transplantation1,612 (49%)1,043 (52%)569 (45%)< 0.001HLA mismatched1326 (10.0%)192 (9.5%)134 (11%)0.269Reduced-intensity conditioning regimen978 (30%)666 (33%)312 (25%)< 0.001Detailed conditioning regimens< 0.001 CY/TBI742 (23%)513 (25%)229 (18%) BuCy439 (13%)256 (13%)183 (15%) FBM250 (7.6%)75 (3.7%)175 (14%) FB4864 (26%)510 (25%)354 (28%) FM523 (16%)349 (17%)174 (14%) FB2455 (14%)317 (16%)138 (11%)
1HLA mismatch was not included in cord blood transplantation

AML, acute myeloid leukemia; Bu/Cy, busulfan and cyclophosphamide; CR, complete remission; CY/TBI, cyclophosphamide and total body irradiation; FB2, fludarabine and a non-myeloablative dose of busulfan; FB4, fludarabine and a myeloablative dose of busulfan; FBM, fludarabine, a myeloablative dose of busulfan and melphalan; FM, fludarabine and melphalan; HCT-CI, hematopoietic cell transplant comorbidity index. HLA, human leukocyte antigen; MAC, myeloablative conditioning regimen; RIC, reduced-intensity conditioning regimen







### Machine-learning model for identifying optimal conditioning intensity


We first preprocessed the variables to ensure the model’s performance and easy application in clinical practice. Continuous variables were converted into categorical variables. Then, we selected those with P for interaction on PFS ≤ 0.5 to the final candidate. Age and HCT-CI were considered final candidates for the cutoff with the lowest P for interaction because they are vital factors in determining conditioning intensity. The interaction terms of the final candidates were created and used for model development. The flowchart of this method is shown in Supplemental Fig. 1. The primary candidate variables, P for interaction, and the final candidates used to develop the model are summarized in Supplemental Table 2.

Furthermore, we used the group identification model to estimate patient subsets with substantially different heterogeneous treatment effects within a training cohort, as described previously [14]. The framework only models the relationship between covariates pertinent to group identification and the outcome change when the individual has a different treatment. Therefore, we modeled the magnitude of the interaction between treatment and covariates without the main effect of covariates, thus constructing a scoring system that measures the individualized treatment effect [14, 15]. The objective variable was the restricted mean survival time for 1-year PFS, and we estimated the interaction effects between treatment and covariates using the regression model with propensity score weight and lasso regularization. The developed model was defined as the “Model for RIC vs. MAC (RICMAC model),” and the sum of the interaction term between treatment and covariates was defined as the “RICMAC score.” In the model, the high RICMAC score suggested that RIC was more appropriate than MAC. In addition, we divided patients into two groups (High-score and Low-score groups), with the median in patients who received RIC as the cutoff level. The methods were performed using the “personalized” package in the R software.




### Statistical analysis


Patient and disease characteristics were compared using the Mann–Whitney U and chi-square tests for continuous and categorical variables. Event rates were estimated using the Kaplan–Meier method for the PFS and Gray’s method for the cumulative incidence of relapse rate and NRM. We defined patients who had high scores and received RIC or who had low scores and received MAC as the optimal conditioning group and others as the non-optimal conditioning group. We estimated the impact of optimal conditioning compared with non-optimal conditioning using Cox proportional hazards models for PFS and the Fine and Gray method for relapse and NRM. Additionally, we divided patients who had high scores and low scores. For each subgroup, we estimated the therapeutic impact of RIC compared with that of MAC.

The endpoints were described using adjusted hazard ratios (HRs) and 95% confidence intervals (CIs). Gray’s method and Fine and Gray’s methods were used to consider the competing risks. We used the inverse probability weight (IPW) analysis to reduce the effect of confounding factors in these analyses [27]. First, we calculated the propensity score and the probability of receiving RIC using a logistic regression model considering the following factors: Age, sex, HCT-CI, PS, CR status, karyotype risk, treatment-related AML, AML with myelodysplastic change, extra bone marrow involvement, source, an unrelated donor in bone marrow or peripheral blood transplantation, HLA mismatch in bone marrow or peripheral blood transplantation. We then calculated the average treatment effect weight, which was defined as 1/PS for patients receiving RIC and 1/(1-PS) for patients receiving MAC. Using the Cox regression analysis, we used this weight to adjust for confounding factors. Statistical significance was set at P < 0.05. All statistical analyses were performed using the R software (version 4.0.2; R Development Core Team).





### Results




### Study patients


We analyzed 3273 patients, divided into training (n = 2020) and validation (n = 1,253) cohorts. The patients’ clinical characteristics are shown in Table 1. In the training cohort, the median age was 55 years (IQR, 48–61 years), 1402 patients (69%) were aged > 50 years, and 1110 (55%) were male. Regarding the conditioning intensity and outcomes, 666 patients (33%) underwent RIC, whereas the other 1354 (67%) underwent MAC. In the training cohort, the 1-year PFS was 63.4% (95% CI: 59.6–67.0%) and 65.8% (95% CI: 63.2–68.3%) in the RIC and MAC groups, respectively (P = 0.275, Supplemental Fig. 2A). In the validation cohort, the median age was 56 years (IQR, 48–62 years); 871 patients (69%) were aged > 50 years, and 691 (55%) were men. Regarding conditioning intensity and outcomes, 313 patients (25%) underwent RIC, and 940 (75%) underwent MAC. The 1-year PFS was 67.7% (95% CI: 62.1–72.6%) and 70.3% (95% CI: 67.2–73.1%) in the RIC and MAC groups, respectively (P = 0.318, Supplemental Fig. 2B).




### Model development and performance


The RICMAC model was developed based on the training cohort. The model was consistent with eight variables and combinations (Table 2). The sum of the model was defined as the RICMAC score, and the median of the score was 2.1 (1.4–2.2) in patients who received RIC and 1.4 (0-2.1) in those who received MAC. We set the cutoff value to 2.1, the median RICMAC score in patients receiving RIC. The patient characteristics are shown in Supplemental Table 3. Then, we divided patients into the optimal conditioning group and non-optimal conditioning group and evaluated the impact of the optimal conditioning group compared with that of the non-optimal conditioning group using the IPW analysis. The weighted HR of the optimal conditioning group compared to the non-optimal conditioning group on the PFS, relapse, and NRM was 0.80 (95%CI; 0.67–0.96, p = 0.014), 0.93 (95%CI; 0.71–1.21, p = 0.580) and 0.75 (95%CI: 0.59–0.94, p = 0.014), respectively (Supplemental Fig. 3). The detailed outcomes of the training cohort are presented in Supplemental Fig. 4 and Supplemental Table 4.



Table 2

Developed model for RIC vs. MAC

Conditioning Intensity ModelVariablesScoreAge > 491.4 and male Sex0.7 and poor Karyotype risk0.8 and cord blood transplantation0.8Poor karyotype risk
-1.2
 and bone marrow transplantation
-5.6
Cord blood transplantation and hematopoietic cell comorbidity index > 22.0 and extra bone marrow involvement
-8.0







### Transplant outcomes in the validation cohort


We calculated the RICMAC score in the validation cohort to validate the model and divided the patients into high- and low-score groups. The validation cohort’s detailed patient characteristics are shown in Table 3. In the cohort, 127 patients who had high scores and received RIC and 769 patients who had low scores and received MAC were categorized into the optimal conditioning group (total: 896, 71.5%). The 1-year PFS was 71.9% (95% CI: 68.8–74.7%) in the optimal conditioning group vs. 64.1% (95% CI: 58.8–68.9%) in the non-optimal conditioning group (log-rank P = 0.005) (Fig. 2A). The weighted hazard ratio (HR) for PFS was 0.73 (95% confidence interval [CI]: 0.57–0.94) in the optimal conditioning group compared with the non-optimal conditioning group (P = 0.016). The 1-year relapse rate was 14.3% (95% CI: 12.1–16.7%) in the optimal conditioning group vs. 15.5% (95% CI: 11.9–19.5%) in the non-optimal conditioning group (log-rank P = 0.516) (Fig. 2B) and the 1-year NRM was 13.8% (95% CI: 11.6–16.2%) in the optimal conditioning group vs. 20.4% (95% CI: 16.3–20.8%) in the MAC group (log-rank P = 0.005) (Fig. 2C). The weighted HR for the optimal conditioning group compared with that of the non-optimal conditioning group was 0.85 (95% CI: 0.59–1.23, P = 0.385) for the cumulative incidence of relapse and 0.68 (95% CI: 0.48–0.98, P = 0.036) for the cumulative incidence of NRM. The detailed outcomes are presented in Supplemental Fig. 5 and Supplemental Table 5.



Table 3

Patient characteristics in the validation cohort

CharacteristicHigh-ScoreLow-ScoreOverallN = 299MACN = 172RICN = 127p-valueOverallN = 954MACN = 769RICN = 185p-valueAge
61

(56, 64)

59

(54, 63)

63

(58, 66)
< 0.001
52

(46, 60)

50

(45, 58)

60

(56, 64)
< 0.001Male sex171 (57%)101 (59%)70 (55%)0.534520 (55%)416 (54%)104 (56%)0.603Performance Status0 (0, 1)0 (0, 1)0 (0, 1)0.0580 (0, 1)0 (0, 1)0 (0, 1)0.064Hematopoietic Cell Transplant. Comorbidity Index1 (0, 2)1 (0, 2)1 (0, 3)0.5800 (0, 2)0 (0, 1)0 (0, 2)0.006First complete remission235 (79%)132 (77%)103 (81%)0.364745 (78%)595 (77%)150 (81%)0.274Karyotype Risk0.1420.034 Favorite29 (9.7%)20 (12%)9 (7.1%)135 (14%)116 (15%)19 (10%) Intermediate228 (76%)124 (72%)104 (82%)656 (69%)532 (69%)124 (67%) Poor42 (14%)28 (16%)14 (11%)163 (17%)121 (16%)42 (23%)Treatment-related AML22 (7.4%)9 (5.2%)13 (10%)0.10135 (3.7%)28 (3.6%)7 (3.8%)0.926Myelodysplastic Related Change84 (28%)47 (27%)37 (29%)0.731210 (22%)160 (21%)50 (27%)0.067Extra bone marrow involvement0 (0%)0 (0%)0 (0%)1.00087 (9.1%)73 (9.5%)14 (7.6%)0.414Primary induction failure14 (4.7%)9 (5.2%)5 (3.9%)0.60062 (6.5%)53 (6.9%)9 (4.9%)0.315Donor Source1.0000.004 Bone marrow0 (0%)0 (0%)0 (0%)549 (58%)423 (55%)126 (68%) Peripheral blood0 (0%)0 (0%)0 (0%)250 (26%)211 (27%)39 (21%) Cord blood299 (100%)172 (100%)127 (100%)155 (16%)135 (18%)20 (11%)Unrelated Donor Transplantation0 (0%)0 (0%)0 (0%)569 (60%)439 (57%)130 (70%)0.001HLA mismatched10 (0%)0 (0%)0 (0%)134 (14%)97 (13%)37 (20%)0.009Detailed conditioning regimens< 0.001< 0.001 CY/TBI20 (6.7%)20 (12%)0 (0%)209 (22%)209 (27%)0 (0%) BuCy5 (1.7%)5 (2.9%)0 (0%)178 (19%)178 (23%)0 (0%) FBM98 (33%)98 (57%)0 (0%)77 (8.1%)77 (10%)0 (0%) FB449 (16%)49 (28%)0 (0%)305 (32%)305 (40%)0 (0%) FM98 (33%)0 (0%)98 (77%)76 (8.0%)0 (0%)76 (41%) FB229 (9.7%)0 (0%)29 (23%)109 (11%)0 (0%)109 (59%)
1HLA mismatch was not included in cord blood transplantation

Bu/Cy, busulfan and cyclophosphamide; CY/TBI, cyclophosphamide and total body irradiation; FB2, fludarabine, and non-myeloablative busulfan; FB4, fludarabine and myeloablative busulfan; FBM, fludarabine, myeloablative busulfan and melphalan; FM, fludarabine and melphalan; HLA, human leukocyte antigen; MAC, myeloablative conditioning regimen; RIC, reduced-intensity conditioning regimen


Fig. 2

Progression-free survival, relapse, and non-relapse mortality comparing optimal conditioning group vs. non-optimal conditioning group in validation cohort. Progression-free survival in the training cohort (A) and in the validation cohort (B). The numbers at the bottom of the figure represent each group’s at-risk numbers. MRM, non-relapse mortality; and PFS, progression-free survival

[ORIGINAL IMAGE / POSSIBLE FORMULA: 277_2026_6881_Fig2_HTML.jpg; not reconstructed]






### Discussion


This multicenter registry-based study developed a RICMAC model to identify patient groups in which RIC had superior PFS to MAC or those in which MAC had superior PFS to RIC in patients with AML in CR. The patients were divided into two subgroups based on the RICMAC score and received conditioning. The optimal conditioning group had a superior 1-year PFS compared with the non-optimal conditioning group due to a lower 1-year NRM. This information is essential for hematologists because conditioning regimens can be selected independently of the background of patients with AML in CR. On the other hand, most studies using machine learning in the HSCT setting have aimed to predict prognosis, such as NRM, acute graft versus host disease, and so on [28, 29]. We used a machine learning model to help determine treatment decisions. Although further efforts are needed to improve the accuracy of the models and validate the model, it is possible that treatment decisions can be made more accurately using such a method.

Randomized control trials and several observational studies have compared the conditioning intensity in patients with AML in CR [2–12]. A randomized control trial compared MAC and RIC in 272 patients aged 18–65 years with AML or MDS in CR. In this study, RIC resulted in a lower NRM but a higher relapse rate than MAC, with a significant advantage in PFS with MAC [7]. A long-term follow-up of the study confirmed the superiority of MAC for the enrolled patients [8]. Guideline recommended MAC for fit patients with AML in CR because MAC had similar to better outcomes compared to RIC [30]. However, RIC had some advantages over MAC, including fewer adverse events and a lower incidence of graft-versus-host disease. Therefore, identifying subgroups of patients who would benefit from RIC is crucial. In addition, these RCT which compared MAC and RIC focused on relatively young and fit patients as those only eligible for MAC [5–7]. However, improvements in conditioning regimens and supportive care have expanded eligibility of MAC, considering older and relatively unfit patients suitable candidates for MAC. Registry-based studies conducted on middle-aged patients with AML in CR revealed that RIC had a similar PFS, with higher relapse rates and lower NRM in patients with AML in CR. However, the results were similar to other registry-based studies and had concerns regarding selection biases [4]. The heterogeneity may be present even in comparable patients in intervention or observation groups, as we previously described [13]. Therefore, finding optimal conditioning intensity for each patient is important for selecting conditioning regimen. Our study used a machine learning-based identification model to establish RICMAC model for patients aged > 40 years with AML in CR. According to the developed model and received conditioning, we divided patients into optimal conditioning and non-optimal conditioning groups and revealed optimal conditioning group had a superior PFS than non-optimal conditioning group. Although 71.5% of study patients were included into optimal conditioning group, remaining 28.5% patients may improve prognosis with change in conditioning intensity.

Notably, some studies have focused on the heterogeneous treatment effect and performed a subgroup analysis with single patient factors [16–19]. Additional analysis of randomized controlled trials that compared outcomes based on conditioning intensity revealed that MAC had superior survival than RIC in patients with measurable residual disease. Conversely, MAC had a similar survival rate to RIC in patients without measurable residual disease [18]. A Japanese registry-based study found that MAC had superior survival than RIC in patients with poor-risk AML. In this study, the survival rates using MAC were similar to those observed using RIC in other patients, although inconsistent results were reported in retrospective studies and subgroup analysis of prospective control trials [12, 16, 17]. These studies also have very critical findings; however, they can only address one variable, and further detailed subgroup analysis reduces the power of detection. A study using the Japanese registry attempted to identify groups with better RIC and MAC using multiple factors similar to ours [31]. In the study, NRM was used as the primary endpoint and was performed on patients aged > 50 years who had received a transplant. They created a RICE score based on age, cord blood transplantation, and HCT-CI. However, the study did not evaluate recurrence because it included various diseases. Therefore, increasing conditioning intensity should usually reduce recurrence, and the sensitivity of conditioning intensity might differ among hematological diseases. Our study was performed in patients aged > 40 years with AML in CR, and PFS was the primary endpoint. We developed the RICMAC model using a lasso-based machine learning method. Our study showed that combining patient factors and each variable’s influence scale is vital. Our study used a different methodology; however, the model’s components were similar to those in previous studies [16, 31]. Furthermore, this model particularly affected NRM, confirming that the model’s components influence the RIC vs. MAC NRM. Conversely, our model probably slightly affects the relapse rate because the recurrence rate was not high in our study patients, including those with relatively high-risk AML. The lack of factors associated with the risk of relapse, including MRD data, may also be a factor. Therefore, the model could be improved by including factors strongly associated with recurrence.

Our study has several limitations. First, we did not consider some essential factors, especially measurable residual disease and genetic data. They influence the selection of conditioning intensity and are associated with outcomes after allogeneic HSCT. Measurable residual disease may alter the beneficial effects of the conditioning regimen [18, 32]. Additionally, some information on the treatment course prior to HSCT was unavailable, including details on pre-HSCT chemotherapy exposure. Second, we used lasso regression, an interpretable machine learning method; however, the effects of some factors on conditioning intensity cannot be fully explained. Third, whether the external validity is maintained in different environments remains unclear. Therefore, external validation studies using other registries should be conducted. Fourth, we extracted well-defined conditioning regimens, categorized them as RIC or MAC, and compared them. However, some reports showed that a specific conditioning regimen is associated with poor or better outcomes in patients with RIC or MAC [33]. Our study could not consider these results.

In conclusion, we demonstrated the feasibility of using a machine-learning method for the subgroup identification of conditioning regimens in patients with AML in CR. The established RICMAC model is easy to use and is helpful for a more patient-specific choice of conditioning regimens. 




### Supplementary Information


Below is the link to the electronic supplementary material.




Supplementary Material 1 (DOCX 1.41 MB)






Publisher’s note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


### Acknowledgements


The authors thank all the physicians and data managers at the centers that contributed to the collection of data on transplantation for the Japanese Data Center for Hematopoietic Cell Transplantation and Transplant Registry Unified Management Program 2.


### Author contributions


YS designed the study, developed the models, performed statistical analysis, and wrote the first draft of the manuscript. SK and TK contributed to the development of the model and data analysis. SK, TK, TS, SY, TK, SM, KH, and MY critically reviewed the data analysis and manuscript. All the other authors contributed to data collection. All the authors approved the final version of the manuscript.


### Funding


None.


### Data availability


The data for this study are not publicly available because of ethical restrictions that exceed the scope of the recipient’s or donor’s consent for research use in the registry.


### Declarations



### Ethics approval


This study was approved by the Data Management Committee of the JDCHCT and the Ethics Committee of Osaka University (approval number: 22143).


### Patient Concent


Patient consent was obtained before the TRUMP 2 registration.


### Competing interests


The authors declare no competing interests.


### References


1.CornelissenJJBlaiseDHematopoietic stem cell transplantation for patients with AML in first complete remissionBlood2016127627010.1182/blood-2015-07-60454626660427Cornelissen JJ, Blaise D (2016) Hematopoietic stem cell transplantation for patients with AML in first complete remission. Blood 127:62–70. 10.1182/blood-2015-07-60454626660427
10.1182/blood-2015-07-604546

2.SengsayadethSSavaniBNBlaiseDReduced intensity conditioning allogeneic hematopoietic cell transplantation for adult acute myeloid leukemia in complete remission - a review from the acute leukemia working party of the EBMTHaematologica201510085986910.3324/haematol.2015.12333126130513PMC4486220Sengsayadeth S, Savani BN, Blaise D et al (2015) Reduced intensity conditioning allogeneic hematopoietic cell transplantation for adult acute myeloid leukemia in complete remission - a review from the acute leukemia working party of the EBMT. Haematologica 100:859–869. 10.3324/haematol.2015.12333126130513
10.3324/haematol.2015.123331PMC4486220

3.RingdénOLabopinMEhningerGReduced intensity conditioning compared with myeloablative conditioning using unrelated donor transplants in patients with acute myeloid leukemiaJ Clin Oncol Off J Am Soc Clin Oncol2009274570457710.1200/JCO.2008.20.969219652066Ringdén O, Labopin M, Ehninger G et al (2009) Reduced intensity conditioning compared with myeloablative conditioning using unrelated donor transplants in patients with acute myeloid leukemia. J Clin Oncol Off J Am Soc Clin Oncol 27:4570–4577. 10.1200/JCO.2008.20.969210.1200/JCO.2008.20.969219652066

4.AoudjhaneMLabopinMGorinNCComparative outcome of reduced intensity and myeloablative conditioning regimen in HLA identical sibling allogeneic Haematopoietic stem cell transplantation for patients older than 50 years of age with acute myeloblastic leukaemia: a retrospective survey from the acute leukemia working party (ALWP) of the European group for blood and marrow transplantation (EBMT)Leukemia2005192304231210.1038/sj.leu.240396716193083Aoudjhane M, Labopin M, Gorin NC et al (2005) Comparative outcome of reduced intensity and myeloablative conditioning regimen in HLA identical sibling allogeneic Haematopoietic stem cell transplantation for patients older than 50 years of age with acute myeloblastic leukaemia: a retrospective survey from the acute leukemia working party (ALWP) of the European group for blood and marrow transplantation (EBMT). Leukemia 19:2304–2312. 10.1038/sj.leu.240396716193083
10.1038/sj.leu.2403967

5.BornhäuserMKienastJTrenschelRReduced-intensity conditioning versus standard conditioning before allogeneic Haemopoietic cell transplantation in patients with acute myeloid leukaemia in first complete remission: a prospective, open-label randomised phase 3 trialLancet Oncol2012131035104410.1016/S1470-2045(12)70349-222959335Bornhäuser M, Kienast J, Trenschel R et al (2012) Reduced-intensity conditioning versus standard conditioning before allogeneic Haemopoietic cell transplantation in patients with acute myeloid leukaemia in first complete remission: a prospective, open-label randomised phase 3 trial. Lancet Oncol 13:1035–1044. 10.1016/S1470-2045(12)70349-222959335
10.1016/S1470-2045(12)70349-2

6.KrögerNIacobelliSFrankeG-NDose-Reduced versus standard conditioning followed by allogeneic Stem-Cell transplantation for patients with myelodysplastic syndrome: A prospective randomized phase III study of the EBMT (RICMAC Trial)J Clin Oncol Off J Am Soc Clin Oncol2017352157216410.1200/JCO.2016.70.734928463633Kröger N, Iacobelli S, Franke G-N et al (2017) Dose-Reduced versus standard conditioning followed by allogeneic Stem-Cell transplantation for patients with myelodysplastic syndrome: A prospective randomized phase III study of the EBMT (RICMAC Trial). J Clin Oncol Off J Am Soc Clin Oncol 35:2157–2164. 10.1200/JCO.2016.70.734910.1200/JCO.2016.70.734928463633

7.ScottBLPasquiniMCLoganBRMyeloablative versus Reduced-Intensity hematopoietic cell transplantation for acute myeloid leukemia and myelodysplastic syndromesJ Clin Oncol Off J Am Soc Clin Oncol2017351154116110.1200/JCO.2016.70.7091PMC545560328380315Scott BL, Pasquini MC, Logan BR et al (2017) Myeloablative versus Reduced-Intensity hematopoietic cell transplantation for acute myeloid leukemia and myelodysplastic syndromes. J Clin Oncol Off J Am Soc Clin Oncol 35:1154–1161. 10.1200/JCO.2016.70.709110.1200/JCO.2016.70.7091PMC545560328380315

8.ScottBLPasquiniMCFeiMMyeloablative versus Reduced-Intensity conditioning for hematopoietic cell transplantation in acute myelogenous leukemia and myelodysplastic Syndromes—Long-Term Follow-Up of the BMT CTN 0901 clinical trialTranspl Cell Ther202127483e110.1016/j.jtct.2021.02.031PMC821737333775615Scott BL, Pasquini MC, Fei M et al (2021) Myeloablative versus Reduced-Intensity conditioning for hematopoietic cell transplantation in acute myelogenous leukemia and myelodysplastic Syndromes—Long-Term Follow-Up of the BMT CTN 0901 clinical trial. Transpl Cell Ther 27:483e1. 10.1016/j.jtct.2021.02.03110.1016/j.jtct.2021.02.031PMC821737333775615

9.BlaiseDTabriziRBoherJRandomized study of 2 reduced-intensity conditioning strategies for human leukocyte antigen‐matched, related allogeneic peripheral blood stem cell transplantation: prospective clinical and socioeconomic evaluationCancer201311960261110.1002/cncr.2778622893313Blaise D, Tabrizi R, Boher J et al (2013) Randomized study of 2 reduced-intensity conditioning strategies for human leukocyte antigen‐matched, related allogeneic peripheral blood stem cell transplantation: prospective clinical and socioeconomic evaluation. Cancer 119:602–611. 10.1002/cncr.2778622893313
10.1002/cncr.27786

10.BeelenDWTrenschelRStelljesMTreosulfan or Busulfan plus fludarabine as conditioning treatment before allogeneic Haemopoietic stem cell transplantation for older patients with acute myeloid leukaemia or myelodysplastic syndrome (MC-FludT.14/L): a randomised, non-inferiority, phase 3 trialLancet Haematol20207e28e3910.1016/S2352-3026(19)30157-731606445Beelen DW, Trenschel R, Stelljes M et al (2020) Treosulfan or Busulfan plus fludarabine as conditioning treatment before allogeneic Haemopoietic stem cell transplantation for older patients with acute myeloid leukaemia or myelodysplastic syndrome (MC-FludT.14/L): a randomised, non-inferiority, phase 3 trial. Lancet Haematol 7:e28–e39. 10.1016/S2352-3026(19)30157-731606445
10.1016/S2352-3026(19)30157-7

11.RambaldiAGrassiAMasciulliABusulfan plus cyclophosphamide versus Busulfan plus fludarabine as a preparative regimen for allogeneic Haemopoietic stem-cell transplantation in patients with acute myeloid leukaemia: an open-label, multicentre, randomised, phase 3 trialLancet Oncol2015161525153610.1016/S1470-2045(15)00200-426429297Rambaldi A, Grassi A, Masciulli A et al (2015) Busulfan plus cyclophosphamide versus Busulfan plus fludarabine as a preparative regimen for allogeneic Haemopoietic stem-cell transplantation in patients with acute myeloid leukaemia: an open-label, multicentre, randomised, phase 3 trial. Lancet Oncol 16:1525–1536. 10.1016/S1470-2045(15)00200-426429297
10.1016/S1470-2045(15)00200-4

12.CraddockCJacksonALokeJAugmented Reduced-Intensity regimen does not improve postallogeneic transplant outcomes in acute myeloid leukemiaJ Clin Oncol20213976877810.1200/JCO.20.0230833373276PMC8078252Craddock C, Jackson A, Loke J et al (2021) Augmented Reduced-Intensity regimen does not improve postallogeneic transplant outcomes in acute myeloid leukemia. J Clin Oncol 39:768–778. 10.1200/JCO.20.0230833373276
10.1200/JCO.20.02308PMC8078252

13.ShimomuraYKomukaiSKitamuraTIdentifying the optimal conditioning intensity for stem cell transplantation in patients with myelodysplastic syndrome: a machine learning analysisBone Marrow Transpl20235818619410.1038/s41409-022-01871-836376472Shimomura Y, Komukai S, Kitamura T et al (2023) Identifying the optimal conditioning intensity for stem cell transplantation in patients with myelodysplastic syndrome: a machine learning analysis. Bone Marrow Transpl 58:186–194. 10.1038/s41409-022-01871-810.1038/s41409-022-01871-836376472

14.Huling JD, Yu M (2021) Subgroup identification using the personalized package. J Stat Softw 98. 10.18637/jss.v098.i05

15.ChenSTianLCaiTYuMA general statistical framework for subgroup identification and comparative treatment scoringBiometrics2017731199120910.1111/biom.1267628211943PMC5561419Chen S, Tian L, Cai T, Yu M (2017) A general statistical framework for subgroup identification and comparative treatment scoring. Biometrics 73:1199–1209. 10.1111/biom.1267628211943
10.1111/biom.12676PMC5561419

16.KonumaTKondoTMizunoSConditioning intensity for allogeneic hematopoietic cell transplantation in acute myeloid leukemia patients with Poor-Prognosis cytogenetics in first complete remissionBiol Blood Marrow Transpl20202646347110.1016/j.bbmt.2019.09.02531562960Konuma T, Kondo T, Mizuno S et al (2020) Conditioning intensity for allogeneic hematopoietic cell transplantation in acute myeloid leukemia patients with Poor-Prognosis cytogenetics in first complete remission. Biol Blood Marrow Transpl 26:463–471. 10.1016/j.bbmt.2019.09.02510.1016/j.bbmt.2019.09.02531562960

17.PasswegJRLabopinMCornelissenJConditioning intensity in middle-aged patients with AML in first CR: no advantage for myeloablative regimens irrespective of the risk group–an observational analysis by the acute leukemia working party of the EBMTBone Marrow Transpl2015501063106810.1038/bmt.2015.12126030052Passweg JR, Labopin M, Cornelissen J et al (2015) Conditioning intensity in middle-aged patients with AML in first CR: no advantage for myeloablative regimens irrespective of the risk group–an observational analysis by the acute leukemia working party of the EBMT. Bone Marrow Transpl 50:1063–1068. 10.1038/bmt.2015.12110.1038/bmt.2015.12126030052

18.HouriganCSDillonLWGuiGImpact of conditioning intensity of allogeneic transplantation for acute myeloid leukemia with genomic evidence of residual diseaseJ Clin Oncol Off J Am Soc Clin Oncol2020381273128310.1200/JCO.19.03011PMC716448731860405Hourigan CS, Dillon LW, Gui G et al (2020) Impact of conditioning intensity of allogeneic transplantation for acute myeloid leukemia with genomic evidence of residual disease. J Clin Oncol Off J Am Soc Clin Oncol 38:1273–1283. 10.1200/JCO.19.0301110.1200/JCO.19.03011PMC716448731860405

19.GilleeceMHLabopinMYakoub-AghaIMeasurable residual disease, conditioning regimen intensity, and age predict outcome of allogeneic hematopoietic cell transplantation for acute myeloid leukemia in first remission: A registry analysis of 2292 patients by the acute leukemia working party EAm J Hematol2018931142115210.1002/ajh.2521129981272Gilleece MH, Labopin M, Yakoub-Agha I et al (2018) Measurable residual disease, conditioning regimen intensity, and age predict outcome of allogeneic hematopoietic cell transplantation for acute myeloid leukemia in first remission: A registry analysis of 2292 patients by the acute leukemia working party E. Am J Hematol 93:1142–1152. 10.1002/ajh.2521129981272
10.1002/ajh.25211

20.VanderWeeleTJKnolMJInterpretation of subgroup analyses in randomized trials: heterogeneity versus secondary interventionsAnn Intern Med201115468068310.7326/0003-4819-154-10-201105170-0000821576536PMC3825512VanderWeele TJ, Knol MJ (2011) Interpretation of subgroup analyses in randomized trials: heterogeneity versus secondary interventions. Ann Intern Med 154:680–683. 10.7326/0003-4819-154-10-201105170-0000821576536
10.7326/0003-4819-154-10-201105170-00008PMC3825512

21.BaumAScarpaJBruzeliusETargeting weight loss interventions to reduce cardiovascular complications of type 2 diabetes: a machine learning-based post-hoc analysis of heterogeneous treatment effects in the look AHEAD trialLancet Diabetes Endocrinol2017580881510.1016/S2213-8587(17)30176-628711469PMC5815373Baum A, Scarpa J, Bruzelius E et al (2017) Targeting weight loss interventions to reduce cardiovascular complications of type 2 diabetes: a machine learning-based post-hoc analysis of heterogeneous treatment effects in the look AHEAD trial. Lancet Diabetes Endocrinol 5:808–815. 10.1016/S2213-8587(17)30176-628711469
10.1016/S2213-8587(17)30176-6PMC5815373

22.GiraltSBallenKRizzoDReduced-intensity conditioning regimen workshop: defining the dose spectrum. Report of a workshop convened by the center for international blood and marrow transplant researchBiol Blood Marrow Transpl J Am Soc Blood Marrow Transpl20091536736910.1016/j.bbmt.2008.12.497PMC311008719203728Giralt S, Ballen K, Rizzo D et al (2009) Reduced-intensity conditioning regimen workshop: defining the dose spectrum. Report of a workshop convened by the center for international blood and marrow transplant research. Biol Blood Marrow Transpl J Am Soc Blood Marrow Transpl 15:367–369. 10.1016/j.bbmt.2008.12.49710.1016/j.bbmt.2008.12.497PMC311008719203728

23.BacigalupoABallenKRizzoDDefining the intensity of conditioning regimens: working definitionsBiol Blood Marrow Transpl J Am Soc Blood Marrow Transpl2009151628163310.1016/j.bbmt.2009.07.004PMC286165619896087Bacigalupo A, Ballen K, Rizzo D et al (2009) Defining the intensity of conditioning regimens: working definitions. Biol Blood Marrow Transpl J Am Soc Blood Marrow Transpl 15:1628–1633. 10.1016/j.bbmt.2009.07.00410.1016/j.bbmt.2009.07.004PMC286165619896087

24.SorrorMLMarisMBStorbRHematopoietic cell transplantation (HCT)-specific comorbidity index: a new tool for risk assessment before allogeneic HCTBlood20051062912291910.1182/blood-2005-05-200415994282PMC1895304Sorror ML, Maris MB, Storb R et al (2005) Hematopoietic cell transplantation (HCT)-specific comorbidity index: a new tool for risk assessment before allogeneic HCT. Blood 106:2912–2919. 10.1182/blood-2005-05-200415994282
10.1182/blood-2005-05-2004PMC1895304

25.StekhovenDJBühlmannPMissForest–non-parametric missing value imputation for mixed-type dataBioinforma Oxf Engl20122811211810.1093/bioinformatics/btr59722039212Stekhoven DJ, Bühlmann P (2012) MissForest–non-parametric missing value imputation for mixed-type data. Bioinforma Oxf Engl 28:112–118. 10.1093/bioinformatics/btr59710.1093/bioinformatics/btr59722039212

26.WaljeeAKMukherjeeASingalAGComparison of imputation methods for missing laboratory data in medicineBMJ Open20133e00284710.1136/bmjopen-2013-00284723906948PMC3733317Waljee AK, Mukherjee A, Singal AG et al (2013) Comparison of imputation methods for missing laboratory data in medicine. BMJ Open 3:e002847. 10.1136/bmjopen-2013-00284723906948
10.1136/bmjopen-2013-002847PMC3733317

27.KurthTWalkerAMGlynnRJResults of multivariable logistic Regression, propensity Matching, propensity Adjustment, and propensity-based weighting under conditions of nonuniform effectAm J Epidemiol200616326227010.1093/aje/kwj04716371515Kurth T, Walker AM, Glynn RJ et al (2006) Results of multivariable logistic Regression, propensity Matching, propensity Adjustment, and propensity-based weighting under conditions of nonuniform effect. Am J Epidemiol 163:262–270. 10.1093/aje/kwj04716371515
10.1093/aje/kwj047

28.ShouvalRLabopinMBondiOPrediction of Allogeneic Hematopoietic Stem-Cell Transplantation Mortality 100 Days After Transplantation Using a Machine Learning Algorithm: A European Group for Blood and Marrow Transplantation Acute Leukemia Working Party Retrospective Data Mining StudyJ Clin Oncol Off J Am Soc Clin Oncol2015333144315110.1200/JCO.2014.59.133926240227Shouval R, Labopin M, Bondi O et al (2015) Prediction of allogeneic hematopoietic stem-cell transplantation mortality 100 days after transplantation using a machine learning algorithm: a European Group for Blood and Marrow Transplantation Acute Leukemia Working Party retrospective data mining study. J Clin Oncol Off J Am Soc Clin Oncol 33:3144–3151. 10.1200/JCO.2014.59.133910.1200/JCO.2014.59.133926240227

29.AraiYKondoTFuseKUsing a machine learning algorithm to predict acute graft-versus-host disease following allogeneic transplantationBlood Adv201933626363410.1182/bloodadvances.201900093431751471PMC6880900Arai Y, Kondo T, Fuse K et al (2019) Using a machine learning algorithm to predict acute graft-versus-host disease following allogeneic transplantation. Blood Adv 3:3626–3634. 10.1182/bloodadvances.201900093431751471
10.1182/bloodadvances.2019000934PMC6880900

30.DholariaBSavaniBNHamiltonBKHematopoietic cell transplantation in the treatment of newly diagnosed adult acute myeloid leukemia: an Evidence-Based review from the American society of transplantation and cellular therapyTranspl Cell Ther20212762010.1016/j.bbmt.2020.09.02032966881Dholaria B, Savani BN, Hamilton BK et al (2021) Hematopoietic cell transplantation in the treatment of newly diagnosed adult acute myeloid leukemia: an Evidence-Based review from the American society of transplantation and cellular therapy. Transpl Cell Ther 27:6–20. 10.1016/j.bbmt.2020.09.02010.1016/j.bbmt.2020.09.02032966881

31.AkahoshiYTadaYSakaidaENovel risk assessment for the intensity of conditioning regimen in older patientsBlood Adv202374738474710.1182/bloodadvances.202200870636508283PMC10468368Akahoshi Y, Tada Y, Sakaida E et al (2023) Novel risk assessment for the intensity of conditioning regimen in older patients. Blood Adv 7:4738–4747. 10.1182/bloodadvances.202200870636508283
10.1182/bloodadvances.2022008706PMC10468368

32.LindsleyRCSaberWMarBGPrognostic mutations in myelodysplastic syndrome after Stem-Cell transplantationN Engl J Med201737653654710.1056/NEJMoa161160428177873PMC5438571Lindsley RC, Saber W, Mar BG et al (2017) Prognostic mutations in myelodysplastic syndrome after Stem-Cell transplantation. N Engl J Med 376:536–547. 10.1056/NEJMoa161160428177873
10.1056/NEJMoa1611604PMC5438571

33.ShimomuraYHaraMYamamotoHAdding Melphalan to fludarabine and a myeloablative dose of Busulfan improved survival after allogeneic hematopoietic stem cell transplantation in a propensity score-matched cohort of hematological malignanciesBone Marrow Transpl2021561691169910.1038/s41409-021-01217-w33658646Shimomura Y, Hara M, Yamamoto H et al (2021) Adding Melphalan to fludarabine and a myeloablative dose of Busulfan improved survival after allogeneic hematopoietic stem cell transplantation in a propensity score-matched cohort of hematological malignancies. Bone Marrow Transpl 56:1691–1699. 10.1038/s41409-021-01217-w10.1038/s41409-021-01217-w33658646
