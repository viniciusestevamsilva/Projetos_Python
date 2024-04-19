
# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 19/04/2024

#Imports
import os

# Limpar terminal
os.system('cls')

print('-'*70)
print('Insira o tamanho do seu triangulo')
print('-'*70)

# Entrada 
altura = int(input('Coloque a altura de seu triangulo: '))
largura = int(input('Coloque a largura de seu trangulo: '))

#Processamento
total = altura * largura

#Saida
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'no final seu triangulo possui {total} de perimetro')
print('')