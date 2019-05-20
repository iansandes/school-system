from pessoa import Pessoa


class Aluno(Pessoa):

    def __init__(self):
        self.codigo = 0
        self.interesse = ""
        self.desconto = 0.0
        super().__init__()

    def cadastrarAluno(self):
        super().Cadastrar()
        self.codigo = input("Digite o código: ")
        self.interesse = input("Digite o interesse: ")
        self.desconto = input("Digite o desconto: ")

    def exibirAluno(self):
        super().Exibir()
        print(self.codigo)
        print(self.interesse)
        print(self.desconto)
