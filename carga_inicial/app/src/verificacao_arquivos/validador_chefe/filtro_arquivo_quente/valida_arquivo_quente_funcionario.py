def filtra_arquivo_validado_funcionario(arquivo_lido):


    arquivo_quente = []
    validacoes_funcionario = [
        "nome_funcionario", "telefone_funcionario", "data_ultima_ferias", "cpf_funcionario",
        "rg_funcionario", "sexo_funcionario", "data_nascimento_funcionario",
        "data_admissao_funcionario", "departamento_funcionario",
        "cargo_funcionario", "salario_funcionario",
        "estado_civil_funcionario", "pcd_funcionario",
        "quantidade_dependentes", "dependentes"
    ]
    validacoes_dependentes = [
        "nome_dependente", "cpf_dependente", "rg_dependente",
        "data_nascimento_dependente", "sexo_dependente",
        "pcd_dependente", "estado_civil_dependente"
    ]

    for pessoa in arquivo_lido:

        if "resumo_validacao" in pessoa:
            continue

        tem_erro_funcionario = False
        if pessoa.get("erros_funcionario"):
            tem_erro_funcionario = True

        tem_erro_dependente = False
        for dependente in pessoa.get("dependentes", []):
            if dependente.get("erros_dependente"):
                tem_erro_dependente = True
                break

        if not tem_erro_funcionario and not tem_erro_dependente:

            for campo_funcionario in list(pessoa):
                if campo_funcionario not in validacoes_funcionario:
                    pessoa.pop(campo_funcionario, None)

            pessoa.pop("erros_funcionario", None)

            for dependente in pessoa.get("dependentes", []):

                for campo_dependente in list(dependente):
                    if campo_dependente not in validacoes_dependentes:
                        dependente.pop(campo_dependente, None)

                dependente.pop("erros_dependente", None)

            arquivo_quente.append(pessoa)

    return arquivo_quente

