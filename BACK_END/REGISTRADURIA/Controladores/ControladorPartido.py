from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("Creando Controlador de Partido")

    def index(self):
        print("lista los partidos")
        partido = {
         "id": 1,
         "nombre":"El de siempre",
        "lema":"los mismos con las mismas"
        }
        return partido

    def create(self,infPartido):
        print("creando partido")
        partido = Partido(infPartido)
        return partido.__dict__

    def show(self, idPartido):
        print("Muestra Info Partido " + idPartido)
        partido = {
         "id": idPartido,
         "nombre":"El de siempre",
        "lema":"los mismos con las mismas"
        }
        return partido

    def update(self,idPartido, dictPartido):
        print("Actualizando partido :" + idPartido )
        partido = Partido(dictPartido)
        return partido.__dict__

    def delete(self, idPartido):
        print("Borrar un partido :" + idPartido)
        return ("deleted_Count ", 1)


