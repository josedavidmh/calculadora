from flask import Blueprint     ## Flask es un microfamework para el uso de python en la web
from flask import jsonify   ## Para retornar las respuestas en formato json
from flask import render_template
## Suma
operaciones_basicas = Blueprint('operaciones_basicas', __name__)

@operaciones_basicas.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@operaciones_basicas.route('/suma', methods=['GET'])
@operaciones_basicas.route('/suma/<float:numero1>/<float:numero2>', methods=['GET'])
@operaciones_basicas.route('/suma/<int:numero1>/<int:numero2>', methods=['GET'])
@operaciones_basicas.route('/suma/<int:numero1>/<float:numero2>', methods=['GET'])
@operaciones_basicas.route('/suma/<float:numero1>/<int:numero2>', methods=['GET'])

def suma(numero1=0,numero2=0):
    resultado=numero1+numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
         "Resultado":resultado,
         "Operacion":"suma",
     }
    return jsonify(data)

## Resta
@operaciones_basicas.route("/resta/<float:numero1>/<float:numero2>")
@operaciones_basicas.route("/resta/<int:numero1>/<int:numero2>")
@operaciones_basicas.route("/resta/<int:numero1>/<float:numero2>")
@operaciones_basicas.route("/resta/<float:numero1>/<int:numero2>")
def resta(numero1=0,numero2=0):
    resultado=numero1-numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
         "Resultado":resultado,
         "Operacion":"resta",
     }
    return jsonify(data)

## multiplicación
@operaciones_basicas.route("/multiplicacion/<float:numero1>/<float:numero2>")
@operaciones_basicas.route("/multiplicacion/<int:numero1>/<int:numero2>")
@operaciones_basicas.route("/multiplicacion/<float:numero1>/<int:numero2>")
@operaciones_basicas.route("/multiplicacion/<int:numero1>/<float:numero2>")
def multiplicacion(numero1=0,numero2=0):
    resultado=numero1*numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
         "Resultado":resultado,
         "Operacion":"multiplicación",
     }
    return jsonify(data)

## División
@operaciones_basicas.route("/division/<float:numero1>/<float:numero2>")
@operaciones_basicas.route("/division/<int:numero1>/<int:numero2>")
@operaciones_basicas.route("/division/<float:numero1>/<int:numero2>")
@operaciones_basicas.route("/division/<int:numero1>/<float:numero2>")
def division(numero1=0,numero2=0):
    resultado=numero1/numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
         "Resultado":resultado,
         "Operacion":"División",
     }
    return jsonify(data)

