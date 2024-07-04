# Faça um programa para criar um dicionário com 4 elementos. Depois imprima a lista completa,
# delete o último elemento e mostre uma listagem nova
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/07/2024
import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 4 elementos.\ne depois remove o ultimo elemento')
print('-'*70)

inventario = {} # Dicionario
mochila = [] # Lista

while True:
    
    print('Seu inventario')
    print()
    print('Comandos')
    print('"A" Adicionar item')
    print('"Q" Dropar ultimo item')
    print('"E" Sair')
    comando = str(input('Escolha uma opção: ')).upper()

    if comando == 'A':
        print('-'*70)
        item = str(input('Nome do elemento: '))
        slot = str(input('Simbolo do elemento: '))
        print('='*70)
        
        inventario['item'] = item
        mochila.append(inventario.copy())# Adicionando uma copia a lista
        
        print('Item  adicionado')
        print(f'Item: {item} | Slot: {slot}')
        input('Pressione enter para voltar')
        print('='*70)
        print()
    elif comando == "Q": # Remover o ultimo elemento 
        if inventario: # Verificando se o inventario existe ou se tem algo nele
            print('='*70)
            item,slot = inventario.popitem() # removendo
            
            print(f'Item dropado: {item}: {slot}')
            print('='*70)
            input('Pressione enter para voltar')
            print()
        else:
            print('Inventario vazio, explore mais para coletar itens')
            input('Pressione enter para voltar')
            print()
    elif comando == "E": # Finliza o programa e mostra a listagem nova
        print('Inventario Atual')
        print()
        for chave, valor in inventario.items():# Para cada chave e o valor do dicionario
            print(f'{chave}: {valor}')
        print()
        print('-'*70)
        print('Fim do programa')
        print('-'*70)
        break
    else:
        print('-'*70) # Caso digite outra coisa fora dos comandos
        print('Comando invalida, digite um dos comandos acima.')
        print()
        input('Pressione enter para voltar')