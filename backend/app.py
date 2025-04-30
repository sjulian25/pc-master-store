from flask import Flask
from flask_cors import CORS
from routes.catalog import catalog_bp
from routes.auth import auth_bp
from flasgger import Swagger
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("API_KEY")
swagger = Swagger(app, template_file=os.path.join("docs", "swagger.yml"))
CORS(app, supports_credentials=True)

app.register_blueprint(catalog_bp, url_prefix="/api/catalog")
app.register_blueprint(auth_bp, url_prefix="/api/auth")


if __name__ == "__main__":
    app.run(debug=True)
