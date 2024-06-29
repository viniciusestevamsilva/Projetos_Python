# Faça um programa para criar um dicionário com 4 elementos.
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 28/06/2024

import os


os.system('cls')

print('/'*70)
print('Dicionario com 4 elementos')
print('-'*70)

dicionario = dict() # Dicionario
elementos = [] # Lista

print(f'Preenchendo a papelada')
for i in range(5):
    print()
    nome = str(input('Digite nomes: '))
    idade = str(input('Digite idade: '))
    
    dicionario['nome'] = nome
    dicionario['idade'] = idade
    
    elementos.append(dicionario.copy())
    
for dicionario in elementos: #Para cada elemento na lista
    for chave,valor in dicionario.items(): # Para cada chave e o valor do dicionario
        print(f'{chave.capitalize()}: {valor}') # Imprime a chave e o valor de maneira legivel
    print('/'*70)