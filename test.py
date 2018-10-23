import pymongo

cliente = pymongo.MongoClient()

coleccion = cliente.testDB.preguntas

# # insertar un saludo
# saludos = [{"Buenos días": "Muy Buenos días"},
#            {"Como estas": "Muy bien"},
#            {"Estamos melos": "Sisas sisas"}
#            ]
#
# coleccion.insert_many(saludos)

saludos = coleccion.find({"Estamos melos":{'$exists': True}})
for registro in saludos:
    print(registro['Estamos melos'])

