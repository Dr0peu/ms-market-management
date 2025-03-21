from flask import Flask, jsonify, render_template
from Application.Controllers.user_controller import UserController


app = Flask (__name__)

@app.route('/')
def home():
    return jsonify(message='Home')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return UserController.register_user()

if __name__ == '__main__':
    app.run(debug=True)