from Usuario import Usuario

nome = input("Digite seu Nome: ")
tipo = input("Digite o tipo da conta (Usuário ou Bibliotecário): ")
login = input("Digite o login: ")
senha = input("Digite a senha: ")
usuario1 = Usuario(nome, tipo, login, senha)

usuario1.login(login, senha)
usuario1.logout()
