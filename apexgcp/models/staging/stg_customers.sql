-- This model creates a view in the apex_dataset_staging dataset.
{{
    config(
        materialized='view',
        schema='staging'
    )
}}

SELECT 
    customer_id,
    name AS customer_name,
    signup_date
FROM {{ source('apex_dataset', 'customer_data_table') }}
