# Curso Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data /06/2024

import os


os.system('cls')

print('-'*70)
print('''
      Após esta entrada de dados, faça o seguinte:
    # • Mostre a quantidade de notas que foram lidas.
    # • Exiba todas as notas na ordem em que foram informadas.
    # • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
    # • Calcule e mostre a soma das notas.
    # • Calcule e mostre a média das notas.')
''')
print('-'*70)

notas = []
soma = 0

entrada = input('Insira as notas separadas por espaço: ').strip()

nota = entrada.split()
notas.extend(nota)

quantidade_notas = len(notas)
print(f'Foram inseridas {quantidade_notas} notas') 
print()
print(f'As notas são: {notas}') 
print()

inverso_notas = notas[::-1] 
print('Na ordem inversa e sobrepostas elas ficam dessa forma: ')
for nota in inverso_notas: 
    print(nota)


for nota in notas:
    soma += int(nota) 

print()
print(f'Soma total das notas: {soma}')
media = soma / quantidade_notas 
print()
print(f'Média das notas: {media:.2f}')