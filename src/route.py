from flask import Flask, jsonify
from Application.Controllers.user_controller import UserController
from config.data_base import init_db

app = Flask(__name__)
init_db(app)

@app.route('/')
def home():
    return jsonify(message='Home')


@app.route('/cadastro', methods=['POST'])
def cadastro():
    return UserController.register_userJson()


@app.route('/ativacao', methods=['POST'])
def ativacao():
    return UserController.activate_user()


@app.route('/login', methods=['POST'])
def login():
    return UserController.login_user()

@app.route('/protegido', methods=['GET'])
def protegido():
    return UserController.protected_route()


if __name__ == '__main__':
    app.run(debug=True)