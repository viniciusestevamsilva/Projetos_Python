
# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 18/04/2024

#Imports
import os

#Limpar terminal
os.system('cls')

print('='*70)
print('Insira os numeros')
print('='*70)

# Entrada
dividendo = float(input('Coloque o dividendo: '))
divisor = float(input('Coloque o divisor: '))


# Processamento
quociente = dividendo / divisor

# Saida
print('='*70)
print('RESULTADO')
print('='*70)
print(f'A divisao dos valores {dividendo} / {divisor} é: {quociente :.4f}')
print('')