import os


os.system('cls')


print('-'*70)
print('---------- TABELA PERIODICA ----------')
print('-'*70)

# Inicialização do dicionario e da lista 
elementos= {} # Dicionario
periodica = [] # Lista

while True:
    os.system('cls')
    
    # Cabeçalho do menu
    print('-'*70)
    print('MENU DE OPÇÕES:')
    print('='*70)
    print('1. Adicionar um elemento')
    print('2. Visualisar todos os elementos')
    print('3. Atualizar um elementos')
    print('4. Remover um elementos')
    print('5. Sair')
    print('-'*70)
    
    # Solicitação da escolha do usuario
    opcao = input("Escolha uma opção (1-5):")
    
    if opcao == '1':
        # Adicionar um elementos
        simbolo = str(input('Simbolo do elementos: '))
        nome = str(input('Nome do elemento: '))
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())
        input("\nElemento adicionado. Pressione Enter para continuar...")
    
    elif opcao == '2':
        # Visualizar todos os elemntos
        print("\nElemntos na tabela periodica: ")
        print('-'*70)
        for elementos in periodica:
            for chave, valor in elemento.items():
                print(f'{chave.capitalize()}: {valor}')
            print('-'*70)
        input("\nPressione Enter para continuar...")
    
    elif opcao == '3':
        # Atualizar um elemento
        simbolo = str(input('Digite o simbolo do elemento para atualizar: '))
        # Inicializar a flag como false
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input(f'Digite o novo simbolo para'
                f'{simbolo} (ou deixe em branco para manter o atual): '))
                novo_nome = str(input(f'Digite o novo nome para'
                f'{simbolo} (ou deixe em brano para manter o atual):'))
                
                # Atualiza o simbolo e o nome se fornecidos
                if novo_simbolo:
                    elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome
                # Define a flag como true quando o elemento é encontrado
                encontrado = True
                break
        
        if encontrado:
            input("\nElemento atualizado. Enter para continuar...")
        else:
            input("\nElemento não econtrado. Enter para continuar...")
    
    elif opcao == '4':
        # Remover um elemento
        simbolo = str(
            input('Digite o simbolo ddo elemento que deseja remover: '))
        encontrado = False #Inicializa a flag como false
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                periodica.remove(elemento)
                # Define a flag como true quando o elemento é encontradp
                encontrado = True
                break
        if encontrado:
            input("\nElemento removido. Enter para continuar...")
        else:
            input("\nElemento não enonotrado. Enter para continuar...")
    
    elif opcao == '5':
        print("Saindo do programa")
        break
    
    else:
        input("Opção inválida. Enter para tentar novamente...")