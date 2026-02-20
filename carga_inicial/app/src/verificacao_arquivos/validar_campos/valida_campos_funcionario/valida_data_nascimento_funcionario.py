
from src.verificacao_arquivos.ferramentas_validador.datas.calcular_idade import calcular_idade
from src.verificacao_arquivos.ferramentas_validador.datas.comparador_data_nascimento_admissao import valida_idade
from src.verificacao_arquivos.ferramentas_validador.campos.valida_data_nascimento import valida_data_nascimento
from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro


def valida_data_nascimento_funcionario(pessoa, campo_data_nascimento, campo_data_admissao):

    erros = []

    resultado_valida_data_nascimento = valida_data_nascimento(pessoa, campo_data_nascimento)
    if resultado_valida_data_nascimento:
        erros.extend(resultado_valida_data_nascimento)
        return erros

    resultado_nascimento_admissao = valida_idade(pessoa, campo_data_nascimento, campo_data_admissao)
    if resultado_nascimento_admissao:
        erros.extend(resultado_nascimento_admissao)
        return erros

    if campo_data_nascimento not in pessoa or pessoa.get(campo_data_nascimento) in (None, ""):
        return erros

    if not erros:

        if calcular_idade(pessoa, campo_data_nascimento) < 16:
            erro_idade_abaixo = f"Erro! campo {campo_data_nascimento} está invalido! idade menor que 16 anos"
            adicionar_erro(erros, campo_data_nascimento, erro_idade_abaixo)
            return erros

        if calcular_idade(pessoa, campo_data_nascimento) > 120:
            erro_idade_acima = f"Erro! campo {campo_data_nascimento} está invalido! idade maior que 120 anos"
            adicionar_erro(erros, campo_data_nascimento, erro_idade_acima)
            return erros



    return erros
