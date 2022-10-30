from modelos.candidatos import Candidatos

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
        return Candidatos

    def createcandidatos(self,datosCandidatos):
        _candidatos:Candidatos(datosCandidatos)
        print(_candidatos)
        return _candidatos.__dict__
        

    def updatecandidatos(self,id,infoCandidatos):
        loscandidatos:Candidatos(infoCandidatos)
        return loscandidatos.__dict__
        pass

    def deletecandidatos(self,cedula):
        print ("candidato"+cedula+"eliminado")


