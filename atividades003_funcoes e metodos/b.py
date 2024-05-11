# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 09/05/2024

# Importando bibliotecas
import os
import math


os.system('cls')

# Entrada
valor1 = float(input('Insira seu primeiro valor: '))
valor2 = float(input('Insira seu segundo valor: '))

resultado = valor1 / valor2

if resultado % 2 == 0:
    resposta = print(f'É inteiro')
else:
    arredondar_para_cima = math.ceil(resultado)
    arredondar_para_baixo = math.floor(resultado)
    resposta = print(f'Não é inteiro')
    
print('-'*70)
print(f'{resultado}')
print('-'*70)
print('')