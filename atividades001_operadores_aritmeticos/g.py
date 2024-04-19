# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 19/04/2024

 # Imports
import os

os.system('cls')

#Entrada
print('-'*70)
print('Centimentro pra milimetros')
print('-'*70)
metro = int(input('Coloque o numero: '))

#Processamento
centimetro = metro*100
milimetro = metro*1000

#Saida
print('RESULTADO')
print('-'*70)
print(f'De centimetros para metros é: {centimetro}')
print(f'De milimetro para metros é: {milimetro}')
print('-'*70)