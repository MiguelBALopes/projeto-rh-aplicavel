from src.verificacao_arquivos.validador_chefe.conjunto_validado.conjunto_validado_dependentes import \
    conjunto_validado_dependente
from src.verificacao_arquivos.validador_chefe.conjunto_validado.conjunto_validado_funcionario import \
    conjunto_validado_funcionario
from src.verificacao_arquivos.validar_campos.validador_basico.valida_func_dependente_repetido import \
    valida_func_dependente_repetido
from src.verificacao_arquivos.validar_campos.validador_basico.valida_func_repetido import validador_de_repeticao_funcionario
from src.verificacao_arquivos.ferramentas_validador.campos.valida_existencia_dependentes import \
    valida_existencia_dependentes
from src.verificacao_arquivos.validar_campos.validador_basico.valida_dependente_repetido import \
    validador_de_repeticao_dependentes


def valida_funcionario(arquivo_lido_carga_incial):

    retorno_erros_funcionario = []
    retorno_quente_funcionario = []

    for funcionario in arquivo_lido_carga_incial:

        if "resumo_validacao" in funcionario:
            continue

        erros_funcionarios = conjunto_validado_funcionario(funcionario)

        erros_repeticao_funcionario = validador_de_repeticao_funcionario(arquivo_lido_carga_incial, "cpf_funcionario")

        for erro_clone in erros_repeticao_funcionario:
            if erro_clone and str(funcionario.get("cpf_funcionario")) in erro_clone["erro"]:
                erros_funcionarios.append(erro_clone)

        erros_existencia_dependentes = valida_existencia_dependentes(funcionario)
        if erros_existencia_dependentes:
            erros_funcionarios.extend(erros_existencia_dependentes)


        erros_repeticao_dependente = validador_de_repeticao_dependentes(funcionario, "cpf_dependente")

        erro_dependente_existe = False

        erros_repeticao_func_dep = valida_func_dependente_repetido(funcionario)
        if erros_repeticao_func_dep:
            erros_funcionarios.extend(erros_repeticao_func_dep)

        for dependente in funcionario.get("dependentes", []):

            erros_dependentes = conjunto_validado_dependente(dependente)

            for erro_clone in erros_repeticao_dependente:
                if erro_clone and str(dependente.get("cpf_dependente")) in erro_clone["erro"]:
                    erros_dependentes.append(erro_clone)

            if erros_dependentes:
                dependente["erros_dependente"] = erros_dependentes
                erro_dependente_existe = True



        if erros_funcionarios or erro_dependente_existe:
            if erros_funcionarios:
                funcionario["erros_funcionario"] = erros_funcionarios
            retorno_erros_funcionario.append(funcionario)
        else:
            retorno_quente_funcionario.append(funcionario)


    return retorno_erros_funcionario, retorno_quente_funcionario