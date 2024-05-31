# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 31/06/2024

#INCOMPLETOOOO

# Importando biblioteca
import os


os.system('cls')

# Entrada
print('-'*70)
print('Número par ou impar')
print('-'*70)

# ciclo
for c in range(0,4):
    numero = int(input(f'{c + 1}º número: '))
    
    if (numero % 2 == 0):
        print(f'O número {numero} que digitou é par')
    else:
        print(f'O número {numero} que digitou é impar')


print('-'*50)
print()