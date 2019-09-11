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