from Curso import Curso

class Disciplina:
    def __init__(self):
        self.__id = 0
        self.__descricao = ""
        self.__Curso = Curso()
        self.__turmas = []

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_Curso(self):
        return self.__Curso

    def set_Curso(self, Curso):
        self.__Curso = Curso

    def get_turmas(self):
        return self.__turmas

    def set_turmas(self, turmas):
        self.__turmas = turmas