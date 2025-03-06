{{
    config(
        materialized='view',
        schema='staging'
    )
}}

SELECT * 
FROM {{ source('apex_dataset', 'region_data_table') }}

