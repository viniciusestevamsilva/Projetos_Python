import os


os.system('cls')

# Inicializa uma lista vazia
lista_numero = []

# Pede ao usuário para inserir três números
for i in range(3):
    numero = int(input("Digite um número: "))
    
    # Adiciona o númeor á lista
    lista_numero.append(numero)
    
# Verifica se o número insrido está na lista e
# exibe uma mensagem correspondente
numero_verificar = int(input("Digite um número: "))

if numero_verificar in lista_numero:
    print(f'O número {numero_verificar} está na lista!')
else:
        print(f'O número {numero_verificar} não está na lista!')