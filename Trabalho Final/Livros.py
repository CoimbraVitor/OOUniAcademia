class Livro:
    def __init__(self, codigo, nome, autor):
        self.__codigo = codigo
        self.__nome = nome
        self.__autor = autor

    @staticmethod
    def visualizar_livros():
        with open("livros.txt", 'r') as livros:
            linha = livros.readlines()

            for i in linha:
                print(i)