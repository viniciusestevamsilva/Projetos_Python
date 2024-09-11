# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024

import os

class Intervalo:
    def __init__(self, comeco, fim):
        # Método construtor
        self.comeo = comeco # Atributos
        self.fim = fim


class Invertido(Intervalo):
    def __init__(self, comeco, fim):
        # Construtor da classe que inicializa os atributos
        self.comeco = comeco
        self.fim = fim
        
    def inverso(self, comeco, fim):

        final = fim
        while final >= comeco:
            print(f'{final}', end='  ')
            final -= 1
            


os.system('cls')
print('/'*70)
print('Imprimir numeros de 1 a 10\nem ordem reversa')
print('='*70)

# Cria uma instância da classe
gerador = Invertido(1, 10)
resultado = gerador.inverso(1, 10) # Chama o método
print('')
print('/'*70)