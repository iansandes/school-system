import pickle


class Curso:
    def __init__(self):
        self.titulo = ""
        self.descricao = ""
        self.valor = 0.0
        self.sala = ""

    def cadastrarCurso(self):
        self.titulo = input("Digite o título: ")
        self.descricao = input("Digite a descrição: ")
        self.valor = input("Digite o valor: ")
        self.sala = input("Digite a sala: ")

        dados_curso = dict(titulo=self.titulo, descricao=self.descricao,
                        valor=self.valor, sala=self.sala)

        try:

            with open('curso.pkl', 'rb') as cursos:
                antiga_lista = pickle.load(cursos)
            with open('curso.pkl', mode='wb') as cursos:
                antiga_lista.append(dados_curso)
                nova_lista = pickle.dumps(antiga_lista)
                cursos.write(nova_lista)
        except:
            with open('curso.pkl', mode='wb') as cursos:
                nova_lista = [dados_curso]
                lista = pickle.dumps(nova_lista)
                cursos.write(lista)

    def calcularNumMinAluno(self):   
        contador = 0
        with open('professor.pkl', 'rb' ) as lista_profs:
            lista = pickle.load(lista_profs)
            for professor in lista:
                contador = contador +  1

            valor_prof = contador * 12568.43
            calculo = (valor_prof / 865.23) + 1
            print("{:.0f}".format(calculo))



       
        
