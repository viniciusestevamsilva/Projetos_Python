# Importando biblioteca csv
import csv
import os


# Criando uma lista de dicionarios: cada dicionario é uma linha (registro)
lista = [
    {'nome':'Agata', 'telefone': '(32)99196-0000', 'cidade': 'Juiz de Fora'},
    {'nome': 'Bia', 'telefone': '(32)99196-1111', 'cidade': 'Juiz de Fora'},
    {'nome': 'Coly', 'telefone': '(32)99196-2222', 'cidade': 'Juiz de Fora'},
    {'nome': 'Isis', 'telefone': '(32)99196-3333', 'cidade': 'Juiz de Fora'},
]

# Caminho para apasta onde o arquivo CSV será salvo
pasta = 'aulas/aula015_arquivos'

# Verificando se a pasta existe, não irá criá-la
os.makedirs(pasta, exist_ok=True)

# nome para o arquivo CSV para gravar as infromações
arquivo = 'aulas/aula015_arquivos/alunas.csv'

# caminho completo do arquivo CSV
caminho_arquivo = os.path.join(pasta, arquivo)

# Abre  o arquivo 'arquivo' no modo de escrita ('w')
# Se o arquivo não existir, ele será criado; se existir, será truncado (esvaziado)
# newline='':  Evita a adição de linhas em branco extras ao gravar o arquivo em algumas plataformas.
# as arquivo_csv atribui o objeto arquivo ao 'arquivo_csv' para ser usado dentro do bloco with.
with open(arquivo, 'w', newline='') as arquivo_csv:
    
    # campos = ["names", "telefone", "cidade"]: define a lista de nomes de campos
    # (cabeçalhos das colunas do CSV).
    campos = ['nome', 'telefone', 'cidade']
    
    # writer = csv.DictWriter(arquivo_csv, fieldnames=campos):
    # Cria um objeto DictWriter que usará 'arquivo_csv' para gravar os campos.
    # fieldnames define a ordem dos campos no arquivo CSV
    # Delimiter=';': é o separador
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    # writer.writerheader(): grava a linha de cabeçalho no
    # arquivo CSV usando os nomes de campos definidos em fieldnames.
    escrever.writeheader()
    
    # writer.writerows(lista): grava todas as linhas da lista no arquivo CSV
    # cada dicionario em 'lista' se torna  uma linha de arquivo.
    escrever.writerows(lista)
    
os.system('cls')
# exibe uma mensagem indicando que o arquivos foi gravado com sucesso
print(f'Arquivo {arquivo} gravado com sucesso!')