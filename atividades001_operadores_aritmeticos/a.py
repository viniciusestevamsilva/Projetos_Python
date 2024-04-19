# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 18/04/2024

 # Imports
import os

os.system('cls')

print('-'*70)
print('Calcular a soma e multiplição')
print('='*70)

# Entrada
print('Coloque os valores')
print('-'*70)
valor1 = float(input('Coloque o valor 1: '))
valor2 = float(input('Coloque o valor 2: '))
valor3 = float(input('Coloque o valor 3: '))
print('-'*70)

# Processamento
soma = valor1 + valor2 + valor3
produto = valor1 * valor2 * valor3

#Saida
print('RESULTADOS:')
print(f'a soma dos valores {valor1} + {valor2} + {valor3} é: {soma}')
print(f'a multiplicação dos valores {valor1} * {valor2} * {valor3} é: {produto}')
print('='*70)