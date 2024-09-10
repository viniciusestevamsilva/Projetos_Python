# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os


class Dados:
    def __init__(self, nome,senha):
        self.nome = nome
        self.senha = senha
        

class Info(Dados):
    def infomacoes(nome, senha):
        while (True):
            cadastro = nome + senha
            
            dados = str(input('Digite dados [digite sua "senha" e "nome" para Sair]: ')).lower()
            
            if (dados != cadastro):
                print('Estou armazenando dados ,para sair digite os dados do cadastro.')
                print('='*70)
            else:
                print('-'*70)
                print('Você saiu de banco de dados.')
                
                break
                
print('-'*70)
print('Digitar seus dados para sair')
print('-'*70)


senha = (input('Digite sua senha: '))
nome = (input('Digite seu nome: '))

verificar = Info.infomacoes(nome, senha)

print('-'*70)