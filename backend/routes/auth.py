from flask import request,Blueprint,jsonify
from models.user import register_user,get_user_by_email,get_user_by_id,get_all_user,get_login


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

@auth_bp.route('/search/<string:email>', methods=['GET'])
def search_email_user(email):
    
    user=get_user_by_email(email)

    if user:
        user_data={
            "id":user[0],
            "name":user[1],
            "email":user[2],
            "last_login":user[3]
        }
        return jsonify(user_data), 200
    else:
        return jsonify({'message':'User not found'}), 404
    
@auth_bp.route('/search/<int:id_users>', methods=['GET'])
def search_id_user(id_users):
    
    user=get_user_by_id(id_users)

    if user:
        user_data={
            "name":user[0],
            "email":user[1],
            "last_login":user[2]
        }
        return jsonify(user_data), 200
    else:
        return jsonify({'message':'User not found'}), 404
    
@auth_bp.route('/login', methods=['POST'])
def login_user():
    data=request.get_json()
    user_email=data.get('email')
    user_password=data.get('user_password')
    if not user_email or not user_password:
        return ({'message':'email and password are requerided'}), 400

    result, status_code = get_login(user_email, user_password)
    return result, status_code
    
@auth_bp.route('/search/all', methods=['GET'])
def search_all_user():
    
    users=get_all_user()

    if users:
        return jsonify(users), 200
    else:
        return jsonify({'message':'Users not found'}), 404








