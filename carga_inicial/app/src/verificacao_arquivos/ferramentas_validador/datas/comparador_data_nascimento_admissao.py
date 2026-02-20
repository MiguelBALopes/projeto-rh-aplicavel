import datetime

from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro



def valida_idade(funcionario, campo_data_nascimento, campo_data_admissao):
    erros = []
    try:


        data_nascimento = datetime.date(
            int(funcionario[campo_data_nascimento][6:10]),
            int(funcionario[campo_data_nascimento][3:5]),
            int(funcionario[campo_data_nascimento][0:2])
        )

        data_admissao = datetime.date(
            int(funcionario[campo_data_admissao][6:10]),
            int(funcionario[campo_data_admissao][3:5]),
            int(funcionario[campo_data_admissao][0:2])
        )

        if data_nascimento > data_admissao:
            erro_data_nascimento_admissao = f"Erro! campo {campo_data_nascimento} está mais recente que a data de admissão, como ta admitido se ainda não nasceu?"
            adicionar_erro(erros, campo_data_nascimento, erro_data_nascimento_admissao)
            return erros


        return erros

    except Exception:
        return erros

