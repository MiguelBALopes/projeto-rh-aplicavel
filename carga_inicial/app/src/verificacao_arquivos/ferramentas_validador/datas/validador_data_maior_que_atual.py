import datetime

from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def valida_data_atual(funcionario, campo):

    try:

        erros = []
        data_para_validar = datetime.date(int(funcionario[campo][6:10]), int(funcionario[campo][3:5]), int(funcionario[campo][0:2]))
        data_atual = datetime.date.today()


        if data_para_validar > data_atual:
            erro_data_futura = f"Erro! campo {campo} está com a data no futuro do dia de hoje"
            adicionar_erro(erros, campo, erro_data_futura)
            return erros

        return erros

    except Exception:
        return False

