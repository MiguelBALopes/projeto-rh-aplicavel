from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def valida_mes_data(funcionario, campo):

    erros = []
    if not funcionario[campo][3:5].isdigit():
        return erros

    else:
        if int(funcionario[campo][3:5]) < 1:
            erro_mes_abaixo = f"Erro! campo {campo} está a baixo do mês padrão calendário"
            adicionar_erro(erros, campo, erro_mes_abaixo)
            return erros

        if int(funcionario[campo][3:5]) > 12:
            erro_mes_acima = f"Erro! campo {campo} está a cima do mês padrão calendário"
            adicionar_erro(erros, campo, erro_mes_acima)
            return erros

    return erros
