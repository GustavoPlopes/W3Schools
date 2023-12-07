import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Retorne uma lista dos bancos de dados do seu sistema
# print(myclient.list_database_names())


# verifica um banco de dados específico pelo nome se existe
# dblist = myclient.list_database_names()
# if "Teste" in dblist:
#     print("The database exists.")

# cria uma coleção no MongoDB, use o objeto de banco de dados e especifique o nome da coleção que deseja criar,
# o MongoDB criará a coleção se ela não existir.
mycol = mydb["clientes"]
mydelete = mydb["Excluir"]


# Retorne uma lista de todas as coleções do seu banco de dados:
# print(mydb.list_collection_names())

# verifica uma coleção específica pelo nome
# collist = mydb.list_collection_names()
# if "clientes" in collist:
#     print('The collection exists.')

# Para inserir um registro, ou documento como é chamado no MongoDB, em uma coleção, usamos o insert_one()método.
# mydict = {"name": "John", "address": "Highway 37"}
# x = mycol.insert_one(mydict)
# mydict = {"name": "Peter", "address": "Lowstreet 27"}
# x = mycol.insert_one(mydict)
# print(x.inserted_id)

# Para inserir vários documentos em uma coleção no MongoDB, usamos o insert_many()método.
# mylist = [
#   {"name": "Amy", "address": "Apple st 652"},
#   {"name": "Hannah", "address": "Mountain 21"},
#   {"name": "Michael", "address": "Valley 345"},
#   {"name": "Sandy", "address": "Ocean blvd 2"},
#   {"name": "Betty", "address": "Green Grass 1"},
#   {"name": "Richard", "address": "Sky st 331"},
#   {"name": "Susan", "address": "One way 98"},
#   {"name": "Vicky", "address": "Yellow Garden 2"},
#   {"name": "Ben", "address": "Park Lane 38"},
#   {"name": "William", "address": "Central st 954"},
#   {"name": "Chuck", "address": "Main Road 989"},
#   {"name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

# Insira vários documentos, com IDs especificados
# mylist = [
#   {"_id": 1, "name": "John", "address": "Highway 37"},
#   {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   {"_id": 3, "name": "Amy", "address": "Apple st 652"},
#   {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   {"_id": 5, "name": "Michael", "address": "Valley 345"},
#   {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   {"_id": 8, "name": "Richard", "address": "Sky st 331"},
#   {"_id": 9, "name": "Susan", "address": "One way 98"},
#   {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   {"_id": 12, "name": "William", "address": "Central st 954"},
#   {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

# O find_one()método retorna a primeira ocorrência na seleção.
# x = mycol.find_one()
# print(x)

# seleciona todos os documentos da coleção.
# for x in mycol.find():
#     print(x)

# for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
#     print(x)

# Encontre documento(s) com o endereço
# myquery = {"address": "Park Lane 38"}
# mydoc = mycol.find(myquery)
# for x in mydoc:
#     print(x)

# # para encontrar os documentos onde o campo “endereço” começa com a letra “S” ou superior (em ordem alfabética)
# myquery = {"address": {"$gt": "S"}}
# mydoc = mycol.find(myquery)
# for x in mydoc:
#     print(x)

# Para localizar apenas os documentos onde o campo “endereço” inicia com a letra “S”
# mydoc = mycol.find({"address": {"$regex": "^S"}})
# for x in mydoc:
#     print(x)

# classificar o resultado em ordem crescente
# mydoc = mycol.find().sort("name")
# for x in mydoc:
#     print(x)

# Classificar em ordem decrescente
# mydoc = mycol.find().sort("name", -1)
# for x in mydoc:
#     print(x)

# Excluir documento
# mycol.delete_one({"address": "Mountain 21"})

# Excluir muitos documentos
# x = mycol.delete_many({"address": {"$regex": "^S"}})
# print(x.deleted_count, "documents deleted")

# Excluir todos os documentos de uma coleção
# x = mydelete.delete_many({})
# print(x.deleted_count, " documents deleted.")

# Excluir coleção
# mydelete.drop()

# Atualizar coleção
# mycol.update_one({"address": "Valley 345"}, {"$set": {"address": "Canyon 123"}})
# for x in mycol.find():
#     print(x)

# Atualizar muitos
# myquery = {"address": {"$regex": "^S"}}
# newvalues = {"$set": {"name": "Minnie"}}
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

