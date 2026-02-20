from src.verificacao_arquivos.ferramentas_validador.campos.valida_quantidade_dependentes import \
    valida_quantidade_dependentes

def valida_quantidade_dependentes_funcionario(pessoa, campo):

    erros = []
    erros.extend(valida_quantidade_dependentes(pessoa, campo))

    return erros
