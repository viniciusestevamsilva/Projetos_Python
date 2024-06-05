# Importando bibliotecas
import os
import random


os.system('cls')

# Entrada
print('='*70)
print('TENTE ADIVINHAR EM QUAL NUMERO ESTOU PENSANDO (1 a 30)')
print('='*70)

numero = int(input('Qual número estou pensando?: '))

# Processamento
numero_aleatorio = random.randint(1, 30)

print(f'O número que eu pensei foi: {numero_aleatorio}')

# Condicional
if numero < 0 or numero > 30:
    resultado = f'ISSO NÃO TEM NADA A VER, coloque um numero valido'
elif numero == numero_aleatorio:
    resultado = f'Parabens você ACERTOU! :D'
else:
    resultado = f'ERROU! Boa sorte na proxima vez :('


# Saida
print('-'*70)
print(f'{resultado}')
print('-'*70)
print('Caso queira jogar novamente digite "r"')