#!/usr/bin/python

import os
import boto
import boto.s3.connection
from boto.s3.key import Key

rgw_host = os.environ['RGW_HOST']
access_key = os.environ['RGW_ACCESS_KEY']
secret_key = os.environ['RGW_SECRET_KEY']

bucket_name = "sorry_dave"

conn = boto.connect_s3(
aws_access_key_id = access_key,
aws_secret_access_key = secret_key,
host = rgw_host,
is_secure=False,
calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

# delete it
conn.delete_bucket(bucket_name)
