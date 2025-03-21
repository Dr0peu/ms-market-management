from flask import Flask, jsonify, render_template
from Application.Controllers.user_controller import UserController
from config.data_base import init_db

app = Flask(__name__)
init_db(app)

@app.route('/')
def home():
    return jsonify(message='Home')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return UserController.register_user()

if __name__ == '__main__':
    app.run(debug=True)