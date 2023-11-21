def limpaTela():
    """
    Redireciona e limpa o prompt
    """
    import os
    from time import sleep
    sleep(1.5)
    print('Redirecionando...')
    print()
    sleep(1.5)
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
