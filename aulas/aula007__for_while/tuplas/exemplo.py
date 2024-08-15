# Solicitar ao usuário a quantidade de elementos da tupla
import os


os.system('cls')

# Solicita o usuário a qauntidade de elementos na tupla
numero_elementos = int(input("Quantos elementos na tupla ?"))

# Inicializar uma lista vazia para armazenar os elementos
elementos = []

# Estrutura de repetição para obeter os elementos do usuário
for i in range(numero_elementos):
    while (True):
        valor = input(f"Digite o valor  {i +1}: ")
        if valor.isdigit(): # Verifica se a entrada é número
            elementos.append(int(valor))
            break
        else:
            print("Entrada inválida. Digite um número.")

#  Converte a lista para um tupla
tupla = tuple(elementos)

print('-'*70)
# Exibir a tupla criada
print(f"Tupla criada {tupla}")

# Estrutura de repetição para permitir múltiplas
# operações até que o usuário deseje sair
while (True):
    # Condicional para verificar a presença de
    # um número especifico
    valor = int(input("Verificar se o numero na Tupla: "))
    
    if valor in tupla:
        print(f"O número {valor} está na tupla.")
        # Contar quantas vezes o número aparece
        contagem = tupla.count(valor)
        print(f"O número {valor} aparece {contagem} vez(es).")
        # Encontrar o índice da primeira ocorrencia 
        
        indice = tupla.index(valor)
        print(f"A 1° ocorrencia de  {valor} stá no índice  {indice}).")

    else:
        print(f"O número {valor} não está na Tupla.")
    
    # Pergunta ao usuário se deseja realizar
    # outra operação
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break
print('-'*70)
print("Fim do programa.")
print('-'*70)