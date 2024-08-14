import os


os.system('cls')

# Solicita ao usuário para inserir números separados por espaços
entrada = input("Digite números separados por espaços: ")

# Divide a string de entrada em uma lista de string
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário para decidir se deseja
# criar uma copia da lista
escolha = input("Deseja criar uma copia? (s/n):  ").strip().lower()

# Verificar a escolha do usuario e cria uma copia da
# lista se a reposta for 's'
if escolha == 's':
    lista_copiada = numeros.copy()
    print(f"Copia da lista: {lista_copiada}")
else:
    print(f"A lista não foi copiada")

# Exibe a lista fornecida para referencia
print(f"Lista fornecida: {numeros}")
