# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 22/05/2024

import os

os.system('cls')

#ENTRADA
print('-'*70)
print('Verificar se tem Olivira o nome')
print('-'*70)

nome = str(input("Insira seu nome: "))

#CONDICIONAL
print(f'Nome : {nome}')
if "Oliveira" in nome:
    print('Seu nome possui Oliveira no nome')
else:
    print('Seu nome não possui Oliveira no nome')

