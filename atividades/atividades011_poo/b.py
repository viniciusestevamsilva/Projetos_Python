# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data //
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
nascimento = int(input('Data de nascimento: '))
data = Data(nascimento)

print('-'*70)
print()
print('Resultado')
print(f'voce tem {data.idade(nascimento)} de anos')
print('='*70)