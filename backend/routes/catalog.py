from flask import Blueprint,jsonify
from models_controllers.category_controller import process_get_all_category,process_create_category,process_delete_category,process_update_category,process_activate_category

category_bp = Blueprint("catalog", __name__)

@category_bp.route("/category")
def list_category(id_category):
    response, status_code = process_get_all_category(id_category)
    return jsonify(response), status_code

@category_bp.route("/create/category", methods = ['POST'])
def create():
    response, status_code = process_create_category()
    return jsonify(response), status_code

@category_bp.route("/delete/category/<int:id_category>", methods=['PUT'])
def delete(id_category):
    response, status_code = process_delete_category(id_category)
    return jsonify(response), status_code

@category_bp.route("/activate/category/<int:id_category>", methods=['PUT'])
def activate(id_category):
    response, status_code = process_activate_category(id_category)
    return jsonify(response), status_code

@category_bp.route("/update/category/<int:id_category>", methods=['PUT'])
def update(id_category):
    response, status_code = process_update_category(id_category)
    return jsonify(response), status_code