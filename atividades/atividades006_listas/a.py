# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 12/06/2024

import os


os.system('cls')

print('-'*70)
print('''
      Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.
      ''')
print('-'*70)

# Entrada
posicao = int(input('Posição em que vai inserir o numero: '))
numero = input('Elemento que vai ser inserido: ')

lista = [ 1, 2, 3, 5, 6]

# validação
if posicao >= 0 and posicao <= len(lista):
    lista.insert(posicao, numero)
    print('-'*70)
    print('Lista após a inserção:', lista)
    print('-'*70)
else:
    print('-'*70)
    print(f'Invalido!! está fora da lista que tem {len(lista)}!!')
    print('-'*70)