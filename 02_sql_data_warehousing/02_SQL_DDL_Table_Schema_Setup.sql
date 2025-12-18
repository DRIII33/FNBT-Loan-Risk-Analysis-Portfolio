-- File: 02_SQL_DDL_Table_Schema_Setup.sql
-- Purpose: Define the master table schema for the FNBT Loan Portfolio.

CREATE OR REPLACE TABLE `driiiportfolio.fnbt_ds.loan_portfolio_master`
(
  loan_id STRING OPTIONS(description="Unique identifier for each loan"),
  customer_id STRING OPTIONS(description="Unique identifier for the customer"),
  loan_type STRING OPTIONS(description="Product category (e.g., CRE, Mortgage)"),
  origination_date DATE OPTIONS(description="Date the loan was funded"),
  maturity_date DATE OPTIONS(description="Date the loan is scheduled to be paid off"),
  origination_amount NUMERIC OPTIONS(description="Initial loan balance"),
  current_balance NUMERIC OPTIONS(description="Outstanding principal balance"),
  interest_rate FLOAT64 OPTIONS(description="Annual interest rate"),
  collateral_value NUMERIC OPTIONS(description="Appraised value of underlying asset"),
  purpose_segment STRING OPTIONS(description="Detailed sub-segment (e.g., Office, Retail)"),
  days_past_due INT64 OPTIONS(description="Number of days payment is late"),
  loan_status STRING OPTIONS(description="Status: Current, Past Due, or Default"),
  region_killeen STRING OPTIONS(description="Flag for Killeen, TX Metro market"),
  dti_ratio FLOAT64 OPTIONS(description="Debt-to-Income ratio (Consumer only)"),
  annual_income NUMERIC OPTIONS(description="Customer annual income"),
  credit_score INT64 OPTIONS(description="Customer credit score"),
  ltv_ratio FLOAT64 OPTIONS(description="Loan-to-Value ratio calculation"),
  -- ETL Calculated Fields
  aggregated_risk_score FLOAT64 OPTIONS(description="Weighted risk score (LTV and DPD)"),
  net_interest_income_monthly NUMERIC OPTIONS(description="Estimated monthly income after funding costs")
);
