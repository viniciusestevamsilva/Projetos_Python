import os


os.system('cls')

class Intervalo:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
class Primos(Intervalo):
    def descobrir_par(self,inicio, final):
        
        inicio = 3
        fim = 100
        contador = inicio
        
        for numero_primo in range(contador, fim):
            for divisor in range(2, int(numero_primo**0.5) + 1):
                if numero_primo % divisor == 0:
                    break
            else:
                print(f'{numero_primo}', end=" | ")
 
inicio = int(input('Digite o valor inicial do intervalo: '))
final = int(input('Digite o valor final do intervalo: '))
print('-'*70)

resultados = Primos(inicio,final)
numeros_impares = resultados.descobrir_par(inicio,final)