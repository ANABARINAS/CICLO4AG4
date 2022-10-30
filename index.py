from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controladores.controladorCandidatos import controladorcandidatos

#instancia flask
app = Flask(__name__)

cors = CORS(app)

def loadFileConfig ():
    with open ('config.json') as f:
        data= json.load (f)
        return data
#Iniciar aplicación
if __name__=='__main__':
    dataConfig = loadFileConfig ()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
"""

if __name__=='__main__':
    print("Server running")
    serve(app,host="127.0.0.1",port="5000")

"""
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
def modificar_candidadtos(id):
    data = request.get_json()
    json=_controlador_candidatos.updateCandidatos(id,data)
    return jsonify(json)    
