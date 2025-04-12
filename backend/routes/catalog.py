from flask import Blueprint, jsonify, request
from controllers.category_controller import (
    get_all_category_controller,
    create_category_controller,
    delete_category_controller,
    update_category_controller,
    activate_category_controller,
)
from controllers.brand_controller import (
    get_brands_controller,
    get_brands_by_id_controller,
    delete_brand_controller,
    get_products_by_brand_controller,
    insert_brand_controller,
    activate_brand_controller,
)

# * CREATE BLUEPRINT
catalog_bp = Blueprint("catalog", __name__)


# * ROUTES FOR CATEGORY
@catalog_bp.route("/category", methods=["GET"])
def list_category():
    response, status_code = get_all_category_controller()
    return jsonify(response), status_code


@catalog_bp.route("/category", methods=["POST"])
def create_category():
    response, status_code = create_category_controller()
    return jsonify(response), status_code


@catalog_bp.route("/category/<int:id_category>", methods=["DELETE"])
def delete_category(id_category):
    response, status_code = delete_category_controller(id_category)
    return jsonify(response), status_code


@catalog_bp.route("/category/restore/<int:id_category>", methods=["PATCH"])
def restore_category(id_category):
    response, status_code = activate_category_controller(id_category)
    return jsonify(response), status_code


# TODO: Mejorar este endpoint ya que si se quiere actualizar un solo campo igual requiere ponerlos todos... (Sugerencia, revisar metodo PATCH)
@catalog_bp.route("/category/<int:id_category>", methods=["PUT"])
def update_category(id_category):
    response, status_code = update_category_controller(id_category)
    return jsonify(response), status_code


# * ROUTES FOR BRAND
@catalog_bp.route("/brand", methods=["GET"])
def get_brands():
    response, status_code = get_brands_controller()
    return (
        jsonify(response),
        status_code,
    )  # Llama al controlador para obtener todas las marcas


@catalog_bp.route("/brand/<int:id_brand>", methods=["GET"])
def get_brand_by_id(id_brand):
    response, status_code = get_brands_by_id_controller(id_brand)
    return (
        jsonify(response),
        status_code,
    )  # Llama al controlador para obtener la marca por ID


@catalog_bp.route("/brand", methods=["POST"])
def create_brand():
    return (
        insert_brand_controller()
    )  # Llama al controlador para agregar una nueva marca


@catalog_bp.route("/brand/<int:id_brand>", methods=["DELETE"])
def delete_brand(id_brand):
    response, status_code = delete_brand_controller(id_brand)
    return jsonify(response), status_code


@catalog_bp.route("/brand/restore/<int:id_brand>", methods=["PATCH"])
def restore_brand(id_brand):
    response, status_code = activate_brand_controller(id_brand)
    return jsonify(response), status_code


# ! Este endpoint no debería ir en las rutas de brand
@catalog_bp.route("/brand/<int:id_brand>/products", methods=["GET"])
def get_products_by_brand(id_brand):
    response, status_code = get_products_by_brand_controller(id_brand)
    return (
        jsonify(response),
        status_code,
    )  # Llama al controlador para obtener productos por marca
