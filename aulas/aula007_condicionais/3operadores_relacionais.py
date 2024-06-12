# Curso de desenvolbimento de sistemas
# Turma 0152
# Data 25/04/2024
# Autor: Vinícius Estevam da Silva
# Estudo de condicionais: Parte 3
# Operadores relacionais

import os


os.system('cls')

a = 10
b = 5
c = 'José'
d = 'José'

print('-'*70)
print('Condicionais: Operadores Relacionados')
print('='*70)

# Igualdade (==)
if c == d:
    print('-'*70)
    print(f' {c} é igual a {d}')
    print('='*70)
else:
    print(f' {c} é diferente de {d}')

# Diferença
if a != c:
    print('-'*70)
    print(f' {a} é diferente de {c}')
    print('='*70)
else:
    print(f' {a} não é diferente de {c}')

# Maior que (>)
if a > b:
    print('-'*70)
    print(f' {a} é maior que {b}')
    print('='*70)
else:
    print(f' {a} não é maior que {b}')

# Menor que (<)
if b < a:
    print('-'*70)
    print(f' {b} é menor que {a}')
    print('='*70)
else:
    print(f' {b} não é menor que {a}')

# Maior ou igual a (>=)
if a >= b:
    print('-'*70)
    print(f' {a} é maior ou igual a {b}')
    print('='*70)
else:
    print(f' {a} não é maior ou igual a {b}')

# Menor ou igual a (<=)
if b <= a:
    print('-'*70)
    print(f' {b} é menor ou igual {a}')
    print('='*70)
else:
    print(f' {b} não menor ou igual a {a}')
    
print('Fim do Programa!')
print('-'*70)
print()