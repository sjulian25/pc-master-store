from flask import Blueprint, jsonify
from models.product import get_all_products, get_product_by_id  # ejemplo

catalog_bp = Blueprint("catalog", __name__)


@catalog_bp.route("/products", methods=["GET"])
def list_products():
    products = get_all_products()
    return jsonify(products)


@catalog_bp.route("/products/<int:id_product>", method=["GET"])
def get_product(id_product):
    product = get_product_by_id(id_product)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404
