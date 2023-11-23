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
                global admin
                admin = 1 
                break
            if validaUsuario(nome, email, senha, usuarios) == True:
                print('-'*60)
                print('Login realizado com sucesso!')
                global login 
                login = True
                break
            else:
                op = ' '
                while op not in 'SN':
                    op = str(input('Deseja tentar realizar o login novamente? [S/N]')).strip().upper()[0]
                if op == 'N':
                    break
        except(ValueError, TypeError):
            print('Preenchimento inválido!')
