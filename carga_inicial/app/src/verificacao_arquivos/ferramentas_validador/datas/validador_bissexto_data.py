def valida_ano_bissexto_data(funcionario, campo):
    ano = int(funcionario[campo][6:10])
    return (ano % 4 == 0)