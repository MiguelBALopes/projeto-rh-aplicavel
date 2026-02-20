from src.verificacao_arquivos.ferramentas_validador.str.validador_numerico_str import validador_numerico_str
from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica
from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro

def valida_quantidade_dependentes(pessoa, campo):

    erros = []
    presenca = True

    resultado_basico = validacao_basica(pessoa, campo, presenca, 2, 2, str)
    if resultado_basico:
        erros.extend(resultado_basico)
        return erros

    resultado_numerico_str = validador_numerico_str(pessoa, campo, "")
    if resultado_numerico_str:
        erros.extend(resultado_numerico_str)
        return erros

    if int(pessoa.get(campo)) != 0:
        if pessoa.get("dependentes") is None:
            erro = "Erro! campo dependentes não existe, sendo que o campo quantidade_dependentes, está indicando que dependente existente"
            adicionar_erro(erros, "dependentes", erro)

    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros

    return erros