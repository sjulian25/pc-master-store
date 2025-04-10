from db_connection import get_connection
from flask import jsonify, session
import MySQLdb.cursors,hashlib,secrets
from werkzeug.security import generate_password_hash, check_password_hash


#crear un nuevo usuario
def register_user(data):
    cnn = get_connection()
    if cnn:
        cursor=cnn.cursor(MySQLdb.cursors.DictCursor)
        salt = secrets.token_hex(16)
        raw_password = data['user_password']+salt
        hashed_password = hashlib.sha256(raw_password.encode('utf-8')).hexdigest()
        recovery_token = secrets.token_hex(32)
        insertardatos = 'INSERT INTO users (username,user_password,email,salt,recovery_token) values(%s,%s,%s,%s,%s)'
        values=(
            data['username'],
            hashed_password,
            data['email'],
            salt,
            recovery_token
        )
        cursor.execute(insertardatos,values)
        cnn.commit()
        new_id=cursor.lastrowid
        cursor.close()
        cnn.close()
        return new_id
    return None

#consultar un usuario por el email
def get_user_by_email(email):
    try:
        cnn = get_connection()
        if not cnn:
            return None
        
        with cnn.cursor() as cursor:
            search="SELECT id_users,username,email,last_login FROM users WHERE email = %s"
            cursor.execute(search,(email,))
            user = cursor.fetchone()
            
        cnn.close()
        return user
        
    except Exception as e:
        print(f'Errot searching user by email: {e}')
        return None
    

#consultar el cliente por el id
def get_user_by_id(id_users):
    try:
        cnn=get_connection()
        with cnn.cursor() as cursor:
            search="SELECT username,email,last_login FROM users WHERE id_users = %s"
            cursor.execute(search,(id_users,))
            user = cursor.fetchone()

        cnn.close()
        return user
    
    except Exception as e:
        print(f'Errot searching user by id: {e}')
        return None