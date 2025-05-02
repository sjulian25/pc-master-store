from flask import jsonify, request
from models.brand import (
    get_brands,
    get_brands_by_id,
    delete_brand_by_id,
    get_inactive_brands,
    insert_brand,
    get_products_by_brand,
    activate_brand_by_id,
    update_brand,
)


def get_brands_controller():
    success, result = get_brands()
    if not success:
        return {
            "Status": "Error",
            "Message": "Eror en el servidor",
            "detailed": result,
        }, 500
    if not result:
        {
            "Status": "Success",
            "Message": "No hay marcas por mostrar",
            "detailed": result,
        }, 404
    return {
        "Status": "Success",
        "Message": "Marcas disponibles",
        "detailed": result,
    }, 200


def get_brands_by_id_controller(id_brand):
    success, result = get_brands_by_id(id_brand)
    if not success:
        {"Status": "Error", "Message": "Eror en el servidor", "detailed": result}, 500
    if not result:
        {
            "Status": "Success",
            "Message": "No se encuentra la marca ingresada",
            "detailed": result,
        }, 404
    return {"Status": "Success", "Message": "Marca consultada", "detailed": result}, 200


def delete_brand_controller(id_brand):
    success, result = delete_brand_by_id(id_brand)
    if not success:
        {"Status": "Error", "Message": "Eror en el servidor", "detailed": result}, 500
    if result == 0:
        {"Status": "Succes", "Message": "NOT FOUND", "detailed": result}, 404
    return {"Status": "Succes", "Message": "Datos eliminados", "detailed": result}, 200


def activate_brand_controller(id_brand):
    success, result = activate_brand_by_id(id_brand)
    if not success:
        {"Status": "Error", "Message": "Eror en el servidor", "detailed": result}, 500
    if result == 0:
        {"Status": "Succes", "Message": "NOT FOUND", "detailed": result}, 404
    return {
        "Status": "Succes",
        "Message": "Datos reestablecidos",
        "detailed": result,
    }, 200


# ! Este controlador no hace parte de la lógica de brand
def get_products_by_brand_controller(id_brand):
    success, result = get_products_by_brand(id_brand)
    if not success:
        return {
            "Status": "error",
            "message": "Fallo del servidor",
            "detailed": result,
        }, 500
    if not result:
        return {
            "Status": "Success",
            "message": "No hay productos con esa marca",
            "detailed": result,
        }, 404
    return {
        "Status": "success",
        "message": "Productos consultados",
        "detailed": result,
    }, 200


def insert_brand_controller():
    datos = request.json  # Obtiene el cuerpo de la solicitud
    name = datos.get("name")  # Extrae el nombre de la marca

    if not name:  # Verifica si el nombre está presente
        return (
            jsonify({"error": "El nombre de la marca es requerido."}),
            400,
        )  # Respuesta 400 si falta el nombre
    if isinstance(name, str):
        name = [name]

    # Llama a la función insert_brand y pasa solo el nombre
    response, status_code = insert_brand(
        name
    )  # Llama a insert_brand pasando solo el nombre
    return jsonify(response), status_code  # Devuelve la respuesta como JSON


def update_brand_controller(id_brand, data):
    response = update_brand(id_brand, data)
    if response:
        return jsonify({"message": "brand updated"}), 200
    else:
        return jsonify(response), 500


def get_inactive_brands_controller():
    response = get_inactive_brands()
    if not response:
        return jsonify({"message": "There's no deleted brands"}), 200
    return jsonify(response), 200
