from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def valida_ano_data(funcionario, campo):

    erros = []
    if not funcionario[campo][6:10].isdigit():
        return erros


    else:
        if int(funcionario[campo][6:10]) < 1900:
            erro_ano_abaixo = f"Erro! campo {campo} está a baixo do ano mínimo [1900 d.C]"
            adicionar_erro(erros, campo, erro_ano_abaixo)
            return erros

    return erros