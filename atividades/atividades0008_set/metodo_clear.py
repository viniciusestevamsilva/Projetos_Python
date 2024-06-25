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
    
    # Criando um SET()
    conjunto1 = set([1,2,3,4])
    conjunto2 = set(['Pedro','Taiz','Bruno'])
    conjunto3 = set([1,2,6,'Jonas',6,'mike','Bruno'])
    
    print('Conjunto de Números:',conjunto1)
    print('Conjunto de Nomes:',conjunto2)
    print('Conjunto Misto:',conjunto3)
    print('Caso queira parar, digite "@"')
    print('='*70)
    print()
    print('Comandos: "A" "B" "C"')
    entrada = str(input('Digite qual conjunto deseja alterar:  ')).upper()
    print()
    print('Será adicionado 5 elementos ao conjunto.')
    print('-'*70)
    
    if entrada == 'A':
        for i in range(1,5):
            elementos = input('Digite o elemento que será adicionar ao conjunto:\n')
            conjunto1.add(elementos)#  Adiciona elementos ao conjunto
            if elementos == '@':
                print()
                print('Você saiu do programa')
                print('/'*70)
                break
        print()
        print(f'Conjunto antes do CLEAR():  {conjunto1}')
        # Remove todos os elementos do conjunto
        conjunto1.clear()
        
        # Imprimi  "set()" ja que o conjunto está vazio
        print(f'Conjunto Depois do CLEAR():  {conjunto1}')
        print()
        break
        
    if entrada == 'B':
        for i in range(1,5):
            elementos = input('Digite o elemento quer adicionar ao conjunto:\n')
            conjunto2.add(elementos)#  Adiciona elementos ao conjunto
            if elementos == '@':
                print()
                print('Você saiu do programa')
                print('/'*70)
                break
        print()
        print(f'Conjunto antes do CLEAR():  {conjunto2}')
        # Remove todos os elementos do conjunto
        conjunto2.clear()
        
        # Imprimi  "set()" ja que o conjunto está vazio
        print(f'Conjunto Depois do CLEAR():  {conjunto2}')
        print()
        break
    
    if entrada == 'C':
        for i in range(1,5):
            elementos = input('Digite o elemento que será adicionar ao conjunto:\n')
            conjunto3.add(elementos)#  Adiciona elementos ao conjunto
            if elementos == '@':
                print()
                print('Você saiu do programa')
                print('/'*70)
                break

        print()
        print(f'Conjunto antes do CLEAR():  {conjunto3}')
        # Remove todos os elementos do conjunto
        conjunto3.clear()
        
        # Imprimi  "set()" ja que o conjunto está vazio
        print(f'Conjunto Depois do CLEAR():  {conjunto3}')
        print()
        break
    
print('-'*70)
print('Fim do Programa.')
print('-'*70)