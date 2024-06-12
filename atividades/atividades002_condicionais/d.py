# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 26/04/2024

# Iporta bibliotecas
import os


# Limpar terminal
os.system('cls')

# Entrada
print('-'*70)
print('Monitoramento de salarios')
print('='*70)

salario = float(input('Digite seu salario atual: '))


#processos
aumento1 = (5 / 100) * salario
aum1 = aumento1 + salario

aumento2 = (10 / 100) * salario
aum2 = aumento2 + salario

#Condicional
if salario >= 1500.00:
    print(f'seu salario recebeu um aumento de 5% {aum1}')
elif salario <= 1000.00:
    print(f'seu salario recebeu um aumento 5 $ {aum2}')
else:
    print(f'o salario {salario} esta errado')

