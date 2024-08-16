import csv
import os

os.system('cls')

arquivo = 'aulas/aula014_arquivos/alunas.csv'
nome_para_alterar = input('Alterar dados: ')
novo_nome = input('Novo nome: ')
novo_telefone = input('Novo telefone: ')
nova_cidade = input('Nova cidade: ')

alterado = False

with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)


for registro in cadastro:
    if registro['nome'] == nome_para_alterar:
        if novo_nome:
            registro['nome'] = novo_nome
        if novo_telefone:
            registro['telefone'] = novo_telefone
        if nova_cidade:
            registro['cidade'] = nova_cidade
        alterado = True

with open(arquivo, 'w', newline='') as arquivo_csv:
    campos = ['nome', 'telefone', 'cidade']
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    escrever.writeheader()
    escrever.writerows(cadastro)

if alterado:
    print('Alterado com sucesso!')
else:
    print('Erro!!')
