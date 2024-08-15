# Curso de Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 05/06/2024
#Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
#O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

#Importando biblioteca
import os


os.system('cls')

# Entrada
print('-'*70)
print('Digitar seus dados para sair')
print('-'*70)


senha = (input('Digite sua senha: '))
nome = (input('Digite seu nome: '))

# Variavel
cadastro = senha + nome

# Condicional
while (True):
    
    dados = str(input('Digite dados [digite sua "senha" e "nome" para Sair]: ')).lower()
    
    if (dados != cadastro):
        print('Estou armazenando dados ,para sair digite os dados do cadastro.')
        print('='*70)
    else:
        print('-'*70)
        print('Você saiu de banco de dados.')
        
        break

print('-'*70)