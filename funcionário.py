from salario import Salario
from pessoa import Pessoa
import pickle


class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = 0
        self.setor = ""
        self.cargo = ""
        self.nivel = 0
        super().__init__()
        self.salario = ""

    def cadastrarFuncionario(self):
        dados_pessoa = super().Cadastrar()
        self.matricula = input("Digite a matrícula: ")
        self.setor = input("Digite o setor: ")
        self.cargo = input("Digite o cargo: ")
        self.nivel = input("Digite o nível: ")
        dados_funcao = dict(matricula=self.matricula, setor=self.setor, 
                        cargo=self.cargo, nivel=self.nivel)
            
        dados_pessoa.update(dados_funcao)

        try:

            with open('funcionarios.pkl', 'rb') as lista_funcionarios:
                antiga_lista = pickle.load(lista_funcionarios)
            with open('funcionarios.pkl', mode='wb') as lista_funcionarios:
                antiga_lista.append(dados_pessoa)
                nova_lista = pickle.dumps(antiga_lista)
                lista_funcionarios.write(nova_lista)
        except:
            with open('funcionarios.pkl', mode='wb') as lista_funcionarios:
                nova_lista = [dados_pessoa]
                lista = pickle.dumps(nova_lista)
                lista_funcionarios.write(lista)
        
        return dados_pessoa
        
    def exibirFuncionario(self):
        super().Exibir()
        print(self.matricula)
        print(self.setor)
        print(self.cargo)
        print(self.nivel)

    def calcularSalarioFunc(self):
        self.salario = Salario(self.nivel)
        self.salario = Salario.calcularSalario(self)
        


