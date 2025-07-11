def intercalar_listas(lista1, lista2):
    resultado = []
    for par in zip(lista1, lista2):
        resultado.extend(par)
    return resultado


print(intercalar_listas([1, 2, 3], ["a", "b", "c"]))
