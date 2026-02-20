

def gerar_resumo_validacao(arquivo_lido):

    total_verificacoes = 0
    total_erros = 0
    total_sucessos = 0

    for funcionario in arquivo_lido:



        total_verificacoes += 1

        teve_erro = False

        if funcionario.get("erros_funcionario"):
            teve_erro = True

        for dependente in funcionario.get("dependentes", []):
            if dependente.get("erros_dependente"):
                teve_erro = True

        if teve_erro:
            total_erros += 1
        else:
            total_sucessos += 1

    return {
        "total_funcionarios_verificados": total_verificacoes,
        "total_de_funcionarios_com_erros": total_erros,
        "total_de_funcionarios_corretos": total_sucessos
    }