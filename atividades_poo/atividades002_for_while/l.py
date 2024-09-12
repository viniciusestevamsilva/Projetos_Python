# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os

class Dados: # Classe Pai
    def __init__(self, nome, senha, seuID):
        self.nome = nome
        self.senha = senha
        self.seuID = seuID

    def obter_cadastro(self):
        return self.nome + self.senha + self.seuID

class Info: # Classe Filha
    def __init__(self, nome, senha, seuID):
        self.nome = nome
        self.senha = senha
        self.seuID = seuID
        self.cadastro = self.nome + self.senha + self.seuID

    def dados(self):
        while True:
            print('=' * 70)
            dados = input('Digite os dados [digite sua "senha" e "nome" para sair]: ').lower()
            
            if dados != self.cadastro.lower(): 
                print('Estou armazenando dados. Para sair, digite os dados do cadastro.')
                print('=' * 70)
            else:
                print('-' * 70)
                print('Você saiu do banco de dados.')
                break

os.system('cls')

print('/' * 70)
print('Digite seus dados para sair')
print('=' * 70)
print('')

nome = input('Digite seu nome: ').lower()
senha = input('Digite sua senha: ').lower()
seuID = input('Digite seu ID: ').lower()

# Criar uma instância 
info = Info(nome, senha, seuID)

info.dados()# Chama o método

print('/' * 70)
