# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 16/06/2024

import os


os.system('cls')

print('-'*70)
print('''
      Faça um programa que leia um número indeterminado de notas (pressione s ou 0 para sair).
      ''')

while True:
    notas = []
    print('='*70)
    print('Digite "s" para sair!')
    print('-'*70)
    # Entrada
    entrada = input('Insira qualquer valor separado por vírgulas: ').replace(' ','')
    
    valor = entrada.split(',')
    notas.extend(valor) # iterando na lista
#saida
    if not (entrada.lower() == 's' in notas):
        print()
        print(f'{notas}')
        print()
    else:
        print('='*70)
        print('Voce saiu do programa!')
        print('/'*70)
        break
