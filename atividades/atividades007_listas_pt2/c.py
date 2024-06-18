# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 17/06/2024

import os
import random

os.system('cls')

print('-'*90)
print('''
      Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
      ''')
print('='*90)

# gerando numeros aleatorios
numeros = [random.randint(1,100) for _ in range(50)]

# fatiando e imprimeindo
print(numeros[1:10])
print(numeros[11:20])
print(numeros[21:30])
print(numeros[31:40])
print(numeros[41:50])
print('='*90)