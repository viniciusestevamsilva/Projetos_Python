# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 25/04/2024

# Iporta bibliotecas
import os


# Limpar terminal
os.system('cls')

# Entrada
print('-'*70)
print('Analise de Estatistica')
print('='*70)

nu1 = float(input('Insira seu primeiro numero: '))
nu2 = float(input('Insira seu segundo numero: '))
nu3 = float(input('Insira seu terceiro numero: '))


# Maior
if nu1 > nu2 and nu1 > nu3:
    maior = nu1
elif nu2 > nu1 and nu2 > nu3:
    maior = nu2
else:
    maior = nu3
    
# Menor
if nu1 < nu2 and nu1 < nu3:
    menor = nu1
elif nu2 < nu1 and nu2 < nu3:
    menor = nu2
else:
    menor = nu3


#igual
if nu1 == nu2 == nu3:
    print('Todos sao iguais')
else:
    print(f'o numero {maior} e o maior e o {menor} e o menor')

# Saida
print('-'*70)
print('Final do programa')
print('-'*70)