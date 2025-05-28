from flask import request, jsonify, make_response
from Application.Service.auth_service import AuthService
from Application.Service.sale_service import SaleService
from Application.Service.product_service import ProductService

class SaleController:
    @staticmethod
    def register_sale():
        user_data = AuthService.decode_token(request)
        if not user_data:
            return make_response(jsonify({"erro": "Token inválido ou expirado"}), 401)

        id_user = user_data['user_id']
        data = request.get_json()

        id_produto = data.get("id_produto")
        quantidade = data.get("quantidade")

        if not id_produto or not quantidade:
            return make_response(jsonify({"erro": "Campos obrigatórios: id_produto, quantidade"}), 400)

        try:
            venda = SaleService.register_sale(id_user, id_produto, quantidade)
        except ValueError as e:
            return make_response(jsonify({"erro": str(e)}), 400)

        return make_response(jsonify({
            "mensagem": "Venda registrada com sucesso!",
            "venda": venda.to_dict()
        }), 201)
    
    @staticmethod
    def sales_report():
        user_data = AuthService.decode_token(request)
        if not user_data:
            return make_response(jsonify({"erro": "Token inválido ou expirado"}), 401)

        id_user = user_data['user_id']
        resumo = SaleService.get_sales_summary_by_user(id_user)

        return make_response(jsonify(resumo), 200)
