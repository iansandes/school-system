class Matricula:
    def __init__(self):
        self.id = 0
        self.mesMatricula = 0
        self.anoMatricula = 0

    def matricular(self):
        self.id = input("Digite o ID: ")
        self.mesMatricula = input("Digite o mês de matrícula: ")
        self.anoMatricula = input("Digite o ano de matrícula: ")
