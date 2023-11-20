from datetime import datetime

class Dependente():
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    def get_idade(self):
        data_atual = datetime.now().date()
        idade = data_atual.year - self.data_nascimento.year - ((data_atual.month, data_atual.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade
    def calcular_proximo_aniversario(self, ano_referencia, mes_referencia):
        data_referencia = datetime(ano_referencia, mes_referencia, 1).date()
        proximo_aniversario = datetime(ano_referencia, self.data_nascimento.month, self.data_nascimento.day).date()

        if proximo_aniversario < data_referencia:
            proximo_aniversario = datetime(ano_referencia + 1, self.data_nascimento.month, self.data_nascimento.day).date()

        dias_faltantes = (proximo_aniversario - data_referencia).days
        nome_dia_semana = self.obter_nome_dia_semana(proximo_aniversario)

        return proximo_aniversario, dias_faltantes, nome_dia_semana

    def obter_nome_dia_semana(self, data):
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        return dias_semana[data.weekday()]
    def __str__(self):
        proximo_aniversario, dias_faltantes, nome_dia_semana = self.calcular_proximo_aniversario(2023, 11)
        return f"Nome: {self.nome}, Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}, Dias Faltantes: {dias_faltantes}, Dia da Semana: {nome_dia_semana}"