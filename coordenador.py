from professor import Professor
import pickle


class Coordenador(Professor):

    def __init__(self):
        self.area = ""
        self.plusSalario = 0.15
        super().__init__()

    def cadastrarCoordenadorProf(self):
        dados_funcionario = super().cadastrarFuncionario()
        self.area = input("Digite a área: ")

        dados_plus = dict(area=self.area)

        dados_funcionario.update(dados_plus)

        try:

            with open('coordenadoresProf.pkl', 'rb') as lista_coordProf:
                antiga_lista = pickle.load(lista_coordProf)
            with open('coordenadoresProf.pkl', mode='wb') as lista_coordProf:
                antiga_lista.append(dados_funcionario)
                nova_lista = pickle.dumps(antiga_lista)
                lista_coordProf.write(nova_lista)
        except:
            with open('coordenadoresProf.pkl', mode='wb') as lista_coordProf:
                nova_lista = [dados_funcionario]
                lista = pickle.dumps(nova_lista)
                lista_coordProf.write(lista)

    def exibirCoordenadorProf(self):
        super().exibirProfessor()
        print(self.area)
        print(self.plusSalario)

    def calcularPlusSalario(self):
        aumento = float(self.salario) * float(self.plusSalario)
        self.salario = self.salario + aumento
        print("O valor do salário com aumento: R${:.2f}".format(self.salario))




