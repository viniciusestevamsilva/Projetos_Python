# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os



class Intervalo:
    def __init__(self, inicio, final): # Método construtor
        self.inicio = inicio # Atributos
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
print('/'*70)
print('Somar a quantidade de números pares\nencontrados no intervalo entre 0 e 100.')
print('='*70)
print()
resultados = Pares(0, 100)# Cria uma instância da classe 
pares = resultados.par(0, 100)# Chama o método