# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


class Intervalo:
    def __init__(self, comeco, fim):
        self.comeo = comeco
        self.fim = fim


class Gerador(Intervalo):

    def de1a100(self, comeco, fim):

        inicio = comeco
        while inicio <= fim:
            print(f'numero: {inicio}', end='  ')
            inicio += 1
            


os.system('cls')
print('/'*70)
print('Imprimir numeros de 1 a 100')
print('='*70)

gerador = Gerador(1, 100)
resultado = gerador.de1a100(1, 100)
print('')
print('/'*70)