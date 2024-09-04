# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os

class Converter():
    def __init__(self, metro):
        self.metro = metro
        
    def metro_centimetro(self, metro):
        centimetro = metro*100
        return centimetro
        
    def metro_milimetro(self, metro):
        milimetro = metro*1000
        return milimetro

os.system('cls')
print('/'*70)
print('Converter centimetros para metros e\nMilimetros para metros')
print('='*70)
metro = int(input('Coloque o numero em metros: '))

convercao = Converter(metro)
cm = convercao.metro_centimetro(metro)
ml = convercao.metro_milimetro(metro)

print('='*70)
print(f'A converção de {metro} metros para milimetro é {cm}')
print('')
print(f'A converção de {metro} metros para milimetro é {ml}')
print('')
print('/'*70)