# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os

class Media():
    def __init__(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        
    def resultado_media(self, nota1, nota2, nota3, nota4):
        media_geral = (nota1 + nota2 + nota3 + nota4) / 4
        
        return media_geral
        

os.system('cls')   
 
print('-'*70)
print('Soma de Notas')
print('-'*70)
nota1 = float(input('Digite a 1 °nota: '))
nota2 = float(input('Digite a 2° nota: '))
nota3 = float(input('Digite a 3° nota: '))
nota4 = float(input('Digite a 4° nota: '))


resultado = Media(nota1, nota2, nota3, nota4)
media = resultado.resultado_media(nota1, nota2, nota3, nota4)

#Saida
print('-'*70)
print('RESULTADOS')
print('-'*70)
print(f'Nota1: {nota1} | Nota2: {nota2}')
print(f'Nota3: {nota3} | Nota4: {nota4}')
print('='*70)
print(f'Media: {media}')
print('='*70)