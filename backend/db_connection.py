import os
import MySQLdb
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        connection = MySQLdb.connect(
            host=os.getenv("host"),
            user=os.getenv("user"),
            passwd=os.getenv("password"),
            db=os.getenv("database"),
            charset="utf8mb4",
        )
        return connection
    except MySQLdb.Error as err:
        print("Connection refuse: ", err)
        return None