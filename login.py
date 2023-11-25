def menuLogin(usuarios, dadosAdmin):
    from valida import validaUsuario
    print('~-'*30)
    print('Login'.center(60))
    print('~-'*30)
    while True: 
        try:    
            nome = str(input('Nome: ')).title().strip()
            email = str(input('Email: ')).strip()
            senha = str(input('Senha: ')).strip()
            if nome == dadosAdmin['Nome'] and email == dadosAdmin['Email'] and senha == dadosAdmin['Senha']: 
                admin = 1 
                login = True
                break
            else:
                if validaUsuario(nome, email, senha, usuarios) == True:
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
                    while op not in 'SN':
                        op = str(input('Deseja tentar realizar o login novamente? [S/N]')).strip().upper()[0]
                    if op == 'N':
                        break
                    print('-'*60)
        except(ValueError, TypeError):
            print('Preenchimento inválido!')
    return [login, admin]