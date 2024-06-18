# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 17/06/2024

import os


os.system('cls')

print('-'*70)
print('''
      Faça um programa que recebe 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares. 
      ''')
print('-'*70)

# lista
lista = []
lista_par = []
lista_impar = []
numeros_int = input('Digite numeros 7 números inteiros:')
numero = numeros_int.split()
# inseir valor na lista
lista.extend(numeros_int)

for num in lista:
    # passar o valor para inteiro
    num = int(num)
    
    if num % 2 ==0: # vendo se é par
        lista_par.append(num)
        
    else:# se nao, é impar
        lista_impar.append(num)
        
print(f'')
print(f'')