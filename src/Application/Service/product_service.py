from Domain.product import ProductDomain
from Infrastructure.Models.product import Product
from config.data_base import db

class ProductService:
    @staticmethod
    def create_product(id_user, nome, preco, quantidade, status=False, imagem=None):
        new_product = Product(
            id_user=id_user,
            nome=nome,
            preco=preco,
            quantidade=quantidade,
            status=status,
            imagem=imagem
        )
 
        db.session.add(new_product)
        db.session.commit()
        return new_product
    
    @staticmethod
    def list_products_by_user(id_user):
        products = Product.query.filter_by(id_user=id_user).all()
        return [product.to_dict() for product in products]
    
    @staticmethod
    def get_product_by_id(id_product, id_user):
        return Product.query.filter_by(id=id_product, id_user=id_user).first()
    
    @staticmethod
    def update_product(id_product, id_user, nome=None, preco=None, quantidade=None, status=None, imagem=None):
        product = Product.query.filter_by(id=id_product, id_user=id_user).first()
        if not product:
            return None

        if nome is not None:
            product.nome = nome
        if preco is not None:
            product.preco = preco
        if quantidade is not None:
            product.quantidade = quantidade
        if status is not None:
            product.status = status
        if imagem is not None:
            product.imagem = imagem

        db.session.commit()
        return product
    
    @staticmethod
    def delete_product_by_id(id_product, id_user):
        product = Product.query.filter_by(id=id_product, id_user=id_user).first()
        if not product:
            return False
        
        db.session.delete(product)
        db.session.commit()
        return True
    

   