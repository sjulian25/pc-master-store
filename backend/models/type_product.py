from db_connection import get_connection
import MySQLdb.cursors


def type_product_exists(id_type_product):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_type_product FROM type_product WHERE id_type_product = %s",
            (id_type_product,),
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    return False


def get_all_type_of_products():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM type_product WHERE is_active = 1")
        type_of_products = cursor.fetchall()
        cursor.close()
        conn.close()
        return type_of_products
    return None


# TODO: hacer metodos de crear, actualizar, y eliminar (lógico) añade la opción de ser restaurado
