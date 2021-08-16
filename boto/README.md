https://stackoverflow.com/questions/30249069/listing-contents-of-a-bucket-with-boto3


<https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/s3.html>

```
 import boto3
 boto3.__version__
 1.9.124
```

<https://www.slsmk.com/use-boto3-to-open-an-aws-s3-file-directly/>

<https://www.slsmk.com/amazon-aws-tech-notes-and-articles/>

https://hackersandslackers.com/s3-boto3-python-sdk/

<https://medium.com/swlh/using-s3-just-like-a-local-file-system-in-python-497737783f11>

### How to read AWS file names
```
objs = boto3.client.list_objects(Bucket='my_bucket')
    while 'Contents' in objs.keys():
        objs_contents = objs['Contents']
        for i in range(len(objs_contents)):
            filename = objs_contents[i]['Key']
```

###  How to get the actual content of the AWS file

/Users/mlubinsky/CODE/GIT/data-processing/src/main/python/utils/S3Utils.py
```def read_contents_from_s3(bucket_name, bucket_key):```

<https://stackoverflow.com/questions/36205481/read-file-content-from-s3-bucket-with-boto3>

 similarly to a open(filename).readlines():
 
 ```
 s3 = boto3.resource('s3')
bucket = s3.Bucket('test-bucket')
# Iterates through all the objects, doing the pagination for you. Each obj
# is an ObjectSummary, so it doesn't contain the body. You'll need to call
# get to get the whole body.
for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()
```

File data will be a binary stream.  We have to decode it 
```contents = filedata.decode('utf-8')) ```


```
def s3_read(source, profile_name=None):
    """
    Read a file from an S3 source.

    Parameters
    ----------
    source : str
        Path starting with s3://, e.g. 's3://bucket-name/key/foo.bar'
    profile_name : str, optional
        AWS profile

    Returns
    -------
    content : bytes

    botocore.exceptions.NoCredentialsError
        Botocore is not able to find your credentials. Either specify
        profile_name or add the environment variables AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY and AWS_SESSION_TOKEN.
        See https://boto3.readthedocs.io/en/latest/guide/configuration.html
    """
    session = boto3.Session(profile_name=profile_name)
    s3 = session.client('s3')
    bucket_name, key = mpu.aws._s3_path_split(source)
    s3_object = s3.get_object(Bucket=bucket_name, Key=key)
    body = s3_object['Body']
    return body.read()
 ```
### Write to S3 
 
 /Users/mlubinsky/CODE/GIT/data-processing/src/main/python/utils/S3Utils.py
```def s3_copy_data(bucket_name, bucket_key, data):```

###  Delete file:
 ```
 s3_resource.Object(second_bucket_name, first_file_name).delete()
 ```
 
 <https://realpython.com/python-boto3-aws-s3/>
 
