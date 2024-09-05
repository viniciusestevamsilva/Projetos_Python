# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os


class Converter(): # criando a classe
    def __init__(self, real): # metodo construtor
        self.valor = real # atributos
        
    def compra_dol(self, real): # metodo para converter em reais
        dolar = real / 5.65
        
        return dolar

os.system('cls')

print('/'*70)
print('Converter o valor real em dolares')
print('='*70)
real = float(input('Coloque o valor da nota em REAL: '))

valor = Converter(real) # variavel recebendo a instancia de uma classe
resultado = valor.compra_dol(real) # Chamando o metodo 

print('/'*70)
print('')
print(f'{real} está valendo {resultado:.2f} em dolares')
print('')
print('/'*70)