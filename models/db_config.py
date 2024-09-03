from pymongo import MongoClient

# Conectando ao mongo_db
mongo_db = MongoClient("localhost", 27017)

# Criando a base de dados
database = mongo_db["blog_database"]

# Criação das coleções
users_collection = database["users"]
receipt_collection = database["receipts"]
comments_collection = database["comments"]