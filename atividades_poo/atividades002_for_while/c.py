# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024

import os

class Intervalo:
    def __init__(self, comeco, fim):
        self.comeo = comeco
        self.fim = fim


class Invertido(Intervalo):
    def __init__(self, comeco, fim):
        self.comeco = comeco
        self.fim = fim
        
    def inverso(self, comeco, fim):

        final = fim
        while final >= comeco:
            print(f'numero: {final}', end='  ')
            final -= 1
            


os.system('cls')
print('/'*70)
print('Imprimir numeros de 1 a 100')
print('='*70)

gerador = Invertido(0, 10)
resultado = gerador.inverso(0, 10)
print('')
print('/'*70)