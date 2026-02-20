
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_cargo_funcionario import \
    valida_cargo_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_cpf_funcionario import \
    valida_cpf_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_data_admissao_funcionario import valida_data_admissao_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_data_nascimento_funcionario import valida_data_nascimento_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_departamento_funcionario import \
    valida_departamento_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_estado_civil_funcionario import \
    valida_estado_civil_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_nome_funcionario import \
    valida_nome_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_pcd_funcionario import \
    valida_pcd_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_quantidade_dependentes_funcionario import \
    valida_quantidade_dependentes_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_rg_funcionario import \
    valida_rg_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_salario_funcionario import \
    valida_salario_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_sexo_funcionario import \
    valida_sexo_funcionario
from src.verificacao_arquivos.validar_campos.valida_campos_funcionario.valida_telefone_funcionario import \
    valida_telefone_funcionario



def conjunto_validado_funcionario(funcionario):

    erros_nome = valida_nome_funcionario(funcionario, "nome_funcionario")
    erros_telefone = valida_telefone_funcionario(funcionario, "telefone_funcionario")
    erros_cpf = valida_cpf_funcionario(funcionario, "cpf_funcionario")
    erros_rg = valida_rg_funcionario(funcionario, "rg_funcionario")
    erros_salario = valida_salario_funcionario(funcionario, "salario_funcionario")
    erros_departamento = valida_departamento_funcionario(funcionario, "departamento_funcionario")
    erros_cargo = valida_cargo_funcionario(funcionario, "cargo_funcionario")
    erros_data_admissao = valida_data_admissao_funcionario(funcionario, "data_admissao_funcionario")
    erros_data_nascimento = valida_data_nascimento_funcionario(funcionario, "data_nascimento_funcionario", "data_admissao_funcionario")
    erros_sexo = valida_sexo_funcionario(funcionario, "sexo_funcionario")
    erros_pcd = valida_pcd_funcionario(funcionario, "pcd_funcionario")
    erros_estado_civil = valida_estado_civil_funcionario(funcionario, "estado_civil_funcionario")
    erros_quant_dependentes = valida_quantidade_dependentes_funcionario(funcionario, "quantidade_dependentes")

    erros = erros_nome, erros_telefone, erros_cpf, erros_rg, erros_salario, erros_departamento, erros_data_admissao, erros_data_nascimento, erros_sexo, erros_pcd, erros_estado_civil, erros_quant_dependentes, erros_cargo

    lista_erros = []

    for erro in erros:
        if erro:
            lista_erros.append(erro)

    return lista_erros
