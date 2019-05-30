from pessoa import Pessoa
from matricula import Matricula
import pickle


class Aluno(Pessoa):

    def __init__(self):
        self.codigo = 0
        self.interesse = ""
        self.desconto = 0.0
        self.mensalidade = 865.23
        super().__init__()
        self.matricula = Matricula()

    def cadastrarAluno(self):
        dados_aluno = super().Cadastrar()
        self.codigo = input("Digite o código: ")
        self.interesse = input("Digite o interesse: ")
        self.desconto = input("Digite o desconto: ")

        self.mensalidade = float(self.mensalidade) - float(self.desconto)

        dados = dict(codigo=self.codigo, interesse=self.interesse,
                        mensalidade=self.mensalidade, desconto=self.desconto)

        dados_aluno.update(dados)

        try:

            with open('alunos.pkl', 'rb') as lista_alunos:
                antiga_lista = pickle.load(lista_alunos)
            with open('alunos.pkl', mode='wb') as lista_alunos:
                antiga_lista.append(dados_aluno)
                nova_lista = pickle.dumps(antiga_lista)
                lista_alunos.write(nova_lista)
        except:
            with open('alunos.pkl', mode='wb') as lista_alunos:
                nova_lista = [dados_aluno]
                lista = pickle.dumps(nova_lista)
                lista_alunos.write(lista)

    def exibirAluno(self):
        super().Exibir()
        print(self.codigo)
        print(self.interesse)
        print(self.desconto)
