from funcionário import Funcionario

class CoordenadorAdm(Funcionario):

    def __init__(self):
        self.area = ""
        self.plusSalario = 0.0
        super().__init__()

    def cadastrarCoordenadorAdm(self):
        super().cadastrarFuncionario()
        self.area = input("Digite a área: ")
        self.plusSalario = input("Digite o aumento: ")

    def exibirCoordenadorAdm(self):
        super().exibirFuncionario()
        print(self.area)
        print(self.plusSalario)


