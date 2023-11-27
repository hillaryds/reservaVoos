def validaEmail(email, usuarios):
    """
    Valida o email cadastrado.
    + param email - recebe o email cadastrado;
    + param usuarios - recebe a lista de usuarios
    + return - retorna True se o email for válido
    """
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
    """
    Valida o usuário no login
    + param email - recebe o email digitado no login;
    + param senha - recebe a senha digitada no login;
    + param usuarios - recebe a lista de usuarios;
    + return - retorna verdadeiro se o usuário existir.
    """
    for dadoUsuario in usuarios:
        if dadoUsuario['Email'] == email and dadoUsuario['Senha'] == senha:
            return(True)
        # elif dadoUsuario['Email'] == email and dadoUsuario['Senha'] != senha:
        #     print('Senha incorreta!')

