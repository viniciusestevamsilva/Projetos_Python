# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data /06/2024

import os


os.system('cls')

print('-'*70)
print('Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.')
print('-'*70)

nomes = []

for i in range(0, 5): 
    nome = input('Insira um nome: ')
    nomes.append(nome)

print()
print('Lista de Nomes: ')
for indice, nome in enumerate(nomes, start = 1):
    pessoas = f'{indice}: {nome}'