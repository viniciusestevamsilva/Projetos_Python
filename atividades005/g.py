# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 01/06/2024

#Importando biblioteca
import os


os.system('cls')

#Entrada
print('-'*70)
print('Calcular os números primos no intervalo pré-determinado pelo usuário')
print('='*70)

comeco = int(input('Digite o valor do começo: '))
final = int(input('Digite o valor do final: '))
print('-'*70)

# Validação
if comeco < 2:
    comeco = 2
    print("Coloque um valor no inicio maior que 2, ja que não existe primo menor que 2")
    print('-'*70)
    #Processamento
for primo in range(comeco, final):
    for divisor in range(2, int(primo**0.5) + 1): # Verifica se é divisivel por 1 e por ele mesmo
        if primo % divisor == 0:# verificando se é primo, se o resto for 0, é primo
            break
    else:
            print(primo)

print('-'*70)
print()