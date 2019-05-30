from funcionário import Funcionario
import pickle

class Professor(Funcionario):

    def __init__(self):
        self.formacao = ""
        self.nivel = ""
        self.disciplina = ""
        super().__init__()

    def cadastrarProfessor(self):
        dados_funcionario = super().cadastrarFuncionario()
        self.formacao = input("Digite a formação: ")
        self.disciplina = input("Digite a disciplina: ")
        
        dados_prof = dict(formacao=self.formacao, nivel=self.nivel,
                        disciplina=self.disciplina)

        dados_funcionario.update(dados_prof)

        try:

            with open('professor.pkl', 'rb') as lista_profs:
                antiga_lista = pickle.load(lista_profs)
            with open('professor.pkl', mode='wb') as lista_profs:
                antiga_lista.append(dados_funcionario)
                nova_lista = pickle.dumps(antiga_lista)
                lista_profs.write(nova_lista)
        except:
            with open('professor.pkl', mode='wb') as lista_profs:
                nova_lista = [dados_funcionario]
                lista = pickle.dumps(nova_lista)
                lista_profs.write(lista)
        

    def exibirProfessor(self):
        super().exibirFuncionario()
        print(self.formacao)
        print(self.nivel)
        print(self.disciplina)