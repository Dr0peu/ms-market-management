class ProductDomain:
    def __init__(self, nome, preco, quantidade, status=False, imagem=None):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.status = status
        self.imagem = imagem 