class Salario:
    def __init__(self, nivel):
        self.salarioBruto = 0.0
        self.salarioLiquido = 0.0
        self.inss = 0.0
        self.irrf = 0.0
        self.planoDeSaude = 125 
        self.nivel = nivel
    
    def calcularSalario(self):
        if self.nivel.upper() == 'A':
            self.salarioBruto = float(1520.25)
        elif self.nivel.upper() == 'B':
            self.salarioBruto = float(2362.67)
        elif self.nivel.upper() == 'C':
            self.salarioBruto = float(2988.92)
        elif self.nivel.upper() == 'D':
            self.salarioBruto = float(3572.77)
        elif self.nivel.upper() == 'E':
            self.salarioBruto = float(4878.67)
        elif self.nivel.upper() == 'I':
            self.salarioBruto = float(6500.00)
        elif self.nivel.upper() == 'II':
            self.salarioBruto = float(8325.50)
        elif self.nivel.upper() == 'III':
            self.salarioBruto = float(12568.43)  

        self.inss = float(input('Digite a porcentagem do INSS: '))
        self.irrf = float(input('Digite a porcentagem do IRFF: '))
        calculo_inss = self.salarioBruto * (self.inss / 100)
        calculo_irrf = (self.salarioBruto - calculo_inss) * (self.irrf / 100)
        self.salarioLiquido = (self.salarioBruto - (calculo_inss + calculo_irrf)) - 125
        print('R$ {:.2f}'.format(self.salarioLiquido))
        return self.salarioLiquido

        


      
