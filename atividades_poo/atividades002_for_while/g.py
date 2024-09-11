# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os



class Numeros:
    def __init__(self, inicio, final):  # Método construtor
        self.inicio = inicio # Atributos
        self.final = final
        
class Primos(Numeros):
    def calcular_primos(self):
        primos = []
        for numero_primo in range(self.inicio, self.final + 1):
            if numero_primo > 1:
                for divisor in range(2, int(numero_primo**0.5) + 1):
                    if numero_primo % divisor == 0:
                        break
                else:
                    primos.append(numero_primo)
        return primos

os.system('cls')

print('/'*70)
inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
print('='*70)


resultados = Primos(inicio, final) # Cria uma instância da classe 
primos = resultados.calcular_primos() # Chama o método

print(f'Números primos entre {inicio} e {final}:')
for primo in primos:
    print(primo)
