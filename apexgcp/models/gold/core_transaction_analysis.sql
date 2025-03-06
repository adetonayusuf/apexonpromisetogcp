{{
    config(
        materialized='table',
        schema='marts_core',
        tags=['core', 'daily']
    )
}}

WITH transactions AS (
    SELECT
        t.transaction_id,
        t.transaction_date,
        t.amount,
        t.discount_offered,
        t.payment_method,
        t.pricing_model,
        c.customer_name,
        p.product_name,
        r.region_name,
        r.country,
        DATE_DIFF(CURRENT_DATE(), c.signup_date, YEAR) AS customer_tenure_years
    FROM {{ ref('stg_transactions') }} t
    JOIN {{ ref('stg_customers') }} c 
        ON t.customer_id = c.customer_id
    JOIN {{ ref('stg_products') }} p 
        ON t.product_id = p.product_id
    JOIN {{ ref('stg_regions') }} r 
        ON t.region_id = r.region_id
)

SELECT
    *,
    amount - discount_offered AS net_amount,
    CASE 
        WHEN pricing_model = 'subscription' THEN 'recurring'
        ELSE 'one-time'
    END AS revenue_type,
    CASE
        WHEN customer_tenure_years < 1 THEN 'new'
        WHEN customer_tenure_years BETWEEN 1 AND 3 THEN 'established'
        ELSE 'veteran'
    END AS customer_segment
FROM transactions
