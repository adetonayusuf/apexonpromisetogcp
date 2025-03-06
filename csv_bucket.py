<<<<<<< HEAD
from google.cloud import storage

# Set up the client
client = storage.Client.from_service_account_json('credentials.json')

# Specify the bucket and the CSV file details
bucket_name = 'apex-solutions-bucket'
source_file_path_1 = "C:\\Users\\yusto\\Downloads\\Project 3 Transforming On-Premises Infrastructure with Google Cloud Platform for Scalable, Data-Driven Insights\\gcp\\regions.csv"
destination_blob_name_1 = 'regions.csv'  # Target file name for the first CSV

source_file_path_2 = "C:\\Users\\yusto\\Downloads\\Project 3 Transforming On-Premises Infrastructure with Google Cloud Platform for Scalable, Data-Driven Insights\\gcp\\products.csv"
destination_blob_name_2 = 'products.csv'  # Target file name for the second CSV

# Upload the first CSV file
bucket = client.get_bucket(bucket_name)
blob_1 = bucket.blob(destination_blob_name_1)
blob_1.upload_from_filename(source_file_path_1)
print(f"CSV file {source_file_path_1} uploaded to {destination_blob_name_1}.")

# Upload the second CSV file
blob_2 = bucket.blob(destination_blob_name_2)
blob_2.upload_from_filename(source_file_path_2)
print(f"CSV file {source_file_path_2} uploaded to {destination_blob_name_2}.")
=======
from google.cloud import storage

# Set up the client
client = storage.Client.from_service_account_json('credentials.json')

# Specify the bucket and the CSV file details
bucket_name = 'apex-solutions-bucket'
source_file_path_1 = "C:\\Users\\yusto\\Downloads\\Project 3 Transforming On-Premises Infrastructure with Google Cloud Platform for Scalable, Data-Driven Insights\\gcp\\regions.csv"
destination_blob_name_1 = 'regions.csv'  # Target file name for the first CSV

source_file_path_2 = "C:\\Users\\yusto\\Downloads\\Project 3 Transforming On-Premises Infrastructure with Google Cloud Platform for Scalable, Data-Driven Insights\\gcp\\products.csv"
destination_blob_name_2 = 'products.csv'  # Target file name for the second CSV

# Upload the first CSV file
bucket = client.get_bucket(bucket_name)
blob_1 = bucket.blob(destination_blob_name_1)
blob_1.upload_from_filename(source_file_path_1)
print(f"CSV file {source_file_path_1} uploaded to {destination_blob_name_1}.")

# Upload the second CSV file
blob_2 = bucket.blob(destination_blob_name_2)
blob_2.upload_from_filename(source_file_path_2)
print(f"CSV file {source_file_path_2} uploaded to {destination_blob_name_2}.")
>>>>>>> 3ad4425 (Initial commit)
