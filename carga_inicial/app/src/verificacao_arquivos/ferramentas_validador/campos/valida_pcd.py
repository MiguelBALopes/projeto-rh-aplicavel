from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro
from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica


def valida_pcd(pessoa, campo):

    erros = []
    presenca = True

    resultado_basico = validacao_basica(pessoa, campo, presenca, 1, 1, str)

    if resultado_basico:
        erros.extend(resultado_basico)
        return erros

    ''''resultado_str_numerico = validador_str_numerico(pessoa, campo, "")
    if resultado_str_numerico:
        erros.extend(resultado_str_numerico)
        return erros'''

    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros

    opcoes = ["S", "N"]

    if pessoa[campo] not in opcoes:
        erro_pcd_s_n = f"Erro! campo {campo} preenchido incorretamente! preencha S ou N (maiúsculo)"
        adicionar_erro(erros, campo, erro_pcd_s_n)
        return erros

    return erros