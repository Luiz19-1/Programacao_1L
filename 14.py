def numeros_primos(n):
    if n < 2:
        return False
    for numeros in range(2, int(n**0.5)+1):
        if n % numeros == 0:
            return False
    return True


def primos_2an(n):
    return [i for i in range(2, n+1) if numeros_primos(i)]


print(numeros_primos(7))
print(primos_2an(7))
