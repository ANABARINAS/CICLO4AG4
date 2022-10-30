from modelos.candidatos import Candidatos
from modelos.mesas import mesas
from modelos.partidos import patidos
from modelos.resultados import resultados

class controladorcandidatos():

    def __init__(self,):
        print ("controlador creado")

    def getcandidatos(self):
        Candidatos = {
            "resolución":"23322",
            "cedula":"10920923",
            "nombre":"maria",
            "apellido":"perez"
        }    

    def createcandidatos():
        pass

    def updatecandidatos():
        pass

    def deletecandidatos(self,cedula):
        print ("candidato"+cedula+"eliminado")


class controladormesas():

    def __init__(self,):
        print ("controlador creado")

    def getmesas(self):
        mesas = {
            "resolución":"23322",
            "numero_mesa":"uno",
        }    

    def createmesas():
        pass

    def updatemesas():
        pass

    def deletemesas(self,numero_mesa):
        print ("mesas"+numero_mesa+"eliminado")

class controladorpartidos():

    def __init__(self,):
        print ("controlador creado")

    def getpartidos(self):
        partidos = {
            "resolución":"23322",
            "cedula":"10920923",
            "nombre":"partido de",
            
        }    

    def createpartidos():
        pass

    def updatepartidos():
        pass

    def deletepartdos(self,nombre):
        print ("partidos"+nombre+"eliminado")

class controladorresultados():

    def __init__(self,):
        print ("controlador creado")

    def getresultados(self):
        resultados = {
            "resolución":"23322",
            "total": "0"
           
        }    

    def createresultados():
        pass

    def updateresultados():
        pass

    def deleteresultados(self,total):
        print ("resultados"+total+"eliminado")
