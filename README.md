# FNBT-Loan-Risk-Analysis-Portfolio
An end-to-end data analysis portfolio project for the Data Analyst role at First National Bank Texas (FNBT).

## 🎯 Business Problem
First National Bank Texas (FNBT) aims to meet its aggressive growth and Return on Assets (ROA) goals while navigating the challenging economic environment, specifically the systemic risks associated with the **Commercial Real Estate (CRE)** market and the need to optimize loan product profitability.

This project implements an automated ETL and analysis pipeline to proactively:
1.  **Assess and segment high-risk loans** (e.g., CRE Office properties) based on key metrics like Loan-to-Value (LTV) and Days Past Due (DPD).
2.  **Analyze loan product profitability** to inform strategic capital allocation and optimize Net Interest Margin (NIM).

## ✨ Project Mapping to FNBT Data Analyst Role
This project directly addresses the core duties of the FNBT Data Analyst job description:
| Job Duty | Project Component |
| :--- | :--- |
| **Query and extract data** | Python data generation (`FNB_Loan_Data_Generator.ipynb`) simulates vendor program extraction. |
| **Maintain datasets using SQL** | Full SQL DDL and DML scripts (`BQ_Loan_Data_ETL.sql`) are used for maintenance in Google BigQuery. |
| **Integrate automation, ETL / ELT** | Python for data generation/cleansing and SQL for data loading/transformation demonstrate ETL/ELT expertise. |
| **Create and distribute reporting** | The Looker Studio Dashboard and `Stakeholder_Report.gdoc` serve as the final deliverable. |
| **Reconciliation of data loads** | SQL scripts include validation checks (e.g., row counts, unique constraints). |
| **Perform research and analysis** | The core Risk Score calculation and Profitability Segmentation are the final analytical products. |

## 🛠️ Tools & Technologies
* **Data Sourcing & ETL:** Python (Pandas, NumPy), Google Colab
* **Data Warehousing:** Google BigQuery (Project ID: `driiiportfolio`), SQL
* **Analysis & Modeling:** Python (Scikit-learn/Custom Risk Model)
* **Reporting & Visualization:** Looker Studio, Google Docs, Google Sheets
