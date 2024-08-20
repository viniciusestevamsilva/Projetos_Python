import os


class Pessoa:
    def __init__(self,nome, cpf, nascimento, cep, cidade, estado):
        # Inicializando os atributos
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado


# Solicitando entrada de dados do usuario
os.system('cls')
print('-'*70)
nome = input('Digite seu nome: ')
cpf = input('Digite o CPF: ')
nascimento = input('Digite o ano de nascimento: ')
cep = input('Digite o CEP: ')
cidade = input('Digite sua cidade: ')
estado = input('Digite o estado: ')

# Criando um objeto da classe Pessoa com os dados fornecidos pelo usuario
pessoa1 = Pessoa(nome, cpf, nascimento, cep, cidade, estado)

# Acessando we imprimindo atributos do objetos
print('-'*70)
print('\nInformações da Pessoa:')
print('='*70)
print(f'Nome: {pessoa1.nome}')
print(f'CPF: {pessoa1.cpf}')
print(f'Ano de Nascimeno: {pessoa1.nascimento}')
print(f'CEP: {pessoa1.cep}')
print(f'Cidade: {pessoa1.cidade}')
print(f'Estado: {pessoa1.estado}')
print('-'*70)