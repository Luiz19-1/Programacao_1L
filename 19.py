import random


def jogo_adivinhacao(numero_secreto):
    while True:
        palpite = int(input("Digite um numero de (1 a 10): "))

        if palpite == numero_secreto:
            print("Voce acertou!")
            break
        elif palpite < numero_secreto:
            print("O numero secreto é MAIOR que", palpite)
        else:
            print("O numero secreto é MENOR que", palpite)


print(jogo_adivinhacao(random.randint(1, 10)))
