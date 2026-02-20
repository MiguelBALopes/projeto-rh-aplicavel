
from src.verificacao_arquivos.ferramentas_validador.campos.valida_nome import valida_nome

def valida_nome_funcionario(pessoa, campo):
    erros = []
    erros.extend(valida_nome(pessoa, campo))

    return erros
