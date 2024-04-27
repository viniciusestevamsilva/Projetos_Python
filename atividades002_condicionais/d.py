# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 26/04/2024

# Iporta bibliotecas
import os


# Limpar terminal
os.system('cls')

# Entrada
print('-'*70)
print('Monitoramento de salarios')
print('='*70)

salario = float(input('Digite seu salario atual: '))
aumento = salario / 5 * 1500
aum = salario / 100 * 1000.00


if salario > aumento:
    print('seu salario recebeu um aumento de 5%')
    