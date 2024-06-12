# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 26/04/2024

# Importa bibliotecas
import os

# Limpar terminal
os.system('cls')


# Entrada
print('-'*70)
print('Equações quadraticas')
print('='*70)

# Declaração
a = 1
b = -6
c = 5
resultado = ''

# Processamento
delta = (b ** 2) - (4 * a * c)

x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)

# Condicional
if delta < 0:
    resultado = print('Os numeros dos valores não deram a raiz real')
else:
    resultado = f'x1 = {x1} | x2 = {x2}'

# Saida
print('-')
print('-'*70)
print(f'{resultado}')
print('-'*70)
print('')