# Curso de desenvolbimento de sistemas
# Turma 0152
# Autor: Vinícius Estevam da Silva
# Estudo de condicionais: Parte 1
# Objetivo: Verificando um valor decimal

import os

os.system('cls')

print('-'*70)
print('Estudo de Condicional: Parte 1')
print('-'*70)

#  Entrada
valor = float(input('Digite um número: '))
resposta = ''

# Condicional
if valor % 2 == 0:
    resposta = f'O número {valor} é par'
else:
    resposta = f'O número {valor} é impar!'

# Saida
print('='*70)
print(resposta)

print('Fim do programa !\n')  # \n salta uma linha
