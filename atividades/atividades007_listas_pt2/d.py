# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 17/06/2024

import os
import random

os.system('cls')

print('-'*70)
print('''
      Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor
      ''')
print('-'*70)

# gerando numeros aleatorios
numeros = [random.randint(1,100) for _ in range(50)]

# fatiando e imprimeindo
numeros.sort() # organizando em forma crescente
print('Lista 1' ,numeros[1:10])
print('Lista 2' ,numeros[11:20])
print('Lista 3' ,numeros[21:30])
print('Lista 4' ,numeros[31:40])
print('Lista 5' ,numeros[41:50])
print('='*90)