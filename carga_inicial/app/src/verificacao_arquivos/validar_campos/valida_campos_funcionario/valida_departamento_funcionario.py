from src.verificacao_arquivos.ferramentas_validador.campos.valida_departamento import valida_departamento


def valida_departamento_funcionario(pessoa, campo):

    erros = []
    erros.extend(valida_departamento(pessoa, campo))

    return erros