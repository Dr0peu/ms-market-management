from flask import Flask, jsonify, render_template


app = Flask (__name__)

@app.route('/')
def home():
    return jsonify(message='Home')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)