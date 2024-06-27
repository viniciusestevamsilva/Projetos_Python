import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    #exibindo menu de opções
    print("\nMenu opções:")
    print("1. Adicionar um par chave-valor")
    print("2. Mostrar chaves do dicionario")
    print("3. Mostrar valores do dicionario")
    print("4. Mostras os itens no dicionario")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        # Adicionar um par chave-valor ao dicionario
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        meu_dicionario[chave] = valor
        print(f"Par {chave}: {valor} adicionado. ")
        
    elif opcao == '2':
        # Mostrar as chaves do dionario usando keys()
        if meu_dicionario:
            print("Chave do dicionario:", meu_dicionario.keys())
        else:
            print("O dicionario esta vazio. Adicione itens primeiro.")
            
    elif opcao == '3':
        # Mostrar os valores do dicionario usando values()
        if meu_dicionario:
            print("Valores do dicionario:", meu_dicionario.values())
            
    elif opcao == '4':
        # Mostrar os itens (chave-valor) do dicionario usando item()
        if meu_dicionario:
            print("Itens do dicionario:", meu_dicionario.values())
        
    elif opcao == '5':
        # Sai do programa
        print("Saindo do programa.")
        break
    
    else:
        # Mensagem para opção invalida
        print("Opção inválida. Tente novamente.")