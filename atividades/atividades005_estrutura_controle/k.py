# Curso de Desenvolvimento de sistemas
# Autro : Vinícius Estevam da Silva
# Data 05/06/2024
#Crie um programa que pede que o usuário digite um nome ou uma frase,
#verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.
#Importando biblioteca
import os


os.system('cls')

# Entrada
print('-'*70)
print('É palíndromo')
print('-'*70)

frase = str(input('Digite uma palavra ou frase: '))

# Transformando em minusculo
frase = frase.lower()

# Validação
if frase == frase[::-1]:
    print('-'*70)
    print(f'A frase "{frase}" é um palíndromo.')
    print('-'*70)
else:
    print('-'*70)
    print(f'A frase "{frase}"não é um palíndromo.')
    print('-'*70)