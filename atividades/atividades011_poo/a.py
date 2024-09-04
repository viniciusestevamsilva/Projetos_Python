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
    b = input('Digite o 2° valor: ')
    c = input('Digite o 3° valor: ')
    
    
    resultado = Conta(a, b, c)  # Criando um objeto

    opcao = str(input('Você deseja Somar ou multiplicar? ')).lower()
    if opcao == 'somar':
            
        soma = resultado.soma(a,b,c)
            
        os.system('cls')

        print()
        print('-'*70)
        print('Resultados da conta:')
        print(f'A soma é: {soma}')
        print('/'*70)
        input('Digite enter pra voltar')
            
    elif opcao == 'multiplicar':
        multiplicar = resultado.multiplicar(a,b,c)
            
        os.system('cls')
            
        print('/'*70)
        print()
        print('-'*70)
        print('Resultados da conta:')
        print(f'A multiplicação é: {multiplicar}')
        print('/'*70)
        input('Digite enter pra voltar')
    else:

        print('Opção inváida')
        input('Digite enter pra voltar')
            
    os.system('cls')
    print('/'*70)
    continuar = input('Deseja continuar ou sair do programa (s/n)? ').lower()
    print('='*70)
    if continuar == 'n':
        os.system('cls')
        print('Programa Finalizado')
        print('/'*70)
        break
    else:

        print('Opção inváida')
        input('Digite enter pra voltar')