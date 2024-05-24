# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 23/05/2024

import os

os.system('cls')
#ENTRADA
print('-'*70)
print('Nome de Aluno')
print('-'*70)

nome = str(input('Nome do aluno: '))

#PROCESSAMENTO
quantidade_de_os = nome.count('o')
primeira_vez = nome.find('o')
ultima_vez = nome.rfind('o')

#SAIDA
print(f'"O" apareceu {quantidade_de_os}')
print(f'Primeira vez que apareceu foi {primeira_vez}')
print(f'Ultima vez que aparece foi {ultima_vez}')
print('-'*70)
print()