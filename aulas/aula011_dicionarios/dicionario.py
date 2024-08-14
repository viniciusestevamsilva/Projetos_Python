import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIOS ') #dict => {}
print('-'*70)

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# Atribuindo valores
compras['id'] = 1
compras['item'] = 'caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'Sherlock Homes'
pessoas['endereço'] = 'Baker Street'
pessoas['numero'] = '221b'
pessoas['cidade'] = 'Londres'
pessoas['pais'] = 'Inglaterra'

cores['red'] = 'Vermelho'
cores['green'] = 'Verde'
cores['blue'] = 'Azul'

elementos['Pb'] = 'Chumbo'
elementos['Au'] = 'Ouro'
elementos['N'] = 'Nitrogenio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

# Saída simples
print(f'Minhas compras: {compras}')
print(f'Detetves: {pessoas}')
print(f'Cor RGB: {cores}')
print(f'Tabela Periodica: {elementos}')
print(f'Listagem de números: {numeros}')
print()
print('-'*100)