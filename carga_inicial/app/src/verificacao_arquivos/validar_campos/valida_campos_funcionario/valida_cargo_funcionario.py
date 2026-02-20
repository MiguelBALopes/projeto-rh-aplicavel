from src.verificacao_arquivos.ferramentas_validador.campos.valida_cargo import valida_cargo

def valida_cargo_funcionario(funcionario, campo):

    erros = []
    erros.extend(valida_cargo(funcionario, campo))

    return erros