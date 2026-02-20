import boto3
import json


def write_s3(key, bucket, arquivo_lido):
    s3 = boto3.client('s3')

    try:
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(arquivo_lido)
        )
        return True

    except:
        raise Exception(f"Erro ao tentar gravar do bucket: {bucket} e key: {key}")

