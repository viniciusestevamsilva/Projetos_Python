# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 05/06/2024


#Importando biblioteca
import os


os.system('cls')

#Entrada
print('-'*70)
print('Imprimi os números primos')
print('='*70)
    
#declaração
inicio = 2
fim = 100
contador = inicio

for numero_primo in range(contador, fim):
    for divisor in range(2, int(numero_primo**0.5) + 1):
        if numero_primo % divisor == 0:
            break
    else:
        print(f'{numero_primo}')

print('-'*70)