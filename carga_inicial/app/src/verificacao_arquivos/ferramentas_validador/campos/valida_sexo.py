
from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro
from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica


def valida_sexo(pessoa, campo):
    erros = []
    presenca = True

    resultado_basico = validacao_basica(pessoa, campo, presenca, 1, 1, str)
    if resultado_basico:
        erros.extend(resultado_basico)
        return erros


    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros

    opcoes = ["M", "F"]

    if pessoa[campo] not in opcoes:
        erro_sexo_m_f = f"Erro! campo {campo} preenchido incorretamente! preencha M ou F (maiúsculo)"
        adicionar_erro(erros, campo, erro_sexo_m_f)
        return erros



    return erros