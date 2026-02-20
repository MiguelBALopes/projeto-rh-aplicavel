from src.verificacao_arquivos.validador_chefe.escrever_retorno_erros.gera_resumo_validacao import gerar_resumo_validacao


def retorno_resumo(arquivo_lido):
    for funcionario in arquivo_lido:

        novo_arquivo = []

        for item in arquivo_lido:
            if not item:
                continue
            if "resumo_validacao" not in item:
                novo_arquivo.append(item)

        arquivo_lido.clear()

        for item in novo_arquivo:
            arquivo_lido.append(item)

        if "resumo_validacao" in funcionario:
            continue

    resumo = gerar_resumo_validacao(arquivo_lido)

    return [{
        "resumo_validacao": resumo
    }]