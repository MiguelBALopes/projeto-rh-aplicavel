from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica


def valida_rg(pessoa, campo):

    erros = []
    presenca = True

    resultado = validacao_basica(pessoa, campo, presenca, 7, 11, str)
    if resultado:
        erros.extend(resultado)
        return erros

    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros

    return erros