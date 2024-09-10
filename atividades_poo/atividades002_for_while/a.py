# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


class Intervalo:
    def __init__(self, comeco, fim):# Método construtor
        self.comeco = comeco  # Atributos
        self.fim = fim        

class Gerador(Intervalo):
    def __init__(self, comeco, fim):
        # Construtor da classe que inicializa os atributos
        self.comeco = comeco  
        self.fim = fim        

    def de1a100(self):
        inicio = self.comeco 
        while inicio <= self.fim:
            print(f'Número: {inicio}', end='  ')
            inicio += 1 
        print()


os.system('cls')

print('/' * 70)
print('Imprimir números de 1 a 100')
print('=' * 70)

# Cria uma instância da classe 
gerador = Gerador(1, 100)
# Chama o método 
gerador.de1a100()

print('/' * 70)