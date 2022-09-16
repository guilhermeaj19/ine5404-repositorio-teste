class URLError(Exception):
    def __init__(self,mensagem,codigo):
        self.mensagem = mensagem
        self.codigo = codigo

    def __str__(self):
        return f'Error: {self.mensagem}; {self.codigo}'

class DataError(Exception):
    def __init__(self,mensagem,codigo):
        self.mensagem = mensagem

    def __str__(self):
        return f'Error: {self.mensagem}'