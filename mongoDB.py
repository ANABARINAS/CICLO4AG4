from pymongo import MongoClient
from bson.objectid import ObjectId
"""client = MongoClient("mongosh "mongodb+srv://cluster0.sbdwoto.mongodb.net/databaseg4" --apiVersion 1 --username anaibarinas")
db = client["app-registraduria"]
"""
client = MongoClient("mongodb+srv://anaibarinas:AnaIsa1227@cluster0.sbdwoto.mongodb.net/?retryWrites=true&w=majority")
db = client["app-registraduria"]

print(db.list_collection_names())
"""
#CRUD de Candidatos

#CREATE
_candidato = {
"Nombre": "Gustavo",
"Segundo Nombre": "Francisco",
"Primer Apellido": "Petro",
"Segundo Apellido":"Urrego",
"Nombre de partido politico":"pacto historico"
}
"""
CandidatosCollection = db.Candidatos 
"""
Candidatos_id = CandidatosCollection.insert_one(_candidato).inserted_id

print(Candidatos_id)

#RED
print(CandidatosCollection.find_one())
for Candidatos in CandidatosCollection.find():
    print(Candidatos)

#DELETE
busqueda = {"_id": ObjectId("636d0a7ed75fb9ad19fac790")}
CandidatosCollection.delete_one(busqueda)
"""
#UPDATE
busquedaUpdate = {"_id": ObjectId("636d0b5deede7a44f4173138")}
update2 = {"$set": {"Nombre": "juan",
"Segundo Nombre": "Manuel",
"Primer Apellido": "Santos",
"Segundo Apellido":"Rodriguez",
"Nombre de partido politico":"centro democratico"}
}
CandidatosCollection.update_one(busquedaUpdate, update2)
