from Infrastructure.Models.sale import Sale
from Infrastructure.Models.product import Product
from Infrastructure.Models.user import User
from sqlalchemy import func
from datetime import datetime, timedelta
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
    
    @staticmethod
    def get_sales_summary_by_user(id_user):
        hoje = datetime.utcnow()
        sete_dias_atras = hoje - timedelta(days=6)

        vendas = db.session.query(
            func.date(Sale.data_venda).label('dia'),
            Product.nome.label('produto'),
            func.sum(Sale.quantidade).label('quantidade'),
            func.sum(Sale.quantidade * Sale.preco_unitario).label('total')
        ).join(Product, Product.id == Sale.id_produto)\
        .filter(
            Sale.id_user == id_user,
            Sale.data_venda >= sete_dias_atras
        ).group_by(
            func.date(Sale.data_venda), Product.nome
        ).order_by(func.date(Sale.data_venda)).all()

        resumo = {}

        for dia, produto, quantidade, total in vendas:
            str_dia = str(dia)
            if str_dia not in resumo:
                resumo[str_dia] = {
                    "total": 0,
                    "quantidade": 0,
                    "produtos": []
                }
            resumo[str_dia]["total"] += float(total)
            resumo[str_dia]["quantidade"] += int(quantidade)
            resumo[str_dia]["produtos"].append({
                "nome": produto,
                "quantidade": int(quantidade),
                "subtotal": float(total)
            })

        for i in range(6, -1, -1):
            data = str((hoje - timedelta(days=i)).date())
            if data not in resumo:
                resumo[data] = {
                    "total": 0,
                    "quantidade": 0,
                    "produtos": []
                }

        return resumo
