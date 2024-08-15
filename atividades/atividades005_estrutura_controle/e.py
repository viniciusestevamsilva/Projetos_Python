# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 02/06/2024

import os


os.system('cls')

print('-'*70)
print('Números pares intervalo entre 0 e 100.')
print('='*70) 

#declaração
contador = 0 
soma = 0

for contador in range(contador, 100):
    
    contador += 1
    if (contador % 2 == 0): 
        print(f'numero par:{contador}')
        soma += contador 

print('-'*70)
print(f'Soma dos pares: {soma}')
print('-'*70)