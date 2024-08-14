import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: LISTA COMPREHENSION [ ]')
print('-'*70)

lista_numeros = [1, 2, 3, 5]

#Triplicando os valores
lista_nova_triplicadas = []

for item in lista_numeros:
    lista_nova_triplicadas.append(item * 3)

print('Triplicando os valores: forma normal')
print(f'Lsita triplicadas: {lista_nova_triplicadas}')
print()

# List Comprehesions
lista_nova_triplicadas_2 = [item * 3 for item in lista_numeros]
print('Triplicar os valores: List Comprehensions')
print(f'Listaa triplicada: {lista_nova_triplicadas_2}\n')