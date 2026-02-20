from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def valida_formato_data(funcionario, campo):
    erros = []

    if funcionario[campo][2] != "/" or funcionario[campo][5] != "/":
        erro_formato_data = f"Erro! campo {campo} está formatado incorretamente. [dd/mm/aaaa]"
        adicionar_erro(erros, campo, erro_formato_data)

        return erros

    return erros