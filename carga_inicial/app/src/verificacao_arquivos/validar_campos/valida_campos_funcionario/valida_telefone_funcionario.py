from src.verificacao_arquivos.ferramentas_validador.campos.valida_telefone import valida_telefone

def valida_telefone_funcionario(pessoa, campo):
    erros = []
    erros.extend(valida_telefone(pessoa, campo))

    return erros

