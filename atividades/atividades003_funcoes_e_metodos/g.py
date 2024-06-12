# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 10/05/2024

# Importando bibliotecas
import os
import math


os.system('cls')

# Entrada
print('='*70)
print('Calcule as raízes da equação do 2º grau')
print('='*70)

a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

# Processamento
delta = (b ** 2) - (4 * a * c)
resultado = ''

x1 = (-b + math.pow(delta, 2)) / (2 * a)
x2 = (-b - math.pow(delta, 2)) / (2 * a)

# Condicional
if delta < 0 :
    resultado = f'Esses número não possuiem raizes reais'
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    resultado = f'x1:{x1}| x2: {x2}'


# Saida
print('='*70)
print(f'{resultado}')
print('='*70)