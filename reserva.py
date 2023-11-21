def reservarVoo(voos, dadosVoo):
    from uteis import mostrarVoos
    mostrarVoos(voos, dadosVoo)
    while True:
        id = int(input('Digite o ID do voo que deseja reservar: [5410 para sair]'))
        if id == 5410:
            break
        elif id < len(voos):
            print(f'+ Reserva do voo {voos[id]["Nome"]}: ')
            while True:
                reservante = str(input('Digite seu nome para fazer a reserva: ')).strip()
                if reservante == '':
                    print('Não foi possível realizar sua reserva. Tente novamente!')
                else:
                    print(f'Reserva realizada com sucesso no nome de {reservante}')
                    voos[id]['Reservas'] += 1
                    voos[id]['Assentos'] -= 1
                    break
        else:
            print(f'ERRO! Não existe um voo com o ID {id}.')
            print('=+' * 35) 
            id = int(input('Escolha um dos IDs para realizar a reserva do voo: '))
    return voos, dadosVoo