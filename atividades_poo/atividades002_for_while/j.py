# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os


class Numeros: # Classe pai
    def __init__(self, comeco): # Metodo construtor
        self.comeco = comeco  # Atributos
        
    def enunciado(self):
        print('/' * 70)
        print('Imprimir de 0 a 100 somente números ímpares')
        print('=' * 70)
    
    def contador(self):
        pass

class Impar(Numeros): # Classe filha
    def __init__(self, comeco):
        Numeros.__init__(self, comeco)  # Iniciando a classe diretamente

    def contador(self):
        soma = 0
        quantidade = 0
        
        for i in range(self.comeco, 101): 
            if i % 2 != 0:
                print(f'{i}', end='   ')
                soma += i
                quantidade += 1
        return soma, quantidade


os.system('cls')

numeros = Numeros(0)
numeros.enunciado()


comeco = 1


impar = Impar(comeco)  # Cria uma instância da classe 
soma, quantidade = impar.contador()  # Chama o método
print()
print(f'\nSoma dos números ímpares: {soma}')
print(f'Quantidade de números ímpares: {quantidade}')
print('/' * 70)
