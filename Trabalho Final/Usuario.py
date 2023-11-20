import random

class Usuario:
    def __init__(self, nome, tipo, login, senha):
        self.__codigo = 0
        self.__nome = nome
        self.__tipo = tipo
        self.__login = login
        self.__senha = senha
        self.logado = False

    def register(self):
        with open('usuarios.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            if self.__login in linha:
                print("Login já existe, digite outro.")
                return

        self.__codigo = random.randint(1, 1000)
        novo_usuario = f"{self.__codigo},{self.__nome},{self.__tipo},{self.__login},{self.__senha}\n"

        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(novo_usuario)
        print("Usuário registrado com sucesso.")

    def login(self, login, senha):
        with open('usuarios.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            if len(dados) >= 5 and login == dados[3] and senha == dados[4]:
                print("Login bem-sucedido.")
                self.logado = True
                return
        print("Login falhou. Verifique suas credenciais.")

    def logout(self):
        if self.logado:
            self.logado = False
            return print("Deslogado com sucesso")
