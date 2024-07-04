# Faça um programa para criar um dicionário com 5  ferramentas. Depois,  imprima os valores e a quantidade de elementos do dicionário.
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data  03/07/2024

import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 5 ferramentas.')
print('-'*70)

# Declaração de dicionario
dicionario = dict()

for c in range(5):
    print(f'Informe os dados da {c}º ferramenta:')
    nome = str(input('Nome da ferramenta: '))
    descricao = str(input('Descrição da ferramenta: '))
    
    # Adiciona a ferramenta ao dicionário
    dicionario[nome] = descricao

print('-'*70)
print('Ferramentas foram adicionadas!')
print('-'*70)

# Imprime os valores dos elementos do dicionário
for nome,descricao in dicionario.items():
    print(f'Ferramenta: {nome}, Descrição: {descricao}')
    print('-'*70)
print(f'Quantidade de ferramentas: {len(dicionario)}') #ferramentas no dicionario atual
print('')