https://boto3.amazonaws.com/v1/documentation/api/latest/index.html


https://stackoverflow.com/questions/30249069/listing-contents-of-a-bucket-with-boto3

https://stackoverflow.com/questions/27292145/python-boto-list-contents-of-specific-dir-in-bucket

https://towardsdatascience.com/demystifying-boto3-how-to-use-any-aws-service-with-python-b5c69593bcfa

<https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/s3.html>

```
 import boto3
 boto3.__version__
 1.9.124
```

### Use paginator to get > 1,000 objects 

The inbuilt boto3 Paginator class is the easiest way to overcome the 1000 record limitation of list-objects-v2. This can be implemented as follows
```
s3 = boto3.client('s3')

paginator = s3.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket='bucket', Prefix='prefix')

for page in pages:
    for obj in page['Contents']:
        print(obj['Size'])
        
```        
Python - boto paginator: 
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Paginator.ListObjectsV2

Java paginator:

https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/pagination.html

https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/paginators/package-summary.html

https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html





<https://www.slsmk.com/use-boto3-to-open-an-aws-s3-file-directly/>

<https://www.slsmk.com/amazon-aws-tech-notes-and-articles/>

https://hackersandslackers.com/s3-boto3-python-sdk/

<https://medium.com/swlh/using-s3-just-like-a-local-file-system-in-python-497737783f11>

### How to get list of subfolders:

```
def get_keys_in_bucket_folder(bucket_name, prefix=None):
    try:
      c = boto3.client('s3')
      result = c.list_objects(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
      for o in result.get('CommonPrefixes'):
          print 'sub folder : ', o.get('Prefix')
      return
      
my_bucket="xxxx"
my_prefix = "yyyy/zzzz/"      - last / is important!
get_keys_in_bucket_folder(my_bucket, my_prefix)
```

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
 
