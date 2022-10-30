from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")  #Constructor

    def index(self):
        print("Listar todas las Mesas")
        mesa = {
            "idMesa": 1,
            "inscritos": 10
        }
        return [mesa]

    def create(self,dictMesa):
        print ("Crea un Mesa")
        mesa = Mesa(dictMesa)
        return mesa.__dict__

    def show(self,id):
        print("Mostrar un Mesa por cedula" )
        mesa = {
            "idMesa": id,
            "inscritos": 10
        }
        return mesa   #diccionario

    def update(self, idMesa, dictMesa):
        print("Update de Mesa pór Id" + idMesa)
        mesa = Mesa(dictMesa)
        return mesa.__dict__

    def delete(self,idMesa):
        print("Borrar un mesa :", idMesa)
        return {"deleted_count ": 1}





