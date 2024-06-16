# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data /06/2024

import os


os.system('cls')

print('-'*70)
print('Faça um programa que leia um número indeterminado de notas (pressione s ou 0 para sair). ')
print('-'*70)

while True:
    notas = []
    print('0 sai do sistema!')
    entrada = input('Insira qualquer valor separado por vírgulas: ').replace(' ','')
    
    valor = entrada.split(',')
    notas.extend(valor)

    if not (entrada == '0' or entrada.lower() == 's' in notas):
        print()
        for i in notas:
            print(i, end=', ')
        print()
    else:
        print()
        saida = input(
            'Valor identificado, deseja sair do sistema? [S]: ').lower()
        if saida == 's':
            break
        else:
            os.system('cls')