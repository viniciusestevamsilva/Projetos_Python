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

# Solicita ao usuario para decidir se deseja limpar a lista
escolha = input("Deseja criar uma copia? (s/n):  ").strip().lower()

# Verifica a escolha do usuario e limpa a lista se a resposta for 's'
if escolha == 's':
    numeros.clear()
    print(f"A lista limpa: {numeros}")
else:
    print("A lista não foi limpa")
    
# Exibe a lista fornecida para referencia 
print(f"Lista fornecida: {numeros}")
