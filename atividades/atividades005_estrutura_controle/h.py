# Curso de Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 03/06/2024

#Importando biblioteca
import os

os.system('cls')

#Entrada
print('-'*70)
print('3 números não serão impressos1')
print('-'*70)

comeco = int(input("Digite o numero do começo do intervalo: "))
final = int(input("Digite o numero final do intervalo: "))

print('-'*70)

ignorar_1º = int(input("Digite o 1º que sera ignorado: "))
ignorar_2º = int(input("Digite o 2º que sera ignorado: "))
ignorar_3º = int(input("Digite o 3º que sera ignorado: "))

print('-'*70)

# Declaração
contador = comeco

# Saída
while contador <= final:
    # Ignora os números que o usuario digitou
    if contador != ignorar_1º and contador != ignorar_2º and contador != ignorar_3º:
        print(f'{contador}')
    contador += 1
    
print('-'*70)