from config.data_base import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    imagem = db.Column(db.String(255), nullable=True, default=None)

    def to_dict(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "status": self.status,
            "imagem": self.imagem
        }
    
    def criacao_tabelas(app):
        with app.app_context():
            db.create_all()
            print('Tabela de produtos criada com sucesso!!')

    def listar_tabelas():
        with app.app_context():
            with db.engine.connect() as connection:
                result = connection.execute(text("SHOW TABLES"))
                print("Tabelas no banco de dados:")
                for row in result:
                    print(row[0])