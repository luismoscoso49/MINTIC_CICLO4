from datetime import datetime
from bson import ObjectId
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.RepositorioCandidato import RepositorioCandidato

from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Partido import Partido
from Modelos.Candidato import Candidato


class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioPartido = RepositorioPartido()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioResultado.findAll()

    """
    Asignacion mesa y partido  a resultado
    """

    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Resultado(infoResultado)
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        partido  = Partido(candidato.partido)
        nuevoResultado.mesa = mesa
        nuevoResultado.candidato = candidato.nombre
        nuevoResultado.partido = partido.nombre
        nuevoResultado.fecha = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        nuevoResultado.cantidad = 1
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificación de resultado (mesa y candidato)
    """

    def update(self, id_resultado, infoResultado, id_mesa, id_partido):
        resultadoActual = Resultado(self.repositorioResultado.findById(id_resultado))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        parti = Partido(self.repositorioPartido.findById(id_partido))
        resultadoActual.mesa = mesa
        resultadoActual.partido = parti
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "listado de Votos por Partido"
    def totalvotosxpartido(self):
        return self.repositorioResultado.totalvotosxpartido()

    def totalvotosxmesa(self):
        return self.repositorioResultado.totalvotosxmesa()


    def votosxmesa(self, id_mesa):
        return self.repositorioResultado.votosxmesa(id_mesa)

    def totalvotos(self):
        return self.repositorioResultado.totalvotos()

    def votosxpartidoxmesa(self, id_mesa):
        return self.repositorioResultado.votosxpartidoymesa(id_mesa)

    def distribucionPorcentual(self):
        return self.repositorioResultado.distribucionPorcentualVotos()




















