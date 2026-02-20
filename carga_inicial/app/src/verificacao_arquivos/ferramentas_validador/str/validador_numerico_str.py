from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def filtrador_caracteres_campo(campo_original, caractere_ignorado):
    try:
        campo_modificado = campo_original.replace(caractere_ignorado, "")
        return campo_modificado.isdigit()
    except Exception:
        return False


def validador_numerico_str(pessoa, campo, caractere_ignorado):
    try:
        erros = []
        if not filtrador_caracteres_campo(pessoa[campo], caractere_ignorado):
            erro_numerico_str = f"Campo {campo} contém caracteres não numéricos"
            adicionar_erro(erros, campo, erro_numerico_str)
            return erros

        return erros

    except Exception:

        return False


