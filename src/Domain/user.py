class UserDomain:
    def __init__(self, nome, cnpj, email, celular, senha, status=False, code=None):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.celular = celular
        self.senha = senha
        self.status = status
        self.code = code 