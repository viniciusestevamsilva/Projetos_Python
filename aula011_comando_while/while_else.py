import os


os.system('cls')

print('-'*70)
print('Estrutura de controle WHILE ELSE BREAK')
print('-'*70)

print()

while (True):
    
    #lower() garante o tratamento para entrada de 's' ou 'S'
    nome = str(input('Digite um nome [s - Sair]: ')).lower()
    
    if (nome != 's'):
        print('Continue digitando...')
    else:
        print('-'*70)
        print('Você digitou "s" pra sair!')
        
        #interrompe o laço
        break

print('-'*70)
print()