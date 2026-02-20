from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica

def valida_salario(pessoa, campo):

    erros = []
    presenca = True

    resultado = validacao_basica(pessoa, campo, presenca, 3, 100, float)
    if resultado:
        erros.extend(resultado)
        return erros

    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros

    return erros