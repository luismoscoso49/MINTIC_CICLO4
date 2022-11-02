from Modelos.Resultado import Resultado

class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")  #Constructor

    def index(self):
        print("Listar todos los Resultados")
        resultado = {
            "id": 1,
            "idMesa": 2,
            "idPartido": 1
        }
        return [resultado]

    def create(self,dictResultado):
        print ("Crea un Resultado")
        resultado = Resultado(dictResultado)
        return resultado.__dict__

    def show(self,idPartido):
        print("Mostrar un Resultado por Partido" )
        resultado = {
            "id": 1,
            "idMesa": 2,
            "idPartido": idPartido
        }
        return resultado   #diccionario

    def update(self, id, dictResultado):
        print("Update de Resultado por idpartido")
        resultado = Resultado(dictResultado)
        return resultado.__dict__

    def delete(self, id):
        print("Borrar un resultado :")
        return {"deleted_count ": 1}





