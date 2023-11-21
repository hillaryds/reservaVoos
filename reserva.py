def reservarVoo(voos, dadosVoo):
    from uteis import mostrarVoos
    mostrarVoos(voos, dadosVoo)
    while True:
        op = int(input('Digite o ID do voo que deseja reservar: [5410 para sair]'))
        if op == 5410:
            break
        elif op < len(voos):
            print(f'+ Reserva do voo {voos[op]["nome"]}: ')
            while True:
                reservante = str(input('Digite seu nome para fazer a reserva: ')).strip()
                if reservante == '':
                    print('Não foi possível realizar sua reserva. Tente novamente!')
                else:
                    print(f'Reserva realizada com sucesso no nome de {reservante}')
                    dadosVoo[op]['Reservas'] += 1
        else:
            print(f'ERRO! Não existe um voo com o ID {op}.')
            print('=+' * 35) 
            op = int(input('Escolha um dos IDs para realizar a reserva do voo: '))
    return voos, dadosVoo