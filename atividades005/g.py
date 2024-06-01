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


contador_primo = comeco


while contador_primo <= final:
    contador_primo += 1
#verificando se e primo
    if ( contador_primo / contador_primo ) and (contador_primo / 1):
        print(f' O número {contador_primo} é primo!')
        
print('-'*70)
print()