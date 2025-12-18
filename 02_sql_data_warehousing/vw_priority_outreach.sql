CREATE OR REPLACE VIEW `driiiportfolio.fnbt_ds.vw_priority_outreach` AS
SELECT 
    *,
    CASE 
        WHEN credit_score >= 700 AND ltv_ratio <= 0.70 THEN 'Priority' 
        ELSE 'Standard' 
    END AS Safe_Balance_Flag
FROM `driiiportfolio.fnbt_ds.vw_customer_risk_profile`;
