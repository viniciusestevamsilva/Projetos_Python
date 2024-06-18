# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 17/06/2024

import os
import random


os.system('cls')

print('-'*90)
print('''
      Faça um programa que sorteia os números da Mega Sena e da Lotofácil
      ''')
print('='*90)

# listas 
megasena = []
lotofacil = []


for i in range(1,60): # gerando os numeros de 1 a 60
    i = int(i)
    megasena.append(i) # iterando a lista
    if i <= 25:
        lotofacil.append(i) # iterando a lista

# 
mega = random.sample(megasena, 6)
facil = random.sample(lotofacil, 15)

# orgnizando de ordem crescente
mega.sort()
facil.sort()

# Saida
print(f" Números do sorteio da Mega Sena: {mega}")
print('-'*90)
print(f" Números do sorteio da Lotafacil: {facil}")
print('-'*90)