from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)  # instancia del servidor
cors = CORS(app)  # instancia de CORS. PERMITE HACER PRUEBAS DESDE LA MISMA MAQUINA QUE EL SERVIDOR


#from Controladores.ControladorEstudiante import ControladorEstudiante
#from Controladores.ControladorDepartamento import ControladorDepartamento
#from Controladores.ControladorInscripcion import ControladorInscripcion
#from Controladores.ControladorMateria import ControladorMateria

#miControladorEstudiante = ControladorEstudiante()
#miControladorDepartamento = ControladorDepartamento()
#miControladorInscripcion = ControladorInscripcion()
#miControladorMateria = ControladorMateria()


#@app.route("/estudiantes", methods=['GET'])
#def getestudiantes():  # devuelve todos los estudiantes
#    json = miControladorEstudiante.index()
#    return jsonify(json)
#    return "<h3>mensaje en pantalla</h3>"      ##si se qiuere devolver un mnensaje


#@app.route("/estudiantes", methods=['POST'])
#def crearEstudiante():
#    data = request.get_json()  # data tiene la info del body. La informacion viene como formato JSON
#    json = miControladorEstudiante.create(data)
#    return jsonify(json)



#@app.route("/estudiantes/<string:id>", methods=['GET'])
#def getEstudiante(id):
#    json = miControladorEstudiante.show(id)
#    return jsonify(json)


#@app.route("/estudiantes/<string:id>", methods=['PUT'])
#def modificarEstudiante(id):
#    data = request.get_json()
#    json = miControladorEstudiante.update(id, data)
#    return jsonify(json)


#@app.route("/estudiantes/<string:id>", methods=['DELETE'])
#def eliminarEstudiante(id):
#    json = miControladorEstudiante.delete(id)
#    return jsonify(json)

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
