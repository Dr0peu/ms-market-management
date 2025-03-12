from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost/ms_market_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    celular = db.Column(db.String(16), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    code = db.Column(db.Integer, nullable=True, default=None)

def criacao_tabelas():
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

if __name__ == "__main__":
    criacao_tabelas()
    listar_tabelas()