def epar(num):
    resto = num % 2
    if resto == 0:
        return True
    else:
        return False


par = epar(3)
print(par)

par = epar(2)
print(par)
