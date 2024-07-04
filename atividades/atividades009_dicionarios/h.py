# Faça um programa para ler o dicionário nomes = {‘nome’: ’John, ‘idade’: 40, ‘peso’: 80, ‘altura’: 1.70}.
# Em seguida realize as seguintes ações:
# - Listar chaves e valores com laço - Deletar o peso
# - Listar novamente chaves e valores - mostrar o nome e altura
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/07/2024
import os


os.system('cls')

print('='*70)
print('Programa que cadastra alunos de uma escola.')
print('-'*70)

# Dicionario
dicionario = {'nome': 'John', 'idade': 40, 'peso': 80, 'altura': 1.70}
print('Chaves e Valores presentes no dicionario:')
for chave, valor in dicionario.items(): # Para cada chave e o valor do dicionario
    print(f'{chave}: {valor}')
print('-'*70)
del dicionario['peso'] # deleta a chave 'peso' do dicionario
print('Chaves e Valores depois de deletar "peso" do dicionario:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')
print('-'*70)
# Mostrar as chaves 'nome' , 'altura'
print('Chaves no dicionario atual')
print(f'Nome: {dicionario["nome"]}, \nAltura: {dicionario["altura"]}')
print()
print('='*70)
print('Fim do programa')
print('/'*80)