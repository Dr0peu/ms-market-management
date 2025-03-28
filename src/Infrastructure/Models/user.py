from config.data_base import db
import random 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    celular = db.Column(db.String(16), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    code = db.Column(db.Integer, nullable=True, default=None)

    def generate_activation_code(self):
        self.code = random.randint(1000, 9999)

    def to_dict(self):
            return {
                "id": self.id,
                "nome": self.nome,
                "cnpj": self.cnpj,
                "email": self.email,
                "celular": self.celular,
                "senha": self.senha,
                "status": self.status,
                "code": self.code
            }

    def criacao_tabelas(app):
        with app.app_context():
            db.create_all()
            print('Tabelas criadas com sucesso!!')


    def listar_tabelas():
        with app.app_context():
            with db.engine.connect() as connection:
                result = connection.execute(text("SHOW TABLES"))
                print("Tabelas no banco de dados:")
                for row in result:
                    print(row[0])

