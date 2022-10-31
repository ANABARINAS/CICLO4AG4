from modelos.candidatos import Candidatos

class controladorcandidatos():

    def __init__(self,):
        print ("controlador creado")

    def getcandidatos(self):
        _candidatos = {
            "resolución":"23322",
            "cedula":"10920923",
            "nombre":"maria",
            "apellido":"perez"
        }    
        return _candidatos

    def createcandidatos(self,datosCandidatos):
        _candidatos1 = None
        _candidatos1 = Candidatos(datosCandidatos)
        ##print(_candidatos1)
        return _candidatos1.__dict__
        

    def updatecandidatos(self,id,infoCandidatos):
        loscandidatos1=Candidatos(infoCandidatos)
        return loscandidatos1.__dict__
    

    def deletecandidatos(self,cedula):
        print ("candidato"+cedula+"eliminado")


