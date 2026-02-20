from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import \
    adicionar_erro


def valida_func_dependente_repetido(pessoa):
    erros_func = []
    cpf_funcionario = pessoa.get("cpf_funcionario")

    if not cpf_funcionario:
        return erros_func


    for dependente in pessoa.get("dependentes", []):
        cpf_dependente = dependente.get("cpf_dependente")

        if not cpf_dependente:
            return erros_func

        if cpf_funcionario == cpf_dependente:
            erro = f"Funcionário detentor do cpf: {cpf_funcionario} está inválido por repetição do cpf com seus dependentes"
            adicionar_erro(erros_func, "cpf_funcionario", erro)
            break


    return erros_func
