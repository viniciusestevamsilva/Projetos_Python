# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024

import os


class Palindromo:
    def __init__(self, palindromo):
        self.palindromo = palindromo
        
class Invertido(Palindromo):
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

# Entrada
print('/'*70)
print('Verificando se é palindromo ou não')
print('='*70)

frase = str(input('Digite uma palavra ou frase: '))

# Transformando em minusculo
Palindromo = Invertido.verificando(frase)