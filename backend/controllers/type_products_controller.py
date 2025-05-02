from flask import jsonify
from models.type_product import (
    delete_type_product,
    get_all_type_of_products,
    get_inactive_type_products,
    get_type_product_by_id,
    create_type_product,
    type_product_exists,
    update_type_product,
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
    status, response = create_type_product(data)
    if not status:
        return jsonify({"message": "request failed", "detail": response}), 500
    if not response:
        return jsonify({"message": "request failed"}), 400
    return (
        jsonify(
            {"message": "type product created", "detail": f"id_product: {response}"}
        ),
        201,
    )


def update_type_product_controller(id_type_product, data):
    response = update_type_product(id_type_product, data)
    if response:
        return (
            jsonify({"message": "type product updated"}),
            200,
        )
    else:
        return jsonify({"message": "update query failed"}), 500


def delete_type_product_controller(id_type_product):
    if not type_product_exists(id_type_product):
        return jsonify({"message": "type product not found"}), 404

    response = delete_type_product(id_type_product)
    if response:
        return jsonify({"message": "type product deleted"}), 200
    else:
        return jsonify(response), 500


# TODO: restore an type product by its id
def restore_type_product_controller(id_type_product):
    pass
