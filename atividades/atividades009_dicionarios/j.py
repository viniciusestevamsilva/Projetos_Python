# Faça um programa para criar um dicionário com nomes de frutas. Em seguida verifique se tem abacaxi nos valores.
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/07/2024
import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 4 elementos.')
print('-'*70)

# Declaração de dicionario
dicionario = dict()
lista = []
while True:
    os.system('cls')
    
    print('Lista para frutas')
    print()
    print('Deseja adicionar uma fruta?')
    print('"s" - Sim')
    print('"n" - Não')
    comando = str(input('Escolha uma opção: ')).lower()
    if comando == 's':
        print('-'*70)
        nome = str(input('Nome da fruta: ')).lower
        print('-'*70)
        dicionario['Nome'] = nome # Adiciona a fruta no dicionário
        lista.append(dicionario.copy()) # Adiciona uma cópia do dicionário à lista
        print(f'Lista de frutas:\n{nome}')
        print()
        if 'abacaxi' not in dicionario or 'abacaxi' not in lista: # Verificando se abacaxi esta presenta
            print('Não tem a   Abacaxi na lista :(')
            print('/'*70)
        else:
            print('Tem abacaxi na lista! :D')
            print('/'*70)
        input('Pressione enter para voltar')
        
    elif comando == 'n':
        print()
        print('Fim do programa')
        print('/'*70)
        break
    else:
        print()
        print('Coloque uma das opções acima')
        input('Pressione enter para voltar')
        print()