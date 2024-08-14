import os

os.system('cls')


def numeros(a, b, c):
    a +=1
    b +=1
    c +=1
    return a, b, c


valor1,valor2,valor3 = numeros(10,10,10)

print(f'Valor1: {valor1}| Valor2: {valor2}| Valor3: {valor3}')