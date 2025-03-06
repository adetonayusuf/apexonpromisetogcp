{{
    config(
        materialized='view',
        schema='staging'
    )
}}

SELECT * 
FROM {{ source('apex_dataset', 'product_data_table') }}

