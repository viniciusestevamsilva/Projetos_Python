import random
import os


os.system('cls')

print('-'*70)
print('BIBLIOTECA RANDOM')
print('='*70)

print('Número Aleatório')
numero_aleatorio = random.random()
print(f'O número gerado foi: {numero_aleatorio} ')
print('.'*70)

print('Número Aleatório inteiro')
numero_aleatorio = random.randint(1, 20)
print(f'O número inteiro gerado foi: {numero_aleatorio}')
print('.'*70)

print('Número Aleatório decimal no intervalo')
aleatorio_decimal = random.uniform(1, 10)
print(f'O número decimal gerado foi: {aleatorio_decimal}')
print('.'*70)

print('Sorteio em uma Lista')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nome_sorteado}')
print('.'*70)

print('Embaralhar sequencia')
lista2 = ['Ágata', 'Coly', 'Isis', 'Bia']
print(f'Lista antiga: {lista2}')
# Embaralhado = list(random.shuffle(lista)) dá erro
# Embaralhado = random.shuffle(lista) saída vazia
random.shuffle(lista2)
print(f'Lista nova: {lista2}')
print('.'*70)

print('Retorno de elementos únicos de uma população')
numero = [1, 2, 3, 4, 5, 6, 7]
amostra_aleatoria = random.sample(numero, 5)
print(f'Retorno da amostragem: {amostra_aleatoria}')
print('.'*70)