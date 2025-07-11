def maior_numero(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


print(maior_numero(1, 2, 3))

print(maior_numero(1, 3, 2))

print(maior_numero(3, 1, 2))
