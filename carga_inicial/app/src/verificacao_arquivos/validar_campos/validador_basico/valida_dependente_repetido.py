from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def validador_de_repeticao_dependentes(funcionario, pk):
    vistos = set()
    repetidos = set()
    erros = []
    erro_ja_gerado = set()

    dependentes = funcionario.get("dependentes", [])


    for dependente in dependentes:
        cpf = dependente.get(pk)
        if not cpf:
            continue

        if cpf in vistos:
            repetidos.add(cpf)
        else:
            vistos.add(cpf)


    for cpf in repetidos:
        if cpf in erro_ja_gerado:
            continue

        erro_clone = f"Dependente detentor do cpf: {cpf} está inválido! Por repetição de cpf entre os dependentes do funcionário"

        adicionar_erro(erros, pk, erro_clone)
        erro_ja_gerado.add(cpf)

    return erros
