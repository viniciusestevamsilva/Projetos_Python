# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data /06/2024

import os


os.system('cls')

print('-'*70)
print('Ler uma lista com 10 números, depois apresente o maior e o menor número da lista')
print('-'*70)

lista_numeros = []

entrada = input('Insira 10 valores separados por vírgula: ').replace(' ','')

numeros = entrada.split(',')

lista_numeros.extend([int(numero) for numero in numeros])


lista_numeros.sort()

print()
print(f'Lista completa: {lista_numeros}')
menor = lista_numeros[0]
maior = lista_numeros[-1]
print()
print(f'O menor número da lista é: {menor} e o maior: {maior}')