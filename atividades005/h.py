# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 31/06/2024

#Importando biblioteca
import os

os.system('cls')

#Entrada
print('-'*70)
print('3 números não serão impressos')
print('-'*70)

numero = int(input('Digite um numero entre 1 e 9: '))

# verificando se é maior que 9 e menor que 0
if numero > 1 and numero < 9:
    print('Insira um numero valido')
# ciclo para retirar  3 numeros dele
for numero in range(1, 9):
    if numero == 6 and numero == 7 and numero ==8:
        continue
    
    print(f' Estou contando... {numero}')

print('-'*70)
print()