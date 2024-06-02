# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 02/06/2024

import os


os.system('cls')

print('-'*70)
print('Programa anterior porem com input')
print('='*70) 

inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

contador = inicio

while contador <= final:
    print(f'numero: {contador}', end=' | ')
    contador += 1

print('-'*70)