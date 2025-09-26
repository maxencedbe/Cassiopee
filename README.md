# Cassiopee Project 
**Evaluation of anonymized databases regarding privacy risks using OSINT (Open Source Intelligence) sources**

## Overview
This repository contains the final report of the **Cassiopeia project**, carried out between January and June 2025.  
The objective of the project is to assess the risk of re-identification in anonymized databases by exploiting **OSINT** (Open Source Intelligence) sources.

## Authors
- Maxence Debes  
- Vadim Hemzellec-Davidson  

Supervised by:  
- Maryline Laurent  
- Louis Philippe Sondeck  

## Repository structure
- `RAPPORT_CASSIOPEE.pdf` : final project report.  
- `data/` : synthetic datasets used for testing.  
- `scripts/` : Python scripts for analysis and demonstrations.  
- `figures/` : illustrations and diagrams from the report.  
- `references/` : bibliography and additional resources.  

### Details of directories and scripts
- `elections/` : study on the results of the 2022 French presidential elections.  
  - `elections.py` : generates a spreadsheet listing the 10 smallest municipalities from the initial dataset.  
  - `elections2.py` : generates 3 spreadsheets listing the 10 municipalities that voted the most for each political orientation (left/ultra-left, presidential party, far-right).  

- `depression/` : study on a synthetic dataset related to mental health.  
  - Running the script generates an HTML page `result.html` listing unique profiles likely to be re-identified, with links to simulated Google searches.  

## Notes
All data used in this project is **synthetic or anonymized** in order to comply with confidentiality and regulatory requirements (GDPR).  

## License
Copyright Télécom SudParis and Institut Mines-Télécom,  
developed by Maxence DEBES and Vadim HEMZELLEC-DAVIDSON,  
based on an idea by Louis-Philippe SONDECK and Maryline LAURENT, 2025.  

Distributed under the **CC BY 4.0 license**.  
→ [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
