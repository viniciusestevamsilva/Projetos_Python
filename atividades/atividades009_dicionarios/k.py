# Faça um programa que peça continuamente o nome e a idade de uma pessoa. Caso o usuário digite a idade 999,
# o programa será finalizado e executará uma impressão com os nomes cadastrados.
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/07/2024

import os

os.system('cls')
dicionario = {} # Dicionario
lista = []# Lista

while True:
    print('Pedir continuamente o nome e a idade ao usuario.')
    print('-'*70)
    print('idade = 999 para sair')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    print('-'*70)
    dicionario['Nome'] = nome # Adiciona nome ao dicionário
    dicionario['Idade'] = idade # Adiciona idade ao dicionario
    lista.append(dicionario.copy())# Adiciona uma cópia do dicionário a lista
    print('Dados foram adicionados')
    print(dicionario)
    input('Enter pra continuar com o formulario')
    if idade == 999:
        print('Programa finalizado')
        print()
        break
    else:
        os.system('cls')
        print()
print()
print('Nomes cadastrados ate então')
print('-'*70)
for dados in lista: # Para cada chave e o valor do dicionario
    print(dados['Nome'])
print('-'*70)
print()
print('Fim do programa')
print()
print('/'*70)