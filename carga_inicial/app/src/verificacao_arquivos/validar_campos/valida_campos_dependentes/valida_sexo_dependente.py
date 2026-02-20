from src.verificacao_arquivos.ferramentas_validador.campos.valida_sexo import valida_sexo

def valida_sexo_dependente(pessoa, campo):
    erros = []
    erros.extend(valida_sexo(pessoa, campo))

    return erros