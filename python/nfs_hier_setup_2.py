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

bname = "nfsroot"
bucket = conn.create_bucket(bname)

fnames = ["foo/bar/baz/quux",
          "foo/f1",
          "foo/f2",
          "foo/bar/f1",
          "foo/bar/d1/",
          "foo/bar/baz/sasquatch",
          "foo/bar/baz/sasquatch/"]

for oname in fnames:
        k = Key(bucket)
        k.key = oname
        if oname[:-1] == "/":
                oval = "test directory %s" % (oname)
        else:
                oval = "test file %s" % (oname)
        k.set_contents_from_string(oval)
