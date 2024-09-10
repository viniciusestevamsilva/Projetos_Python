# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


class Ignorando:
    def __init__(self, ignorado1, ignorado2, ignorado3):
        self.ignorado1 = int(ignorado1)
        self.ignorado2 = int(ignorado2)
        self.ignorado3 = int(ignorado3)

    def enunciado(self):
        print('/'*70)
        print('3 Números seram ignorado')
        print('='*70)
        
    
    def contador(self, contador):
        self.contador = contador
        
        contador = 0
        pass

class Numeros(Ignorando):
    def separador(self, ignorado1, ignorado2, ignorado3):
        
        self.contador = comeco
        print('='*70)
        while self.contador <= final:
        # Ignora os números que o usuario digitou
            if self.contador != ignorado1 and self.contador != ignorado2 and self.contador != ignorado3:
                print(f'{self.contador}', end= ' ')
            self.contador += 1
            print('/'*70)

os.system('cls')
enunciado = print
enunciado = Ignorando.enunciado(enunciado)

comeco = int(input("Digite o numero do começo do intervalo: "))
final = int(input("Digite o numero final do intervalo: "))
ignorado1 = int(input("Digite o 1º que sera ignorado: "))
ignorado2 = int(input("Digite o 2º que sera ignorado: "))
ignorado3 = int(input("Digite o 3º que sera ignorado: "))

ignorados = Numeros(ignorado1, ignorado2, ignorado3)
resultado = ignorados.separador(ignorado1, ignorado2, ignorado3)