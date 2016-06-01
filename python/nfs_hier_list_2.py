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

try:
        bucket_name = os.environ['RGW_NFS_BUCKET']
except:
	bucket_name = 'nfsroot'
b = conn.get_bucket(bucket_name)

# prefixes
prefixes = ["",
            "/",
            "nfsroot/foo",
            "nfsroot/foo/bar",
            "foo",
            "bar",
            "foo/bar",
            "foo/bar/baz",
            "foo/bar/baz/quux"]

for p in prefixes:
        print "Listing objects with prefix '%s'" % (p)
        objs = b.list(prefix = p)
        for key in objs:
                print ' ' * 4, key.name

# common prefixes
prefixes = ["",
            "/",
            "foo/",
            "foo/bar/",
            "foo/bar/baz/",
            "foo/bar/baz/quux/"]

for p in prefixes:
        print "Listing objects sharing prefix '%s' with Delimiter '/'" % (p)
        objs = b.get_all_keys(prefix=p, delimiter="/")
        for k in objs:
                print k.name

p = "foo/bar/baz/sasquatch"
print "match file or directory prefix='%s' (i.e., lookup)" % (p)
objs = b.get_all_keys(prefix=p, delimiter="/")
for k in objs:
        print k.name
