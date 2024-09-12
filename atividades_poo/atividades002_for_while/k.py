# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024

import os


class Palindromo: # Classe Pai
    def __init__(self, palindromo): # Metodo construtor
        self.palindromo = palindromo # Atributos
        
class Invertido(Palindromo): # Classe Filha
    def verificando(self):
        
        if frase == frase[::-1]:
            print('')
            print(f'A frase "{frase}" é um palíndromo.')
            print('')
            print('/'*70)
        else:
            print('')
            print(f'A frase "{frase}"não é um palíndromo.')
            print('')
            print('/'*70)

os.system('cls')


print('/'*70)
print('Verificando se é palindromo ou não')
print('='*70)

frase = str(input('Digite uma palavra ou frase: '))

Palindromo = Invertido.verificando(frase)# Cria uma instância da classe 