# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


class Intervalo:
    def __init__(self, comeco, fim):
        self.comeo = comeco
        self.fim = fim
    
    def gerador(self, comeco, fim):
        comeco = 1
        fim = 100
        while comeco <= fim:
            print(f'numero: {comeco}', end=' | ')
            comeco += 1

os.system('cls')
print('-'*70)
print('Mesma coisa de antes com input')
print('='*70) 

comeco = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))

gerador = Intervalo(comeco, fim)
resultado =  gerador.gerador(comeco, fim)
print('-'*70)