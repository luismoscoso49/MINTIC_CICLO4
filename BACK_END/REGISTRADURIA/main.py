from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)  # instancia del servidor
cors = CORS(app)  # instancia de CORS. PERMITE HACER PRUEBAS DESDE LA MISMA MAQUINA QUE EL SERVIDOR


from Controladores.ControladorCandidato import Candidato, ControladorCandidato
from Controladores.ControladorPartido import Partido, ControladorPartido
from Controladores.ControladorMesa import Mesa, ControladorMesa
from Controladores.ControladorResultado import Resultado, ControladorResultado

controladorCandidato= ControladorCandidato()
controladorPartido 	= ControladorPartido()
controladorMesa 	= ControladorMesa()
controladorResultado= ControladorResultado()

#CANDIDATOS
@app.route("/candidatos", methods=['GET'])
def getcandidatos():  # devuelve todos los candidatos
    json = controladorCandidato.index()
    return jsonify(json)
    return "<h3>mensaje en pantalla</h3>"   #   si se qiuere devolver un mnensaje

@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()   #data tiene la info del body. La informacion viene como formato JSON
    json = controladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = controladorCandidato.show(id)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = controladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = controladorCandidato.delete(id)
    return jsonify(json)

#PARTIDOS
@app.route("/partidos", methods=['GET'])
def getpartidos():   #devuelve todos los partidos
    json = controladorPartido.index()
    return jsonify(json)
    return "<h3>mensaje en pantalla</h3>"   #   si se qiuere devolver un mnensaje


@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()   #data tiene la info del body. La informacion viene como formato JSON
    json = controladorPartido.create(data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = controladorPartido.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = controladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = controladorPartido.delete(id)
    return jsonify(json)


#MESAS
@app.route("/mesas", methods=['GET'])
def getmesas():   #devuelve todos los mesas
    json = controladorMesa.index()
    return jsonify(json)
    return "<h3>mensaje en pantalla</h3>"      #si se quiere devolver un mnensaje


@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()   #data tiene la info del body. La informacion viene como formato JSON
    json = controladorMesa.create(data)
    return jsonify(json)



@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    json = controladorMesa.show(id)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = controladorMesa.update(id, data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = controladorMesa.delete(id)
    return jsonify(json)

#RESULTADOS
@app.route("/resultados", methods=['GET'])
def getresultados():   #devuelve todos los resultados
    json = controladorResultado.index()
    return jsonify(json)
    return "<h3>mensaje en pantalla</h3>"      #si se qiuere devolver un mnensaje


@app.route("/resultados", methods=['POST'])
def crearResultado():
    data = request.get_json()   #data tiene la info del body. La informacion viene como formato JSON
    json = controladorResultado.create(data)
    return jsonify(json)



@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = controladorResultado.show(id)
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json = controladorResultado.update(id, data)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultado(id):
    json = controladorResultado.delete(id)
    return jsonify(json)

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running"
    return jsonify(json)

def loadFileConfig():  # funcion que lee archivo de conf del proyecto
    with open('config.json') as f:  # leer archivo de configuracion
        data = json.load(f)  # pasa el json a diccionario
    return data


if __name__ == '__main__':  # primera linea que se ejecuta del main
    dataConfig = loadFileConfig()  # carga el archivo config.json
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(
        dataConfig["port"]))  # muestra ruta de ejecucion
    serve(app, host=dataConfig["url-backend"],
          port=dataConfig["port"])  # crea la instancia del server con datos del confij.json
