# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 01/06/2024

#Importando biblioteca
import os

os.system('cls')

#Entrada
print('-'*70)
print('3 números não serão impressos1')
print('-'*70)

começo = int(input("Digite o numero do começo do intervalo: "))
fim = int(input("Digite o numero final do intervalo: "))

ign1 = int(input("Digite o 1º que sera ignorado: "))
ign2 = int(input("Digite o 2º que sera ignorado: "))
ign3 = int(input("Digite o 3º que sera ignorado: "))


contador = começo


# Imprime os valores no intervalo, ignorando os números que o usuario digitou
while contador <= fim:
    if contador != ign1 and contador != ign2 and contador != ign3:
        print(f'{contador}')
    contador += 1
    
print()