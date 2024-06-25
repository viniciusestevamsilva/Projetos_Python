# Trabalho sobre estrutura de dados SET{}
# Senac Minas Gerais/Juiz de Fora
# Aluno: Vinícius Estevam da Silva
# Turma: 0152
# Ano: 2024

# Enunciado: Meu programa irá remover todos os elementos do SET

import os


os.system('cls')

print('/'*70)
print('''
      
      "Remover todos os elementos de uma lista
      usando o metodo CLEAR()"
      
      ''')
print('/'*70)

while (True):
    
    conjunto = set([1,2,3,4]) # Criando um SET()
    print('Conjunto:',conjunto)
    print('Caso queira parar, digite "sair"')
    print('='*70)
    for i in range(1,5):
    
        elementos = input('Digite um elemento:  ').replace(' ', ',')
        print('-'*70)
        # Adiciona elementos ao conjunto
        conjunto.add(elementos)
        if elementos == "sair":
            print('Você saiu do programa.')
            print('/'*70)
            break
    
    print()
    print(f'Conjunto antes do CLEAR():  {conjunto}')
     # Remove todos os elementos do conjunto
    conjunto.clear()
    
    # Imprimi  "set()" ja que o conjunto está vazio
    print(f'Conjunto Depois do CLEAR():  {conjunto}')
    print()
    break # "Quebra" finaliza o programa

print('-'*70)
print('Fim do Programa.')
print('-'*70)