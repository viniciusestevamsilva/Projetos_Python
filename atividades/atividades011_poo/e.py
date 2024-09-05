# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os


class Sucessor_anterior(): # Criando a classe
    def __init__(self, numero): # Metodo construtor
        self.numero = numero
        
    def resultado_sucessor(self, numero): # Metodo para o sucessor
        sucessor = numero + 1
        
        return sucessor
    
    
    def resultado_anterior(self, numero): # metodo para o antecessor
        antecessor = numero - 1
        
        return antecessor
        
    
    
os.system('cls')
print('-'*70)
print('Coloque um numero')
print('-'*70)
numero = int(input('Digite um numero: '))

resposta = Sucessor_anterior(numero) # Variavle recebdno a instancia da classe
sucessor = resposta.resultado_sucessor(numero)
anterior = resposta.resultado_anterior(numero)

print('')
print('-'*70)
print(f'o sucessor do {numero} é {sucessor} e o antecessor é {anterior}')
print('-'*70)
print('')