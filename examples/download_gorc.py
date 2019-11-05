"""
This script downloads the GORC corpus to disk
WARNING: You will need 870GB of disk space to store all of GORC!

You will need to setup AWS access locally before you can download any files from an S3 bucket
See README.md for instructions.

Files are downloaded into the data directory,
"""

import os
import json
import boto3

S3_BUCKET = 'ai2-s2-gorc-release'
LOCAL_GORC_DIR = 'data/'

# GORC is located in a requester pays bucket
# You will be charged for access.
aws_attribs = {'RequestPayer': 'requester'}

s3 = boto3.resource('s3')
bucket = s3.Bucket(S3_BUCKET)

# download manifest file
local_manifest_file = os.path.join(LOCAL_GORC_DIR, 's2-gorc-manifest.json')
bucket.download_file('s2-gorc-manifest.json', local_manifest_file, aws_attribs)

# read manifest file
with open(local_manifest_file, 'r') as f:
    manifest = json.load(f)

# download all files
for file_entry in manifest['files']:
    local_gorc_file = os.path.join(LOCAL_GORC_DIR, file_entry['filename'])
    bucket.download_file(file_entry['filename'], local_gorc_file)