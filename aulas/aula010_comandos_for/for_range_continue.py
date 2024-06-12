import os


os.system('cls')

print('-'*70)
print('Estrutura de controle: CONTINUE')
print('-'*70)

print()

for c in range(1, 11):
    if c == 5:
        #  5 está fora do loop, se retirar a linha abaixo
        # ele não apaecerá na saída deixei parar verificação
        print(f'O número {c} está fora do loop')
        continue    # Salta e o ciclo continua
    
    print(f'o número é {c}')

print('-'*70)
print()