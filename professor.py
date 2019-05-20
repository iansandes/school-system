from Funcionário import Funcionario

class Professor(Funcionario):

    def __init__(self):
        self.formacao = ""
        self.nivel = ""
        self.disciplina = ""
        super().__init__()

    def cadastrarProfessor(self):
        super().cadastrarFuncionario()
        self.formacao = input("Digite a formação: ")
        self.nivel = input("Digite o nível: ")
        self.disciplina = input("Digite a disciplina: ")

    def exibirProfessor(self):
        super().exibirFuncionario()
        print(self.formacao)
        print(self.nivel)
        print(self.disciplina)
        