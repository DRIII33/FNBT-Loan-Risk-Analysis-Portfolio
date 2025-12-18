#INSTALL PACKAGES
!pip install pandas

# 01_Python_Data_Generator_Script.ipynb
# Project: FNBT-Loan-Risk-Analysis-Portfolio
# Purpose: Generate synthetic loan data using NumPy 2.x safe methods for manual BigQuery upload.
# Author: Daniel Rodriguez III
# Date: 12-17-2025

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import calendar

# --- Configuration ---
NUM_RECORDS = 50000
START_DATE = datetime(2018, 1, 1)
END_DATE = datetime(2023, 12, 31)

# --- 1. Data Generation Functions ---

def generate_dates(start, end, n):
    """Generates random dates and handles Leap Year (Feb 29) edge cases."""
    time_delta = end - start
    random_days = np.random.randint(0, time_delta.days, n)
    orig_dates = [start + timedelta(days=int(d)) for d in random_days]
    maturity_years = np.random.randint(5, 25, n)
    maturity_dates = []
    for d, y in zip(orig_dates, maturity_years):
        target_year = d.year + y
        try:
            maturity_dates.append(d.replace(year=target_year))
        except ValueError:
            # Reverts Feb 29 to Feb 28 if target year isn't a leap year
            max_day_in_month = calendar.monthrange(target_year, d.month)[1]
            maturity_dates.append(d.replace(year=target_year, day=min(d.day, max_day_in_month)))
    return orig_dates, maturity_dates

def calculate_status(dpd_days):
    """Maps DPD to bank-standard loan statuses."""
    if dpd_days == 0: return 'Current'
    elif dpd_days <= 30: return 'Past Due (30)'
    elif dpd_days <= 60: return 'Past Due (60)'
    elif dpd_days <= 90: return 'Past Due (90+)'
    else: return 'Default/Charge-Off'

# --- 2. Synthetic Data Creation ---
np.random.seed(42)

df = pd.DataFrame({
    'loan_id': ['L' + str(i).zfill(8) for i in range(1, NUM_RECORDS + 1)],
    'customer_id': ['C' + str(i).zfill(6) for i in np.random.randint(100000, 999999, NUM_RECORDS)],
    'loan_type': np.random.choice(
        ['Commercial Real Estate (CRE)', 'Residential Mortgage', 'Consumer Auto', 'Personal Unsecured'],
        NUM_RECORDS, p=[0.30, 0.40, 0.20, 0.10]
    ),
    'region_killeen': np.random.choice(['Killeen, TX Metro', 'Other Texas Region'], NUM_RECORDS, p=[0.35, 0.65])
})

orig_dates, maturity_dates = generate_dates(START_DATE, END_DATE, NUM_RECORDS)
df['origination_date'] = orig_dates
df['maturity_date'] = maturity_dates

# --- 3. Financial Generation (NUMPY 2.X SAFE CLIP) ---
# Using np.clip(array, a_min, a_max) to avoid NumPy 2.x method keyword errors
cre_amounts = np.random.normal(loc=1500000, scale=800000, size=NUM_RECORDS)
other_amounts = np.random.normal(loc=150000, scale=100000, size=NUM_RECORDS)

df['origination_amount'] = np.where(
    df['loan_type'] == 'Commercial Real Estate (CRE)',
    np.clip(cre_amounts, 100000, None).round(2),
    np.clip(other_amounts, 1000, None).round(2)
)

df['current_balance'] = (df['origination_amount'] * np.random.uniform(0.1, 1.0, NUM_RECORDS)).round(2)

df['interest_rate'] = np.where(
    df['loan_type'].str.contains('CRE'),
    np.random.uniform(5.5, 9.5, NUM_RECORDS).round(4),
    np.random.uniform(4.0, 15.0, NUM_RECORDS).round(4)
)

df['collateral_value'] = (df['origination_amount'] / np.random.uniform(0.7, 1.0, NUM_RECORDS)).round(2)

# --- 4. Risk Logic & Segmentation ---
cre_segments = np.random.choice(['Office', 'Retail', 'Multi-Family', 'Industrial'], NUM_RECORDS, p=[0.25, 0.25, 0.30, 0.20])
df['purpose_segment'] = np.where(df['loan_type'] == 'Commercial Real Estate (CRE)', cre_segments, df['loan_type'].str.replace(' ', '_'))

df['days_past_due'] = 0
is_cre_office = (df['loan_type'] == 'Commercial Real Estate (CRE)') & (df['purpose_segment'] == 'Office')
df.loc[is_cre_office, 'days_past_due'] = np.random.choice([0, 30, 60, 90, 120, 180], size=is_cre_office.sum(), p=[0.80, 0.05, 0.05, 0.05, 0.03, 0.02])
df.loc[~is_cre_office, 'days_past_due'] = np.random.choice([0, 30, 60, 90], size=(~is_cre_office).sum(), p=[0.95, 0.02, 0.02, 0.01])

df['loan_status'] = df['days_past_due'].apply(calculate_status)

# Consumer Metrics (NUMPY 2.X SAFE CLIP)
income_vals = np.random.normal(loc=90000, scale=40000, size=NUM_RECORDS)
credit_vals = np.random.normal(loc=720, scale=50, size=NUM_RECORDS)

df['annual_income'] = np.where(df['loan_type'] != 'Commercial Real Estate (CRE)', np.clip(income_vals, 20000, None).round(0), -1)
df['credit_score'] = np.where(df['loan_type'] != 'Commercial Real Estate (CRE)', np.clip(credit_vals, 550, 850).round(0), -1)
df['dti_ratio'] = np.where(df['loan_type'] != 'Commercial Real Estate (CRE)', np.random.uniform(0.15, 0.55, NUM_RECORDS).round(2), -1.0)

# Final Cleanup
df['LTV_ratio'] = (df['current_balance'] / df['collateral_value']).round(4)
df.loc[df['loan_type'] == 'Personal Unsecured', 'collateral_value'] = -1.0

# Export
OUTPUT_FILE = 'fnbt_loan_portfolio_data_raw.csv'
df.to_csv(OUTPUT_FILE, index=False)

print(f"Success! {OUTPUT_FILE} generated for manual BigQuery load.")
