# Crie uma função que verifica se uma aluno está cadastrado ou não em um dicionário. Se estiver cadastrado
# imprima o nome desse aluno e o resto dos seus dados. O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.
import os


os.system('cls')

dados = dict()
def verifica(verf):
    if nome_aluno not in dados:
        print('Este aluno não esta no registro')
    else:
        print('Ele está nos registros')

def cadastro(info):


    dados['Nome:'] = nome_aluno
    dados['Nome:'] = 'Anna'
    dados['Nome:'] = 'Marcus'
    dados['Numero da matricula:'] = matricula_aluno
    dados['Numero da matricula:'] = '123456789'
    dados['Numero da matricula:'] = '987654321'
    dados['Data de nascimento:'] = data_nascimento
    dados['Data de nascimento:'] = '10/02/02'
    dados['Data de nascimento:'] = '02/25/03'

    for i in dados:
        print(i)
    return info


nome_aluno = input('Nome do aluno: ')
verifica
matricula_aluno = input('Numero da matricula: ')
data_nascimento = input('Data de nascimento: ')
cadastro(info=0)
verifica(verf=0)