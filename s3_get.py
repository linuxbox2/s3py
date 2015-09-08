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
b = conn.get_bucket('my-new-bucket')
k = Key(b)
k.key = 'obj_t1'

print "object: {key}\t{value}".format(
    key = k.key,
    value = k.get_contents_as_string(),
)
