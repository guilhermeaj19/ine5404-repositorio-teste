def checkData(dados):
    index = len(dados)
    
    if dados['address']['geo']['lat'] is str:
        try:
            dados['adress']['geo']['lat'] = float(dados['adress']['geo']['lat'])   
        except ValueError:
            return f'Error: Usuário {index}: valor de latitude inválido'

    if dados['address']['geo']['lng'] is str:
        try:
            dados['address']['geo']['lng'] = float(dados['adress']['geo']['lng'])
        except ValueError:
            return f'Error: Usuário {index}: valor de longitude inválido'

    if '@' in dados['email']:
        for crt in dados['email']:
            if ord(crt) > 200 or ord(crt) == 32:
                return f'Error: Usuário {index}: e-mail inválido; uso de caracter inválido: {crt}'
    else:
        return f'Error: Usuário {index}: e-mail inválido'

    if len(dados['address']['zipcode']) == 10:
        for crt in range(5):
            if not(ord(dados['adress']['zipcode'][crt]) > 47 and ord(dados['adress']['zipcode'][crt]) < 58):
                return f"Error: Usuário {index}: zipcode inválido, caracter inválido: {dados['zipcode'][crt]}"
        if not dados['adress']['zipcode'][5] == '-':
            return f"Error: Usuário {index}: zipcode inválido, caracter inválido: {dados['zipcode'][crt]}"
        
        for crt in range(6,10):
            if not(ord(dados['adress']['zipcode'][crt]) > 47 and ord(dados['adress']['zipcode'][crt]) < 58):
                return f"Error: Usuário {index}: zipcode inválido, caracter inválido: {dados['zipcode'][crt]}"
    
    elif len(dados['adress']['zipcode']) == 5:
        for crt in range(5):
            if not(ord(dados['adress']['zipcode'][crt]) > 47 and ord(dados['adress']['zipcode'][crt]) < 58):
                return f"Error: Usuário {index}: zipcode inválido, caracter inválido: {dados['zipcode'][crt]}"
    
    else:
        return f"Error: Usuário {index}: zipcode inválido, número de caracteres fora do padrão"

    if len(dados['username']) > 24:
        return f'Error: Usuário {index}: nome de usuário inválido: caracteres excessivos'

    if 'x' in dados['phone']:
        pass