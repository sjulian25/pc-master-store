import os
from dotenv import load_dotenv

load_dotenv()


def conexiondb():
    return{
        'host':os.getenv('host'),
        'user':os.getenv('user'),
        'password':os.getenv('password'),
        'database':os.getenv('database')
    }