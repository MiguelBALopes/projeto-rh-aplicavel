
from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro
from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica


def valida_estado_civil(pessoa, campo):

    erros = []
    presenca = True

    resultado_basico = validacao_basica(pessoa, campo, presenca, 1, 1, str)

    if resultado_basico:
        erros.extend(resultado_basico)
        return erros

    '''resultado_str_numerico = validador_str_numerico(pessoa, campo, "")
    if resultado_str_numerico:
        erros.extend(resultado_str_numerico)
        return erros'''

    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros

    opcoes = ["S", "C", "V", "U"]

    if pessoa[campo] not in opcoes:

        erro_estado_civil_opcoes = f"Erro! campo {campo} preenchido incorretamente! preencha S ou C ou V ou U (maiúsculo)"
        adicionar_erro(erros, campo, erro_estado_civil_opcoes)
        return erros

    return erros