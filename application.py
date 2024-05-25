from google.cloud import bigquery
from googleapiclient.discovery import build
import pandas as pd
import os

# Set up authentication credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './api-project-396215-aafaa4f6da87.json'

# Create a BigQuery client
bigquery_client = bigquery.Client()
# dataset_ref = bigquery_client.dataset('bigquery-public-data.new_york_taxi_trips')

# Construct a query
query = """
SELECT * 
FROM `bigquery-public-data.census_bureau_acs.blockgroup_2010_5yr` 
LIMIT 10
"""

# Execute the query
query_job = bigquery_client.query(query)
results = query_job.result()

# Store the results in a pandas DataFrame
data = []
for row in results:
    data.append(row._xxx_values)

columns = [key for key in row._xxx_field_to_index]
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
# save model to directory
data_dir = './data/'
os.makedirs(data_dir, exist_ok=True)
df.to_csv(os.path.join(data_dir, 'us_census_acs.csv'), index=False)