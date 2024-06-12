# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 22/05/2024

import os

os.system('cls')

# ENTRADA
print('='*70)
print('Verificar se tem Olivira o nome')
print('='*70)

nome = str(input("Insira seu nome: "))

# CONDICIONAL/VALIDAÇÃO
print(f'Nome : {nome}')
if "Oliveira" in nome:
    print('-'*70)
    print('Seu nome possui Oliveira no nome')
else:
    print('-'*70)
    print('Seu nome não possui Oliveira no nome')

if "Oliveira" not in nome:
    print('-'*70)
    print('A palavra "Oliveira" não está presente no nome.')
    print('='*70)
else:
    print('-'*70)
    print('A palavra "Oliveira" está presenta no nome.')
    print('='*70)
