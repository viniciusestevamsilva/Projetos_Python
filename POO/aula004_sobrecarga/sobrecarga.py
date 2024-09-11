# Sobrecarrega de metodos

class ClassePai: # Super classe
    # Metodo Construtor
    def __init__(self, a,b):
        self.a = a
        self.b = b
    
    # Para sobrecarregar 
    # Vai ser usada para a soma 2 numeros
    def metodo_classe(self, a, b):
        pass


class ClasseFilha: #Classe derivada 
    # Metodo construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    #sobrecarga de metodo
    def metodo_classe(self):
        return self.a + self.b


# Programa principal
teste = ClasseFilha(1, 2)
teste.metodo_classe()