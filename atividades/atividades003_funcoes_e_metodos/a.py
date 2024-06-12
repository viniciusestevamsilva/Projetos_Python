# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 09/05/2024

# EM DESENVOLVIMENTO / INCOMPLETO OU ERRADO

# Importando as bibliotecas
import os
import math

# Entrada
os.system('cls')

print('-'*70)
print('INSIRA SUA RAIZ')
print('-'*70)

radicando = int(input('INSIRA SEU VALOR: '))
raizQuadrada = math.sqrt(radicando)

# Processamento
arredondar_para_cima = math.ceil(radicando)
arredondar_para_baixo = math.floor(radicando)

# 
if radicando <= 0:
    print('esse valor não é valido')
else:
    print(f'A raiz quadrada de {radicando} é:{raizQuadrada}')
print('-'*70)

