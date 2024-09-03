# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data //
import os

#Limpar terminal

class Quociente():
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
        
    def resultado(self, dividendo, divisor):
        quociente = dividendo / divisor
        
        return quociente
    

os.system('cls')

print('='*70)
print('Insira os numeros')
print('='*70)

# Entrada
dividendo = float(input('Coloque o dividendo: '))
divisor = float(input('Coloque o divisor: '))

resultado = Quociente(dividendo, divisor)
resto = resultado.resultado(dividendo, divisor)

# Saida
print('')
print('='*70)
print('Resultado final')
print('='*70)
print(f'A divisao dos valores é: {resto:.4f}')
print('')