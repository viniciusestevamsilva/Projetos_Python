# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


class Pares:
    def __init__(self):
        # Método construtor
        self.numero = 0 # Atributos
        self.numero_final = 100

    def processa(self):
        pass

class Num_pares(Pares):
    def __init__(self, numero_inicial, numero_final):
        # Construtor da classe que inicializa os atributos
        self.numero = numero_inicial
        self.numero_final = numero_final

    def conta(self):
        while self.numero <= self.numero_final:
            if self.numero % 2 == 0:
                print(f'Número par: {self.numero}')
            self.numero += 1

# Limpa a tela
os.system('cls')

print('/' * 70)
print('Imprimindo Números somente pares entre 0 e 100')
print('=' * 70) 

# Cria uma instância da classe 
par = Num_pares(0, 100) 

par.conta()# Chama o método

print('/' * 70)