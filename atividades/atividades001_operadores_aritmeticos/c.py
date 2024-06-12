
# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 18/04/2024

#Imports
import os

os.system('cls')

# Entrada
nota1 = float(input('nota1: '))
nota2 = float(input('nota2: '))
nota3 = float(input('nota3: '))
nota4 = float(input('nota4: '))

 #Processamento
soma = nota1 + nota2 + nota3 + nota4
media = (nota1 + nota2 + nota3 + nota4) / 4

#Saida
print('-'*70)
print('RESULTADOS')
print('-'*70)
print(f'Nota1: {nota1} | Nota2: {nota2} | '
      f'Nota3: {nota3} | Nota4: {nota4} | ')
print('='*70)
print(f'Media: {media}')
print('='*70)