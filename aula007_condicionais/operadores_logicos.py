# Curso de desenvolbimento de sistemas
# Turma 0152
# Autor: Viícius Estevam da Silva
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
    valor = int(valor)
    resposta = f'Entrada incorreta, o valor {valor} é um inteiro!'
else:
    resposta = f'Entrada correta, o valor {valor} é decimal!'

# Saida
print('='*70)
print(resposta)

print('Fim do programa !\n')  # \n salta uma linha
