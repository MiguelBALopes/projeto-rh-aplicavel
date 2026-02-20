import boto3

def create_table(table_name, region):

    try:
        dynamodb = boto3.resource('dynamodb', region_name=region)

        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'cpf_funcionario',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'cpf_funcionario',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }

        )

        print("Criando tabela...")
        table.wait_until_exists()
        print("Tabela criada com sucesso!")

        return True

    except:
        raise Exception(f"Erro ao tentar criar uma tabela no dynamoDB: {table_name} e region: {region}")