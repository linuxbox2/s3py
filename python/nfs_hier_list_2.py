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

prefixes = ["",
            "/",
            "nfsroot/foo",
            "nfsroot/foo/bar",
            "foo",
            "bar",
            "foo/bar",
            "foo/bar/baz",
            "foo/bar/baz/quux"]

b = conn.get_bucket("nfsroot")

for p in prefixes:
        print "Listing objects with prefix '%s'" % (p)
        objs = b.list(prefix = p)
        for key in objs:
                print ' ' * 4, key.name
