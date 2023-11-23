""" Comando Principal """
dadosVoo = {}
voos = []
admin = 0 # variável que pode ser mudada nas função menuLogin
login = False # variável que pode ser mudada nas função menuLogin caso ele tenha sido realizado ou não
dadosAdmin = {'Nome': 'Admin',  'Email': 'admin@.com' , 'Senha': 'admin123'} #login administrador da Hill Airplines
dadosUsuario = {}
usuarios = []

def menuInicial():
    while True:
        """
        """
        from uteis import limpaTela
        from cadastra import menuCadastroUsuario
        from login import menuLogin
        print('~-'*30)
        print('Hill Airlines'.center(60))
        print('~-'*30)
        print('[1] Realizar login')
        print('[2] Realizar cadastro')
        print('[3] Sair')
        print('-'*60)
        try:   
            op = int(input('Escolha uma das opções a seguir: '))
            if op == 1:
                limpaTela()
                menuLogin(usuarios, dadosAdmin)
                limpaTela()
                menuPrincipal()
            elif op == 2:
                limpaTela()
                menuCadastroUsuario(usuarios, dadosUsuario)
                limpaTela()
                if login:
                    menuPrincipal()
            elif op == 3:
                print('Espero que a Hill Airplines tenha te ajudado. Volte sempre!')
                break
            else:
                print('Opção inválida!')
        except(ValueError, TypeError):
            print('Opção inválida!')
            limpaTela()


def menuPrincipal():
    """
    """
    from uteis import limpaTela , mostrarVoos
    from cadastra import cadastrarVoo
    from reserva import reservarVoo
    print(f'Seja bem vindo, usuário ')
    while True:
        limpaTela()
        print('~-'*30)
        print('Hill Airlines'.center(60))
        print('~-'*30)
        print('[1] Cadastrar voos')
        print('[2] Reservar voos')
        print('[3] Mostrar voos')
        print('[4] Sair')
        print('-'*60)
        try:
            op = int(input('Escolha uma das opções a seguir: '))
            if op == 1:
                limpaTela()
                cadastrarVoo(voos, dadosVoo)
            elif op == 2:
                limpaTela()
                reservarVoo(voos, dadosVoo)
            elif op == 3:
                mostrarVoos(voos, dadosVoo)
            elif op == 4:
                print('Espero que a Hill Airplines tenha te ajudado. Volte sempre!')
                menuInicial()
            else:
                print('Opção inválida')
        except(ValueError, TypeError):
            print('Opção inválida!')





menuInicial()