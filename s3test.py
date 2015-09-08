import boto
import boto.s3.connection
access_key = "C4B4D3E4H355VTDTQXRF"
secret_key = "NRBkhM2rUZNUbydD86HpNJ110VpQjVroumCOHJXw"
conn = boto.connect_s3(
aws_access_key_id = access_key,
aws_secret_access_key = secret_key,
host = 'serpent',
is_secure=False,
calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)
bucket = conn.create_bucket('my-new-bucket')
for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
)
