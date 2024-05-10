import math
import os


os.system('cls')

print('-'*50)
print('ESTUDO DA BIBLIOTECA DE MATH')
print('='*50)
print()

# Entrada de dados
numero_decimal = float(input('Entre com um numero decimal: '))

# Processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

# Saida
print('-'*50)
print(f'O numero {numero_decimal} arredondado para cima é: {arredondar_para_cima}')
print(f'O numero {numero_decimal} arreondado para baixo é: {arredondar_para_baixo}')
print('-'*50)