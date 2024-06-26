import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIO')
print('-'*70)

# indices iguais: só irá exibir um item
dicionario1 = {'nomes': 'Jonh', 'nome': 'Jane'}

# Posso ter uma tupla como indice e uma lista como valor
dicionario2 = {(1,2) : [1,2]}

# Mas não posso ter uma lista como índice e uma tupla como valor
dicionario3 = {[1,2] : (1,2)}

# saída
print('-'*80)
print(dicionario1)
print(dicionario2)

print()