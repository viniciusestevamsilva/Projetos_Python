import os

os.system('cls')

print('-'*70)
print('Funções Strings')
print('-'*70)

frase1 = "Olá Mundo!"
quantidade_caracteres = len(frase1) #Conta os caracteres
print(f'A frase {frase1} \ncontém {quantidade_caracteres} caracteres ')
print('.'*70)

minusculas = frase1.lower() # frase em minusulo
print(f'Frase original: {frase1}')
print(f'Frase nova: {minusculas}')
print('.'*70)

maiuscula= frase1.upper() # frase em maiuscula
print(f'Frase original: {frase1}')
print(f'Frase nova: {minusculas}')
print('.'*70)

captalizada = frase1.capitalize() # frase capitalizada
print(f'Frase original: {frase1}')
print(f'Frase nova: {captalizada}')
print('.'*70)

frase2 = '  Olá, Mundo  '
sem_espacos = frase2.strip() # Retirar espaços, antes e depois
print(f'Frase original: {frase2}')
print(f'Frase novo: {sem_espacos}')
print('.'*70)

substituicao = frase1.replace("Mundo", "Python") # Troca palavra
print(f'Frase original: {frase1}')
print(f'Frase novo: {substituicao}')
print('.'*70)

lista = frase1.split(",") # Separar as palavras de uma str em uma lista
print(f'Frase original: {frase1}')
print(f'Frase novo: {lista}')
print('.'*70)

lista = ['Olá', 'Mundo']
juncao = "-".join(lista) # Transforma uma lista  em uma strign  com separador
print(f'Frase original: {lista}')
print(f'Frase novo: {juncao}')
print('.'*70)