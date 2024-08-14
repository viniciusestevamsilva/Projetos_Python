import os


os.system('cls')

# Definindo a função
def dados_paciente(nome='Coly', nascimento=2005, peso=46, altura=1.68):
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}.')
    print(f'O peso {nome} é {peso}Kg.')
    print(f'A altura da {nome} é {altura}m.')
    print('-'*70)

# Início para Lembrar
def posicional_nomeado(nascimento, nome='Coly', ): # OK! funciona!
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(F'O ano de nascimento da {nome} é {nascimento}.')
    print('-'*70)


# def nomeado_posicional(nome='Coly', nascimento): # Not OK! Não funciona!
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}')
    print('-'*70)
# Fim para lembrar


# Invocando a função
dados_paciente()

dados_paciente(nome='Isis', nascimento=1985, peso=46, altura=1.56)
dados_paciente(nascimento=2008, nome='Ágata', peso=46, altura=1.58)
dados_paciente(altura=1.66, peso=46, nome='Bia', nascimento=2008)