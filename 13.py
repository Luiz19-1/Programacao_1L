def palindromo(palavra):
    invertida = palavra[::-1]
    if invertida == palavra:
        return True
    else:
        return False


print(palindromo("arara"))

print(palindromo("luis"))
