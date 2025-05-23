from Domain.user import UserDomain
from Infrastructure.Models.user import User
from Infrastructure.http.whats_app import send_whatsapp_message
from config.data_base import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(nome, cnpj, email, celular, senha):
        senha_hash = generate_password_hash(senha)
        new_user = User(
            nome=nome, 
            cnpj=cnpj,
            email=email, 
            celular=celular,
            senha=senha_hash
        )

        new_user.generate_activation_code()  
        db.session.add(new_user)
        db.session.commit()

        send_whatsapp_message(new_user.celular, new_user.code)
        return new_user
    
    @staticmethod
    def activate_user(email, code):
        user = User.query.filter_by(email=email, code=code).first()
        if user:
            user.status = True
            user.code = None
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_user_by_email(email):
        user = User.query.filter_by(email=email).first()
        if user:
            return user
        return None