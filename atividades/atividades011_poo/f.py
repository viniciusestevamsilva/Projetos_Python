# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os

class Conta():
    def __init__(self, numero):
        self.numero = numero
        
    def dobro(self, numero):
        dobro = numero * 2
        return dobro
    
    
    def triplo(self, numero):
        triplo = numero * 3
        return triplo

os.system('cls')
print('/'*70)
print('Insira o seu valor')
print('='*70)
numero = int(input('Coloque o numero aqui: '))

resposta = Conta(numero)
x2 = resposta.dobro(numero)
x3 = resposta.triplo(numero)

print('-'*70)
print('')
print(f'O dobro de {numero} é {x2}')
print('')
print(f'O triplo de {numero} é {x3}')
print('')
print('/'*70)