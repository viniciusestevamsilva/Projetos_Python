# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 26/04/2024

# Iporta bibliotecas
import os


# Limpar terminal
os.system('cls')

# Entrada
print('-'*70)
print('Monitoramento de velocidade')
print('='*70)

veloc = float(input('Insira a velocidade do carro:  '))
limit = 60

# Condicional
if veloc > limit:
    print(f'Reduzada velocidade, isso podera causa um acidente o recomendado é {limit}km/h')
    print('='*70)
else:
    print(f'Tente manter essa velocida,o limite é {limit}km/h')
    print('='*70)
