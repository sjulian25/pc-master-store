import MySQLdb.cursors
from db_connection import get_connection


def get_all_products():
    conn = get_connection()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products
    return []


def get_product_by_id(id_product):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM product WHERE id_product = %s", (id_product,))
        product = cursor.fetchone()
        cursor.close()
        conn.close()
        return product
    return None
