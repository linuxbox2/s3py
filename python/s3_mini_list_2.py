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

nbuckets = 0
nobjects = 0

for bucket in conn.get_all_buckets():
        nbuckets += 1
        if nbuckets > 1:
                break
        print "bucket %s" % bucket.name
        for o in bucket.list():
                print "obj: %s" % (o.key)
                nobjects += 1

print "bucket count: %d\ttotal objects: %d" % (nbuckets, nobjects)
