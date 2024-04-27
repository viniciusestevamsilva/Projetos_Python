# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 26/04/2024

# Importa bibliotecas
import os
 
# Limpar terminal
os.system('cls')

print('-'*70)
print('Verificção de ano bissexto')
print('='*70)

# Entrada
ano = int(input('Digite o ano que quer verificar se é bissexto: '))

# Condicionais
if ano % 4 == 0 and ( ano % 100 != 0 or ano % 400 == 0):
    resposta = f'O ano {ano} é bissexto'
else:
    resposta = f'0 Ano {ano} não é bissexto'

# Saida
print('-'*70)
print(f'{resposta}')
print('-'*70)
print('')