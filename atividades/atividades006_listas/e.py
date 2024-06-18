# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 16/06/2024

import os


os.system('cls')

print('-'*70)
print('''
      Faça um programa que leia as vogais, depois mostre-as em ordem inversa.
      ''')
print('-'*70)

# entrada
entrada = input('Insira as vogais: ')

# lista de vogais
vogais = []

letras = entrada.split(',')
vogais.extend(letras)

# invertendo a lista
vogais.sort(reverse = True)
print()
print(f'As vogais em ordem de tras pra frente : {vogais}')