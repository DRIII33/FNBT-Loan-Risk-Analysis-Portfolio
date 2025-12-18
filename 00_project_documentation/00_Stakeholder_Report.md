## 📝 Stakeholder Report and Dashboard Summary
---

### **3.2 Stakeholder Report (00_Stakeholder_Report.md)**

**Title:** Loan Portfolio Risk & Profitability Strategic Review (Q4 2023)

#### **Executive Summary:**

This report outlines the results of a strategic data analysis on FNBT's loan portfolio, identifying key areas of credit risk concentration (specifically within **Commercial Real Estate - Office**) and providing an assessment of loan product profitability. Our analysis reveals a measurable high-risk exposure that warrants immediate portfolio management action, while also confirming the continued profitability of the Residential Mortgage and Consumer Auto segments. This is essential for meeting the bank's 2024 ROA target.

#### **Methodology (Data Analysis & Stakeholder Delivery Framework):**

* **Acquire & ETL (Python/SQL):** Simulated data extraction, initial cleansing (FNB_Loan_Data_Generator.ipynb), and robust ETL/ELT in BigQuery (BQ_Loan_Data_ETL.sql) to ensure data quality and integrity (reconciliation checks).
* **Transform & Model (SQL/Python):** Creation of two critical analytical features in BigQuery: **LTV Bucket** and the **Aggregated Risk Score** (a weighted average of LTV and DPD, with high scores indicating elevated risk).
* **Analyze (Python):** Focused Python analysis on CRE-Office exposure and a calculation of **Net Interest Income (NII)** to determine product profitability.
* **Visualize & Report (Looker Studio/Google Docs):** Presented key findings in a clear, digestible dashboard for executive review.

#### **Key Findings & Recommendations:**

| Finding | Recommendation |
| --- | --- |
| **Credit Risk Concentration:** A significant portion of the total Commercial Real Estate (CRE) portfolio is concentrated in the Office segment, a sector currently under duress due to macroeconomic factors (high interest rates, remote work). | **Prioritize stress testing** on all CRE Office loans with an Aggregated Risk Score \ge 4.0. These loans should be immediately flagged for a deeper credit review or potential strategic loan sale to reduce future charge-offs. |
| **Profitability Drivers:** The Residential Mortgage and Consumer Auto segments are the primary drivers of Net Interest Income (NII). | **Allocate capital and marketing resources** to profitable segments, especially within the high-performing Killeen, TX Metro region, to ensure consistent, quality growth as FNBT pursues its asset growth targets. |

#### **Data Quality and Reconciliation Summary:**

* **Reconciliation:** Initial load count from the simulated vendor system matched the BigQuery staging table count, confirming a successful ETL.
* **Exception Handling:** All null values for key risk factors (Credit Score, DTI) were successfully converted to a standard sentinel value (-1) during the BigQuery ELT process, ensuring the data is reliable for downstream analysis and modeling.

---

### **3.3 Looker Studio Dashboard (Conceptual)**

The final deliverable is a dashboard to visually communicate the findings to stakeholders.

**Dashboard Title:** FNBT Loan Portfolio Risk & Profitability Monitor

| Section | Visualization Type | Key Metric/Focus | Stakeholder Value |
| --- | --- | --- | --- |
| **I. Key Performance Indicators (KPIs)** | Scorecards | Total Current Loan Balance, Total Monthly NII, High-Risk Balance (Aggregated Score \ge 4.0), CRE-Office 90+ DPD Rate. | Quick view of overall portfolio health and risk exposure. |
| **II. Credit Risk Distribution** | Stacked Bar Chart | Loan Status by Aggregated Risk Score Bucket. | Visualizes where the most immediate risk (DPD) sits within the LTV/DPD score. |
| **III. Strategic Exposure View** | Pie Chart/Treemap | Current Balance by Purpose Segment (CRE Focus). Highlight the "Office" segment in red/amber. | Demonstrates the concentration risk identified in the research. |
| **IV. Profitability & Efficiency** | Bar Chart | Monthly Net Interest Income (NII) by Loan Type. | Informs capital allocation strategy by showing the most/least profitable products. |
| **V. Geographic Health** | Filter/Scorecard | Risk Profile (Aggregated Score Average) for Killeen, TX Metro vs. Other Regions. | Provides local context, aligning with the Killeen-specific job location. |

---
