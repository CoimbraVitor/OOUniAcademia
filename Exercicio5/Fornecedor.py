from Pessoa import Pessoa
class Fornecedor(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.__cnpj = cnpj