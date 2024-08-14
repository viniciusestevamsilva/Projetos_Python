import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    #exibindo menu de opções
    print("\nMenu opções:")
    print("1. Adicionar um par chave-valor")
    print("2. Definir valor padrão para umchave usando setdefault()")
    print("3. Atualiza o dicionario usando update()")
    print("4. Mostras o dicionario aual")
    print("5. Sair")
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        # Adiciona um par chave-valor ao dicionario
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        meu_dicionario[chave] = valor
        
    elif opcao == '2':
        # Definir valor padrão par aumva chave usando setdefault()
        chave = input("Digite a chave para definir um valor padrão: ")
        valor_padrao = input("Digite o valor padrão: ")
        valor_existente = meu_dicionario.setdefault(chave, valor_padrao)
        print(f"Valor para a chave '{chave}': {valor_existente}")
    
    elif opcao == '3':
        # Atualizar o dicionario usando update()
        novos_pares = input("Digite os novos pares chave-valor: ")
        novos_pares_lista = novos_pares.split(',')
        novos_dados = {}
        for par in novos_pares_lista:
            chave, valor = par.split(',')
            novos_dados[chave] = valor
        meu_dicionario.update(novos_dados)
        print("Dicionario atualizado:", meu_dicionario)
    
    elif opcao == '4':
        # Mostrar o dicionario atual
        if meu_dicionario:
            print("Dicionario atua:", meu_dicionario)
        else:
            print("O dicionario está vazio.")
    elif opcao == '5':
        # Sai do programa
        print("Saindo do programa.")
        break
        
    else:
        #Mensagem para opção invalida
        print("Opção inválida. Tente novamente.")