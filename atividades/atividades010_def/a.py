# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 30/07/2024

# Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares,
# os números ímpares, a quantidade de números pares e a quantidade de números ímpares.


import os
import random

os.system('cls')


lista = [random.randint(0, 10) for i in range(10)]


def numeros(lista):
    """separando par e impar

    Args:
        lista (*list): lista de numeros

    Returns:
        lista: numeros pares e impares
    """    
    par = []
    impar = []
    
    for num in lista:
        if num % 2 == 0:
            pares = num
            par.append(pares)
            quantidade_p = len(par)
        else:
            impares = num
            impar.append(impares)
            quantidade_i = len(impar)
    par.sort()
    impar.sort()
    print(f'Pares : {par}\nQuantidade de números pares: {quantidade_p}')
    print(f'Impares: {impar}\nQuantidade de números impares: {quantidade_i}')
    return lista

numeros(lista)