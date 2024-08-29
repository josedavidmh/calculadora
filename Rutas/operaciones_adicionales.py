from flask import Blueprint     ## Flask es un microfamework para el uso de python en la web
import math as mt           ## Libreria que implementa funciones matemáticas
from flask import jsonify   ## Para retornar las respuestas en formato json

operaciones_adicionales = Blueprint('operaciones_adicionales', __name__)

## potenciación
@operaciones_adicionales.route("/potenciacion/<float:numero1>/<float:numero2>")
@operaciones_adicionales.route("/potenciacion/<int:numero1>/<int:numero2>")
@operaciones_adicionales.route("/potenciacion/<int:numero1>/<float:numero2>")
@operaciones_adicionales.route("/potenciacion/<float:numero1>/<int:numero2>")
def potenciacion(numero1=0,numero2=0):
    resultado=numero1**numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
         "Resultado":resultado,
         "Operacion":"potenciación",
     }
    return jsonify(data)

## seno
@operaciones_adicionales.route("/seno/<float:numero1>")
@operaciones_adicionales.route("/seno/<int:numero1>")
def seno(numero1=0):
    resultado=mt.sin(numero1)
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
         "Resultado":resultado,
         "Operacion":"seno",
     }
    return jsonify(data)

## seno
@operaciones_adicionales.route("/coseno/<float:numero1>")
@operaciones_adicionales.route("/coseno/<int:numero1>")
def coseno(numero1=0):
    resultado=mt.cos(numero1)
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
         "Resultado":resultado,
         "Operacion":"coseno",
     }
    return jsonify(data)