# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os



class Intervalo:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
class Pares(Intervalo):
    def par(self,inicio, final):
        
        contador = inicio
        soma = 0
        for contador in range(final + 1):
            contador += 1 
            
            if (contador % 2 == 0): 
                print(f'{contador}', end= ' | ')
                soma += contador 
        print()
        print(f'Soma dos pares: {soma}')
        print('/'*70)
     
     
os.system('cls')   
resultados = Pares(0, 100)
pares = resultados.par(0, 100)