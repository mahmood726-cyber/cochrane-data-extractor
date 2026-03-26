# CochraneDataExtractor: Automated Extraction of Study-Level Data from Cochrane Systematic Reviews

Mahmood Ahmad^1 | ^1 Royal Free Hospital, London, UK | mahmood.ahmad2@nhs.net | ORCID: 0009-0003-7781-4478

## Abstract

CochraneDataExtractor is a Python pipeline (~1,500 lines) that automatically extracts study-level meta-analytic data from Cochrane systematic reviews. Using Selenium browser automation and BeautifulSoup HTML parsing, the tool authenticates to the Cochrane Library, navigates review data tables, and extracts structured per-study data including effect sizes, confidence intervals, sample sizes, and subgroup classifications. Output is categorized into four meta-analysis types: pairwise, diagnostic test accuracy (DTA), network (NMA), and multilevel. The tool was used to construct the Pairwise70 dataset (501 reviews, 14,340 studies) and the DTA70 dataset (76 reviews, 1,966 studies), both widely used for meta-analytic methods research. Available at https://github.com/mahmood726-cyber/cochrane-data-extractor.

## Introduction

Large-scale meta-analytic methods research requires structured datasets from hundreds of systematic reviews. Manual extraction is prohibitively slow. CochraneDataExtractor automates this process, enabling construction of benchmark datasets for heterogeneity estimation, publication bias detection, and model comparison research.

## Implementation

The pipeline operates in three stages: (1) authentication to the Cochrane Library via Selenium WebDriver, (2) navigation and extraction of RevMan data tables using CSS selectors and BeautifulSoup, and (3) classification and export to structured CSV/RDA formats. Multi-strategy extraction handles variation in Cochrane review HTML structure across publication years. Error handling includes retry logic, session management, and partial-extraction recovery.

## Availability

Python 3.11+, requires Selenium + ChromeDriver. Source: https://github.com/mahmood726-cyber/cochrane-data-extractor

## Funding
None.

## References
1. Higgins JPT, et al. Cochrane Handbook for Systematic Reviews. Version 6.4, 2023.
2. Page MJ, et al. The PRISMA 2020 statement. BMJ. 2021;372:n71.
