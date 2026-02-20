from src.verificacao_arquivos.ferramentas_validador.campos.valida_estado_civil import valida_estado_civil

def valida_estado_civil_dependente(pessoa, campo):
    erros = []
    erros.extend(valida_estado_civil(pessoa, campo))

    return erros
