def menuLogin(usuarios, dadosAdmin):
    """
    Menu de login
    + param usuarios - recebe as lista usuarios;
    + param dadosAdmin - recebe o dicionário dadosAdmin;
    + return - retorna uma lista com as variáveis login e admin.
    """
    from valida import validaUsuario
    print('~-'*30)
    print('Login'.center(60))
    print('~-'*30)
    while True: 
        try:  
            email = senha = ''  
            while len(email) == 0:
                email = str(input('Email: ')).strip()
                if len(email) == 0: print('Digite algo.')
            while len(senha) == 0:
                senha = str(input('Senha: ')).strip()
                if len(senha) == 0: print('Digite algo.')
            if email == dadosAdmin['Email'] and senha == dadosAdmin['Senha']: 
                admin = 1 
                login = True
                break
            else:
                if validaUsuario(email, senha, usuarios) == True:
                    print('-'*60)
                    print('Login realizado com sucesso!') 
                    login = True
                    admin = 0
                    break
                else:
                    login = False
                    admin = 0
                    print('-'*60)
                    print('Login inválido! ')
                    op = ' '
                    while True:
                        op = str(input('Quer realizar o login novamente? [S/N]')).strip().upper()
                        if op == '':
                            print('Responda com [S] ou [N]')
                            continue
                        if op in 'SIMNÃONAO':
                            break
                    if op in 'NÃONAO':
                        break
                    print('-'*60)
        except(ValueError, TypeError):
            print('Preenchimento inválido!')
    return [login, admin]