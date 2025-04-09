from flask import Blueprint,Flask,jsonify,request
import MySQLdb
import MySQLdb.cursors
from db_connection import conexiondb

category_bp = Blueprint("category", __name__)
cnn = conexiondb()

@category_bp.route("/products")
def get_category():
    try:
        con = MySQLdb.connect(**cnn,cursorclass=MySQLdb.cursors.DictCursor)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM category')
        categories = cursor.fetchall()
        con.close()
        return jsonify(categories)
    except Exception as e:
        return jsonify({'error': str(e)})
    
