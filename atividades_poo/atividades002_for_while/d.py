# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


class Pares:
    def __init__(self ,numero):
        self.numero = numero

class Num_pares(Pares):
    def conta(self):
        
        while (contador <= 100):
        
            contador += 1 
            
            if (contador % 2 == 0): 
                print(f'numero par:{contador}')
        
    

os.system('cls')

print('/'*70)
print('Imprimindo Números somente pares entre 0 e 100')
print('='*70) 

par = Num_pares.conta()

print('/'*70)