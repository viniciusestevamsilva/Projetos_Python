import os 


os.system('cls')

print('-'*70)
print('SAIDA COM FOR...INUMERATE')
print('-'*70)

soma = 0 

# Criando lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# percorrendo a lista enumerate()
# O comando enumerate adiciona um indice
# para cada valor nossa lista
# start opcional, para não começar no indice

# Para cada numero dentro da lista de numeros, enumere com um indice
for indice, numero in enumerate(lista_numeros):
    soma += numero # soma os numeros
    print(f'indice: {indice} = Número: {numero}')
    
print('-'*70)
print(f'A soma de todos os números é: {soma}')
print("Fim do programa!")
print('-'*70)

