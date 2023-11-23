def validaEmail(email, usuarios):
    if email.count('@') == 1:
        if '.com' in email.split('@')[1] or '.org' in email.split('@')[1] or '.br' in email.split('@')[1]:
            if email.split('@')[0] != '' and email.split('@')[0] != ' ':
                contEmail = 0
                if len(usuarios) != 0:
                    for dado in usuarios:
                        if dado['Email'] == email:
                            contEmail += 1 
                if contEmail == 0: return(True)


def validaUsuario(nome, email, senha, usuarios):
    for dadoUsuario in usuarios:
        if dadoUsuario['Nome'] == nome and dadoUsuario['Email'] == email and dadoUsuario['Senha'] == senha:
            return(True)
        if dadoUsuario['Nome'] == nome and dadoUsuario['Email'] == email and dadoUsuario['Senha'] != senha:
            print('Senha incorreta!')
        elif dadoUsuario['Nome'] == nome and dadoUsuario['Email'] != email and dadoUsuario['Senha'] != senha:
            print('Dados incorretos!')
        elif dadoUsuario['Nome'] != nome and dadoUsuario['Email'] != email and dadoUsuario['Senha'] != senha:
            print('Dados incorretos!')

                
            
# usuarios = [{'Email': 'hill@.br'}]
# email = str(input('Email: '))
# validaEmail(email, usuarios)