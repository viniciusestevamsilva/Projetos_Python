# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 18/04/2024

#Imports
import os
import datetime

# Limpar terminal
os.system('cls')

print('-'*70)
print('Entre com seus dados')
print('-'*70)

#Entrada
print
nascimento = int(input('Data de nascimento: '))

# Processamento do ano atual
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

#Saida
print('-'*70)
print('RESULTADOS')
print('-'*70)
print('Data de nascimeno: ', nascimento)

# Saida intterpolada
print(f'voce tem {idade} de anos')
print('='*70)