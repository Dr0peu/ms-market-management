class ProductDomain:
    def __init__(self, nome, id_user, preco, quantidade, status=False, imagem=None):
        self.nome = nome
        self.id_user = id_user
        self.preco = preco
        self.quantidade = quantidade
        self.status = status
        self.imagem = imagem 