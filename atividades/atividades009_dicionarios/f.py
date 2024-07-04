# Faça um programa que cadastra 5 tipos de vinho. Para os campos deste cadastro tome como referência nome do vinho, tipo,
# teor alcoólico e safra.
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/07/2024
import os


os.system('cls')

print('='*70)
print('Programa que cadastra 5 tipos de vinho.')
print('-'*70)

# Declaração de dicionario
vinhos = dict()
lista = []
while True:
    os.system('cls')
    print('-'*70)
    print('Adega de vinhos')
    print()
    print('Comandos...')
    print('"A". Adicionar um vinho')
    print('"M". Mostrar os vinhos')
    print('"S". Sair')
    print()
    
    comando = str(input('Escolha uma opção: ')).upper()
    print('-'*70)
    print()
    
    if comando == 'A': # Adicionar um novo vinho ao cadastro
        print('-'*70)
        print(f'Informe os dados do vinho')
        nome = input('Nome do vinho: ')
        tipo = input('Tipo do vinho: ')
        teor = input('Teor alcoolico: ')
        safra = input('Safra: ')
        if not safra.isnumeric():
            print('-'*70)
            print('Digite apenas os numeros da safra')
            input('\nPressione enter para voltar')
            
        print('-'*70)
        # Adicionando os dados ao dicionario
        vinhos['nome'] = nome
        vinhos['tipo'] = tipo
        vinhos['teor'] = teor
        vinhos['safra'] = safra
        
        lista.append(vinhos.copy())# Adicionando uma copia a lista
        print()
        print('O vinho foi adicionado')
        print(f'Informações do vinho adicionado: {vinhos}')
        print()
    elif comando == 'M': #  Mostra os vinhos adicionados no dicionario
        if vinhos: # se o dicionario existe 
            print('-'*70)
            print('Vinho adicionados:')
            print('-'*70)
            for vinho in lista:  # Itera sobre cada dicionário de vinho na lista
                for chave, valor in vinho.items(): # Para cada chave e o valor do dicionario
                    print()
                    print(f'{chave}: {valor}') # Imprime a chave e o valor formatados
                print()
            input('\nPressione enter para voltar')
        else: # se o diconario estiver vazio
            print('Lista de vinhos esta vazia')
            input('\nPressione enter para voltar')
    elif comando == 'S': # Finaliza o programa
        print()
        print('Fim do programa')
        print()
        break
    else:
        print('-'*70) # Caso digite outra coisa fora dos comandos
        print('Comando invalida, digite um dos comandos acima.')
        print()
        input('\nPressione enter para voltar')