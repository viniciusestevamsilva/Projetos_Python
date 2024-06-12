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

# Solicita ao usuário para escolher a ordem de classificação
ordem = input(
    "Digite 'asc' para ordem ascendente ou 'desc'"
    "para ordem descendente: ").strip().lower()

# Verifica a escolha do usuário e ordena a lista de acordo
if ordem == 'asc':
    numeros.sort()
    print(f"Lista ordenada em ordem ascendente: {numeros}")
elif ordem == 'desc':
    numeros.sort(reverse=True)
    print(f"Lista ordenada em ordem descendente: {numeros}")
else:
    print(f"Opção invalida! A lista não foi ordenada")

# Exibe a lista fornecida para referencia
print("lista fornecida:", numeros)
