# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os


class Converter():# Criando a classe
    def __init__(self, metro): # metodo construtor
        self.metro = metro # atributos
        
    def metro_centimetro(self, metro): # Metodo para converter em centimetros
        centimetro = metro*100
        return centimetro
        
    def metro_milimetro(self, metro):# Metodo para converter em milimetros
        milimetro = metro*1000
        return milimetro

while True:
    
    os.system('cls')
    
    print('/'*70)
    print('Converter centimetros para metros e\n Milimetros para metros')
    print('='*70)
    metro = int(input('Coloque o numero em metros: '))
    convercao = Converter(metro) # variavel recebendo a instancia da classe
    opcao = input('Deseja converter para milimetros(ml)\n ou centimetros(cm?')

    
    if opcao.isnumeric() or opcao == '':
        print('Digite algo valido')
        input('Pressioe enter para voltar')
        
    if opcao == 'cm':
        
        cm = convercao.metro_centimetro(metro) # Chamando o metodo 
        
        os.system('cls')
        
        print('='*70)
        print(f'A converção de {metro} metros para milimetro é {cm}')
        print('')
        input('Pressioe enter para voltar')
        
    elif opcao == 'ml':
        
        ml = convercao.metro_milimetro(metro)# Chamando o metodo 
        
        os.system('cls')
        
        print(f'A converção de {metro} metros para milimetro é {ml}')
        print('')
        print('/'*70)
        input('Pressioe enter para voltar')
    else:
        print('Coloque algo valido')
        input('Pressioe enter para voltar')