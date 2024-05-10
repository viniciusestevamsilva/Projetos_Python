# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 09/05/2024

# Importando as bibliotecas
import os
import math

# Entrada
os.system('cls')

print('-'*70)
print('INSIRA SUA BASE E EXPOENTE')
print('-'*70)

base = int(input('INSIRA SUA BASE: '))
expoente = int(input('INSIRA SEU EXPOENTE: '))
# Processamento
potencia = math.pow(base, expoente)

# Saida
print(f' A {base} elevada a potencia de {expoente} o resultado será {potencia}')
