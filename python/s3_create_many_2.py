#!/usr/bin/python

import boto
import boto.s3.connection
from boto.s3.key import Key
import os

rgw_host = os.environ['RGW_HOST']
rgw_port = int(os.environ['RGW_PORT'])
access_key = os.environ['RGW_ACCESS_KEY']
secret_key = os.environ['RGW_SECRET_KEY']

conn = boto.connect_s3(
aws_access_key_id = access_key,
aws_secret_access_key = secret_key,
host = rgw_host,
port = rgw_port,
is_secure=False,
calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

nobjects = 10000

bname = "bmany"

bucket = conn.create_bucket(bname)
print bname
for o in range(0,nobjects):
        oname = "%s_o%d" % (bname, o)
        print oname
        k = Key(bucket)
        k.key = oname
        oval = "value for me=%s" % oname
        k.set_contents_from_string(oval)

