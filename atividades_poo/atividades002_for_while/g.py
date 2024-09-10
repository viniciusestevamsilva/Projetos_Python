# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os



class Numeros:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
class Primos(Numeros):
    def par(self,inicio, final):
        
        inicio = 3
        fim = 100
        contador = inicio
        
        for numero_primo in range(contador, fim):
            for divisor in range(2, int(numero_primo**0.5) + 1):
                if numero_primo % divisor == 0:
                    break
            else:
                print(f'{numero_primo}', end=" | ")

os.system('cls')
print('/'*70)
inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
print('='*70)

resultados = Primos(inicio,final)
impar = resultados.par(inicio,final)