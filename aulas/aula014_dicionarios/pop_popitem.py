import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    #exibindo menu de opções
    print("\nMenu opções:")
    print("1. Adicionar um par chave-valor")
    print("2. Remover um item usando pop()")
    print("3. Remover o ultimo item usando popitem()")
    print("4. Mostras o dicionario aual")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        # Adicionar um par chave-valor ao dicionario
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        meu_dicionario[chave] = valor
        print(f"Pár {chave}: {valor} adicionado.")
    elif opcao == '2':
        # Remover um item especifico usando pop()
        if meu_dicionario:
            chave = input("Digite a chave do item que deseja remover: ")
            valor_removido = meu_dicionario.pop(chave, "Chave não encontrada")
            print(f"Item removido: {chave}: {valor_removido}")
        else:
            print("O dicionario está vazio. Adicione itens primeiro.")
    elif opcao == '3':
        # Remover o ultimo item usando popitem()
        if meu_dicionario:
            chav, valor = meu_dicionario.popitem()
            print(f"Ultimo item removido: {chave}: {valor}")
        else:
            print("O dicionario está vazio. adicione itens primeiro.")
            
    elif opcao == '4':
        # Mostrar o dicionario atual
        if meu_dicionario:
            print("Dicionario atual:", meu_dicionario)
        else:
            print("O dicionario está vazio.")
            
    elif opcao == '5':
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente")