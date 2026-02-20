from src.verificacao_arquivos.validar_campos.validador_basico.adicionar_erro import adicionar_erro
from src.verificacao_arquivos.validar_campos.validador_basico.validador_basico_entrada import validacao_basica

def valida_nome(pessoa, campo):
    erros = []
    presenca = True

    resultado = (validacao_basica(pessoa, campo, presenca, 12, 50, str))
    if resultado:
        erros.extend(resultado)
        return erros

    if campo not in pessoa or pessoa.get(campo) in (None, ""):
        return erros

    if " " not in pessoa.get(campo):
        erro_nome_espaco = f"Erro! campo {campo} não está separado, o nome e os sobrenomes"
        adicionar_erro(erros, campo, erro_nome_espaco)

    return erros
