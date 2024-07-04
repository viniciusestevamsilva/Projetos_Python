# Utilizando o exercício anterior , retire um elemento do dicionário.
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 28/06/24
import os


os.system('cls')

print('/'*70)
print('Dicionario com 4 elementos e depois mais 2')
print('-'*70)

dicionario = dict()  # Dicionario
elementos = []  # Lista

while True:
    print('')
    print('')
    print("1. Adicionar um par chave-valor")
    print("2. Remover um item")
    print("s. Sair")
    
    opcao = input("Escolha uma opção (1-2): ")
    
    if opcao == '1':
        os.system('cls')
        # Adicionar um par chave-valor ao dicionario
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        dicionario[chave] = valor
        print(f"{chave}: {valor} foram adicionados.")
    elif opcao == '2':
        os.system('cls')
        # Remover um item especifico usando pop()
        if dicionario:
            os.system('cls')
            chave = input("Digite a chave do item que deseja remover: ")
            valor_removido = dicionario.pop(chave, "Chave não encontrada")
            print(f"Item removido: {chave}: {valor_removido}")
        else:
            os.system('cls')
            print("O dicionario está vazio..")
    elif opcao == 's':
        os.system('cls')
        print("Fim do programa.")
        break
    
    else:
        
        print("Opção inválida. Tente novamente")
