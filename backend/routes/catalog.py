from flask import Blueprint,jsonify
from models_controllers.category_controller import process_get_all_category,process_create_category,process_delete_category,process_update_category

category_bp = Blueprint("category", __name__)

@category_bp.route("/category")
def list_category():
    response, status_code = process_get_all_category()
    return jsonify(response), status_code

@category_bp.route("/create/category", methods = ['POST'])
def create():
    response, status_code = process_create_category()
    return jsonify(response), status_code

@category_bp.route("/delete/category/<int:id_category>", methods=['DELETE'])
def delete(id_category):
    response, status_code = process_delete_category(id_category)
    return jsonify(response), status_code

@category_bp.route("/update/category/<int:id_category>", methods=['PUT'])
def update(id_category):
    response, status_code = process_update_category(id_category)
    return jsonify(response), status_code