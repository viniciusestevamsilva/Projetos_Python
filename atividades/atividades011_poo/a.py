# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os  # Importanto bibliotecas


class Conta():  # Criando a classe
    def __init__(self, a, b, c):  # Metodo construtor
        self.a = a
        self.b = b
        self.c = c

    # Metodos
    def soma(self, a, b, c):  # Função para somar
        soma = a + b + c
        return soma

    def multiplicar(self, a, b, c):  # Função para multiplicar

        multiplicar = a * b * c
        return multiplicar


while True:

    os.system('cls')
    print('/'*70)
    print('Multipicar e somar três valores')
    print('='*70)

    a = input('Digite o 1° valor: ')
    
    if a.isalpha() or a == '':
        os.system('cls')
        print('-'*70)
        print('Digite apenas números')
        input('Digite enter pra voltar')
        continue
    
    b = input('Digite o 2° valor: ')
    
    if b.isalpha() or b == '':
        os.system('cls')
        print('-'*70)
        print('Digite apenas números')
        input('Digite enter pra voltar')
        continue
    
    c = input('Digite o 3° valor: ')
    
    if c.isalpha() or c == '':
        os.system('cls')
        print('-'*70)
        print('Digite apenas números')
        input('Digite enter pra voltar')
        continue
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    resultado = Conta(a, b, c)  # Criando um objeto
    adicao = resultado.soma(a, b, c)
    vezes = resultado.multiplicar(a, b, c)
    
    opcao = str(input('Você deseja Somar ou multiplicar (s/m)?\n(caso queira sair digite, "n") ')).lower()
    
    if opcao == 'n':
        
        os.system('cls')
        
        print('Programa Finalizado')
        print('/'*70)
        break
    
    elif opcao.isnumeric() or opcao == '':
        
        print('-'*70)
        print('Digite algo valido')
        input('Digite enter pra voltar')
    else: 
        if opcao == 's':
        
            os.system('cls')

            print()
            print('-'*70)
            print('Resultados da conta:')
            print(f'A soma é: {adicao}')
            input('Digite enter pra continuar')
                
        elif opcao == 'm':
                
            os.system('cls')
                
            print('/'*70)
            print()
            print('-'*70)
            print('Resultados da conta:')
            print(f'A multiplicação é: {vezes}')
            print('/'*70)
            input('Digite enter pra continuar')
        else:
            print('/'*70)
            print('Opção inváida')
            input('Digite enter pra voltar')
