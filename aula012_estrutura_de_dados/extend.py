import os


os.system('cls')

# Inicialize a lista vazia
lista_numero = []

# Solicita ao usuário para inserir números separados por espaços
entrada = input("Digite números separados por espaços: ")

# Divide a string de entrada em uma lista de strings
numeros = entrada.split()

# Crie uma lista para armazenar os números pares
pares = [ ]

# Itera sobre os números inseridos
for numero in numeros:
    # Converte a string para inteiro
    numero_aux = int(numero)
    # Verifica se o número é par
    if numero_aux % 2 == 0:
        # Adiciona o número par á lista de pares
        pares.append(numero_aux)
        
# Usa extend() para adicionar todos os números para á lista principal
lista_numero.extend(pares)

# Exibe a lista resultante
print(f'Números pares adicionados á lista:{lista_numero}' )