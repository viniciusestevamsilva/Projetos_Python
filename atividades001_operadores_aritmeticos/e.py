
# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 18/04/2024

#Imports
import os

os.system('cls')

# Entrada
print('-'*70)
print('Coloque um numero')
print('-'*70)
numero = int(input('Digite um numero: '))

# Processamento
sucessor = numero + 1
antecessor = numero - 1

# Saida
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'o sucessor do {numero} é {sucessor} e o antecessor é {antecessor}')