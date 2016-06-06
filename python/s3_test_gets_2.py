#!/usr/bin/python

import os
import boto
import boto.s3.connection
from boto.s3.key import Key

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

nbuckets = 0
nobjects = 0

for bucket in conn.get_all_buckets():
        nbuckets += 1
        print "bucket %s" % bucket.name
        for o in bucket.list():
                k = Key(bucket)
                k.key = o.key
                print "obj: %s %s" % (o.key, k.get_contents_as_string())
                nobjects += 1

print "bucket count: %d\ttotal objects: %d" % (nbuckets, nobjects)
