# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 16/06/2024

import os


os.system('cls')

print('-'*70)
print('''
      Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.
      ''')
print('-'*70)


numeros_inteiros = [] # Lista vazia
soma = 0


for i in range(0, 5): 
    numeros = int(input('Insira um número inteiro: ').strip()) 
    numeros_inteiros.append(numeros) #subindo os numeros
    soma += numeros #somando

# Saida
print()
print(f'Lista dos valores: {numeros_inteiros} e a soma entre eles é de: {soma}')