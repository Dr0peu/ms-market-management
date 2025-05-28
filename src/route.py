import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

from Application.Controllers.user_controller import UserController
from Application.Controllers.product_controller import ProductController
from config.data_base import init_db

app = Flask(__name__)
init_db(app)
CORS(app)

# Agora a pasta uploads está na raiz do projeto
UPLOAD_FOLDER = os.path.abspath('uploads')  # caminho absoluto
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Garante que a pasta de uploads exista
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@app.route('/cadastro_produto', methods=['POST'])
def cadastro_produto():
    return ProductController.register_productJson()

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return ProductController.list_products()

@app.route('/produtos/<int:id_product>', methods=['GET'])
def get_product(id_product):
    return ProductController.get_product(id_product)

@app.route('/produtos/<int:id_product>', methods=['PUT'])
def update_product(id_product):
    return ProductController.update_product(id_product)

@app.route('/produtos/<int:id_product>', methods=['DELETE'])
def deletar_produto(id_product):
    return ProductController.delete_product(id_product)

@app.route('/upload_imagem', methods=['POST'])
def upload_imagem():
    if 'imagem' not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    file = request.files['imagem']

    if file.filename == '':
        return jsonify({"erro": "Nome de arquivo inválido"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        url = f"/uploads/{filename}"  # caminho público relativo
        return jsonify({"url": url}), 201

    return jsonify({"erro": "Formato de arquivo não permitido"}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)