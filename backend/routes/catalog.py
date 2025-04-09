from flask import Blueprint,Flask,jsonify,request
from models.category import get_category

category_bp = Blueprint("category", __name__)

@category_bp.route("/category")
def list_category():
    categories = get_category()
    return jsonify(categories)
