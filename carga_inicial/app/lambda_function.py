from services.dynamoDB.create_table import create_table
from services.dynamoDB.write_table import write_table
from services.s3.excluir_s3 import delete_s3
from services.s3.gravar_s3 import write_s3
from services.s3.read_s3 import read_s3
from src.verificacao_arquivos.validador_chefe.filtro_arquivo_quente.valida_arquivo_quente_funcionario import \
        filtra_arquivo_validado_funcionario
from src.verificacao_arquivos.validador_chefe.validar_campos import valida_arquivo_entrada



def lambda_handler(event, context):

    arquivo_lido = read_s3("s3-carga-inicial-funcionarios", "carga_inicial_funcionario.json")
    if not arquivo_lido:
        return "Arquivo não encontrado no bucket"

    retorno_funcionarios_com_erros, funcionarios_quentes = valida_arquivo_entrada(arquivo_lido)

    if not write_s3("carga_inicial_funcionario_retorno_erros.json", "s3-carga-inicial-funcionarios", retorno_funcionarios_com_erros):
        return "Erro ao gravar retorno de erros"

    arquivo_quente_funcionario = filtra_arquivo_validado_funcionario(funcionarios_quentes)


    if arquivo_quente_funcionario:
        if not create_table('funcionarios', 'sa-east-1'):
            return "Falha ao criar a tabela no dynamoDB"

        if not write_table('funcionarios', arquivo_quente_funcionario):
            return "Falha ao gravar o arquivo quente em uma tabela dynamoDB"

    if not delete_s3("s3-carga-inicial-funcionarios", "carga_inicial_funcionario.json"):
        return "Erro ao excluir a carga_inicial do bucket"

    return "Carga inicial validada, retornando erros em um bucket_S3, gravando os funcionarios quentes em uma tabela dynamoDB, deletado a carga_inicial_funcionarios ao final do processo"