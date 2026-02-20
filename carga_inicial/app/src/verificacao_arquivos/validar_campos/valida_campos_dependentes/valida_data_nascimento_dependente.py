from src.verificacao_arquivos.ferramentas_validador.campos.valida_data_nascimento import valida_data_nascimento

def valida_data_nascimento_dependente(pessoa, campo):
    erros = []
    erros.extend(valida_data_nascimento(pessoa, campo))
    return erros