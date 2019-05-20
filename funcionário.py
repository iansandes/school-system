from pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self):
        self.matricula = 0
        self.setor = ""
        self.cargo = ""
        self.nivel = 0
        super().__init__()
        
    def cadastrarFuncionario(self):
        super().Cadastrar()
        self.matricula = input("Digite a matrícula: ")
        self.setor = input("Digite o setor: ")
        self.cargo = input("Digite o cargo: ")
        self.nivel = input("Digite o nível: ")

    def exibirFuncionario(self):
        super().Exibir()
        print(self.matricula)
        print(self.setor)
        print(self.cargo)
        print(self.nivel)