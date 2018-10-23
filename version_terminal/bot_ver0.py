import pymongo

#Traemos la base
cliente = pymongo.MongoClient()
coleccion = cliente.testDB.preguntas

saludos = {
    "Hola": "Hola como estas",
    "Buenas": "A la orden",
    "Tons que": "En la buena"
}

entrada = input('En que puedo ayudarte')

if entrada in saludos:
    print(saludos[entrada])

# # Contar saludos del usuario
# saludos = 0
#
# while True:
#     entrada = input('En que puedo ayudarte')
#     if coleccion.find(entrada):
#         print(coleccion.find(entrada))
#     else:
#         break
