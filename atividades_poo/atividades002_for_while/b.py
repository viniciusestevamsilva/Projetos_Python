# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os 


class Intervalo:
    def __init__(self, comeco, fim):
        self.comeo = comeco
        self.fim = fim


class Gerador(Intervalo):
    def __init__(self, comeco, fim):
        self.comeco = comeco
        self.fim = fim
        
    def de1a100(self, comeco, fim):

        inicio = comeco
        while inicio <= fim:
            print(f'numero: {inicio}', end=' | ')
            inicio += 1


os.system('cls')
print('/'*70)
print('Gerar numeros, digite o inicio eo fim do ciclo')
print('='*70)
inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
print('')
gerador = Gerador(inicio, final)
resultado = gerador.de1a100(inicio, final)
print('')
print('')
print('/'*70)