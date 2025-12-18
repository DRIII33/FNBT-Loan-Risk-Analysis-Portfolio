-- File: 03_SQL_Risk_Profile_ETL_View.sql
-- Project: FNBT-Loan-Risk-Analysis-Portfolio
-- Purpose: ELT transformation creating a Risk Profile View (Free-Tier Compatible).

CREATE OR REPLACE VIEW `driiiportfolio.fnbt_ds.vw_customer_risk_profile` AS
SELECT
    s.loan_id,
    s.customer_id,
    s.loan_type,
    CAST(s.origination_date AS DATE) AS origination_date,
    CAST(s.maturity_date AS DATE) AS maturity_date,
    s.origination_amount,
    s.current_balance,
    s.interest_rate,
    s.collateral_value,
    s.purpose_segment,
    s.days_past_due,
    s.loan_status,
    s.region_killeen,
    s.dti_ratio,
    s.annual_income,
    s.credit_score,
    s.LTV_ratio,

    -- FEATURE: AGGREGATED RISK SCORE (60% LTV, 40% DPD)
    -- This addresses the "Data Integrity" and "Efficiency" objectives 
    ROUND(
      (CASE 
        WHEN s.LTV_ratio >= 0.90 THEN 5 
        WHEN s.LTV_ratio >= 0.75 THEN 3 
        ELSE 1 
      END * 0.6) + 
      (CASE 
        WHEN s.days_past_due >= 90 THEN 5 
        WHEN s.days_past_due >= 30 THEN 3 
        ELSE 1 
      END * 0.4)
    , 2) AS aggregated_risk_score,

    -- FEATURE: NET INTEREST INCOME (NII)
    -- Formula: $NII = (\text{Balance} \times \frac{\text{Rate}}{100} \div 12) - (\text{Balance} \times 0.02 \div 12)$
    ROUND(
      (s.current_balance * (s.interest_rate / 100) / 12) - 
      (s.current_balance * 0.02 / 12)
    , 2) AS net_interest_income_monthly

FROM `driiiportfolio.fnbt_ds.loan_portfolio_staging` s
-- EXCEPTION HANDLING: Job duty to ensure accuracy prior to distribution 
WHERE s.current_balance <= s.origination_amount 
  AND s.days_past_due >= 0;
