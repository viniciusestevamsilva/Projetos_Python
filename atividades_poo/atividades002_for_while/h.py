# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


import os

class Ignorando: # classe pai
    def __init__(self, ignorado1, ignorado2, ignorado3):   # Método construtor
        self.ignorado1 = int(ignorado1)  # Atributos
        self.ignorado2 = int(ignorado2)
        self.ignorado3 = int(ignorado3)

    def enunciado(self):
        
        print('/' * 70)
        print('3 Números serão ignorados')
        print('=' * 70)

class Numeros(Ignorando): # classe filha
    
    def separador(self, comeco, final):
        print('=' * 70)
        
        self.contador = comeco
        
        while self.contador <= final:
            
            if self.contador != self.ignorado1 and self.contador != self.ignorado2 and self.contador != self.ignorado3:
                print(f'{self.contador}', end=' ')
            self.contador += 1
            
        print()
        print('/' * 70)

# Clear screen based on OS
os.system('cls' if os.name == 'nt' else 'clear')


ignorando = Ignorando(0, 0, 0)  # Cria uma instância da classe 
ignorando.enunciado()  # Chama o método

# Input numbers
comeco = int(input("Digite o número do começo do intervalo: "))
final = int(input("Digite o número final do intervalo: "))
ignorado1 = int(input("Digite o 1º que será ignorado: "))
ignorado2 = int(input("Digite o 2º que será ignorado: "))
ignorado3 = int(input("Digite o 3º que será ignorado: "))

# Create an instance of Numeros and call separador
ignorados = Numeros(ignorado1, ignorado2, ignorado3)
ignorados.separador(comeco, final)