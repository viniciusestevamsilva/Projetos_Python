
# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 18/04/2024

# d. Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais

#Imports
import os

os.system('cls')

# Entrada
print('='*70)
print('Insira os numeros')
print('='*70)
dividendo = float(input('Coloque o dividendo: '))
divisor = float(input('Coloque o divisor: '))

# Processamento
quociente = dividendo / divisor

# Saida
print('='*70)
print('RESULTADO')
print('='*70)
print(f'A divisao dos valores {dividendo} / {divisor} é: {quociente}')