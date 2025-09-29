# Cassiopee Project
**Evaluation of anonymized databases regarding privacy risks using OSINT (Open Source Intelligence) sources.**

## Overview
This repository contains the final report of the **Cassiopeia project**, carried out between January and June 2025.
The objective of the project is to assess the risk of re-identification in anonymized databases by exploiting **OSINT** (Open Source Intelligence) sources.

## Authors
- Maxence DEBES
- Vadim Hemzellec-Davidson

Supervised by:
- Maryline LAURENT
- Louis Philippe SONDECK

## Repository structure
- `Rapport Cassiopée.pdf` : final project report (in French).
- `data/` : synthetic datasets used for testing.
- `scripts/` : Python scripts for analysis and demonstrations.
- `figures/` : illustrations and diagrams from the report.
- `references/` : bibliography and additional resources.

## Details of directories and scripts

- **`data/`**
  Contains the input datasets used for analysis.
  - `data/depression/Student Depression Dataset.csv` → synthetic dataset on student mental health.
  - `data/elections/` → official dataset of the 2022 French presidential election results (CSV and Excel formats).

- **`scripts/`**
  Contains Python scripts reproducing the analyses from the report.
  - `scripts/elections/elections.py` → generates the list of the 10 smallest municipalities.
  - `scripts/elections/elections2.py` → generates 3 spreadsheets with the top 10 municipalities voting mostly for left/ultra-left, presidential party, or far-right.
  - `scripts/depression/depression.py` → analyzes the mental health dataset and generates `depression.html` showing unique profiles at risk of re-identification.

- **`results/`**  
  Contains the outputs produced by running the scripts.
  - `results/elections/` → processed Excel files with subsets of election data.
  - `results/depression/depression.html` → HTML page displaying unique profiles and simulated re-identification risks.

## Notes
All data used in this project is **synthetic or anonymized** in order to comply with confidentiality and regulatory requirements (GDPR).

## License
Copyright Télécom SudParis and Institut Mines-Télécom,
developed by Maxence DEBES and Vadim HEMZELLEC-DAVIDSON,
based on an idea by Louis-Philippe SONDECK and Maryline LAURENT, 2025.

Distributed under the **CC BY 4.0 license**.
→ [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
