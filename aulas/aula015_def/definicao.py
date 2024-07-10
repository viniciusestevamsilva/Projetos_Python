# Fenindo funções

def limpar_tela():
    """Função para limpar o terminal
    """
    import os
    os.system('cls')


def soma(a, b):
    """Função para somar 2 numeros

    Args:
        a (int): valor a
        b (int): valor b

    Returns:
        Retorna a soma de 2 números
    """    
    return a + b


def firula():
    print('-'*70)

# Program principal


# chamando a função 
limpar_tela()
firula()
resposta = soma(1,2)
print(f'A soma dos 2 números é: {resposta}')
firula()
print()