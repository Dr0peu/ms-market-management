class UserDomain:
    def __init__(self, nome, email, senha, cnpj, celular):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cnpj = cnpj
        self.celular = celular
        
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "cnpj": self.cnpj,
            "celular": self.celular
        }