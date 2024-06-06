# Importando bibliotecas
import os
import random


os.system('cls')

# Entrada
print('='*70)
print('TENTE ADIVINHAR EM QUAL NUMERO ESTOU PENSANDO (1 a 30)')
print('='*70)



# Processamento
numero_aleatorio = random.randint(1, 30)

print(f'O número que eu pensei foi: {numero_aleatorio}')

numero = int(input('Qual número estou pensando?: '))

# Condicional

    if numero < 0 or numero > 30:
    resultado = f'ISSO NÃO TEM NADA A VER, coloque um numero valido'
    
    elif numero == numero_aleatorio:
    resultado = f'Parabens você ACERTOU! :D'
    
    else:
    resultado = f'ERROU! Boa sorte na proxima vez :('

while (True):
    


    quer_jogar_de_novo = (input('Qual número estou pensando?: ')).lower()
    
    if (quer_jogar_de_novo != "d"):
        print('Digite "d" para jogar novamente')
        print('='*70)
    else:
        print('-'*70)
        print('Você saiu de banco de dados.')
        
        break
# Saida
print('-'*70)
print(f'{resultado}')
print('-'*70)
print('Caso queira jogar novamente digite "r"')