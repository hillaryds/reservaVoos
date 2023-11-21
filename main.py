""" Comando Principal """
dadosVoo = {}
voos = []

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
            break
        else:
            print('Opção inválida')







menuPrincipal()