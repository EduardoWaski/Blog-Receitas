from flask import flash
from models.db_config import *

# Condições para um input de cadastro/login válidos
def is_valid_input(inputed_username):
    
    # Tratando os dados
    inputed_username = str(inputed_username).strip()

    # Usuários cadastrados no banco de dados
    repeated_user = users_collection.find_one({"username": inputed_username})

    if repeated_user:
        flash("Usuário já existe!")
        return False

    if not (len(inputed_username) > 2 and len(inputed_username) <= 12):
        flash("Seu nome de usuário deve ter de 3 a 12 caracteres!")
        return False
    
    if not inputed_username.isalnum():
        flash("Seu nome de usuário deve conter apenas letras e números")
        return False
    
    if inputed_username.isnumeric():
        flash("Seu nome de usuário não deve conter apenas números!")
        return False

    return True

def is_valid_login(inputed_username, inputed_password):

    inputed_username = str(inputed_username).strip()
    inputed_password = str(inputed_password).strip()

    db_user = users_collection.find_one({"username": inputed_username})

    if not db_user:
        flash("O usuário indicado não existe!")
        return False
    
    if not inputed_password == db_user["password"]:
        flash("Senha incorreta!")
        return False
    
    return True