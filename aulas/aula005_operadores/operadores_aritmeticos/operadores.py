# import
import os

# limpar o terminal
os.system('cls')

print('-'*70)
print('OPERADORES ARTIMETICOS')
print('-'*70)

# Entrada de dados
print('--- SOMA')
print('-'*70)
parcela_1 = float(input('Entre com a 1 parcela: '))
parcela_2 = float(input('Entre com a 2 parcela: '))

print()
print('--- SUBTRACAO')
print('-'*70)
minuendo = float(input('Entre com o minuendo: '))
subtraendo = float(input('Entre com o subtraendo: '))

print()
print('--- PRODUTO')
print('-'*70)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print()
print('--- DIVISÃO')
print('-'*70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

# Procesamento 
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor

# Saída 
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} ÷ {divisor} é: {quociente}' )

# Seguindo os passos anteriores, desenvolva o restante
# Acrecente a raiz quadrada e a raiz cúbica.