# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 17/06/2024

import os


os.system('cls')

print('-'*70)
print('''
      Ler uma lista com 10 números, depois apresente o maior e o menor número da lista
      ''')
print('-'*70)

lista_numeros = [] # lista vazia

# entrada
entrada = input('Insira 10 valores: ')
# separando valores com ","
numeros = entrada.split(',')

# iterando a lista
lista_numeros.extend([(numero) for numero in numeros])
lista_numeros.sort()

# saida
print()
print(f'Lista completa: {lista_numeros}')
menor = lista_numeros[0]
maior = lista_numeros[-1]
print()
print(f'O menor número da lista é: {menor} e o maior: {maior}')