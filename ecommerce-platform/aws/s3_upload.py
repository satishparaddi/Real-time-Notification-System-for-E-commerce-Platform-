import boto3

def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response
