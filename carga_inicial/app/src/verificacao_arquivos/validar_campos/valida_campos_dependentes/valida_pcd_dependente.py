from src.verificacao_arquivos.ferramentas_validador.campos.valida_pcd import valida_pcd

def valida_pcd_dependente(pessoa, campo):
    erros = []
    erros.extend(valida_pcd(pessoa, campo))

    return erros
