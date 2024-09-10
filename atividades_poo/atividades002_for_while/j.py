# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os
#imcompleta

class Numeros:
    def __init__(self, comeco):
        self.comeco = int(comeco)
        
    def enunciado(self):
        print('/'*70)
        print('Imprimir de 0 a 100 somente numeros impares')
        print('='*70)
        
        
class Impar(Numeros):
    def contador(self):
        comeco = 1 
        
        while (comeco <= 100):
            
            comeco += 1
            if (comeco % 2 != 0):
                print(f'{comeco}', end= '   ')


            
os.system('cls')
    

enunciado = print
enunciado = Numeros.enunciado(enunciado)
comeco = int
contagem = Impar.contador(comeco)