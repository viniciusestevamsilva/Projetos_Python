# Imports 
import os


os.system('cls')

print('-'*70)
print('Operadores Aritmeticos: Ordem de precedencia')
print('-'*70)

#Entrada
nota1 = float(input('1 nota: '))
nota2 = float(input('2 nota: '))
nota3 = float(input('3 nota: '))
nota4 = float(input('4 nota: '))

# Processamento
soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4 
media_correta = (nota1 + nota2 + nota3 + nota4) / 4

# Saída
print('---- Notas ----')
print(f'Nota 1: {nota1} | Nota 2: {nota2} | '
      f'Nota 3: {nota3} | Nota 4: {nota4} | ')
print('-'*70)
print(f'Média errada: {media} ')
print(f'Média correta: {media_correta}')
print('-'*70)