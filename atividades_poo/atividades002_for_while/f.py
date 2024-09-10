# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os



class Numeros:
    def __init__(self, inicio):
        self.inicio = inicio

        
class Primos(Numeros):
    def par(self,inicio):
        
        inicio = 3
        fim = 100
        contador = inicio
        
        for primo in range(contador, fim):
            for divisor in range(2, int(primo**0.5) + 1):
                if primo % divisor == 0:
                    break
            else:
                print(f'{primo}', end=" | ")
    print('/'*70)
 
os.system('cls')

resultado = Primos(0,100)
impar = resultado.par(0,100)