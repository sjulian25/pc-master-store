from flask import Blueprint, jsonify, request
from models.product import get_all_products, get_product_by_id
from models.controllers.brand_controller import (
    process_get_brands,
    procces_get_brands_by_id,
    process_delete_brand,
    process_get_products_by_brand,
    process_insert_brand,
    process_activate_brand
)

catalog_bp = Blueprint("catalog", __name__)


@catalog_bp.route("/products", methods=["GET"])
def list_products():
    products = get_all_products()
    return jsonify(products)


@catalog_bp.route("/products/<int:id_product>", methods=["GET"])
def get_product(id_product):
    product = get_product_by_id(id_product)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404


# ?filter by category or product type should be do it here or in the frontend?

#consultar marcas 
@catalog_bp.route('/brand', methods=['POST'])
def create_brand():
    return process_insert_brand()  # Llama al controlador para agregar una nueva marca

@catalog_bp.route('/brand', methods=['GET'])
def get_brands():
    response, status_code= process_get_brands() 
    return jsonify(response), status_code # Llama al controlador para obtener todas las marcas



@catalog_bp.route('/brand/<int:id_brand>', methods=['GET'])
def get_brand_by_id(id_brand):
    response, status_code= procces_get_brands_by_id(id_brand)
    return jsonify(response), status_code  # Llama al controlador para obtener la marca por ID

    





@catalog_bp.route('/brand/delete/<int:id_brand>', methods=['PUT'])
def delete_brand_route(id_brand):
    response, status_code = process_delete_brand(id_brand)
    return jsonify(response), status_code


@catalog_bp.route('/brand/activate/<int:id_brand>', methods=['PUT'])
def activate_brand_route(id_brand):
    response, status_code = process_activate_brand(id_brand)
    return jsonify(response), status_code


@catalog_bp.route('/brand/<int:id_brand>/products', methods=['GET'])
def get_products_by_brand(id_brand):
    response, status_code= process_get_products_by_brand(id_brand) 
    return jsonify(response), status_code  # Llama al controlador para obtener productos por marca