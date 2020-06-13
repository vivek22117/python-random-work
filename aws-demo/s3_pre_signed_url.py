import urllib

import json
import boto3
from botocore.client import Config
import botocore.session

PROFILE = "qa-admin"

TABLE = "productManuals"
BUCKET = "product-manual-data"
KEY = "products/passport.pdf"
EXPIRATION = 3600   # In Seconds
print('Loading function')

# USE THIS WHEN DEPLOYING ON EC2
# s3 = boto3.client('s3', config=Config(signature_version='s3v4'))

# THIS IS FOR LOCAL RUN
session = boto3.Session(profile_name=PROFILE)
s3 = session.client('s3', config=Config(signature_version='s3v4'))


def generate_url():
    # print("Received event: " + json.dumps(event, indent=2))
    # Get the object from the event and show its content type
    bucket = BUCKET
    key = KEY

    try:
        url = s3.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': bucket, 'Key': key}, expires_in=EXPIRATION)
        print("retrieved pre-signed url:{}".format(url))
    except Exception as ex:
        print('error getting pre-signed url error:e'.format(ex))
        return None
    return url


url = generate_url()
print(url)

