from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_data import validacao_basica_data
from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica


def valida_data_admissao_funcionario(pessoa, campo):

    erros = []
    presenca = True


    resultado_basico = validacao_basica(pessoa, campo, presenca, 10, 10, str)
    if resultado_basico:
        erros.extend(resultado_basico)
        return erros

    resultado_basico_data = validacao_basica_data(pessoa, campo)
    if resultado_basico_data:
        erros.extend(resultado_basico_data)
        return erros

    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros


    return erros
