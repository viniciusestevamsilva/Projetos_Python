# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 30/07/2024

# Faça um programa de perguntas e respostas sobre os estados e capitais brasileiras. O programa deverá exibir para o usuário o está e perguntar qual a sua capital. Se o usuário errar a resposta, 
# o programa será finalizado apresentando quantas perguntas estão corretas. Utilize ao menos uma função e não há a necessidade de modularizar o código.
import os
import random


os.system('cls')

# Criando uma lista de dicionários com todos os estados e suas capitais
estados_brasil = [
    {"estado": "Acre", "capital": "Rio Branco"},
    {"estado": "Alagoas", "capital": "Maceió"},
    {"estado": "Amapá", "capital": "Macapá"},
    {"estado": "Amazonas", "capital": "Manaus"},
    {"estado": "Bahia", "capital": "Salvador"},
    {"estado": "Ceará", "capital": "Fortaleza"},
    {"estado": "Distrito Federal", "capital": "Brasília"},
    {"estado": "Espírito Santo", "capital": "Vitória"},
    {"estado": "Goiás", "capital": "Goiânia"},
    {"estado": "Maranhão", "capital": "São Luís"},
    {"estado": "Mato Grosso", "capital": "Cuiabá"},
    {"estado": "Mato Grosso do Sul", "capital": "Campo Grande"},
    {"estado": "Minas Gerais", "capital": "Belo Horizonte"},
    {"estado": "Pará", "capital": "Belém"},
    {"estado": "Paraíba", "capital": "João Pessoa"},
    {"estado": "Paraná", "capital": "Curitiba"},
    {"estado": "Pernambuco", "capital": "Recife"},
    {"estado": "Piauí", "capital": "Teresina"},
    {"estado": "Rio de Janeiro", "capital": "Rio de Janeiro"},
    {"estado": "Rio Grande do Norte", "capital": "Natal"},
    {"estado": "Rio Grande do Sul", "capital": "Porto Alegre"},
    {"estado": "Rondônia", "capital": "Porto Velho"},
    {"estado": "Roraima", "capital": "Boa Vista"},
    {"estado": "Santa Catarina", "capital": "Florianópolis"},
    {"estado": "São Paulo", "capital": "São Paulo"},
    {"estado": "Sergipe", "capital": "Aracaju"},
    {"estado": "Tocantins", "capital": "Palmas"}
]

# Para não repetir os estados
random.shuffle(estados_brasil)


def verificar(quiz, estado, acertos, erros):
    if quiz == estado["capital"]:
        print('Você acertou!')
        acertos += 1
    else:
        print('Você errou!')
        erros += 1
    return acertos, erros


# Iniciando as veriáveis zeradas
acertos = 0
erros = 0
total_acertos = 0
total_erros = 0

for estado in estados_brasil:
    quiz = input(f'Qual é a capital do Estado do {estado["estado"]}? ').strip()
    acertos, erros = verificar(quiz, estado, acertos, erros)
    total_acertos += acertos
    total_erros += erros
    # Parada em caso de erro
    if erros == 1:
        break

print(f'Você obteve {acertos} acertos!')