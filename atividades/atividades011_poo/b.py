# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os
import datetime


class Data():
    def __init__(self, data_nascimento):
        self.data_nascimento = data_nascimento
        
    def idade(self, data_nascimento):
        self._data_nascimento = data_nascimento
        ano_atual = datetime.datetime.now().year
        idade = int(ano_atual) - data_nascimento
        
        return idade
    

os.system('cls')

print('/'*70)
print('Mostrar sua idade(ano)')
print('='*70)
nascimento = int(input('Sua data de nascimento: '))
data = Data(nascimento)

os.system('cls')
    
print('-'*70)
print()
print('Resultado')
print(f'voce tem {data.idade(nascimento)} de anos')
print('/'*70)