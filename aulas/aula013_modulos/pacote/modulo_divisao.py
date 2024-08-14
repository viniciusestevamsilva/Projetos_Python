def dividir(a, b):
    """Método para dividir 2 números

    Args:
        a (any): dividendo
        b (any): divisor
    Returns:
        str: Mensagem de erro ou 'ok' se a divisão for bem-sucedida
        any: Quociente ou none em caso de erro
    """    
    if b == 0:
        return None, 'Erro de divisão'
    else:
        divisao = a / b
        return divisao, 'Ok!'