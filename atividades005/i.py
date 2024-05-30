# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 30/06/2024

#Importando biblioteca
import os


os.system('cls')

#Entrada
print('-'*70)
print('Digitar f ate sair se não continua em looping')
print('-'*70)

while (True):
    
    nome = str(input('Digite um nome [digite "f" para Sair]: ')).lower()
    
    if (nome != 'f'):
        print('Estou em looping')
    else:
        print('-'*70)
        print('Você digitou "f" para sair do looping')
        
        break

print('-'*70)
print()