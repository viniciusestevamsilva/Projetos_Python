import os


os.system('cls')

class Intervalo:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
class Pares(Intervalo):
    def descobrir_par(self,inicio, final):
        
        contador = inicio
        soma = 0
        for contador in range(final + 1):
            contador += 1 
            
            if (contador % 2 == 0): 
                print(f'{contador}', end= ' | ')
                soma += contador 
        print()
        print(f'Soma dos pares: {soma}')
        
resultados = Pares(0,100)
numeros_pares = resultados.descobrir_par(0,100)