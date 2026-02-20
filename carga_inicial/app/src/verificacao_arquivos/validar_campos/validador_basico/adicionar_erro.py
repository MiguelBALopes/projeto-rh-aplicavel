def adicionar_erro(lista, campo, erro):
    lista.append({
        "campo": f"{campo}",
        "erro": f"{erro}"
    })

    return lista
