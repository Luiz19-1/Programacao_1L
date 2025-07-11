def contar_vogais(palavra):
    vogais = ["a", "e", "i", "o", "u"]
    palavra = palavra.lower()
    contador = 0
    for i in palavra:
        if i in vogais:
            contador += 1
    return contador


print(contar_vogais('Eduardo'))
