# Curso de Desenvolvimento de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 29/04/2024

# Importa bibliotecas
import os
 
# Limpar terminal
os.system('cls')

print('-'*70)
print('Verificação de passagem de onbius')
print('='*70)

# Entada
distancia = float(input('Quantos km é sua viagem: '))
resultado = ''

a = distancia * 0.70
b = distancia * 0.40

if distancia > 200:
    resultado = f'o valor total a pagar sera {a}'
else:
    resultado = f'o valor total a pagar sera {b}'
    

print('-'*70)
print(f'{resultado}')
print('-'*70)
print('')