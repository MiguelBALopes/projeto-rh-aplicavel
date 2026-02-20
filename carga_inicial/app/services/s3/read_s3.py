import boto3
import json

def read_s3(bucket, key):

    s3 = boto3.client('s3')

    try:
        resposta = s3.get_object(Bucket=bucket, Key=key)
        arquivo = resposta['Body'].read().decode('utf-8')
        arquivo_lido = json.loads(arquivo)
    except:
        raise Exception(f"Erro ao tentar ler do bucket: {bucket} e key: {key}")

    return arquivo_lido