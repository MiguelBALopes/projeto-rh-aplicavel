from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def validador_basico_formato(pessoa, campo, tamanho_minimo, tamanho_maximo, tipo):
    erros = []

    if tipo:
        if type(pessoa[campo]) != tipo:
            erro_campo_type = f"Campo {campo} tem de ser escrito no formato {tipo}"
            adicionar_erro(erros, campo, erro_campo_type)
            return erros

    if tamanho_minimo:
        if len(str(pessoa[campo])) < tamanho_minimo:
            erro_campo_caracteres_min = f"Campo {campo} a baixo dos caracteres exigidos!"
            adicionar_erro(erros, campo, erro_campo_caracteres_min)
            return erros

    if tamanho_maximo:
        if len(str(pessoa[campo])) > tamanho_maximo:
            erro_campo_caractere_max = f"Campo {campo} a cima dos caracteres exigidos!"
            adicionar_erro(erros, campo, erro_campo_caractere_max)
            return erros

    return erros