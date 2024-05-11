# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 10/05/2024

# Importando bibliotecas
import os
import math

os.system('cls')


# Entrada
print('-'*70)
print('Vou calcular seu angulo')
print('-'*70)

angulo = int(input('Insira seu angulo: '))

# Processamento
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Saida
print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseno:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')