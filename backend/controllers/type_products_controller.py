from flask import jsonify
from models.type_product import (
    get_all_type_of_products,
)


def get_all_type_of_products_controller():
    type_products = get_all_type_of_products()
    return jsonify(type_products), 200
