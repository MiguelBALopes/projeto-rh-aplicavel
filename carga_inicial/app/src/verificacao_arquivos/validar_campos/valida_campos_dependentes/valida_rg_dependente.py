from src.verificacao_arquivos.ferramentas_validador.campos.valida_rg import valida_rg

def valida_rg_dependente(pessoa, campo):
    erros = []
    erros.extend(valida_rg(pessoa, campo))

    return erros
