"""
This script downloads the GORC corpus to disk
WARNING: You will need around 200G of disk space to store all of GORC

You will need to setup AWS access locally before you can download any files from an S3 bucket
See README.md for instructions.

Files are downloaded into the data directory,
"""

import os
import json
import boto3
import tqdm

from config import S3_BUCKET_NAME, CURRENT_VERSION
from api.s3_utils import download_from_s3


LOCAL_GORC_DIR = 'gorc/'

# GORC is currently open access
# Uncomment the following and add to download specification for requester pays access
# aws_attribs = {'RequestPayer': 'requester'}

s3 = boto3.resource('s3')
bucket = s3.Bucket(S3_BUCKET_NAME)

# download manifest file
s3_manifest_file = f'{CURRENT_VERSION}/manifest.json'
local_manifest_file = os.path.join(LOCAL_GORC_DIR, 'manifest.json')
download_from_s3(bucket, s3_manifest_file, local_manifest_file)

# read manifest file
with open(local_manifest_file, 'r') as f:
    manifest = json.load(f)

# download all files
print(f"downloading {len(manifest['files'])} files...")
for file_entry in tqdm.tqdm(manifest['files']):
    local_gorc_file = os.path.join(LOCAL_GORC_DIR, file_entry['filename'])
    download_from_s3(bucket, file_entry['filename'], local_gorc_file)