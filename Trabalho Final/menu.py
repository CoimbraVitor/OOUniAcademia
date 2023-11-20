from Usuario import Usuario
from Livros import Livro
from Emprestimos import Emprestimo

def menu_login():
    print("************************")
    print("\nPrimeiro menu:")
    print("Escolha uma das Opções")

    while True:
        opcao = input("Digite 1 para login, 2 para registrar, ou 0 para sair: ")

        if opcao == "1":
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            usuario = Usuario("", "", login, senha)
            usuario.login(login, senha)
            if usuario.logado:
                return usuario
        elif opcao == "2":
            nome = input("Digite o nome: ")
            tipo = input("Digite o tipo da conta (Bibliotecário ou Usuário): ")
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            novo_usuario = Usuario(nome, tipo, login, senha)
            novo_usuario.register()
        elif opcao == "0":
            print("Saindo do programa.")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
def menu_cliente(usuario):
    print("\nSegundo menu:")
    print("1 – Visualizar Empréstimos")
    print("2 – Visualizar Livros")
    print("3 – Sobre")
    print("4 – Logout")
    print("5 – Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        Emprestimo.visualizar_emprestimos()
    elif escolha == "2":
        Livro.visualizar_livros()
    elif escolha == "3":
        with open('sobre.txt', 'r', encoding='utf-8') as sobre:
            print(sobre.read())

    elif escolha == "4":
        usuario.logout()
        print("Logout realizado com sucesso.")
        return None
    elif escolha == "5":
        print("Saindo do programa.")
        exit()
    else:
        print("Opção inválida. Tente novamente.")

    return usuario