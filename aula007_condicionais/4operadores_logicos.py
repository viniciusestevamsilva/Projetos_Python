# Curso de desenvolbimento de sistemas
# Turma 0152
# Data 25/04/2024
# Autor: Vinícius Estevam da Silva
# Estudo de condicionais: Parte 4
# Operadores logicos

#Importando Bibliotecas
import os


# Limpando terminal
os.system('cls')

# Declaração
a = 10
b = 5
c = 'Jonh'

print('-'*70)
print('Condicionias: Operadores logicos')
print('='*70)

# E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco falso')

print('.'*70)

# E (and) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('.'*70)

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('.'*70)

# OU (or) FALSO
print('OU (or) FALSO')
if (a > 5 or c == 'Jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('-'*70)
print()