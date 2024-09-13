
class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
    
    def info(self, nome, idade, genero, especialidade, salario):
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, genero, especialidade, salario):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.especialidade = especialidade
        self.salario = salario

    def info(self, nome, idade, genero, especialidade, salario):
  
        return print(f'{nome},tenho {idade} anos, \nsou do genero {genero} é formado em {especialidade}, \nrecebo {salario} por mes')


print('/'*70)
print('Informações de usuario')
print('='*70)
nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
genero = input('Digite seu genero:')
especialidade = input('Digite sua formação:')
salario = input('Digite seu salario:')
print('='*70)
Jorge = Professor(nome, idade, genero, especialidade, salario)
Jorge.info(nome, idade, genero, especialidade, salario)
print('/'*70)