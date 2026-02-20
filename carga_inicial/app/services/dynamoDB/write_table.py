import boto3
import json
from decimal import Decimal

def write_table(table_name, arquivo_para_gravar):

    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)

        arquivo_convertido = json.loads(json.dumps(arquivo_para_gravar),parse_float=Decimal)

        with table.batch_writer() as batch:
            for item in arquivo_convertido:
                batch.put_item(Item=item)

        print("Dados inseridos com sucesso!")

        return True


    except Exception as e:
        raise Exception(f"Erro ao tentar gravar itens no dynamoDB: {e}")