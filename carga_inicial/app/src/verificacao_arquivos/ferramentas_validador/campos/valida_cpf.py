from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica
from src.verificacao_arquivos.ferramentas_validador.str.validador_numerico_str import validador_numerico_str


def valida_cpf(pessoa, campo):

    erros = []
    presenca = True

    resultado = validacao_basica(pessoa, campo, presenca, 11, 11, str)
    if resultado:
        erros.extend(resultado)
        return erros

    resultado_numerico_str = validador_numerico_str(pessoa, campo, "")
    if resultado_numerico_str:
        erros.extend(resultado_numerico_str)
        return erros

    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros

    return erros

