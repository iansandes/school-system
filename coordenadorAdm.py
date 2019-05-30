from funcionário import Funcionario
import pickle


class CoordenadorAdm(Funcionario):

    def __init__(self):
        self.area = ""
        self.plusSalario = 0.135
        super().__init__()

    def cadastrarCoordenadorAdm(self):
        dados_funcionario = super().cadastrarFuncionario()
        self.area = input("Digite a área: ")

        dados_plus = dict(area=self.area)

        dados_funcionario.update(dados_plus)

        try:

            with open('coordenadoresAdm.pkl', 'rb') as lista_coordAdm:
                antiga_lista = pickle.load(lista_coordAdm)
            with open('coordenadoresAdm.pkl', mode='wb') as lista_coordAdm:
                antiga_lista.append(dados_funcionario)
                nova_lista = pickle.dumps(antiga_lista)
                lista_coordAdm.write(nova_lista)
        except:
            with open('coordenadoresAdm.pkl', mode='wb') as lista_coordAdm:
                nova_lista = [dados_funcionario]
                lista = pickle.dumps(nova_lista)
                lista_coordAdm.write(lista)
        
    def exibirCoordenadorAdm(self):
        super().exibirFuncionario()
        print(self.area)

    def calcularPlusSalario(self):
        aumento = float(self.salario) * float(self.plusSalario)
        self.salario = self.salario + aumento
        print("O valor do salário com aumento: R${:.2f}".format(self.salario))