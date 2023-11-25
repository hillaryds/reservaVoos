""" Comando Principal """

# Variáveis globais --------------------------------------------------------------------------------------------------------
dadosVoo = {}
voos = []
dadosAdmin = {'Nome': 'Admin',  'Email': 'admin@.com' , 'Senha': 'admin12'} #login administrador da Hill Airplines
dadosUsuario = {}
usuarios = []
reservas = [] # reservas de cada voo
reservante = {}
# Funções de Menus ----------------------------------------------------------------------------------------------------------
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
                logou = menuLogin(usuarios, dadosAdmin)
                print(logou)
                if logou[0] == True:
                    if logou[1] == 1:
                        print('logou')
                        menuPrincipal(1)
                    else:
                        menuPrincipal(0)
                else:
                    print('n logou')
                logou.clear()
            elif op == 2:
                limpaTela()
                menuCadastroUsuario(usuarios, dadosUsuario)
                limpaTela()
            elif op == 3:
                print('Espero que a Hill Airplines tenha te ajudado. Volte sempre!')
                break
            else:
                print('Opção inválida!')
                limpaTela()
        except(ValueError, TypeError):
            print('Opção inválida!')
            limpaTela()


def menuPrincipal(admin):
    """
    """
    from uteis import limpaTela , mostrarVoos, mostrarReservas
    from cadastra import cadastrarVoo
    from reserva import reservarVoo
    print(admin)
    while True:
        limpaTela()
        print('~-'*30)
        print('Hill Airlines'.center(60))
        print('~-'*30)
        if admin == 1:
            print('[0] Cadastrar voos')
        print('[1] Reservar voos')
        print('[2] Mostrar voos')
        print('[3] Sair')
        if admin == 1:
            print('[4] Mostrar reservas')
        print('-'*60)
        try:
            op = int(input('Escolha uma das opções a seguir: '))
            if admin == 1:
                if op == 0:
                    limpaTela()
                    cadastrarVoo(voos, dadosVoo)
            if op == 1:
                limpaTela()
                reservarVoo(voos, dadosVoo, reservas, reservante)
            elif op == 2:
                mostrarVoos(voos, dadosVoo)
            elif op == 3:
                print('Espero que a Hill Airplines tenha te ajudado. Volte sempre!')
                limpaTela()
                break
            elif admin == 1:
                if op == 4:
                    print('Mostrar reservas')
                    mostrarReservas(reservas)
            else:
                print('Opção inválida')
        except(ValueError, TypeError):
            print('Opção inválida!')






# main --------------------------------------------------------------------------------------------------------------------------------

menuInicial()