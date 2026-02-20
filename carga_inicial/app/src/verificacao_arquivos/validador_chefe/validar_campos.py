from src.verificacao_arquivos.validador_chefe.escrever_retorno_erros.valida_funcionario import \
    valida_funcionario
from src.verificacao_arquivos.validador_chefe.escrever_retorno_erros.retorno_resumo import retorno_resumo


def valida_arquivo_entrada(arquivo_lido_carga_inicial):


    funcionarios_com_erros, funcionarios_quente = valida_funcionario(arquivo_lido_carga_inicial)
    resumo = retorno_resumo(arquivo_lido_carga_inicial)
    funcionarios_com_erros.extend(resumo)

    return funcionarios_com_erros, funcionarios_quente