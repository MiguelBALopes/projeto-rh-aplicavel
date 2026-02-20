import boto3

def delete_s3(bucket, key):

    s3 = boto3.client('s3')

    try:
        s3.delete_object(Bucket=bucket, Key=key)
        return True
    except:
        raise Exception(f'Erro ao tentar fazer um delete no bucket: {bucket} e key: {key}')
