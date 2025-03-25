from flask import request, jsonify, make_response, render_template
from Application.Service.user_service import UserService

class UserController:
    @staticmethod
    def register_user():
        if request.method == 'POST':
            nome = request.form.get('nome')
            cnpj = request.form.get('cnpj')
            email = request.form.get('email')
            celular = request.form.get('celular')
            senha = request.form.get('senha')

            if not nome or not cnpj or not email or not celular or not senha:
                return make_response(jsonify({"erro": "Todos os campos são obrigatórios"}), 400)

            user = UserService.create_user(nome, cnpj, email, celular, senha)

            return make_response(jsonify({
                "mensagem": "Cadastro realizado com sucesso",
                "usuario": user.to_dict()
            }), 200)

        return render_template('cadastro.html')

    @staticmethod
    def register_userJson():
        data = request.get_json()
        nome = data.get('nome')
        cnpj = data.get('cnpj')
        email = data.get('email')
        celular = data.get('celular')
        senha = data.get('senha')

        if not nome or not cnpj or not email or not celular or not senha:
                return make_response(jsonify({"erro": "Todos os campos são obrigatórios"}), 400)

        user = UserService.create_user(nome, cnpj, email, celular, senha)
        
        return make_response(jsonify({
            "mensagem": "User salvo com sucesso",
            "usuarios": user.to_dict()
        }), 200)


    @staticmethod
    def activate_user():
        pass


    @staticmethod
    def login_user():
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')

        