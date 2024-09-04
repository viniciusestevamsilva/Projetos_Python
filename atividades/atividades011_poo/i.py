# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os


class Converter():
    def __init__(self, real):
        self.valor = real
        
    def compra_dol(self, real):
        dolar = real / 5.65
        
        return dolar

os.system('cls')

print('/'*70)
print('Converter o valor real em dolares')
print('='*70)
real = float(input('Coloque o valor da nota em REAL: '))

valor = Converter(real)
resultado = valor.compra_dol(real)

print('/'*70)
print('')
print(f'{real} está valendo {resultado:.2f} em dolares')
print('')
print('/'*70)