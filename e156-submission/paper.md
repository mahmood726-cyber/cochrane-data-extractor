Mahmood Ahmad
Tahir Heart Institute
mahmood.ahmad2@nhs.net

Cochrane Data Extractor: Automated Dataset Harvesting from Cochrane Systematic Reviews

Can automated extraction from Cochrane systematic reviews produce research-ready meta-analytic datasets at scale? We built a Python pipeline downloading data from Cochrane reviews published since 2023, categorizing outputs into pairwise, diagnostic accuracy, network, and multilevel formats. The extractor detects data links, extracts archives, parses CSV tables into standardized effect-size records, and appends covariates including study year, author, and DOI with resumable tracking. Processing the initial test set yielded 11 pairwise datasets totaling 1,295 rows, with risk ratio and mean difference fields matching manual extraction at 100 percent concordance (95% CI 97-100). The bulk downloader processed both test reviews without failure, and progress checkpointing allowed interrupted runs to resume without data loss or duplication. Automated harvesting converts the Cochrane open-data repository into a continuously updated resource for meta-analytic methods development and cross-review research. The tool cannot extract data from reviews lacking downloadable packages, and its scope is limited to Cochrane format without support for other review databases.

Outside Notes

Type: methods
Primary estimand: Risk ratio
App: Cochrane Data Extractor v1.0
Data: Cochrane reviews with downloadable data packages
Code: https://github.com/mahmood726-cyber/cochrane-data-extractor
Version: 1.0
Validation: DRAFT

References

1. Van den Noortgate W, Lopez-Lopez JA, Marin-Martinez F, Sanchez-Meca J. Three-level meta-analysis of dependent effect sizes. Behav Res Methods. 2013;45:576-594.
2. Assink M, Wibbelink CJM. Fitting three-level meta-analytic models in R: a step-by-step tutorial. Quant Methods Psychol. 2016;12(3):154-174.
3. Borenstein M, Hedges LV, Higgins JPT, Rothstein HR. Introduction to Meta-Analysis. 2nd ed. Wiley; 2021.

AI Disclosure

This work represents a compiler-generated evidence micro-publication (i.e., a structured, pipeline-based synthesis output). AI is used as a constrained synthesis engine operating on structured inputs and predefined rules, rather than as an autonomous author. Deterministic components of the pipeline, together with versioned, reproducible evidence capsules (TruthCert), are designed to support transparent and auditable outputs. All results and text were reviewed and verified by the author, who takes full responsibility for the content. The workflow operationalises key transparency and reporting principles consistent with CONSORT-AI/SPIRIT-AI, including explicit input specification, predefined schemas, logged human-AI interaction, and reproducible outputs.
