from db_connection import get_connection
import MySQLdb.cursors


def type_product_exists(id_type_product):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
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
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM type_product WHERE is_active = 1")
        type_of_products = cursor.fetchall()
        cursor.close()
        conn.close()
        return type_of_products
    return None


def get_inactive_type_products():
    conn = get_connection()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM type_product WHERE is_active = 0")
        type_products = cursor.fetchall()
        cursor.close()
        conn.close()
        return type_products
    return []


def get_type_product_by_id(id_type_product):
    try:
        conn = get_connection()
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM type_product WHERE id_type_product=%s AND is_active=1",
            (id_type_product,),
        )
        type_product = cursor.fetchone()
        cursor.close()
        conn.close()
        return type_product
    except Exception as e:
        return f"Query failed: {str(e)}"


def create_type_product(data):
    try:
        conn = get_connection()
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        sql = """
            INSERT INTO type_product (name, id_category)
            VALUES (%s, %s)
        """
        values = (
            data["name"],
            data["id_category"],
        )
        cursor.execute(sql, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return True, new_id
    except MySQLdb.Error as e:
        return False, e


# TODO: set data as new values in type product by id_type_product
def update_type_product(id_type_product, data):
    pass


# TODO: set is_active=0 in type product by id_type_product
def delete_type_product(id_type_product):
    pass


# TODO: set is_active=1 in type product by id_type_product
def restore_type_product(id_type_product):
    pass
