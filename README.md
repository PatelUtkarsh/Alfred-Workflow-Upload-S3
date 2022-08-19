# Alfred Workflow: Upload Screenshot to Oracle Object Storage

This workflow helps you upload screenshot in your clipboard or local disk to oracle object-storage using s3 compatible API and put the public url of the image to your clipboard.

Oracle offers [always free 10gb object-storage](https://www.oracle.com/cloud/free/#always-free) which is plenty. 

Using tinypng api will reduce screenshot size drastically and help enduser save bandwidth.

## Overview

This workflow is written in Python and used Boto3 as AWS client to upload files.

Upload clipboard image directly or upload a file.

[![Watch the video](https://s.utkarshpatel.com/video-placeholder-hinP7.png)](https://s.utkarshpatel.com/screenshot-workflow-encoded-4E1b7.mp4)


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
- tinypng_api_key: Get your tinypng api key from https://tinypng.com/developers to compress images before uploading. (optional)
- short_url: You can add proxy to cloudflare or aws lambda to make url short. Example: https://gist.github.com/PatelUtkarsh/0438735990e0b6f373b4deaf7f9be277 (optional)

**Note** 🗒️: when `tinypng_api_key` is set, it will compress original image and replace it before uploading to object storage.

### Upload image from clipboard in alfred type:

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
