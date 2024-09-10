# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os
#imcompleta

class Numeros:
    def __init__(self, comeco):
        self.comeco = comeco
        
        
    def enunciado(self):
        print('/'*70)
        print('Imprimir de 0 a 100 somente numeros impares')
        print('='*70)
    
    def contador(self):
        pass
        
        
class Impar(Numeros):
    def __init__(self, comeco):
        self.comeco = comeco
        
        
    def contador(self):
        soma = 0
        quantidade = 0
        
        for i in range(int(self.comeco), 100):
            if (i % 2 != 0):
                print(f'{i}', end= '   ')
                soma += i
                quantidade += 1
        return soma, quantidade

            
os.system('cls')
    

enunciado = print
enunciado = Numeros.enunciado(enunciado)
comeco = input('Digite o valor inicial do intervalo: ')
qualquer = Impar(comeco)
soma, quatidade = Impar.contador(comeco)
print()
print(soma, quatidade)