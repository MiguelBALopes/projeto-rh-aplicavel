from src.verificacao_arquivos.ferramentas_validador.campos.valida_pcd import valida_pcd


def valida_pcd_funcionario(funcionario, campo):

    erros = []
    erros.extend(valida_pcd(funcionario, campo))
    return erros