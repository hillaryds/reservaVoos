def cadastrarVoo(voos, dadosVoo):
    """
    Cadastra os voos 
    + param voos - recebe a lista voos;
    + param dadosVoo - recebe o dicionário dadosVoo:
    + return - retorna voos e dadosVoo
    """

    print('Cadastrar Voos')
    while True:
        print('-' * 30) 
        codigoVoo = destino = assentos = ''
        
        while len(codigoVoo) == 0:
            codigoVoo = str(input('Digite o código do voo: ')).strip()
            if len(codigoVoo) == 0: print('Digite algo.')
        
        if len(voos) != 0:
            contVoo = 0
            for dado in voos:
                if dado['Código'] == codigoVoo:
                    contVoo += 1 
        else: contVoo = 0
        
        if contVoo == 0:
            dadosVoo['Código'] = codigoVoo
           
            while len(destino) == 0:
                destino = str(input('Digite o destino do voo: '))
                if len(destino) == 0: print('Digite algo.')
                else: dadosVoo['Destino'] = destino
           
            while True:
                while len(assentos) == 0:
                    assentos = str(input('Digite o número de assentos: '))
                    if len(assentos) == 0: print('Digite algo.')
                
                if assentos.isnumeric():
                    if int(assentos) > 0:
                        dadosVoo['Assentos'] = int(assentos)
                        break
                    else: 
                        print('Digite um número inteiro') 
                        assentos = ''
                        continue
                else: 
                    print('O valor digitado não é um número inteiro positivo')
                    assentos = ''

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

        else: 
            print('O código digitado já foi cadastrado')
            
            op = ' '
            while True:
                op = str(input('Quer cadastrar mais um voo? [S/N]')).strip().upper()
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
    Cadastra os usuários
    + param usuarios - recebe a lista de usuarios
    + param dadosUsuario - recebe o dicionário dadosUsuario
    + return - retorna usuarios e dadosUsuario.
    """
    from valida import validaEmail
    print('~-'*50)
    print(' Cadastro de Usuário'.center(100))
    print('~-'*50)
    while True:
        try:
            print('O Email válido possui [@ obrigatório; Terminar com .com/.org/.br; não possuir espaços].')
            print('O sistema fará as correções possíveis.')
            email = str(input('Digite um email válido: ')).strip()
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