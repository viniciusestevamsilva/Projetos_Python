# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os
  # Importando o módulo os

class Numeros:
    def __init__(self, comeco):
        self.comeco = comeco  # O parâmetro comeco já deve ser um inteiro
        
    def enunciado(self):
        print('/' * 70)
        print('Imprimir de 0 a 100 somente números ímpares')
        print('=' * 70)
    
    def contador(self):
        pass

class Impar(Numeros):
    def __init__(self, comeco):
        Numeros.__init__(self, comeco)  # Inicializando a classe base diretamente

    def contador(self):
        soma = 0
        quantidade = 0
        
        for i in range(self.comeco, 101):  # Mudança para 101 para incluir 100, se necessário
            if i % 2 != 0:
                print(f'{i}', end='   ')
                soma += i
                quantidade += 1
        return soma, quantidade

# Limpa a tela
os.system('cls')

# Exibe o enunciado
numeros = Numeros(0)
numeros.enunciado()

# Obtém o valor inicial do intervalo
comeco = 1

# Cria uma instância da classe Impar
impar = Impar(comeco)

# Calcula e imprime a soma e a quantidade de números ímpares
soma, quantidade = impar.contador()
print()
print(f'\nSoma dos números ímpares: {soma}')
print(f'Quantidade de números ímpares: {quantidade}')
print('/' * 70)
