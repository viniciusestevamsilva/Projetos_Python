import os


os.system('cls')

print('-'*70)
print('Na mesmo linha em horizontal')
print('-'*70)

for valores in range (1, 100):
    # end= coloca os números em uma mesma linha
    print(f'Números: {valores}', end=" || ")
    
print('-'*70)
print()
