import csv
import os

# não sei oque fazer, isso está incompleto/errado
arquivo = 'aulas/aula014_arquivos/alunas.csv'
nome_para_alterar = input('Alterar dados: ')
novo_nome = input('Novo nome: ')
novo_telefone = input('Novo telefone: ')
nova_cidade = input('Novo telefone: ')
alterado = False

with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)
    
    for registro in cadastro:
        novo_nome = input('Novo nome: ')
        novo_telefone = input('Novo telefone: ')
        nova_cidade = input('Novo telefone: ')
        if registro ['nome'] == nome_para_alterar:
            if novo_nome:
                registro['nome'] == novo_nome
            if novo_telefone:
                registro['telefone'] == novo_telefone
            if nova_cidade:
                registro['cidade'] == nova_cidade
            alterado = True

if alterado:
    with open(arquivo, 'w', newline=''):
        campos = ['nome', 'telefone', 'cidade']
        escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
        
        escrever.writeheader()
        escrever.writerows(cadastro)
        print('Alterado com sucesso!')
else:
    print('Erro!!')