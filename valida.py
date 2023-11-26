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


def validaUsuario( email, senha, usuarios):
    for dadoUsuario in usuarios:
        if dadoUsuario['Email'] == email and dadoUsuario['Senha'] == senha:
            return(True)
            break
        elif dadoUsuario['Email'] == email and dadoUsuario['Senha'] != senha:
            print('Senha incorreta!')

