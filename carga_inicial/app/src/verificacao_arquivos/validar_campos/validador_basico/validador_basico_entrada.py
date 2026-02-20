from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro
from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_formato import validador_basico_formato


def validacao_basica(pessoa, campo, presenca, tamanho_minimo, tamanho_maximo, tipo):
    erros = []

    if presenca:
        if campo not in pessoa:
            erro_campo_inexistente = f"Campo {campo} inexistente!"
            adicionar_erro(erros, campo, erro_campo_inexistente)
            return erros

        if pessoa[campo] == "":
            erro_campo_vazio = f"Campo {campo} vazio!"
            adicionar_erro(erros, campo, erro_campo_vazio)
            return erros

        resultado = validador_basico_formato(pessoa, campo, tamanho_minimo, tamanho_maximo, tipo)
        if resultado:
            erros.extend(resultado)
            return erros

    else:
        if campo not in pessoa:
            return erros

        resultado_else = validador_basico_formato(pessoa, campo, tamanho_minimo, tamanho_maximo, tipo)
        if resultado_else:
            erros.extend(resultado_else)
            return erros


    return erros
