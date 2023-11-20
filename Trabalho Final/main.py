from menu import menu_login, menu_cliente

def main():
    usuario_logado = None

    while True:
        if not usuario_logado:
            usuario_logado = menu_login()

        if usuario_logado:
            usuario_logado = menu_cliente(usuario_logado)

if __name__ == "__main__":
    main()