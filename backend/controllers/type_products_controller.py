from flask import jsonify
from models.type_product import (
    get_all_type_of_products,
    get_inactive_type_products,
    get_type_product_by_id,
    create_type_product,
)


def get_all_type_of_products_controller():
    type_products = get_all_type_of_products()
    return jsonify(type_products), 200


def get_inactive_type_products_controller():
    response = get_inactive_type_products()
    if not response:
        return jsonify({"message": "There's no deleted type products"}), 200
    return jsonify(response), 200


def get_type_product_by_id_controller(id_type_product):
    response = get_type_product_by_id(id_type_product)

    if response:
        return jsonify(response), 200
    return jsonify({"message": "type product not found"}), 404


def create_type_product_controller(data):
    status, response = create_type_product()
    if not status:
        return {"message": "request failed", "detail": response}, 500
    if not response:
        return {"message": "request failed", "detail": response}, 400
    return {"message": "type product created", "detail": response}


# TODO: update type product using id to identify it
def update_type_product_controller(id_type_product, data):
    pass


# TODO: delete type product using id_type_product
def delete_type_product_controller(id_type_product):
    pass


# TODO: restore an type product by its id
def restore_type_product_controller(id_type_product):
    pass
