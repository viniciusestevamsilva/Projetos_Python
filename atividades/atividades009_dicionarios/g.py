# Faça um programa para cadastrar os alunos de uma escola. Para os campos, tome como referência o nome do aluno, 
# data de nascimento e matrícula.
# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/07/2024
import os


os.system('cls')

print('='*70)
print('Programa que cadastra alunos de uma escola.')
print('-'*70)

# Declaração do dicionario e lista
dicionario = dict()
lista = []
while True:
    print('Escola')
    print()
    print('Comandos...')
    print('"C" Cadastrar um aluno')
    print('"M" Mostrar os alunos ja cadastrados')
    print('"S" Finalizar programa')
    
    comando = str(input('Escolha um dos comandos \n:')).upper()
    print('-'*70)
    
    if comando == 'C': # Adicionar um novo aluno
        print()
        print(f'Informe os dados do aluno')
        nome = (input('Nome do aluno: '))
        data_nascimento = (input('Data de nascimento: '))
        matricula = (input('Data da matrícula: '))
        print('.'*70)
        # Adicionando os dados ao dicionario
        dicionario['Nome do aluno'] = nome
        dicionario['Data de nascimento'] = data_nascimento
        dicionario['Data da matrícula'] = matricula
        lista.append(dicionario.copy())# Adicionando uma copia a lista
        print('O aluno foi cadastrado com sucesso')
        print(f'Informações do aluno cadastrado')
        print(dicionario)
        print('='*70)
        input('\nPressione enter para voltar')
        print('='*70)
        if not data_nascimento.isnumeric() and matricula.isnumeric():
            print('Digite as datas somente em numeros')
            input('\nPressione enter para voltar')
            print('='*70)
            continue
    elif comando == 'M': #  Mostra os alunos adicionados
        if dicionario: # Vendo se o dicoinario existe
            print()
            print('-'*70)
            print('Alunos cadastrados abaixo.')
            print('-'*70)
            print()
            for aluno in lista:  # Itera sobre cada dicionário de alunos na lista 'lista'
                for chave,valor in aluno.items(): # Para cada chave e o valor do dicionario
                    print(f'{chave}: {valor}') # Imprime a chave e o valor formatados
                print('-'*70)
            input('\nPressione enter para voltar')
        else:  # Caso o diconario não exista ou estiverr vazio
            print()
            print('Sem alunos cadastrados ate o momento')
            input('\nPressione enter para voltar')
            print('='*70)
    elif comando == 'S': # Finaliza o programa
        print()
        print('-'*70)
        print('Fim do programa')
        print('-'*70)
        print()
        break
    else:
        print()
        print('-'*70) # Caso digite outra coisa fora dos comandos
        print('Comando invalida, digite um dos comandos acima.')
        print()
        input('\nPressione enter para voltar')