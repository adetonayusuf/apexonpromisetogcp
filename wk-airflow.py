<<<<<<< HEAD
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='apex_data_pipeline',
    default_args=default_args,
    description='Load data from BigQuery using a query job',
    schedule='@daily',
    catchup=False,
) as dag:

    query_config = {
        "query": {
            "query": "SELECT * FROM `apexgcp.apex_dataset_marts_core.core_transaction_analysis`",
            "useLegacySql": False
        }
    }

    load_to_bigquery = BigQueryInsertJobOperator(
        task_id='load_gcs_to_bigquery',
        configuration=query_config
    )
=======
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='apex_data_pipeline',
    default_args=default_args,
    description='Load data from BigQuery using a query job',
    schedule='@daily',
    catchup=False,
) as dag:

    query_config = {
        "query": {
            "query": "SELECT * FROM `apexgcp.apex_dataset_marts_core.core_transaction_analysis`",
            "useLegacySql": False
        }
    }

    load_to_bigquery = BigQueryInsertJobOperator(
        task_id='load_gcs_to_bigquery',
        configuration=query_config
    )
>>>>>>> 3ad4425 (Initial commit)
