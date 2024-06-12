
# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 19/04/2024

#Imports
import os

# Limpar terminal
os.system('cls')

print('-'*70)
print('Insira o tamanho do seu retangulo')
print('-'*70)

# Entrada 
altura = int(input('Coloque a altura de seu retangulo: '))
largura = int(input('Coloque a largura de seu retangulo: '))

#Processamento
total = (altura + largura) *2

#Saida
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'no final seu retangulo possui {total} de perimetro')
print('')