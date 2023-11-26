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
        while True:
            op = str(input('Quer cadastrar mais algum voo? [S/N]')).strip().upper()
            if op == '':
                print('Responda com [S] ou [N]')
                continue
            if op in 'SIMNÃONAO':
                break
        if op in 'NÃONAO':
            break
    
    return voos, dadosVoo


def menuCadastroUsuario(usuarios, dadosUsuario):
    """
    """
    from valida import validaEmail
    print('~-'*30)
    print(' Cadastro de Usuário'.center(60))
    print('~-'*30)
    while True:
        try:
            nome = str(input('Digite seu primeiro nome: '))
            if nome.strip != '':
                dadosUsuario['Nome'] = nome.title().strip().split()[0]
                print(f'Seu nome de usuário é: {dadosUsuario["Nome"]}')
                email = str(input('Digite um eail válido: ')).strip()
                if validaEmail(email, usuarios) == True:
                    dadosUsuario['Email'] = email
                    senha = str(input('Digite uma senha com 8 ou mais caracteres: '))
                    if len(senha.strip()) >= 8:
                        dadosUsuario['Senha'] = senha
                        dadosUsuario['Reservas'] = 0 # adcionar reservas realcionadas ao usuário.
                        usuarios.append(dadosUsuario.copy())
                        break
                    else:
                        print('-' * 60)
                        print('Senha inválida')
                        break
                else:
                    print('-' * 60)
                    print('Email inválido ou já cadastrado!')
                    break
        except(ValueError, TypeError): 
            print('Opção inválida!')

    return(usuarios, dadosUsuario)

