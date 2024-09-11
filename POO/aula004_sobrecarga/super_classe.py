class ClassePai: # Super classe
    # Metdo construtor
    def __init__(self, a,b):
        self.a = a
        self.b = b
    
    # Metodo que vai ser sobrecarregado
    def metodo_classe(self):
        print('Aqui vou multiplicar a e b!')
        resultado = self.a + self.b
        print(f'Este calculo esta sendo realizado')
        print(f'pelo Metodo classe Pai!')
        print(f'O resultado da soma de {self.a} e {self.b} = {resultado}')


class ClasseFilha(ClassePai): # Classe derivada
    # Metodo construtor
    def __init__(self, a, b):
        super().__init__(a, b) # chama o construtor da classe pai
        # não é nescessario redefinir a variavel self.a e self.b,
        # pois ja foram inicializadas pelo construtor da classe pai
    
    # Sobrecarga de metodo
    def metodo_classe(self):
        # Primeiro, executo o metodo classe pai
        super().metodo_classe()
        # Depois , executa o metodo da classe filha
        resultado = self.a + self.b
        print(f'O resultado da soma na Classe Filha é: {resultado}')


# Programa principal
teste = ClasseFilha(1, 2)
teste.metodo_classe()