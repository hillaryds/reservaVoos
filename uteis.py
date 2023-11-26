def limpaTela():
    """
    Redireciona e limpa o prompt
    """
    import os
    from time import sleep
    
    sleep(1.5)
    print('Redirecionando', end = '', flush = True)
    for c in range(0, 3):
        print('.', end = '', flush = True)
        sleep(1)
   
    print()
    os.system('clear') # limpando tela
 
def mostrarVoos( voos, dadosVoo):
    """
    Mostra na tela uma tabela com voos cadastrados:
    + param voos - lista de voos cadastrados;
    + param dadosVoo - dicionário com os dados do voo;
    + return - sem retorno.
    """
    
    if len(voos) == 0:
        print('Sem voos cadastrados.')
    else:
        print('~-' * 35)
        print('  ID ', end = '')
        for indice in dadosVoo.keys():
            print(f'{indice:<20}', end = '')
        print()
        print('--' * 35)
        
        for id, valor in enumerate(voos):
            print(f'{id:>3}) ', end='')
            for dado in valor.values():
                print(f'{str(dado):<20}', end ='')
            print()
        print('~-' * 35)
    print('Pressione Enter para continuar.')
    input()




def mostrarReservas(reservas):
    if len(reservas) == 0:
        print('Nenhuma reserva foi registrada.')
    else:
        print('Reservas')
        print('~-' * 15)
        print(f'{"Código":<20}{"Reservante":<20}')
        print('--' * 15)
        for reserva in reservas:
            for keys, items in reserva.items():
                print(f'{keys:<20}{items:<20}')
                print('--' * 15)
        print('~-' * 15)
    print('Pressione Enter para continuar.')
    input()

