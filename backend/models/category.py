from flask import Flask,jsonify,request
import MySQLdb
import MySQLdb.cursors
from db_connection import get_connection


def get_all_category():
    try:
        con = get_connection()
        cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM category')
        categories = cursor.fetchall()
        con.close()
        return True, categories
    except Exception as e:
        return False,f"Error al obtner categorias {str(e)} " 

def create_category():
        data = request.json
        name = data.get('name')
        description = data.get('description')
        try:
            con = get_connection()
            cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            insertdata = 'INSERT INTO category (name,description) VALUES (%s,%s)'
            cursor.execute(insertdata,(name,description))
            affected_row = cursor.rowcount
            con.commit()
            con.close()
            return True, affected_row
        except Exception as e:
            return False, str(e)

def delete_category(id_category):
    try:
        con = get_connection()
        cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        delete = ('DELETE FROM category WHERE id_category = %s')
        cursor.execute(delete,(id_category,))
        affected_rows = cursor.rowcount
        con.commit()
        con.close()
        return True, affected_rows
    except Exception as e:
        return False, str(e)

def update_category(id_category):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    try:
        con = get_connection()
        cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        update = 'UPDATE category SET name = %s,description = %s WHERE id_category = %s'
        cursor.execute(update,(name,description,id_category))
        affected_rows = cursor.rowcount
        con.commit()
        con.close()
        return True, affected_rows
    except Exception as e:
        return False, str(e)