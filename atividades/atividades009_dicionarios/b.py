# Utilizando o exercício anterior,  adicione mais 2 elementos ao dicionário.
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 28/06/2024

import os


os.system('cls')

print('/'*70)
print('Dicionario com 4 elementos e depois mais 2')
print('-'*70)

dicionario = dict()  # Dicionario
elementos = []  # Lista

while True:
    print('')
    adiconar = str(input('Deseja adicionar? (n/s): '))
    print('-'*70)

    if adiconar == 's':
        os.system('cls')
        print()
        nome = str(input('Digite nomes: '))
        idade = str(input('Digite idade: '))

        dicionario['nome'] = nome
        dicionario['idade'] = idade

        elementos.append(dicionario)
    elif adiconar == 'n':
        break
    else:
        os.system('cls')
        print()
        print('Comando invalido')
        input('Enter para voltar')

    # opcao = str(input('Deseja adicionar mais coisas (s/n)?'))
    # if opcao == 's':
    #     for i in range(3):
    #         print()
    #         nome = str(input('Digite nomes: '))
    #         idade = str(input('Digite idade: '))

    #         dicionario['nome'] = nome
    #         dicionario['idade'] = idade
    #         elementos.append(dicionario.copy())
for dicionario in elementos:  # Para cada elemento na lista
    for chave, valor in dicionario.items():  # Para cada chave e o valor do dicionario
        # Imprime a chave e o valor de maneira legivel
        print(f'{chave.capitalize()}: {valor}')
    print('/'*70)
