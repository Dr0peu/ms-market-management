from config.data_base import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    data_venda = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_produto": self.id_produto,
            "quantidade": self.quantidade,
            "preco_unitario": self.preco_unitario,
            "data_venda": self.data_venda.isoformat(),
            "valor_total": round(self.quantidade * self.preco_unitario, 2)
        }

    @staticmethod
    def criacao_tabelas(app):
        with app.app_context():
            db.create_all()
            print('Tabela de vendas criada com sucesso!')