# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data /06/2024

import os


os.system('cls')


print('-'*70)
print('Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.')
print('-'*70)

notas = [] # Lista vazia
soma = ''

# Entrada
entrada = input('Insira as notas sepadaras por vírgula: ')
notas_3mestre = entrada.split(',')


notas.extend(notas_3mestre)
for nota in notas:
    soma += float(nota)
    
periodos = len(notas) 
media = (soma / periodos) 

print()
print(f'A média das notas nos {periodos} período(s) foi de: {media:.2f}.')