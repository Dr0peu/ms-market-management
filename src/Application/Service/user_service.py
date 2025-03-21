from Domain.user import UserDomain
from Infrastructure.Models.user import User
from config.data_base import db 

class UserService:
    @staticmethod
    def create_user(nome, cnpj, email, celular, senha):
        new_user = UserDomain(nome, cnpj, email, celular, senha)
        user = User(
            nome=new_user.nome, 
            cnpj=new_user.cnpj,
            email=new_user.email, 
            celular=new_user.celular,
            senha=new_user.senha
        )        
        db.session.add(user)
        db.session.commit()
        return user