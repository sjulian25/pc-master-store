import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        connection = MySQLdb.connect(
        host = os.getenv('host'),
        user = os.getenv('user'),
        password = os.getenv('password'),
        database = os.getenv('database'),
        charset = 'utf8mb4'
        )
        return connection
    except MySQLdb.Error as e:
        print({"connection refuse": str(e)})
        return None 