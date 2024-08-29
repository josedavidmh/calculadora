from flask import Flask
from flask_cors import CORS

from Rutas.operaciones_basicas import operaciones_basicas
from Rutas.operaciones_adicionales import operaciones_adicionales
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(operaciones_basicas)
    app.register_blueprint(operaciones_adicionales)
    return app