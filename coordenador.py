from professor import Professor

class Coordenador(Professor):

    def __init__(self):
        self.area = ""
        self.plusSalario = 0.0
        super().__init__()

    def cadastrarCoordenadorProf(self):
        super().cadastrarProfessor()
        self.area = input("Digite a área: ")
        self.plusSalario = input("Digite o aumento: ")

    def exibirCoordenadorProf(self):
        super().exibirProfessor()
        print(self.area)
        print(self.plusSalario)


