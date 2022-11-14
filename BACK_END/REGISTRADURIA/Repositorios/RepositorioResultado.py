from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId


class RepositorioResultado(InterfaceRepositorio[Resultado]):

    #   Total de Votos por Partido y Candidato General . Punto A del Requerimiento
    def totalvotos(self):
        query1 = {
            "$group": {
                "_id": {
                    "candidato": "$candidato",
                    "partido": "$partido"
                },
                "totalVotos": {
                    "$sum": "$cantidad"
                }
            }
        }
        query2 = {
            "$sort": {
                "totalVotos": -1,
                "_id": 1
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    #   Listado de Votos por mesa .  Punto A del Requerimiento
    def votosxmesa(self, id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
            "$group": {
                "_id": {
                    "mesa": "$mesa",
                    "candidato": "$candidato",
                    "partido": "$partido"
                },
                "cantidad": {
                    "$sum": "$cantidad"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    #Votacion por mesa general. Listado B del Requerimiento
    def totalvotosxmesa(self):
        query1 = {
            "$group": {
                "_id": "$mesa",
                "totalVotos": {
                    "$sum": "$cantidad"
                }
            }
        }
        query2 = {
             "$sort": {
              "totalVotos": 1,
              "_id": 1
             }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)


    # Total de Votos por Partido General . Listado C del requerimiento
    def totalvotosxpartido(self):
        query1 = {
            "$group": {
                "_id": "$partido",
                "totalVotos": {
                    "$sum": "$cantidad"
                }
            }
        }
        query2 = {
             "$sort": {
              "totalVotos": -1,
              "_id": 1
             }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

    # Total de Votos por Partido para una mesa Especifica. Listado C del requerimiento
    def votosxpartidoymesa(self, id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
            "$group": {
                "_id": {
                    "partido": "$partido"
                },
                "mesa": {
                    "$first": "$mesa"
                },
                "cantidad": {
                    "$sum": "$cantidad"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    #Distribucion Porcentual de la Votacion. Punto D del requerimiento
    def distribucionPorcentualVotos(self):
        query1 = {
            "$group": {
                "_id": None,
                "sum": {"$sum": "$cantidad"},
                "users": {"$push": {"partido": "$partido","votes": "$cantidad"}}
            }
        }
        query2 = {
            "$unwind": {
                "path": "$users",
            }
        }
        query3 = {
            "$project": {
                "user": "$users.partido",
                "votos": "$users.votes",
                "sum": "$sum",
                "percent": {"$multiply": [{"$divide": ["$users.votes", "$sum"]}, 100]}
            }
        }
        query4 = {
            "$group": {
                 "_id": {
                     "partido": "$user"
                },
                "porcentaje": {
                    "$sum": "$percent"
                }
            }
        }
        pipeline = [query1,query2,query3, query4]
        return self.queryAggregation(pipeline)

