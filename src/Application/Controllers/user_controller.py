from flask import request, jsonify, make_response
from Application.Service.user_service import UserService
from Application.Service.auth_service import AuthService

class UserController:
    @staticmethod
    def register_userJson():
        data = request.get_json()
        nome = data.get('nome')
        cnpj = data.get('cnpj')
        email = data.get('email')
        celular = data.get('celular')
        senha = data.get('senha')

        campos = ['nome', 'cnpj', 'email', 'celular', 'senha']
        falta_campo = [campo for campo in campos if not data.get(campo)]

        if falta_campo:
            return make_response(jsonify({"erro": "Todos os campos são obrigatórios"}), 400)

        user = UserService.create_user(nome, cnpj, email, celular, senha)
        
        return make_response(jsonify({
            "mensagem": "Usuário salvo com sucesso. Código de ativação enviado via WhatsApp.",
            "usuario": user.to_dict()
        }), 200)


    @staticmethod
    def activate_user():
        data = request.get_json()
        email = data.get('email')
        code = data.get('code')

        if not email or not code:
            return make_response(jsonify({"erro": "Email e código de ativação são obrigatórios"}), 400)
        
        result = UserService.activate_user(email, code)
        if result:
            return make_response(jsonify({"mensagem": "Conta ativada com sucesso"}), 200)
        return make_response(jsonify({"erro": "Código inválido ou conta não encontrada"}), 400)


    @staticmethod
    def login_user():
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')

        token = AuthService.authenticate_user(email, senha)

        if token:
            
            user = UserService.get_user_by_email(email)

            if not user:
                return make_response(jsonify({"erro": "Usuário não encontrado"}), 404)
            
            return make_response(jsonify({
                "token": token,
                "user": {"id": user.id, "nome": user.nome, "email": user.email}
                }), 200)
        
        return make_response(jsonify({"messagem": "Email ou senha inválidos"}), 401)
    
    @staticmethod
    def protected_route():
        user_data = AuthService.decode_token(request)
        if not user_data:
            return make_response(jsonify({"erro": "Token inválido ou expirado"}), 401)
        return make_response(jsonify({"mensagem": "Acesso autorizado", "user_data": user_data}), 200)

        