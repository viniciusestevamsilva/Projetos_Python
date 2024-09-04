# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os

class Tabuada:
    def __init__(self, valor):
        self.valor = valor
        
    def multiplicar(self, valor):
        for c in range(1,11):
            resultado = valor*c
            print(f'{valor} x {c} = {resultado}')
            
        return resultado
        
while True:
        os.system('cls')
        print('/'*70)
        print('')
        valor = int(input('Digite o numero que deseja ver a tabuada: '))
        
        if valor <= 0:
            print('Digite um valor valido')
            input('Enter para voltar')
            os.system('cls')
        else:    
            print('')
            print(f'Tabuada do {valor} ate 10')
            print('='*70)
            resposta = Tabuada(valor)
            resto = resposta.multiplicar(valor)
            print('')
            print('/'*70)
