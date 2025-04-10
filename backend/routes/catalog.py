from flask import Blueprint, jsonify, request
from models.product import get_all_products, get_product_by_id, create_product

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


@catalog_bp.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    required_fields = [
        "name",
        "description",
        "price",
        "stock",
        "id_brand",
        "id_type_product",
    ]
    if not all(field in data for field in required_fields):
        return {"message": "Faltan campos requeridos"}, 400

    new_id = create_product(data)
    if new_id:
        return {"message": "Producto creado exitosamente", "product_id": new_id}, 201
    else:
        return {"message": "Error al crear el producto"}, 500


# ?filter by category or product type should be do it here or in the frontend?
