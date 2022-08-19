# Alfred Workflow: Upload Screenshot to Oracle Object Storage

This workflow helps you upload screenshot in your clipboard or local disk to oracle object-storage using s3 compatible API and put the public url of the image to your clipboard.

## Overview

This workflow is written in Python. And used Boto3 as AWS client to upload image.

## Download

https://github.com/PatelUtkarsh/Alfred-Workflow-Upload-S3/releases

## Usage

Check https://www.ateam-oracle.com/aws-s3-to-oci-access-best-practices on how to get environment variables.

Config Environment Variables:

- access_key: Oracle access key
- secret_key: Oracle access secret
- region_name: Oracle cloud region name
- bucket_name: Oracle bucket name. e.g. `my-bucket-name`
- namespace: Oracle namespace.
- tinypng_api_key: Get your tinypng api key from https://tinypng.com/developers to compress images before uploading.
- short_url: You can add proxy to cloudflare or aws lambda to make url short. Example: https://gist.github.com/PatelUtkarsh/0438735990e0b6f373b4deaf7f9be277

**Note** 🗒️: when `tinypng_api_key` is set, it will compress original image and replace it before uploading to object storage.

### Upload image from clipboard:

```bash
upload
```

### Upload any file from local:

TinyPng will compress png, webp and jpg images.


```bash
upload TYPE-FILENAME-HERE
```

### Issue with python 2?
Read setup guide at https://www.alfredapp.com/help/kb/python-2-monterey/

## Forked source: 🙌
- https://github.com/tonyxu-io/Alfred-Workflow-Upload-S3
