from flask import request, jsonify, make_response
from Application.Service.product_service import ProductService


class ProductController:
    @staticmethod
    def register_productJson():
        data = request.get_json()
        id_user = data.get('id_user')
        nome = data.get('nome')
        preco = data.get('preco')
        quantidade = data.get('quantidade')
        status = data.get('status', False)
        imagem = data.get('imagem')

        campos_obrigatorios = ['id_user', 'nome', 'preco', 'quantidade']
        falta_campo = [campo for campo in campos_obrigatorios if data.get(campo) is None]

        if falta_campo:
            return make_response(jsonify({"erro": f"Campos obrigatórios faltando: {', '.join(falta_campo)}"}), 400)

        product = ProductService.create_product(id_user, nome, preco, quantidade, status, imagem)
        
        return make_response(jsonify({
            "mensagem": "Produto criado com sucesso",
            "produto": product.to_dict()
        }), 201)
    
    @staticmethod
    def list_products():
        products = ProductService.list_products()
        return make_response(jsonify(products), 200)

    
    

        