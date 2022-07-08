import os
import boto3
from botocore.exceptions import ClientError

access_key = 'AKIAYM2GHGHPFOYRRU4A'
access_secret = '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'

bucket_name = 'keepay18-folder'

"""
Connection  to S3 service
"""

data_file_folder = os.path.join(os.getcwd(), 'files')

client_s3 = boto3.client('s3', aws_access_key_id=access_key,
                         aws_secret_access_key=access_secret)

"""
Upload Files to S3 Bucket
"""
for file in os.listdir(data_file_folder):
    if not file.startswith('~'):
        try:
            print("Uploading file {0}...".format(file))
            client_s3.upload_file(
                os.path.join(data_file_folder, file),
                bucket_name,
                file

            )

        except ClientError as e:
            print('Credential is incorrect')
            print(e)
        except Exception as e:
            print(e)
