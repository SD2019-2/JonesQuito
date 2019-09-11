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