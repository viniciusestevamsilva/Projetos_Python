import os 


os.system('cls')

# Solicita ao usuário para inserir números separados por espaços
entrada = input('Digite números separados por espaços: ')

# Divide a string de entrada em uma lista de string
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário para inserir o número que deseja encontrar na lista 
busca_numero = int(input('Digite o número que deseja encontrar: '))

# Tenta encontrar o indice do numero fornecido
if busca_numero in numeros:
    indice = numeros.index(busca_numero)
    print(f'O número {busca_numero} está no indice {indice}')
else:
    print(f'O número {busca_numero} não foi encontrado na lista')

# Exibe a lista fornecida para referencia
print(f'lista fornecida: {numeros}')

