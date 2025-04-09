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

@category_bp.route("/delete/products/<int:id_category>", methods=['DELETE'])
def delete_category(id_category):
    try:
        con = MySQLdb.connect(**cnn,cursorclass=MySQLdb.cursors.DictCursor)
        cursor = con.cursor()
        delete = ('DELETE FROM category WHERE id_category = %s')
        cursor.execute(delete,(id_category,))
        con.commit()
        con.close()
        if cursor.rowcount == 0:
            return jsonify({'Mensaje': 'ID no encontrado'})
        return jsonify({'Mensaje':f'Categoria con ID {id_category} eliminada'})
    except Exception as e:
        return jsonify({'Error': str(e)})

@category_bp.route("/update/products/<int:id_category>", methods=['PUT'])
def update_category(id_category):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    try:
        con = MySQLdb.connect(**cnn,cursorclass=MySQLdb.cursors.DictCursor)
        cursor = con.cursor()
        update = 'UPDATE category SET name = %s,description = %s WHERE id_category = %s'
        cursor.execute(update,(name,description,id_category))
        con.commit()
        con.close()
        if cursor.rowcount == 0:
            return jsonify({'Mensaje': 'ID no encontrado'})
        return jsonify({'Mensaje': f'Categoria con ID {id_category} actualizada'})
    except Exception as e:
        return jsonify({'Error': str(e)})