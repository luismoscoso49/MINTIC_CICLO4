from Modelos.Candidato import Candidato

class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")  #Constructor

    def index(self):
        print("Listar todos los Candidatos")
        candidato = {
            "cedula": "110101",
            "nombre": "candidato 1",
            "apellido": "apellido candidato 1",
            "resolucion": "RES 10113212"
        }
        return [candidato]

    def create(self,dictCandidato):
        print ("Crea un Candidato")
        candidato = Candidato(dictCandidato)
        return candidato.__dict__

    def show(self,cedula):
        print("Mostrar un Candidato por cedula" )
        candidato = {
            "cedula": cedula,
            "nombre": "candidato 1",
            "apellido": "apellido candidato 1",
            "resolucion": "RES 10113212"
        }
        return candidato   #diccionario

    def update(self, cedula, dictCandidato):
        print("Update de Candidato pór Cedula" + cedula)
        candidato = Candidato(dictCandidato)
        return candidato.__dict__

    def delete(self,cedula):
        print("Borrar un candidato :", cedula)
        return {"deleted_count ": 1}





