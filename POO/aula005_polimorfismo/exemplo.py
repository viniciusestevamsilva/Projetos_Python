from math import pi

# Define a classe base forma com um metodo area
# que não faz nada (e quase uma classe abstrata)


class Forma:
    def area(self):
        pass


# Define a classe Circulo que herda  de forma
#   o construtor __init__ inicializa o atributo raio
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    # Define o metodo area para calcular a area do
    # circulo usando a formula pi * raio2
    def area(self):
        return pi * (self.raio **2)


# Define a classe  retangulo que herda  dde forma
class Retangulo(Forma):
    def __init__(self, Largura, altura):
        self.largura = Largura
        self.altura = altura
    
    # Define o metodo area para calcular a area 
    # do retangulo usando a formula largura * altura
    def area(self):
        return self.largura * self.altura


# Define a classe quebrado que herda de rentangulo
class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
        
    
    # Define uma função exibir_area que aceite um
    # objeto forma e imprime sua area
    # metodo area ´é chamada no objeto forma
def exibir_area(forma):
    print(f'A area da forma é {forma.area()}')


# Cria instancias e Circulos, Retangulos e quadrado
circulo = Circulo(5)
retangulo = Retangulo(4, 6)
quadrado = Quadrado(3)

# Chama a função exibir_area para cada instancia
# O metodo area apropriado é chamado para
# cada  objeto, mostrando polimorfismo
exibir_area(circulo)
exibir_area(retangulo)
exibir_area(quadrado)    