class Pessoa:

    def __init__(self):
        self.nome = ""
        self.rg = ""
        self.cpf = ""
        self.anoNasc = 0
        self.mesNasc = 0
        self.diaNasc = 0
        self.sexo = ""

    def Cadastrar(self):
        self.nome = input("Digite o nome: ")
        self.rg = input("Digite o RG: ")
        self.cpf = input("Digite o CPF: ")
        self.anoNasc = input("Digite o ano de nascimento: ")
        self.mesNasc = input("Digite o mês de nascimento: ")
        self.diaNasc = input("Digite o dia de nascimento: ")
        self.sexo = input("Digite o sexo: ")

        dados = dict(nome=self.nome, rg=self.rg, cpf=self.cpf, anoNasc=self.anoNasc,
                mesNasc=self.mesNasc, diaNasc=self.diaNasc, sexo=self.sexo)

        return dados

    def Exibir(self):
        print(self.nome)
        print(self.rg)
        print(self.cpf)
        print(self.anoNasc)
        print(self.mesNasc)
        print(self.diaNasc)
        print(self.sexo)





        