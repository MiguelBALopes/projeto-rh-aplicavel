
from src.verificacao_arquivos.ferramentas_validador.datas.validador_bissexto_data import valida_ano_bissexto_data
from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def valida_dia_data(funcionario, campo):

    try:
        erros = []
        if not funcionario[campo][0:2].isdigit():
            return False

        else:

            dia = int(funcionario[campo][0:2])
            mes = int(funcionario[campo][3:5])

            if mes < 1 or mes > 12:
                return False

            else:

                dias_mes = {
                    1: 31,
                    2: 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31
                }

                if mes == 2 and valida_ano_bissexto_data(funcionario, campo):
                    dias_mes[2] = 29


                if dia > dias_mes[mes]:
                    erro_dia_acima = f"Erro! campo {campo} está a cima do dia padrão calendário"
                    adicionar_erro(erros, campo, erro_dia_acima)
                    return erros
        return erros

    except Exception:
        return False