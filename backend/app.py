from flask import Flask
from flask_cors import CORS
from models.category import category_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(category_bp, url_prefix='/category')



if __name__ == "__main__":
    app.run(debug = True)