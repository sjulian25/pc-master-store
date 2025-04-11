from flask import Blueprint, jsonify, request
from controllers.product_controller import (
    get_all_products_controller,
    get_product_by_id_controller,
    create_product_controller,
    update_product_controller,
    delete_product_controller,
    get_inactive_products_controller,
    restore_product_controller,
)

catalog_bp = Blueprint("catalog", __name__)


@catalog_bp.route("/products", methods=["GET"])
def list_products():
    return get_all_products_controller()


@catalog_bp.route("/products/<int:id_product>", methods=["GET"])
def get_product(id_product):
    return get_product_by_id_controller(id_product)


@catalog_bp.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    return create_product_controller(data)


@catalog_bp.route("/products/<int:id_product>", methods=["PUT"])
def update_product(id_product):
    data = request.get_json()
    return update_product_controller(id_product, data)


@catalog_bp.route("/products/<int:id_product>", methods=["DELETE"])
def delete_product(id_product):
    return delete_product_controller(id_product)


@catalog_bp.route("/products/inactive", methods=["GET"])
def list_inactive_products():
    return get_inactive_products_controller()


@catalog_bp.route("/products/<int:id_product>/restore", methods=["PATCH"])
def restore_product(id_product):
    return restore_product_controller(id_product)


# ?filter by category or product type should be do it here or in the frontend?
