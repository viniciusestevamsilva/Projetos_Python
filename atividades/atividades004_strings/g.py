# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 23/05/2024

import os

os.system('cls')

# ENTRADA
print('-'*70)
print('Casas decimais')
print('-'*70)

numero = int(input('Insira um numero: '))

#VALIDAÇÃO

if numero < 0 :
    print('Coloque um numero valido!!!')
else:
    unidades = numero % 10
    dezenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    milhares = (numero // 1000) % 10
    
    print(f'Em unidades:{unidades}')
    print(f'Em dezenas:{dezenas}')
    print(f'Em centenas:{centenas}')
    print(f'Em milhares:{milhares}')
    print('-'*70)
    print()
