from ast import Return
from modelos.partidos import Partidos


class controladorpartidos():

    def __init__(self,):
        print ("controlador creado")

    def getpartidos(self):
        Partidos = {
            "nombre":"partido1",
            "lema":"elmejor",  
        }  
        return Partidos

    def createpartidos(self,datosPartidos):
        _partidos:Partidos(datosPartidos)
        print (_partidos)
        return _partidos.__dict__

    def updatepartidos(self,id,infoPartidos):
        lospartidos:Partidos(infoPartidos)
        return lospartidos.__dict__
        
    def deletepartdos(self,nombre):
        print ("partidos"+nombre+"eliminado")