# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 17/06/2024

import os
import random

os.system('cls')

print('-'*80)
print('''
      Faça um programa que gere 10 números aleatórios. Após gerar esses números,
      crie duas listas novas com ordenação ascendente e descendente.
      ''')
print('-'*80)

# listas 
lista_ascendente = []
lista_descendente = []

# Lista gerando numeros aleatorios ate 10 dentro dela
ascendente = [random.randint(0, 100) for ascendente in range(10)]
descendente = [random.randint(0, 100) for descendente in range(10)]

# organizando em forma crescente e descendente
ascendente.sort()
descendente.sort(reverse = True)

# iterando a lista
lista_ascendente.extend(ascendente)
lista_descendente.extend(descendente)



# Numeros crescentes
print(f"Lista ordenada em ordem ascendente: {lista_ascendente}")
print('-'*80)
#Numeros decrecentes
print(f"Lista ordenada em ordem descendente: {lista_descendente}")
print('-'*80)
