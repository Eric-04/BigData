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
LIMIT 1000
"""

# Execute the query
query_job = bigquery_client.query(query)
results = query_job.result()

for row in results:
    print(row)

# Store the results in a pandas DataFrame
data = []
for row in results:
    data.append((row.column1, row.column2))

# df = pd.DataFrame(data, columns=['column1', 'column2'])

# # Save the DataFrame to a CSV file
# df.to_csv('data.csv', index=False)