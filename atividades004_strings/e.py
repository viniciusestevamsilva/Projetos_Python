# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 22/05/2024

import os

os.system('cls')

#ENTRADA
print('-'*70)
print('Conte as vogais')
print('-'*70)

frase = str(input('Insira sua frase: '))

#PROCESSAMENTO
vogal_a = frase.count('a')
vogal_e = frase.count('e')
vogal_i = frase.count('i')
vogal_o = frase.count('o')
vogal_u = frase.count('u')

#SAIDA
print(f'"A" apareceu: {vogal_a}')
print(f'"E" apareceu: {vogal_e}')
print(f'"I" apareceu: {vogal_i}')
print(f'"O" apareceu: {vogal_o}')
print(f'"U" apareceu: {vogal_u}')