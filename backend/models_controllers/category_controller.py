from models.category import get_all_category,create_category,delete_category,update_category,activate_category


def process_get_all_category(id_category):
    success, result = get_all_category(id_category)
    
    if not success:
        return{
            "status":"error",
            "message":"Error al obtener categorias",
            "detail": result
        }, 500
    
    if not result:
        return{
            "status":"success",
            "message":"No hay categorias disponibles",
            "detail":[],
        }, 200
    
    return {
        "status":"success",
        "message":"categorias obtenidad exitosamente",
        "detail": result,
        "count": len(result)
    }, 200

def process_create_category():
    success, result = create_category()
    
    if not success:
        return{
            "status":"error",
            "message":"No se pudo crear la categoria",
            "detail": result,
        },500
    
    if not result:
        return{
            "status":"error",
            "message":"No se pudo crear la categoria",
            "detail": result,
        },400
    
    return {
        "status":"success",
        "message":"Categoria creada exitosamente",
        "detail": result,
    },200

def process_delete_category(id_category):
    success, result = delete_category(id_category)
    
    if not success:
        return{
            "status":"error",
            "message":"Error al eliminar la categoria",
            "detail": result,
        }, 500
    
    if result == 0:
        return{
            "status":"not_found",
            "message":"ID no encontrada",
            "detail": result,
        }, 404
    
    return{
        "status":"success",
        "message":f"ID {id_category} Eliminado exitosamente",
        "detail": result,
    }, 200

def process_activate_category(id_category):
    success, result = activate_category(id_category)
    
    if not success:
        return{
            "status":"error",
            "message":"Error al Activar la categoria",
            "detail": result,
        }, 500
    
    if result == 0:
        return{
            "status":"not_found",
            "message":"ID no encontrada",
            "detail": result,
        }, 404
    
    return{
        "status":"success",
        "message":f"ID {id_category} Activado exitosamente",
        "detail": result,
    }, 200

def process_update_category(id_category):
    success, result = update_category(id_category)
    
    if not success:
        return{
            "status":"error",
            "message":"Error al actualizar",
            "detail": result,
        }, 500
    
    if result == 0:
        return{
            "status":"not_found",
            "message": f"ID {id_category} No ha Sido encontrada",
            "detail": result,
        }, 204
    
    return{
        "status":"success",
        "message": f"ID {id_category} Ha sido actualizada con exito",
        "detail": result,
    }, 200
