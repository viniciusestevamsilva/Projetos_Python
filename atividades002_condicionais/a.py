# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 25/04/2024

# Iporta bibliotecas
import os


# Limpar terminal
os.system('cls')

# Entrada
print('-'*70)
print('Programa Impar ou Par')
print('='*70)

numero = int(input('INSIRA UM NUMERO INTEIRO: '))
resultado = ''

# Condicional
if numero % 2 == 0:
    resultado = f'O numero {numero} é par'
else:
    resultado = f'O numero {numero} é impar'

# Saida
print('='*70)
print(resultado)
print('='*70)