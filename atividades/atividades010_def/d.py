# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 30/07/2024

# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.
import os


os.system('cls')

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)

print(f'{temperatura_fahrenheit}° Fahrenheit equivalem a {temperatura_celsius:.2f}° Celsius.')