from flask import jsonify
from utils.validators import validate_product_data
from models.product import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
    get_inactive_products,
    restore_product,
)


def get_all_products_controller():
    products = get_all_products()
    return jsonify(products), 200


def get_product_by_id_controller(id_product):
    product = get_product_by_id(id_product)
    if product:
        return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404


def create_product_controller(data):
    is_valid, result = validate_product_data(data)

    if not is_valid:
        return jsonify({"message": result}), 400 if "not found" in result else 404

    new_id = create_product(result)
    if new_id:
        return (
            jsonify({"message": "Product created successfully", "id_product": new_id}),
            201,
        )
    else:
        return jsonify({"message": "Error in create product"}), 500


def update_product_controller(id_product, data):
    is_valid, result = validate_product_data(data, for_update=True)

    if not is_valid:
        return jsonify({"message": result}), 400

    existing_product = get_product_by_id(id_product)
    if not existing_product:
        return jsonify({"message": "Product not found"}), 404

    updated = update_product(id_product, result)
    if updated:
        return jsonify({"message": "Product updated successfully"}), 200
    else:
        return jsonify({"message": "Couldn't update the product"}), 500


def delete_product_controller(id_product):
    exising_product = get_product_by_id(id_product)
    if not exising_product:
        return jsonify({"message": "Product not found"}), 404

    delete = delete_product(id_product)
    if delete:
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"message": "Couldn't delete the product"}), 500


def get_inactive_products_controller():
    products = get_inactive_products()
    return jsonify(products), 200


def restore_product_controller(id_product):
    restored = restore_product(id_product)
    if restored:
        return jsonify({"message": "Product restored"}), 200
    return jsonify({"message": "Couldn't restore product"}), 404
