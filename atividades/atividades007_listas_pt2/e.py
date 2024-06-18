# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 16/06/2024

import os


os.system('cls')

print('-'*70)
print('''
      Crie uma lista com 6 nomes, depois verifique se o nome =Pedro= está nessa lista.
      ''')
print('-'*70)

# Lista
nomes = ['Lara','Pedro','João','Felipe','Marcelo','Leandro' ]

# Verificando se pedro esta presente na lista
print(f'Nome : {nomes}')
if "Pedro" in nomes:
    print('-'*70)
    print('Pedro esta presente nsa lista!')
    print('='*70)
else:
    print('-'*70)
    print('Pedro não esta na lista!')