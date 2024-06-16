# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data /06/2024

import os
import random

os.system('cls')

print('-'*80)
print('''
      Faça um programa que gere 10 números aleatórios. Após gerar esses números,
      crie duas listas novas com ordenação ascendente e descendente.
      ''')
print('-'*80)

# Lista com numeros aleatorios ate 10 dentro dela
ascendente = [random.randint(0, 100) for _ in range(10)]
descendente = [random.randint(0, 100) for _ in range(10)]

# Numeros crescentes
print(f"Lista ordenada em ordem ascendente: {ascendente}")
print('-'*80)
descendente.sort(reverse = True)
#Numeros decrecentes
print(f"Lista ordenada em ordem descendente: {descendente}")
print('-'*80)
