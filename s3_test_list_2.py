import boto
import boto.s3.connection
from boto.s3.key import Key

access_key = "C4B4D3E4H355VTDTQXRF"
secret_key = "NRBkhM2rUZNUbydD86HpNJ110VpQjVroumCOHJXw"

conn = boto.connect_s3(
aws_access_key_id = access_key,
aws_secret_access_key = secret_key,
host = 'serpent',
is_secure=False,
calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

nbuckets = 0
nobjects = 0

for bucket in conn.get_all_buckets():
        nbuckets += 1
        print "bucket %s" % bucket.name
        for o in bucket.list():
                print "obj: %s" % (o.key)
                nobjects += 1

print "bucket count: %d\ttotal objects: %d" % (nbuckets, nobjects)
