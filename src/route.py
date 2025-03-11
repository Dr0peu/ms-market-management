from flask import Flask, jsonify

app = Flask (__name__)

@app.route('/')
def home():
    return jsonify(message='Home')

@app.route('/cadastro')
def cadastro():
    return jsonify(message='Cadastro')

if __name__ == '__main__':
    app.run(debug=True)