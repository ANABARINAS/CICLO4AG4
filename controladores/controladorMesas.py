from modelos.mesas import Mesas

class controladormesas():

    def __init__(self,):
        print ("controlador creado")

    def getmesas(self):
        Mesas = {
            "numero_mesa":"uno",
            "numero_cedulas":"124",
        }    
        return Mesas

    def createmesas(self, datosMesas):
        _mesas = Mesas(datosMesas)
        print(_mesas)
        return _mesas.__dict__
        

    def updatemesas(self,id,infoMesas):
        lasmesas=Mesas(infoMesas)
        return lasmesas.__dict__
        

    def deletemesas(self,numero_mesa):
        print ("mesas"+numero_mesa+"eliminado")