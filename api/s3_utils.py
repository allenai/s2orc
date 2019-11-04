"""

Some common functions for working with S3

"""

import os
import botocore.exceptions

import subprocess

def download_from_s3(s3_bucket, s3_fname: str, target_path: str):
    dirname = os.path.dirname(target_path)
    if dirname != '':
        os.makedirs(dirname, exist_ok=True)
    try:
        s3_bucket.download_file(s3_fname, target_path)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return None
        else:
            raise e

def upload_to_s3(s3_bucket, input_path: str, s3_fname: str):
    try:
        s3_bucket.upload_file(input_path, s3_fname)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            # print(f'Missing {s3_fname}')
            return None
        else:
            raise e

def rsync_to_s3(s3_bucket_name: str, input_dir: str, s3_dir: str):
    # TODO; catch errors
    subprocess.run(['aws', 's3', 'sync', f'{input_dir}', f's3://{s3_bucket_name}/{s3_dir}'])

def rsync_from_s3(s3_bucket_name: str, s3_dir: str, target_dir: str):
    # TODO; catch errors
    subprocess.run(['aws', 's3', 'sync', f's3://{s3_bucket_name}/{s3_dir}', f'{input_dir}'])
