# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 16/06/2024

import os


os.system('cls')

print('/'*70)
print('''
    Faça um programa que procure na lista numeros =
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    e produza:
    • O intervalo de 1 até 9
    • O intervalo de 8 até 13
    • Os números pares
    • Os números ímpares
    • Os múltiplos de 2, 3 e 4
    • Lista reversa
    • O produto dos intervalos 5-6 por 11-12
''')
print('/'*70)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
produtos = []

#Os números ímpares e pares
numeros_impar = 0 
numero_par = 0

#Os múltiplos
multiplo_2 = 0
multiplo_3 = 0
multiplo_4 = 0
#Lista reversa
lista_reversa = lista_numeros


#O intervalo de 1 até 9 e 8 até 13
intervalo_1_9 = lista_numeros[0:9]
intervalo_8_13 = lista_numeros[8:13]

print('Numeros impares: ') # Os números ímpares
while numeros_impar <= 15:
    numeros_impar += 1
    if (numeros_impar % 2 == 0):
        continue
    print(f'{numeros_impar}', end=' - ' )
else:
    numeros_impar -= 1
    print()
    print('='*70)
    
print('Os Numeros pares: ')
while numero_par <= 15:
    numero_par += 1
    if numero_par % 2 != 0: #pula os impares
        continue
    print(f'{numero_par}', end=' - ' )   
else:
    numero_par -= 1
    print()
    print('='*70)

# Verificando múltiplos de 2, 3 e 4
multiplo_2 = [num for num in lista_numeros if num % 2 == 0]
multiplo_3 = [num for num in lista_numeros if num % 3 == 0]
multiplo_4 = [num for num in lista_numeros if num % 4 == 0]

# saida
print(f'Os Múltiplos de 2:{multiplo_2}')
print(f'Os Múltiplos de 3:{multiplo_3}')
print(f'Os Múltiplos de 4:{multiplo_4}')
print('='*70)

#copiando e revertendo a lista
lista_reversa = lista_numeros.copy()
lista_reversa.reverse()
print(f'Lista revertida: {lista_reversa}')
print('='*70)

# Imprimindo os intervalos
for numero_a in lista_numeros[4:6]:
    for numero_b in lista_numeros[10:12]:
        produto = numero_a + numero_b
        produtos.append(produto)
print(f'O produto dos intervalos 5-6 por 11-12 : {produto}')
print('/'*70)