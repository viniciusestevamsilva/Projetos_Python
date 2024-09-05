# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os


class Quociente(): # Criando a classe
    def __init__(self, dividendo, divisor): # metodo construtor
        self.dividendo = dividendo # atributos
        self.divisor = divisor
        
    def resultado(self, dividendo, divisor): # metodo para calcular
        quociente = dividendo / divisor
        
        return quociente
    

os.system('cls')

print('='*70)
print('Insira os numeros')
print('='*70)

# Entrada
dividendo = float(input('Coloque o dividendo: '))
divisor = float(input('Coloque o divisor: '))

resultado = Quociente(dividendo, divisor)# variavel recebendo a instancia da classe
resto = resultado.resultado(dividendo, divisor) # Chamando o metodo 

# Saida
print('')
print('='*70)
print('Resultado final')
print('='*70)
print(f'A divisao dos valores é: {resto:.4f}')
print('')