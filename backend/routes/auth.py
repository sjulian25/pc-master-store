from flask import request,Blueprint
from models.user import register_user


auth_bp=Blueprint("auth",__name__)

@auth_bp.route('/register', methods=['POST'])
def add_user():
    data=request.get_json()
    #validacion basica
    required_field=['username','user_password','email']
    #si no estan todos los datos para cada campos que nosotros marcamos como requeridos
    if not all(field in data for field in required_field):
        return {'message':'fields missing'}, 400
    new_id=register_user(data)
    if new_id:
        #si se ha podido registrar el usuario, el codigo es el 201
        return {'message':'user register succesfuly','user_id':new_id},201
    else:
        return {'message':'user register failed'},500
    
    


