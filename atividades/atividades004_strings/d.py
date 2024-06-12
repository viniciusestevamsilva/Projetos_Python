# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 22/05/2024

import os

os.system('cls')

#ENTRADA
print('-'*70)
print('Leia a frase e suas especificações')
print('-'*70)

frase = "So sei que nada sei"

#PROCESSAMENTO
minusculas = frase.lower()
maisculas = frase.upper()
quantidade = len(frase)
segunda_palavra = frase[3:6]
segunda = len(segunda_palavra)

#SAIDA
print(f'Em minusculo : {minusculas}')
print(f'Em maisculas : {maisculas}')
print(f'Esta frase possui {quantidade} de caracteres')
print(f'A segunda palavra tem {segunda} caracteres')
print('-'*70)
print()