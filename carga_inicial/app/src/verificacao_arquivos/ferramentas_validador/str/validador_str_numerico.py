from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def filtrador_numerico_campo(campo_original, caractere_ignorado):

    campo_modificado = campo_original.replace(caractere_ignorado, "")
    return campo_modificado.isdigit()


def validador_str_numerico(pessoa, campo, caractere_ignorado):

    erros = []

    if campo not in pessoa:
        return erros

    if filtrador_numerico_campo(pessoa[campo], caractere_ignorado):
        erro_str_numerico = f"Erro! campo {campo} contém caracteres numéricos"
        adicionar_erro(erros, campo, erro_str_numerico)

        return erros

    return erros