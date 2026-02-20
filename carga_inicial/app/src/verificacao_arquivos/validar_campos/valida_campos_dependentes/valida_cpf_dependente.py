from src.verificacao_arquivos.ferramentas_validador.campos.valida_cpf import valida_cpf

def valida_cpf_dependente(pessoa, campo):
    erros = []
    erros.extend(valida_cpf(pessoa, campo))

    return erros