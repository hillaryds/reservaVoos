def cadastrarVoo(voos, dadosVoo):
    print('Cadastra')
    while True:
        print('-' * 30) 
        dadosVoo['Nome'] = str(input('Digite o número do voo: '))
        dadosVoo['Destino'] = str(input('Digite o destino do voo: '))
        dadosVoo['Assentos'] = int(input('Digite o número de assentos: '))
        dadosVoo['Reservas'] = 0
        voos.append(dadosVoo.copy())
        op = ' '
        while op not in 'SN':
            op = str(input('Quer cadastrar mais algum voo? [S/N]')).strip().upper()[0]
        if op == 'N':
            break
    
    
    return voos, dadosVoo

        