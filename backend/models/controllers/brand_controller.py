from flask import jsonify, request
from models.brand import (
    get_brands,
    get_brands_by_id,
    delete_brand_by_id,
    insert_brand,
    get_products_by_brand,
    activate_brand_by_id
)


def process_get_brands():
    success, result = get_brands()
    if not success:
        return {
            "Status": "Error",
            "Message": "Eror en el servidor",
            "detailed": result
        }, 500
    if not result:
        {
        "Status": "Success",
        "Message": "No hay marcas por mostrar",
        "detailed": result   
        }, 404
    return {
        "Status": "Success",
        "Message": "Marcas disponibles",
        "detailed": result   
        }, 200




def procces_get_brands_by_id(id_brand):
    success, result=get_brands_by_id(id_brand)
    if not success:
        {
            "Status": "Error",
            "Message": "Eror en el servidor",
            "detailed": result
        }, 500
    if not result:
        {
            "Status": "Success",
            "Message": "No se encuentra la marca ingresada",
            "detailed": result
        }, 404
    return {
        "Status": "Success",
        "Message": "Marca consultada",
        "detailed": result
    }, 200


def process_delete_brand(id_brand):
    success, result= delete_brand_by_id(id_brand)
    if not success:{
            "Status": "Error",
            "Message": "Eror en el servidor",
            "detailed": result
        }, 500
    if result == 0:
        {
            "Status": "Succes",
            "Message": "NOT FOUND",
            "detailed": result
        }, 404
    return {
            "Status": "Succes",
            "Message": "Datos eliminados",
            "detailed": result
        }, 200

def process_activate_brand(id_brand):
    success, result= activate_brand_by_id(id_brand)
    if not success:{
            "Status": "Error",
            "Message": "Eror en el servidor",
            "detailed": result
        }, 500
    if result == 0:
        {
            "Status": "Succes",
            "Message": "NOT FOUND",
            "detailed": result
        }, 404
    return {
            "Status": "Succes",
            "Message": "Datos reestablecidos",
            "detailed": result
        }, 200





def process_get_products_by_brand(id_brand):
    success, result= get_products_by_brand(id_brand)
    if not success:
        return {
            "Status": "error",
            "message": "Fallo del servidor",
            "detailed": result
        }, 500
    if not result:
        return {
            "Status": "Success",
            "message": "No hay productos con esa marca",
            "detailed": result
        },404
    return {
            "Status": "success",
            "message": "Productos consultados",
            "detailed": result
            },200
    




def process_insert_brand():
    datos = request.json  # Obtiene el cuerpo de la solicitud
    name = datos.get('name')  # Extrae el nombre de la marca

    if not name:  # Verifica si el nombre está presente
        return jsonify({'error': 'El nombre de la marca es requerido.'}), 400  # Respuesta 400 si falta el nombre
    if isinstance(name, str):
        name = [name]

    # Llama a la función insert_brand y pasa solo el nombre
    response, status_code = insert_brand(name)  # Llama a insert_brand pasando solo el nombre
    return jsonify(response), status_code  # Devuelve la respuesta como JSON