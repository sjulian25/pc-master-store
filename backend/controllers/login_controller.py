from flask import jsonify
from models.user import (
    register_user,
    get_user_by_email,
    get_user_by_id,
    get_login,
    update_user,
    get_all_user
)

def register_user_controller(data):
    if 'username' not in data or 'email' not in data or 'user_password' not in data:
        return {'message': 'Missing required fields'}, 400

    # Comprobar si ya existe el email
    existing_user = get_user_by_email(data['email'])
    if existing_user:
        return jsonify({'message': 'Email already registered'}), 409

    try:
        new_user_id = register_user(data)
        return {
            'message': 'User registered successfully',
            'user_id': new_user_id
        }, 201
    except Exception as e:
        return jsonify({'message': f'Error registering user: {str(e)}'}), 500
    
# Controlador de login de usuario
def login_user_controller(email, password):
    from backend.models.user import get_login  # se importa aquí para evitar conflicto circular

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    return get_login(email, password)

# Controlador para consultar todos los usuarios
def get_all_users_controller():
    users = get_all_user()
    if users:
        return jsonify(users), 200
    else:
        return jsonify({'message': 'No users found'}), 404
    
# Controlador para buscar un usuario por ID
def get_user_by_id_controller(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found'}), 404
    
# Controlador para actualizar usuario
def update_user_controller(user_id, data):
    if 'username' not in data or 'email' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    return update_user(user_id, data)