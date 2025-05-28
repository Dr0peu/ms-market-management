from flask import request, jsonify, make_response
from Application.Service.auth_service import AuthService
from Application.Service.product_service import ProductService


class ProductController:
    @staticmethod
    def register_productJson():
        user_data = AuthService.decode_token(request)
        if not user_data:
            return make_response(jsonify({"erro": "Token inválido ou expirado"}), 401)
        
        data = request.get_json()
        nome = data.get('nome')
        preco = data.get('preco')
        quantidade = data.get('quantidade')
        status = data.get('status', False)
        imagem = data.get('imagem')

        campos_obrigatorios = ['nome', 'preco', 'quantidade']
        falta_campo = [campo for campo in campos_obrigatorios if data.get(campo) is None]

        if falta_campo:
            return make_response(jsonify({"erro": f"Campos obrigatórios faltando: {', '.join(falta_campo)}"}), 400)
        
        id_user = user_data['user_id']

        product = ProductService.create_product(id_user, nome, preco, quantidade, status, imagem)
        
        return make_response(jsonify({
            "mensagem": "Produto criado com sucesso",
            "produto": product.to_dict()
        }), 201)
    
    @staticmethod
    def list_products():
        user_data = AuthService.decode_token(request)
        if not user_data:
            return make_response(jsonify({"erro": "Token inválido ou expirado"}), 401)
        
        id_user = user_data['user_id']
        products = ProductService.list_products_by_user(id_user)
        return make_response(jsonify(products), 200)
    
    @staticmethod
    def get_product(id_product):
        user_data = AuthService.decode_token(request)
        if not user_data:
            return make_response(jsonify({"erro": "Token inválido ou expirado"}), 401)
        
        id_user = user_data['user_id']
        product = ProductService.get_product_by_id(id_product, id_user)

        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado ou você não tem permissão"}), 404)
        
        return make_response(jsonify(product.to_dict()), 200)
    
    @staticmethod
    def update_product(id_product):
        user_data = AuthService.decode_token(request)
        if not user_data:
            return make_response(jsonify({"erro": "Token inválido ou expirado"}), 401)

        id_user = user_data['user_id']
        data = request.get_json()

        product = ProductService.update_product(
            id_product=id_product,
            id_user=id_user,
            nome=data.get('nome'),
            preco=data.get('preco'),
            quantidade=data.get('quantidade'),
            status=data.get('status'),
            imagem=data.get('imagem')
        )

        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado ou você não tem permissão"}), 404)

        return make_response(jsonify({
            "mensagem": "Produto atualizado com sucesso",
            "produto": product.to_dict()
        }), 200)
    
    @staticmethod
    def delete_product(id_product):
        user_data = AuthService.decode_token(request)
        if not user_data:
            return make_response(jsonify({"erro": "Token inválido ou expirado"}), 401)
        
        id_user = user_data['user_id']
        deleted = ProductService.delete_product_by_id(id_product, id_user)

        if not deleted:
            return make_response(jsonify({"erro": "Produto não encontrado ou você não tem permissão"}), 404)
        return make_response(jsonify({"mensagem": "Produto excluído com sucesso"}), 200)

    
    

        