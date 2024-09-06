# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os


class Conta(): # Criando a classe
    def __init__(self, numero): # Metodo construtor
        self.numero = numero # Atributos
        
    def dobro(self, numero): # Metodo para calcular o dobro
        dobro = numero * 2
        return dobro
    
    
    def triplo(self, numero): # Metodo para calcular o triplo
        triplo = numero * 3
        return triplo

os.system('cls')
print('/'*70)
print('Insira o seu valor')
print('='*70)
numero = int(input('Coloque o numero aqui: '))

resposta = Conta(numero) # variavel recebendo a instancia da classe
x2 = resposta.dobro(numero) # Chamando o metodo 
x3 = resposta.triplo(numero) # Chamando o metodo 

print('-'*70)
print('')
print(f'O dobro de {numero} é {x2}')
print('')
print(f'O triplo de {numero} é {x3}')
print('')
print('/'*70)