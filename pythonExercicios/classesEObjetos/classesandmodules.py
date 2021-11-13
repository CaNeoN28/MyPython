class Pessoa:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

class Student(Pessoa):
    def __init__(self, nome, id, classe, media):
        self.nome = nome
        self.id = id
        self.classe = classe
        self.media = media
        self.sit = Student.situacao(self)

    def situacao(self):
        if self.media >= 7.0:
            return('APROVADO')
        elif self.media >= 5.0:
            return('RECUPERAÇÃO')
        else:
            return('REPROVADO')

class Program:
    aluno = []
    aluno.append(Student('Lucas', 1))
    print(aluno[0].sit)