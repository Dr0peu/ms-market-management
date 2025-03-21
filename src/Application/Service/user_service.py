from src.Domain.user import UserDomain
from src.Infrastructure.Models.user import User
from src.config.data_base import db 

class UserService:
    @staticmethod
    def create_user(nome, email, senha, cnpj, celular):
        new_user = UserDomain(nome, email, senha, cnpj, celular)
        user = User(
            nome=new_user.nome, 
            email=new_user.email, 
            senha=new_user.senha,
            cnpj=new_user.cnpj,
            celular=new_user.celular
        )        
        db.session.add(user)
        db.session.commit()
        return user