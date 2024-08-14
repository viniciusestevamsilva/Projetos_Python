import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: LISTA [ ]')
print('-'*70)

lista_mista = ['a', 'b', 3, 'John', 'e', 500, 'g', 'h']

# Fatia o 1 elemento
lista_fatiada1 = lista_mista[0]

# Fatia todos os elementos
lista_fatiada2 = lista_mista[0:]

# Fatia os elementos do indice 0 até o indicie 6
lista_fatiada3 = lista_mista[0:6]

# Fatia os elementos do indice 0 até o indicie 6 de 2 em 2
lista_fatiada4 = lista_mista[0:6:2]

# Fatia os elementos da direita para esquerda
lista_fatiada5 = lista_mista[::-1]

print(f'Fatiando uma Lista: {lista_fatiada1}\n')
print(f'Fatiando uma Lista: {lista_fatiada2}\n')
print(f'Fatiando uma Lista: {lista_fatiada3}\n')
print(f'Fatiando uma Lista: {lista_fatiada4}\n')
print(f'Fatiando uma Lista: {lista_fatiada5}')

print('-'*70)
print('FIM DO PROGAMA!')
print('-'*70)