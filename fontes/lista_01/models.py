
class Funcionario(object):
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def calcula_reajuste(self):
        if self.cargo.lower() == 'operador':
            return self.salario * (1.2)
        elif self.cargo.lower() == 'programador':
            return self.salario * (1.18)
        else:
            return self.salario

    def toString(self):
        retorno = self.nome + ' recebe ' + str(self.calcula_reajuste())
        return retorno



class Pessoa(object):
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def is_maior(self):
        if str(self.sexo).lower() == 'f' and self.idade >= 21:
            return True
        elif str(self.sexo).lower() == 'm' and self.idade >= 18:
            return True
        elif str(self.sexo).lower() not in ['f', 'm']:
            return 'Sexo inválido'
        else:
            return False


class CalculadoraNotas(object):
    def __init__(self):
        pass

    def calculaAprovacao(self ,notas):
        soma = 0
        media = 0
        for nota in notas:
            soma = soma + nota
        media = soma / len(notas)
        return media