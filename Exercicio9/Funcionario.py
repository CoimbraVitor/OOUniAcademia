from datetime import datetime

class Funcionario():
    def __init__(self, nome,cargo,data_nascimento):
        self.nome = nome
        self.cargo = cargo
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        self.dependentes = []

    def calcular_salario_liquido(self):
        salario_liquido = self.cargo.get_salario_bruto()
        for dependente in self.dependentes:
            if dependente.get_idade() < 18:
                salario_liquido += 100.00
        return salario_liquido

    def adicionar_dependente(self, Dependente):
        self.dependentes.append(Dependente)


    def listar_dependentes(self):
        for dependentes in self.dependentes:
            print(dependentes)