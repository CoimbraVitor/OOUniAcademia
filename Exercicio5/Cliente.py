from Pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.__cpf = cpf

