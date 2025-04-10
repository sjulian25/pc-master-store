from flask import Flask,request, jsonify
import MySQLdb.cursors
from db_connection import get_connection
def brand_exists(id_brand):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_brand FROM brand WHERE id_brand = %s", (id_brand),)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    return False
#funcion para consultar tabla brand
def get_brands():
    
    try:
        conn = get_connection()
        if conn is None:
            return {'error': 'No se pudo establecer conexión con la base de datos'}, 500
        
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM brand WHERE is_active=1")
        brands = cursor.fetchall()  # Trae todos los datos

        cursor.close()
        conn.close()

        return True, brands  # Retorna la lista de marcas

    except Exception as e:
        return False,str(e)
def get_brands_by_id(id_brand):
    
    try:
        conn = get_connection()
        if conn is None:  # Verifica si hay errores en la conexión
            return jsonify({'error': 'No se pudo establecer conexión con la base de datos'}), 500
        
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)  # Devuelve la información en formato diccionario
        cursor.execute("SELECT name FROM brand WHERE id_brand=%s AND is_active=1", (id_brand,))  # Ejecuta la consulta SQL
        brand = cursor.fetchone()  # Trae el dato consultado únicamente
        cursor.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión

        return True, brand 
    except Exception as e:
        return False,str(e)
    
def delete_brand_by_id(id_brand):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE brand SET is_active=0 WHERE id_brand=%s"
        cursor.execute(query, (id_brand,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return True, affected_rows
    except Exception as e:
        return False, str(e)
    
def activate_brand_by_id(id_brand):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE brand SET is_active=1 WHERE id_brand=%s"
        cursor.execute(query, (id_brand,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return True, affected_rows
    except Exception as e:
        return False, str(e)
    
    
def insert_brand(name):
    try:
        conn = get_connection()
        if conn is None:
            return {'error': 'No se pudo conectar a la base de datos'}, 500

        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # 1. Obtener nombres ya existentes
        format_strings = ','.join(['%s'] * len(name))
        select_brand = f"SELECT name FROM brand WHERE name IN ({format_strings})"
        cursor.execute(select_brand, name)
        existentes = [row['name'].lower() for row in cursor.fetchall()]

        # 2. Filtrar marcas nuevas
        nuevas = [n for n in name if n.lower() not in existentes]

        # 3. Informar marcas existentes
        if existentes:
            message = f'Las siguientes marcas ya existen: {", ".join(existentes)}.'
        else:
            message = 'No se encontraron marcas existentes.'

        # 4. Insertar solo las nuevas marcas
        if nuevas:
            insert_query = 'INSERT INTO brand (name) VALUES (%s)'
            valores = [(n,) for n in nuevas]
            cursor.executemany(insert_query, valores)
            conn.commit()
            message += f' Se agregaron {len(nuevas)} marca(s) nueva(s): {", ".join(nuevas)}.'
        else:
            message += ' No se agregaron nuevas marcas.'

        conn.commit()
        cursor.close()
        conn.close()
        return {
            'message': message
        }, 200

    except Exception as e:
        return {'error': str(e)}, 500
def get_products_by_brand(id_brand):
    try:
        conn = get_connection()
        if conn is None:
            return jsonify({'error': 'No se pudo establecer conexión con la base de datos'}), 500
        
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # Obtener productos de la marca específica
        cursor.execute("SELECT p.*, b.name AS brand_name FROM product p JOIN brand b ON p.id_brand = b.id_brand WHERE b.id_brand = %s", (id_brand,))
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return True, products
        
    except Exception as e:
        return False,str(e) # Manejo de errores