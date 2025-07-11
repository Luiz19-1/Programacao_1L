import random


def simular_dado(n):
    return [random.randint(1, 6) for rolagem in range(n)]


print(simular_dado(3))
