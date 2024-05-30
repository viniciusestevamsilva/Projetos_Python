# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 30/06/2024

#Importando biblioteca
import os

# INCOMPLETO ERRADO
os.system('cls')

#Entrada
print('-'*70)
print('3 números não serão impressos')
print('-'*70)

numero = int(input('Digite um numero entre 1 e 9: '))

for numero in range(1, 9):
    if numero == 6 and numero == 7 and numero ==8:
        continue
    
    print(f'o valor é {numero}')

print('-'*70)
print()