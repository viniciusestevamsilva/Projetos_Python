# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


class Pares:
    def __init__(self):
        # Inicializa com valores padrão
        self.numero = 0
        self.numero_final = 100

    def processa(self):
        # Método base que pode ser sobrescrito
        pass

class Num_pares(Pares):
    def __init__(self, numero_inicial, numero_final):
        # Inicializa com valores padrão e configura os atributos
        self.numero = numero_inicial
        self.numero_final = numero_final

    def conta(self):
        # Contar e imprimir números pares entre numero e numero_final
        while self.numero <= self.numero_final:
            if self.numero % 2 == 0:
                print(f'Número par: {self.numero}')
            self.numero += 1

# Limpa a tela
os.system('cls')

print('/' * 70)
print('Imprimindo Números somente pares entre 0 e 100')
print('=' * 70) 

# Cria uma instância da classe Num_pares
par = Num_pares(0, 100)  # Inicializa com o número inicial e final

# Conta e imprime os números pares
par.conta()

print('/' * 70)

