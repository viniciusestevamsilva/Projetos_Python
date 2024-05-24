# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 23/05/2024

import os

os.system('cls')


# ENTRADA
print('-'*70)
print('Primeiro e ultimo nome')
print('-'*70)

nome_completo = str(input('Insira seu nome completo: '))

# PROCESSAMENTO
nome_separado = nome_completo.split(' ')
primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1]

# SAIDA
print(f'Seu Primeiro nome:{primeiro_nome}')
print(f'Seu Ultimo nome:{ultimo_nome}')
print('-'*70)
print()