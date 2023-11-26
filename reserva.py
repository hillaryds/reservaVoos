def reservarVoo(voos, dadosVoo, reservas, reservante):
    from uteis import mostrarVoos
    mostrarVoos(voos, dadosVoo)
    while True:
        if len(voos) > 0:
            
            try:
                id = int(input('Digite o ID do voo que deseja reservar: [5410 para sair]'))
                if id == 5410:
                    break
                elif id < len(voos):
                    print(f'+ Reserva do voo {voos[id]["Código"]}: ')
                    if voos[id]['Assentos'] > 0:
                        while True:
                            passageiro = str(input('Digite seu nome para fazer a reserva: ')).strip()
                            if passageiro == '':
                                print('Não foi possível realizar sua reserva. Tente novamente!')
                            else:
                                reservante[f'{voos[id]["Código"]}'] = passageiro
                                reservas.append(reservante.copy())
                                reservante.clear()
                                print(f'Reserva realizada com sucesso no nome de {passageiro}')
                                voos[id]['Reservas'] += 1
                                voos[id]['Assentos'] -= 1
                                mostrarVoos(voos, dadosVoo)
                                break
                    else: print('Assentos esgotados')
                else:
                    print(f'ERRO! Não existe um voo com o ID {id}.')
                    print('=+' * 35) 
            except (ValueError, TypeError): 
                print('Digite um número, por favor!')
                continue
        else: 
            print('Não será possível realizar nenhuma reserva')
            break
    return voos, dadosVoo, reservas