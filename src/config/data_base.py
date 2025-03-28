from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import text

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa a base de dados com o app Flask e o SQLAlchemy.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost/ms_market_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()


