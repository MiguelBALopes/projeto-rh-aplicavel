from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def validador_de_repeticao_funcionario(arquivo_lido, pk):
    vistos = set()
    repetidos = set()
    erros = []
    erro_ja_gerado = set()

    # Descobre CPFs repetidos
    for pessoa in arquivo_lido:
        cpf = pessoa.get(pk)
        if not cpf:
            continue

        if cpf in vistos:
            repetidos.add(cpf)
        else:
            vistos.add(cpf)

    # Gera UM erro por CPF repetido
    for cpf in repetidos:
        if cpf in erro_ja_gerado:
            continue

        erro_clone = f"Funcionário detentor do cpf: {cpf} está inválido! Por repetição de cpf com demais funcionários"

        adicionar_erro(erros, pk, erro_clone)
        erro_ja_gerado.add(cpf)

    return erros
