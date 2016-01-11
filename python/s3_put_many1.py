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

bname = "large_bucket"
bucket = conn.create_bucket(bname)

for ix in range (0,5000):
        oname = "foo_dir/f_%s" %(ix)
        print "creating obj: %s" % (oname)
        k = Key(bucket)
        k.key = oname
        if oname[:-1] == "/":
                oval = "test directory %s" % (oname)
        else:
                oval = "test file %s" % (oname)
        k.set_contents_from_string(oval)
