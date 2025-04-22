from flask import Flask
from flask_cors import CORS
from routes.catalog import catalog_bp
from flasgger import Swagger
import os

app = Flask(__name__)
swagger = Swagger(app, template_file=os.path.join("docs", "swagger.yml"))
CORS(app)

app.register_blueprint(catalog_bp, url_prefix="/api/catalog")

if __name__ == "__main__":
    app.run(debug=True)
