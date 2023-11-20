class Cargo():
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
        self.salario_bruto = 0
    def calcular_salario_bruto(self, outros_acrescimos):
        self.salario_bruto = self.salario_base + outros_acrescimos
        return self.salario_bruto

    def get_salario_bruto(self):
        return self.salario_bruto