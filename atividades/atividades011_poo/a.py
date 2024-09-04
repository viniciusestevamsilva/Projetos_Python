# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os


class Conta():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def soma(self, a, b, c):
        soma = a + b + c
        return soma
        
    def multiplicar(self, a, b, c):
        
        multiplicar = a * b * c
        return multiplicar
        
while True:
    
    os.system('cls')
    print('-'*70)
    print('Multipicar e somar três valores')
    print('='*70)
    a = float(input('Digite o 1° valor: '))
    b = float(input('Digite o 2° valor: '))
    c = float(input('Digite o 3° valor: '))
    
    resultado = Conta(a,b,c)

    print()
    print('-'*70)
    print('Resultados da conta:')
    print(f'A soma é: {resultado.soma(a,b,c)}')
    print(f'A multiplicação é: {resultado.multiplicar(a,b,c)}')
    print('='*70)
