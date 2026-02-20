from src.verificacao_arquivos.ferramentas_validador.campos.valida_nome import valida_nome

def valida_nome_dependente(funcionario, campo):
    erros = []
    erros.extend(valida_nome(funcionario, campo))

    return erros