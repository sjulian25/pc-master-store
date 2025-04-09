from flask import Flask
from flask_cors import CORS
from routes.catalog import category_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(category_bp, url_prefix='/api/catalog/')




if __name__ == "__main__":
    app.run(debug = True)