# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 30/07/2024

# Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares,
# os números ímpares, a quantidade de números pares e a quantidade de números ímpares.
# Faça um programa para criar um dicionário com 4 elementos.

import os


os.system('cls')


lista = [0,1,2,3,4,5,6,7,8,9]
# pares = [0, 2, 4, 6, 8]
# impares = [1, 3, 5, 7, 9]


def par_impar(lista):
    """separanod par e impar

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

    print(f'Pares : {par}')
    print(f'Quantidade de pares: {quantidade_p}')
    print(f'Impares: {impar}')
    print(f'Quantidade de impares: {quantidade_i}')
    return lista

par_impar(lista)