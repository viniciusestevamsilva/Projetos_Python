import os


os.system('cls')

# Inicialização do dicionário e da lista
elementos = {} # Dicionário
periodica = [] # Lista

# Entrada de dados
for c in range(2):
    print(f"Entrada de dados {c + 1}:")
    simbolo = str(input('Simbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    
    # Adiciona os dados ao dicionario
    elementos['simbolo'] = simbolo
    elementos['nome'] = nome
    
    # Usa append() com copy() para adicionar uma cópia do dicionario a lista
    periodica.append(elementos.copy())

print()
print('-'*70)
print("Elementos na tabela periódica:")
print(periodica)
print('-'*70)
print()

# For aninhado para percorrer a lista e o dicionario
print("Detalhes dos elementos:")
for elemento in periodica: #Para cada elemento na lista
    for chave,valor in elemento.items(): # Para cada chave e o valor do dicionario
        print(f'{chave.capitalize()}: {valor}') # Imprime a chave e o valor de maneira legivel
    print('-'*70) # Linha separadora entre elementos