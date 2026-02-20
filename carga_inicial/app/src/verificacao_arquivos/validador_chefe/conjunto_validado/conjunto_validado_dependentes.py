from src.verificacao_arquivos.validar_campos.valida_campos_dependentes.valida_cpf_dependente import \
    valida_cpf_dependente
from src.verificacao_arquivos.validar_campos.valida_campos_dependentes.valida_data_nascimento_dependente import \
    valida_data_nascimento_dependente
from src.verificacao_arquivos.validar_campos.valida_campos_dependentes.valida_estado_civil_dependente import \
    valida_estado_civil_dependente
from src.verificacao_arquivos.validar_campos.valida_campos_dependentes.valida_nome_dependente import valida_nome_dependente
from src.verificacao_arquivos.validar_campos.valida_campos_dependentes.valida_pcd_dependente import \
    valida_pcd_dependente
from src.verificacao_arquivos.validar_campos.valida_campos_dependentes.valida_rg_dependente import valida_rg_dependente
from src.verificacao_arquivos.validar_campos.valida_campos_dependentes.valida_sexo_dependente import \
    valida_sexo_dependente

def conjunto_validado_dependente(dependente):

    erros_nome = valida_nome_dependente(dependente, "nome_dependente")
    erros_cpf = valida_cpf_dependente(dependente, "cpf_dependente")
    erros_rg = valida_rg_dependente(dependente, "rg_dependente")
    erros_data_nascimento = valida_data_nascimento_dependente(dependente, "data_nascimento_dependente")
    erros_sexo = valida_sexo_dependente(dependente, "sexo_dependente")
    erros_pcd = valida_pcd_dependente(dependente, "pcd_dependente")
    erros_estado_civil = valida_estado_civil_dependente(dependente, "estado_civil_dependente")

    erros = erros_nome, erros_cpf, erros_rg, erros_data_nascimento, erros_sexo, erros_pcd, erros_estado_civil

    lista_erros = []

    for erro in erros:
        if erro:
            lista_erros.append(erro)

    return lista_erros