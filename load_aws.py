import os 
import boto3
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

def load_data_s3(data):

    parquet_buffer=BytesIO()
    data.to_parquet(parquet_buffer, index=False)

    s3_client=boto3.client(
        's3',
        aws_access_key_id =os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
    )

    s3_client.put_object(
        Bucket=os.getenv('BUCKET'),
        Key='aviation_data/flights.parquet',
        Body=parquet_buffer.getvalue()
    )

    print('successfully loaded in s3 ')
    return True