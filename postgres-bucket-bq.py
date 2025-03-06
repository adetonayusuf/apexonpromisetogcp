from google.cloud import bigquery
from google.cloud import storage
import psycopg2
import csv
import os

# Set up the BigQuery client
bq_client = bigquery.Client.from_service_account_json('credentials.json')

# Set up Cloud Storage client
storage_client = storage.Client.from_service_account_json('credentials.json')

# Define your bucket and file details
bucket_name = 'apex-solutions-bucket'

# PostgreSQL table details
postgres_tables = [
    {
        'table_name': 'customers',  # Updated to the correct customer table name
        'file_name': 'customer_data.csv',  # CSV file name for customer data
        'bigquery_table_id': 'customer_data_table',  # BigQuery table for customer data
        'schema': [
            bigquery.SchemaField('Customer_ID', 'INTEGER'),
            bigquery.SchemaField('Name', 'STRING'),
            bigquery.SchemaField('Email', 'STRING'),
            bigquery.SchemaField('Phone', 'STRING'),
            bigquery.SchemaField('Country', 'STRING'),
            bigquery.SchemaField('Industry', 'STRING'),
            bigquery.SchemaField('Signup_Date', 'DATE'),
            bigquery.SchemaField('Last_Interaction_Date', 'DATE'),
        ]
    },
    {
        'table_name': 'transactions',  # Keeping transactions table name as it is
        'file_name': 'transactions.csv',  # CSV file name for transaction data
        'bigquery_table_id': 'transactions_table',  # BigQuery table for transaction data
        'schema': [
            bigquery.SchemaField('Transaction_ID', 'INTEGER'),
            bigquery.SchemaField('Customer_ID', 'INTEGER'),
            bigquery.SchemaField('Region_ID', 'INTEGER'),
            bigquery.SchemaField('Product_ID', 'INTEGER'),
            bigquery.SchemaField('Transaction_Date', 'DATE'),
            bigquery.SchemaField('Amount', 'DECIMAL'),
            bigquery.SchemaField('Discount_Offered', 'DECIMAL'),
            bigquery.SchemaField('Payment_Method', 'STRING'),
            bigquery.SchemaField('Pricing_Model', 'STRING'),
        ]
    }
]

# Set the source URI for the CSV file in Cloud Storage
def get_source_uri(file_name):
    return f'gs://{bucket_name}/{file_name}'

# Function to upload PostgreSQL data to Cloud Storage
def upload_postgres_data_to_gcs(postgres_data_file_path, bucket_name, file_name):
    # Upload the CSV file to Cloud Storage
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(postgres_data_file_path)
    print(f"File {postgres_data_file_path} uploaded to {bucket_name}/{file_name}.")

# Function to export and load data into BigQuery for a specific table
def export_and_load_table_to_bigquery(postgres_table_info):
    table_name = postgres_table_info['table_name']
    file_name = postgres_table_info['file_name']
    bigquery_table_id = postgres_table_info['bigquery_table_id']
    schema = postgres_table_info['schema']

    # Connect to PostgreSQL and export data to CSV
    conn = psycopg2.connect(
        host="localhost",
        dbname="apex_db",
        user="postgres",
        password="School1."
    )
    cursor = conn.cursor()

    # Query to fetch data from the current table
    cursor.execute(f"SELECT * FROM {table_name};")

    # Save query result to CSV
    with open(file_name, 'w', newline='') as f:
        # Write CSV header
        columns = [desc[0] for desc in cursor.description]
        writer = csv.writer(f)
        writer.writerow(columns)  # Write header row
        for row in cursor.fetchall():
            writer.writerow(row)

    cursor.close()
    conn.close()

    # Upload the CSV file to Google Cloud Storage
    upload_postgres_data_to_gcs(file_name, bucket_name, file_name)

    # Set the BigQuery table reference
    dataset_ref = bq_client.dataset('apex_dataset')
    table_ref = dataset_ref.table(bigquery_table_id)

    # Set the configuration for loading data into BigQuery
    load_config = bigquery.LoadJobConfig(
        schema=schema,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Skip header row
        autodetect=False,  # Use the defined schema
    )

    # Load the CSV file from GCS into BigQuery
    source_uri = get_source_uri(file_name)
    load_job = bq_client.load_table_from_uri(
        source_uri, table_ref, job_config=load_config
    )
    load_job.result()  # Wait for the load job to complete
    print(f"Data from {file_name} loaded into BigQuery table {bigquery_table_id}.")

# Export and load data for both tables
for table_info in postgres_tables:
    export_and_load_table_to_bigquery(table_info)
