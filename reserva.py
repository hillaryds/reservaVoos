def reservarVoo(voos, dadosVoo, reservas, reservante):
    from uteis import mostrarVoos
    mostrarVoos(voos, dadosVoo)
    while True:
        if len(voos) > 0:
            id = int(input('Digite o ID do voo que deseja reservar: [5410 para sair]'))
            if id == 5410:
                break
            elif id < len(voos):
                print(f'+ Reserva do voo {voos[id]["Nome"]}: ')
                while True:
                    passageiro = str(input('Digite seu nome para fazer a reserva: ')).strip()
                    if passageiro == '':
                        print('Não foi possível realizar sua reserva. Tente novamente!')
                    else:
                        reservante[f'{voos[id]["Nome"]}'] = passageiro
                        reservas.append(reservante.copy())
                        reservante.clear()
                        #voos[id]['Reservantes'].append(reservante)
                        #print(voos[id]['Reservantes'])
                        print(f'Reserva realizada com sucesso no nome de {passageiro}')
                        voos[id]['Reservas'] += 1
                        voos[id]['Assentos'] -= 1
                        break
            else:
                print(f'ERRO! Não existe um voo com o ID {id}.')
                print('=+' * 35) 
                id = int(input('Escolha um dos IDs para realizar a reserva do voo: '))
        else: 
            print('Não será possível realizar nenhuma reserva')
            break
    return voos, dadosVoo, reservas