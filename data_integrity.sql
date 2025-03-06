-- Check row counts match source systems
SELECT 
  (SELECT COUNT(*) FROM `apexgcp.apex_dataset.customers_data`) AS customers_count,
  (SELECT COUNT(*) FROM `apexgcp.apex_dataset.transactions`) AS transactions_count;

-- Validate critical fields for NULLs
SELECT 
  COUNTIF(customer_id IS NULL) AS missing_customer_ids,
  COUNTIF(amount < 0) AS negative_amounts 
FROM `apexgcp.apex_dataset.transactions`;