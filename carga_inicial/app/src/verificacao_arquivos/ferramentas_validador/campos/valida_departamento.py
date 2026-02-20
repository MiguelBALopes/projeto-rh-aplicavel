from src.verificacao_arquivos.ferramentas_validador.str.validador_numerico_str import validador_numerico_str
from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica


def valida_departamento(pessoa, campo):

    erros = []
    presenca = True

    resultado_basico = validacao_basica(pessoa, campo, presenca, 1, 1, str)
    if resultado_basico:
        erros.extend(resultado_basico)
        return erros

    resultado_numerico_str = validador_numerico_str(pessoa, campo, "")
    if resultado_numerico_str:
        erros.extend(resultado_numerico_str)
        return erros


    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros


    return erros
