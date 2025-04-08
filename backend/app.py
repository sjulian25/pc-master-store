from flask import Flask
from flask_cors import CORS
from routes.catalog import catalog_bp

app = Flask(__name__)
app(CORS)






if __name__ == "__main__":
    app.run(debug = True)