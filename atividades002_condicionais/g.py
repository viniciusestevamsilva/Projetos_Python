# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 26/04/2024

# Importa bibliotecas
import os
 
# Limpar terminal
os.system('cls')

print('-'*70)
print('Determine o segmentos')
print('='*70)

# Entrada
a = float(input('Digite o valor do primeiro: '))
b = float(input('Digite o valor do segundo: '))
c = float(input('Digite o valor do terceiro: '))
resultado = ''

# Condicionais
if (a + b) > c and (a + c) > b and (c + a) > b and (c + b) > a and (b + a) > c and (b + c) > a:
    resultado = f'Os numeros digitados {a},{b},{c} conseguem formar um triangulo'
else:
    resultado = f'Os numeros digitados {a},{b},{c} não conseguem formar um triangulo'

# Saida
print('-')
print('-'*70)
print(f'{resultado}')
print('-'*70)
print('')