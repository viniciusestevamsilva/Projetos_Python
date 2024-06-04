# Curso de Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 01
# 03/06/2024

#Importando biblioteca
import os


os.system('cls')

print('-'*70)
print('Digitar f ate sair, se não continua em looping')
print('-'*70)

# ciclo e validação
while (True):
    # tranformar tudo digitado em minusculo e Entrada
    nome = str(input('Digite um nome [digite "f" para Sair]: ')).lower()
    # Condicional e Saída
    if (nome != 'f'):
        print('Estou em looping... para sair digite "f"')
    else:
        print('-'*70)
        print('Você digitou "f" para sair do looping!')
        
        break

print('-'*70)