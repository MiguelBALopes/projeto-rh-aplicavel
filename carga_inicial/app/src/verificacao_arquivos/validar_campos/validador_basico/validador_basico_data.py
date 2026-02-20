from src.verificacao_arquivos.ferramentas_validador.datas.validador_ano_data import valida_ano_data
from src.verificacao_arquivos.ferramentas_validador.datas.validador_data_maior_que_atual import valida_data_atual
from src.verificacao_arquivos.ferramentas_validador.datas.validador_dia_data import valida_dia_data
from src.verificacao_arquivos.ferramentas_validador.datas.validador_formato_data import valida_formato_data
from src.verificacao_arquivos.ferramentas_validador.datas.validador_mes_data import valida_mes_data
from src.verificacao_arquivos.ferramentas_validador.str.validador_numerico_str import validador_numerico_str


def validacao_basica_data(funcionario, campo):
    erros = []


    if campo not in funcionario or funcionario.get(campo) in (None, ""):
        return erros


    #FORMATO
    resultado_forma_data = valida_formato_data(funcionario, campo)
    if resultado_forma_data:
        erros.extend(resultado_forma_data)
        return erros

    #Validador se a data está em numérico
    resultado_numerico_str = validador_numerico_str(funcionario, campo, "/")
    if resultado_numerico_str:
        erros.extend(resultado_numerico_str)
        return erros

    # DIA
    resultado_dia = valida_dia_data(funcionario, campo)
    if resultado_dia:
        erros.extend(resultado_dia)
        return erros

    # MES
    resultado_mes = valida_mes_data(funcionario, campo)
    if resultado_mes:
        erros.extend(resultado_mes)
        return erros

    # ANO
    resultado_ano = valida_ano_data(funcionario, campo)
    if resultado_ano:
        erros.extend(resultado_ano)
        return erros

    #DATA ATUAL
    resultado_data_atual = valida_data_atual(funcionario, campo)
    if resultado_data_atual:
        erros.extend(resultado_data_atual)
        return erros


    return erros