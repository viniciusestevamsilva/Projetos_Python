# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 22/05/2024

import os

os.system('cls')

#ENTRADA
print('-'*70)
print('Receber nome completo e depois separado')
print('-'*70)

nome = str(input('Insiria seu nome: '))

#PROCESSAMENTO
nome_separado = nome.split(' ')
primeiro_nome = nome_separado[0]
sobronome = nome_separado[1]
penultimo = nome_separado[2]
ultimo_nome = nome_separado[-1]

#SAIDA
print(f'Seu Primeiro nome:{primeiro_nome}')
print(f'Seu Sobrenome é: {sobronome}')
print(f'Seu Penultimo nome é: {sobronome}')
print(f'Seu Ultimo nome:{ultimo_nome}')
print('-'*70)
print()
