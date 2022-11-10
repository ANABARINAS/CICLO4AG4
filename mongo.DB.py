from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb+srv://Ciclo4Grupo5:Jd12201998@ciclo4grupo5.jmc0esl.mongodb.net/?retryWrites=true&w=majority")
db = client["app-Ciclo4Grupo5"]

print(db.list_collection_names())

#CRUD de Candidatos

#CREATE
_candidato = {
"Nombre": "Gustavo",
"Segundo Nombre": "Francisco",
"Primer Apellido": "Petro",
"Segundo Apellido":"Urrego",
"Nombre de partido politico":"pacto historico"
}

CandidatosCollection = db.Candidatos
Candidatos_id = CandidatosCollection.insert_one(_candidato).inserted_id

print(Candidatos_id)

#RED
print(CandidatosCollection.find_one())
for Candidatos in CandidatosCollection.find():
    print(Candidatos)

#DELETE
busqueda = {"_id": ObjectId("")}
CandidatosCollection.delete_one(busqueda)

#UPDATE
busquedaUpdate = {"_id": ObjectId("6353004cb6ddf919fb02f03f")}
update2 = {"$set": {"Nombre": "juan",
"Segundo Nombre": "Manuel",
"Primer Apellido": "Santos",
"Segundo Apellido":"Rodriguez",
"Nombre de partido politico":"centro democratico"}
}
CandidatosCollection.update_one(busquedaUpdate, update2)
