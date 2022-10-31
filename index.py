from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controladores.controladorCandidatos import controladorcandidatos
from controladores.controladorMesas import controladormesas
from controladores.controladorPartidos import controladorpartidos
from controladores.controladorresultados import controladorresultados


#instancia flask
app = Flask(__name__)

cors = CORS(app)

def loadFileConfig ():
    with open ('config.json') as f:
        data= json.load (f)
    return data

#Iniciar aplicación
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))

    #CONFIGURAR UN SERVIDOR DE APLICACIONES
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


"""if __name__=='__main__':
    print("Server running")
    serve(app,host="127.0.0.1",port="5000")"""

@app.route ("/")
def hello_world():
    return "<p> Hello </p>"

@app.route("/", methods=["GET"])
def get_home():
    datos = {
      "Server running":"localhost" 
    }
    return jsonify(datos)

#PATH CANDIDATOS
#path listar

_controlador_candidatos= controladorcandidatos()

@app.route ("/candidatos",methods=["GET"])
def get_candidatos():
    datos= _controlador_candidatos.getcandidatos()
    return jsonify(datos)

#path eliminar
@app.route ("/candidatos/<string:id>",methods=["DELETE"])
def delete_candidatos(id):
    datos=_controlador_candidatos.deletecandidatos(id)
    return jsonify(datos)    

#path crear
@app.route("/candidatos", methods=["POST"])
def create_candidatos():
    datosEntrada = request.get_json()
    datosSalida  = _controlador_candidatos.createcandidatos(datosEntrada)
    return jsonify(datosSalida)    

#path actualizar
@app.route("/candidatos/<string:id>",methods=['PUT']) 
def modificar_candidatos(id):
    data = request.get_json()
    json=_controlador_candidatos.updatecandidatos(id,data)
    return jsonify(json) 

#PATH MESAS
#Path listar

_controlador_mesas= controladormesas()

@app.route ("/mesas",methods=["GET"])
def get_mesas():
    datos= _controlador_mesas.getmesas()
    return jsonify(datos)

#path eliminar
@app.route ("/mesas/<string:id>",methods=["DELETE"])
def delete_mesas(id):
    datos=_controlador_mesas.deletemesas(id)
    return jsonify(datos)    

#path crear
@app.route("/mesas", methods=["POST"])
def create_mesas():
    datosEntrada = request.get_json()
    datosSalida  = _controlador_mesas.createmesas(datosEntrada)
    return jsonify(datosSalida)  

#path actualizar
@app.route("/mesas/<string:id>",methods=['PUT']) 
def modificar_mesas(id):
    data = request.get_json()
    json=_controlador_mesas.updatemesas(id,data)
    return jsonify(json)     

#PATH PARTIDOS
#path listar

_controlador_partidos= controladorpartidos()

@app.route ("/partidos",methods=["GET"])
def get_partidos():
    datos= _controlador_partidos.getpartidos()
    return jsonify(datos)

#path eliminar
@app.route ("/partidos/<string:id>",methods=["DELETE"])
def delete_partidos(id):
    datos=_controlador_partidos.deletepartdos(id)
    return jsonify(datos)    

#path crear
@app.route("/partidos", methods=["POST"])
def create_partidos():
    datosEntrada = request.get_json()
    datosSalida  = _controlador_partidos.createpartidos(datosEntrada)
    return jsonify(datosSalida) 

#path actualizar
@app.route("/partidos/<string:id>",methods=['PUT']) 
def modificar_partidos(id):
    data = request.get_json()
    json=_controlador_partidos.updatepartidos(id,data)
    return jsonify(json)        

#PATH RESULTADOS
#path listar

_controlador_resultados= controladorresultados()

@app.route ("/resultados",methods=["GET"])
def get_resultados():
    datos=_controlador_resultados.getresultados()
    return jsonify(datos)

#path eliminar
@app.route ("/resultados/<string:id>",methods=["DELETE"])
def delete_resultados(id):
    datos=_controlador_resultados.deleteresultados(id)
    return jsonify(datos)    

#path crear
@app.route("/resultados", methods=["POST"])
def create_resultados():
    datosEntrada = request.get_json()
    datosSalida  = _controlador_resultados.createresultados(datosEntrada)
    return jsonify(datosSalida)    

#path actualizar
@app.route("/resultados/<string:id>",methods=['PUT']) 
def modificar_resultados(id):
    data = request.get_json()
    json=_controlador_resultados.updateresultados(id,data)
    return jsonify(json) 
