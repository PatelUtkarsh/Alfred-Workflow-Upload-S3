#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime
import os
import sys
import atexit
import imghdr
import random
import string
import mimetypes
from subprocess import call
from os.path import expanduser, exists, basename, getsize
from workflow import Workflow

def capture():
    random_bit = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(5))
    file_name = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'+random_bit+'.png')
    content_type = 'image/png'
    if (sys.argv[1] != ""):
        file_path = sys.argv[1]
        content_type = mimetypes.MimeTypes().guess_type(file_path)[0]
        _head, file_name = os.path.split(file_path)
        file_names = file_name.split('.')
        file_names.insert(1,'-' + random_bit + '.')
        file_name = "".join(file_names)
    else:
        file_path = os.path.join('/tmp', file_name)
        atexit.register(lambda x: os.remove(x) if os.path.exists(x) else None, file_path)
        save = call(['./pngpaste', file_path])
        if save == 1:
            sys.exit()
    tinypng_key = os.getenv('tinypng_api_key')
    # If content type starts with 'image/' then compress.
    if content_type.startswith('image/') and tinypng_key:
        import tinify
        tinify.key = tinypng_key
        tinify.from_file(file_path).to_file(file_path)
    return file_path, file_name, content_type

def main(wf):
    import boto3
    file_path, file_name, content_type = capture()
    bucket_name = os.getenv('bucket_name')
    region_name = os.getenv('region_name')
    namespace = os.getenv('namespace')
    s3 = boto3.client(
        service_name='s3',
        aws_access_key_id=os.getenv('access_key'),
        aws_secret_access_key=os.getenv('secret_key'),
        region_name=region_name,
        endpoint_url="https://%s.compat.objectstorage.%s.oraclecloud.com" %(namespace, region_name)
    )
    s3.upload_file(file_path, bucket_name, file_name, ExtraArgs={'ContentType': content_type})
    shorturl = os.getenv('shorturl')
    # if short url is not empty and exists.
    if shorturl:
        if shorturl[len(shorturl)-1] != "/":
            shorturl = shorturl + "/"
        output = "%s%s" %(shorturl,file_name)
    else:
        output = "https://objectstorage.%s.oraclecloud.com/n/%s/b/%s/o/%s" %(region_name,namespace,bucket_name,file_name)
    print (output,end='')

if __name__ == '__main__':
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))
