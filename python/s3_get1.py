#!/usr/bin/python

import boto
import boto.s3.connection
from boto.s3.key import Key
import os

rgw_host = os.environ['RGW_HOST']
access_key = os.environ['RGW_ACCESS_KEY']
secret_key = os.environ['RGW_SECRET_KEY']

conn = boto.connect_s3(
aws_access_key_id = access_key,
aws_secret_access_key = secret_key,
host = rgw_host,
is_secure=False,
calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)
b = conn.get_bucket('sorry_dave')
k = Key(b)
k.key = 'obj_t1'

print "object: {key}\t{value}".format(
    key = k.key,
    value = k.get_contents_as_string(),
)
