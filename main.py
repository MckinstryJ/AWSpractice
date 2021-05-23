'''
    AWS Practice
'''
import boto3
import os

# Initial Auth edits
os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = ''
os.environ["AWS_SECRET_ACCESS_KEY"] = ''

# connecting to S3
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='',
    aws_secret_access_key=''
)

for bucket in s3.buckets.all():
    print(bucket.name)
