# Curso de Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 05/06/2024

#Importando biblioteca
import os


os.system('cls')

print('-'*70)
print('Imprimir de 0 a 100 em numeros impares')
print('-'*70)

comeco = 1


while (comeco <= 100):
    comeco += 1 
    
    if (comeco % 2 == 0):
        continue
    print(f'{comeco} é Impar')
else:
    comeco -= 1

    print('-'*70)
    print(f'Nesse cilco foram encontrados {comeco} números impares!')
    print('-'*70)
