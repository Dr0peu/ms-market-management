from Domain.product import ProductDomain
from Infrastructure.Models.product import Product
from config.data_base import db
from werkzeug.security import generate_password_hash, check_password_hash

class ProductService:
    @staticmethod
    def create_product(nome, preco, quantidade, status=False, imagem=None):
        new_product = Product(
            nome=nome, 
            preco=preco,
            quantidade=quantidade, 
            status=status,
            imagem=imagem
        )
 
        db.session.add(new_product)
        db.session.commit()
        return new_product
    

   