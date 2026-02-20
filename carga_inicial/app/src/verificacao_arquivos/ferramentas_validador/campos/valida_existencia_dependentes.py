from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def valida_existencia_dependentes(funcionario):

    erros_existencia_dependentes = []

    if "quantidade_dependentes" in funcionario:

        try:
            quantidade = int(funcionario["quantidade_dependentes"])
        except (ValueError, TypeError):
            quantidade = None

        if quantidade is not None:

            dependentes = funcionario.get("dependentes")

            if quantidade == 0:
                if dependentes:
                    erro = "Erro! campo dependentes existe mesmo a quantidade sendo 0"
                    adicionar_erro(erros_existencia_dependentes, "dependentes", erro)

            elif dependentes:
                if quantidade != len(dependentes):
                    erro = f"Erro! campo quantidade_dependentes indica {quantidade}, mas existem {len(dependentes)} cadastrados"
                    adicionar_erro(erros_existencia_dependentes, "dependentes e quantidade_dependentes", erro)
    list_erros = []

    for erros in erros_existencia_dependentes:
        if erros:
            list_erros.append(erros)

    return list_erros