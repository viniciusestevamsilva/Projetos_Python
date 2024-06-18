# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 16/06/2024

import os


os.system('cls')

print('-'*70)
print('''
    Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
    • O intervalo de 1 até 9
    • O intervalo de 8 até 13
    • Os números pares
    • Os números ímpares
    • Os múltiplos de 2, 3 e 4
    • Lista reversa
    • O produto dos intervalos 5-6 por 11-12
''')
print('-'*70)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Os números ímpares
numeros_impares = 0 
#Os números pares
numero_pares = 0
#Os múltiplos de 2, 3 e 4
multiplos_de_2 = 0
multiplos_de_3 = 0
multiplos_de_4 = 0
#Lista reversa
lista_reversa = lista


#O intervalo de 1 até 9 e 8 até 13
intervalo_1_9 = lista[0:9]
intervalo_8_13 = lista[8:13]

print('Numeros impares: ') # Os números ímpares
while numeros_impares <= 15:
    numeros_impares += 1
    if (numeros_impares % 2 == 0):
        continue
    print(f'{numeros_impares}')
else:
    numeros_impares -= 1
    print('')
    print('.'*70)
    
print('Numeros pares: ')#Os números pares
while numero_pares <= 15:
    numero_pares += 1
    if numero_pares % 2 != 0: #pulando os impares
        continue
    print(f'{numero_pares}')
    
else:
    numero_pares -= 1
    print('')
    print('.'*70)

# Verificando múltiplos de 2, 3 e 4
multiplos_de_2 = [num for num in lista if num % 2 == 0]
multiplos_de_3 = [num for num in lista if num % 3 == 0]
multiplos_de_4 = [num for num in lista if num % 4 == 0]

# saida
print(f'Múltiplos de 2:{multiplos_de_2}')
print(f'Múltiplos de 3:{multiplos_de_3}')
print(f'Múltiplos de 4:{multiplos_de_4}')
print('.'*70)

#Revertendo a lista
lista_reversa.reverse()
print(f'Lista revertida: {lista_reversa}')
print('.'*70)