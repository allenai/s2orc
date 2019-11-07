"""

Some common functions for working with S3

"""

import os
import botocore.exceptions


def download_from_s3(s3_bucket, s3_fname: str, target_path: str, attribs=None):
    dirname = os.path.dirname(target_path)
    if dirname != '':
        os.makedirs(dirname, exist_ok=True)
    try:
        if attribs:
            s3_bucket.download_file(s3_fname, target_path, attribs)
        else:
            s3_bucket.download_file(s3_fname, target_path)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return None
        else:
            raise e