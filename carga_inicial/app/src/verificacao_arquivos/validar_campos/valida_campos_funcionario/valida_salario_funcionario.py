from src.verificacao_arquivos.ferramentas_validador.campos.valida_salario import valida_salario

def valida_salario_funcionario(pessoa, campo):

    erros = []
    erros.extend(valida_salario(pessoa, campo))

    return erros