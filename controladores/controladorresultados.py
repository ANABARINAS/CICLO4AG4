from modelos.resultados import Resultados

class controladorresultados():

    def __init__(self,):
        print ("controlador creado")

    def getresultados(self):
        Resultados = {
            "resolución":"23322",
            "total": "0" 
        }  
        return Resultados

    def createresultados(self,datosResultados):
        _resultados=Resultados(datosResultados)
        print (_resultados)
        return _resultados.__dict__

    def updateresultados (self,id,infoResultados):
        losresultados=Resultados(infoResultados)
        return losresultados.__dict__
        
    def deleteresultados(self,total):
        print ("resultados"+total+"eliminado")