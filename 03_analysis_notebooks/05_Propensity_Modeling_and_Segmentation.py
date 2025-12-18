from google.colab import auth
auth.authenticate_user()
--------
import sys
#INSTALL PACKAGES
!{sys.executable} -m pip install pandas
!{sys.executable} -m pip install numpy
!{sys.executable} -m pip install seaborn
!{sys.executable} -m pip install matplotlib
!{sys.executable} -m pip install google-cloud-bigquery

--------
# 05_Propensity_Modeling_and_Segmentation.ipynb
# Project: FNBT-Loan-Risk-Analysis-Portfolio
# Purpose: Research and analysis of risk profiles to drive strategic outreach.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.cloud import bigquery

# --- 1. Data Extraction (Job Duty: Query and extract data for analysis) ---
client = bigquery.Client(project='driiiportfolio')
query = "SELECT * FROM `driiiportfolio.fnbt_ds.vw_customer_risk_profile`"
df = client.query(query).to_dataframe()

# Print columns to debug missing 'ltv_ratio'
print("DataFrame Columns:")
print(df.columns)

# --- 2. Descriptive Analysis: The "Office" Problem ---
office_stress = df[df['purpose_segment'] == 'Office'].copy()
killeen_office_risk = office_stress.groupby('region_killeen')['aggregated_risk_score'].mean()

print("--- Regional Risk Analysis (Office Segment) ---")
print(killeen_office_risk)

# --- 3. Feature Engineering: Safe Balance Eligibility Score ---
# Identifying low-risk, high-value customers for retention (Safe Balance Line of Credit)
# Criteria: Credit Score > 700 AND LTV < 0.70
df['safe_balance_eligibility'] = np.where(
    (df['credit_score'] >= 700) & (df['LTV_ratio'] <= 0.70), # Corrected column name to 'LTV_ratio'
    'High Eligibility',
    'Standard'
)

# --- 4. Visualization: Risk vs. Profitability (Job Duty: Visualization and Reporting) ---
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df,
    x='aggregated_risk_score',
    y='net_interest_income_monthly',
    hue='purpose_segment',
    alpha=0.5
)
plt.title('FNBT Portfolio: Monthly NII vs. Aggregated Risk Score')
plt.axvline(x=3.0, color='red', linestyle='--', label='High Risk Threshold')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('FNBT Portfolio: Monthly NII vs. Aggregated Risk Score.png') # Save the plot
plt.show()

# --- 5. Exporting Findings (Deliverable 06: Target Eligibility List) ---
eligibility_list = df[df['safe_balance_eligibility'] == 'High Eligibility'][['customer_id', 'loan_id', 'region_killeen']]
eligibility_list.to_csv('Target_Eligibility_List.csv', index=False)

print(f"Analysis Complete. Found {len(eligibility_list)} customers eligible for Safe Balance outreach.")
