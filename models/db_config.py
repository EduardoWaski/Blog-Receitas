from pymongo import MongoClient
import gridfs

# Conectando ao mongo_db
mongo_db = MongoClient("localhost", 27017)

# Criando a base de dados
database = mongo_db["blog_database"]

# Criação das coleções
users_collection = database["users"]
recipes_collection = database["recipes"]
comments_collection = database["comments"]

# Instanciando o gridfs (usado para armazenamento de arquivos maior que 16MB - imagens, por exemplo)
fs = gridfs.GridFS(database=database)