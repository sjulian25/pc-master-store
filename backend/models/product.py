import MySQLdb.cursors
from db_connection import get_connection


def get_all_products():
    conn = get_connection()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM product WHERE is_active = 1")
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


def create_product(data):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = """
            INSERT INTO product (name, description, price, stock, id_brand, id_type_product)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            data["name"],
            data["description"],
            data["price"],
            data["stock"],
            data["id_brand"],
            data["id_type_product"],
        )
        cursor.execute(sql, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id
    return None


def update_product(id_product, data):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = """
            UPDATE product
            SET name = %s, description = %s, price = %s, stock = %s,
                id_brand = %s, id_type_product = %s
            WHERE id_product = %s
        """
        values = (
            data.get("name"),
            data.get("description"),
            data.get("price"),
            data.get("stock"),
            data.get("id_brand"),
            data.get("id_type_product"),
            id_product,
        )
        cursor.execute(sql, values)
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected > 0
    return False


# This is a logic delete, it not truly remove a field, just chanche its state to false
def delete_product(id_product):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        sql = """ 
            UPDATE product SET is_active = 0 WHERE id_product = %s
        """
        cursor.execute(sql, (id_product,))
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected > 0
    return False


# * ONLY FOR ADMIN USERS
def get_all_products(include_inactive=False):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        if include_inactive:
            cursor.execute("SELECT * FROM product")
        else:
            cursor.execute("SELECT * FROM product WHERE is_active = 1")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products
    return []


def get_inactive_products():
    conn = get_connection()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM product WHERE is_active = 0")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products
    return []


def restore_product(id_product):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "UPDATE product SET is_active = 1 WHERE id_product = %s", (id_product,)
        )
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected > 0
    return False
