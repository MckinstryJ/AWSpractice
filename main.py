'''
    AWS Practice
'''
import boto3
import os
import pandas as pd

''' INITIAL AUTH VALUES'''
os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = ''
os.environ["AWS_SECRET_ACCESS_KEY"] = ''

'''

    AWS S3 Section

'''

''' CONNECTING TO S3 '''
s3 = boto3.client(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='',
    aws_secret_access_key=''
)

''' CREATING A BUCKET
s3.create_bucket(
    Bucket='sql-server-shack-practice',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)
'''

''' VIEWING ALL BUCKETS 
for bucket in s3.buckets.all():
    print(bucket.name)
'''

''' CREATING AN S3 OBJECT
obj = s3.get_object(
    Bucket='mckinstryjohnbucket1',
    Key='transaction.txt'
)

# Reading it into a DataFrame
data = pd.read_json(obj['Body'])
print(data)
'''
