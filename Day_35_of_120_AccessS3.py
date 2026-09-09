import boto3
from load_dotenv import load_dotenv
from AccessS3 import s3_client
import os
load_dotenv()
# service - s3
# region  - eu-north-1
# accesskeyId
# accesskeysecret

s3_client = boto3.client( 's3' , 'eu-north-1',
                        aws_access_key_id =os.environ.get("aws_access_key_id_training"),
                        aws_secret_access_key = os.environ.get("aws_secret_key_training"))


# s3_client.upload_file('D:\emp_multiple_sheets.xlsx','adilkhanp-s3-bucket','emp_multiple_sheets.xlsx')
# s3_client.upload_file('D:\Department_split.xlsx','adilkhanp-s3-bucket','landing/Department_2.xlsx')
s3_client.download_file('adilkhanp-s3-bucket' , 'landing/Department_2.xlsx' , 'D:\Downloaded_file.xlsx')
