import os

os.system('cls')

print('-'*70)
print('Solicite separamente o nome e imprmida completo no final')
print('-'*70)

primeiro_nome = str(input('Insira seu primeiro nome: '))
sobrenome = str(input('Insira seu Sobrenome: '))

nome_inteiro = (primeiro_nome) + (sobrenome)

nome_completo = nome_inteiro
nome_inteiro.split()
print(f'Seu nome é {nome_inteiro}')
print('.'*70)