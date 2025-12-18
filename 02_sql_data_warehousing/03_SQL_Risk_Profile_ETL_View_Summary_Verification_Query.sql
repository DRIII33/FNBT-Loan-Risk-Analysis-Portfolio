# Summary Verification Query for 03_SQL_Risk_Profile_ETL_View.sql
## After running the script above, you can verify your work by running this query to see your risk-segmented results:

SELECT 
    purpose_segment, 
    COUNT(*) as total_loans, 
    ROUND(AVG(aggregated_risk_score), 2) as avg_risk,
    SUM(net_interest_income_monthly) as projected_monthly_nii
FROM `driiiportfolio.fnbt_ds.vw_customer_risk_profile`
GROUP BY 1
ORDER BY avg_risk DESC;
