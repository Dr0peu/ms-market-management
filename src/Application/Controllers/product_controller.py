from flask import request, jsonify, make_response
from Application.Service.product_service import ProductService


class ProductController:
    @staticmethod
    def register_productJson():
        data = request.get_json()
        nome = data.get('nome')
        preco = data.get('preco')
        quantidade = data.get('quantidade')
        status = data.get('status')
        imagem = data.get('imagem')

        campos = ['nome', 'preco', 'quantidade', 'status', 'imagem']
        falta_campo = [campo for campo in campos if not data.get(campo)]

        if falta_campo:
            return make_response(jsonify({"erro": "Todos os campos são obrigatórios"}), 400)

        product = ProductService.create_product(nome, preco, quantidade, status, imagem)
        
        return make_response(jsonify({
            "mensagem": "Produto criado com sucesso",
            "produto": product.to_dict()
        }), 200)

    
    

        