{{
    config(
        materialized='view',
        schema='staging'
    )
}}

SELECT *
FROM {{ source('apex_dataset', 'transactions_table') }}
