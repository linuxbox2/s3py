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

nbuckets = 10
nobjects = 10

for b in range(0,nbuckets):
        bname = "bu_%d" % (b)
        bucket = conn.create_bucket(bname)
        print bname
        for o in range(0,nobjects):
                oname = "%s_o%d" % (bname, o)
                print oname
                k = Key(bucket)
                k.key = oname
                oval = "value for me=%s" % oname
                k.set_contents_from_string(oval)

