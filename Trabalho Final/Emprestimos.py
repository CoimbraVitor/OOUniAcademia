from datetime import datetime

class Emprestimo():
    def __init__(self,codigo_emprestimo,codigo_cliente,codigo_livro, data):
        self.__codigo_emprestimo = codigo_emprestimo
        self.__codigo_cliente = codigo_cliente
        self.__codigo_livro = codigo_livro
        self__data = datetime.strptime(data, "%d/%m/%Y").date()

    @staticmethod
    def visualizar_emprestimos():
        with open('emprestimos.txt', 'r') as emprestimos:
            linha = emprestimos.readlines()
            for i in linha:
                print(i)
