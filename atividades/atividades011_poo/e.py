# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os

class Sucessor_anterior():
    def __init__(self, numero):
        self.numero = numero
        
    def resultado_sucessor(self, numero):
        sucessor = numero + 1
        
        return sucessor
    
    
    def resultado_anterior(self, numero):
        antecessor = numero - 1
        
        return antecessor
        
    
    
os.system('cls')
print('-'*70)
print('Coloque um numero')
print('-'*70)
numero = int(input('Digite um numero: '))

resposta = Sucessor_anterior(numero)
sucessor = resposta.resultado_sucessor(numero)
anterior = resposta.resultado_anterior(numero)

print('')
print('-'*70)
print(f'o sucessor do {numero} é {sucessor} e o antecessor é {anterior}')
print('-'*70)
print('')