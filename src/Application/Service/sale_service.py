from Infrastructure.Models.sale import Sale
from Infrastructure.Models.product import Product
from Infrastructure.Models.user import User
from config.data_base import db

class SaleService:
    @staticmethod
    def register_sale(id_user, id_produto, quantidade):
        produto = Product.query.filter_by(id=id_produto, id_user=id_user).first()
        if not produto:
            raise ValueError("Produto não encontrado ou você não tem permissão.")

        if not produto.status:
            raise ValueError("Não é possível vender um produto inativo.")

        if produto.quantidade < quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")

        user = User.query.filter_by(id=id_user).first()
        if not user or not user.status:
            raise ValueError("Usuário inativo ou não encontrado.")

        produto.quantidade -= quantidade

        nova_venda = Sale(
            id_user=id_user,
            id_produto=id_produto,
            quantidade=quantidade,
            preco_unitario=produto.preco
        )

        db.session.add(nova_venda)
        db.session.commit()

        return nova_venda
