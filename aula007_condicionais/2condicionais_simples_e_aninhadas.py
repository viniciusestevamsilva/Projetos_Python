# Curso de desenvolbimento de sistemas
# Turma 0152
# Data 25/04/2024
# Autor: Vinícius Estevam da Silva
# Estudo de condicionais: Parte 2
# Objetivo: Prática com condicionais simples e aninhadas

import os


os.system('cls')

# Declarção
a = 5
b = 10
resposta = ''

print('-'*70)
print('Estudo de Condicionais (simples)')
print('-'*70)

# Condicionais
if a > b:
    resposta = f' {a} é maior que {b}'
else:
    resposta = f' {a} é menor que {b}'
# Saida
print('-'*70)
print(resposta)

# Declarações
a = 5
b = 5

print('-'*70)
print('Estudo de Condicionais (aninhadas)')
print('-'*70)

if a > b:
    resposta = f' {a} é maior que {b}'
elif a < b:
    resposta = f' {a} é menor que {b}'
else:
    resposta = f'Os valores são iguais: {a} = {b}'
# Saida
print('-'*70)
print(resposta)
print('-'*70)
print()