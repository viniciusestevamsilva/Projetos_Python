import os

from pacote.modular_somar import somar
from pacote.subpacote.moldulo_multiplicar import multiplicar as multi
from pacote.modulo_divisao import dividir

while True:
    os.system('cls')
    
    a = input('Entre com o valor de A: ')
    b = input('Entre com o valor de B: ')
    
    if not a.replace('.','', 1).isdigit() or not b.replace('.','', 1).isdigit():
        print('Porfavor, entre com um número valido.')
        continue
    
    a = float(a)
    b = float(b)
    
    resultado_soma = somar(a, b)
    resultado_produto = multi(a, b)
    resultado_divisao, erro = dividir(a, b)
    
    print('-'*70)
    print('CÁCULOS MATEMÁTICOS')
    print('='*70)
    print(f'Cáculo da soma: {resultado_soma}')
    print(f'Cálculo do produto: {resultado_produto}')
    print(f'Cálculo da divisão: {resultado_divisao}, {erro}')
    print('-'*70)
    
    sair = input('Deseja sair do programa? (s/n): ').strip().lower()
    if sair == 's':
        print('Saindo do programa. . .')
        break