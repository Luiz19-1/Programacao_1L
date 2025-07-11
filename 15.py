def analisa_lista(lista):

    maximo = max(lista)
    minimo = min(lista)
    media = sum(lista)/len(lista)

    return maximo, minimo, media


print(analisa_lista([1, 2, 3, 5, 8]))
