# Curso de desenvolvimeno de Sistemas
# Autor: Vinicius Estevam da Silva
# Data: 17/04/2024
# Atividade 1

# Importanto biblioteca
import os

# Limpar terminal
os.system('cls')

print('='*70)
print('DADOS DE USUÁRIO')
print('='*70)

# Entrada com Casting
nome = str(input('Insira seu Nome: '))
idade = int(input('Insira sua Idade: '))
altura = float(input('Insira sua Altura: '))
cep = int(input('Insira seu CEP: '))
deficiencia = bool(True)

# Saída Interpolada
print('='*70)
print(f'Ola meu nome é {nome}, tenho {idade} e {altura} de altura')
print(f'CEP...........: {cep}')
print(f'Deficiencia...? {deficiencia} ')

# Saída
print('='*70)
print('Saida dos tipos de variaveis')
print('='*70)
print('Nome...........: ', type(nome))
print('Idade..........: ', type(idade))
print('Altura.........: ', type(altura))
print('CEP............: ', type(cep))
print('Deficiencia....: ', type(deficiencia))
print('')
print('='*70)
print('')
