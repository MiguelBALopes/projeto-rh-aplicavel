import datetime

def calcular_idade(funcionario, campo_data_nascimento):

    try:
        data_nascimento = datetime.date(
            int(funcionario[campo_data_nascimento][6:10]),
            int(funcionario[campo_data_nascimento][3:5]),
            int(funcionario[campo_data_nascimento][0:2])
        )

        data_atual = datetime.date.today()

        ano_atual = data_atual.year
        ano_nascimento = data_nascimento.year

        idade = ano_atual - ano_nascimento

        if data_atual.month < data_nascimento.month or (
                data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
            idade = idade - 1

        return idade

    except Exception:
        return False

