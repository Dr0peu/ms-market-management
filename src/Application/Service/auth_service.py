import jwt
import datetime
from flask import request
from Infrastructure.Models.user import User
from werkzeug.security import check_password_hash

SECRET_KEY = 'd8c4a2a7f89b3d9b2e543f6a1a12b8d5f1e9a5f5a7d9c3b8e6d2f4c7e1b6a3c4'

class AuthService:
    @staticmethod
    def authenticate_user(email, senha):
        user = User.query.filter_by(email=email, status=True).first()
        if user and check_password_hash(user.senha, senha):
            token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                                SECRET_KEY, algorithm='HS256')
            return token
        return None
    
    @staticmethod
    def decode_token(request):
        token = request.headers.get('Authorization')
        if not token:
            return None
        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return data
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None