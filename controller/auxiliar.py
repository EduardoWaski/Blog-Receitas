from flask import flash, session
from models.db_config import *

# Condições para um input de cadastro/login válidos
def is_valid_input(inputed_username, inputed_password, do_flash=False):
    if is_valid_username(inputed_username, do_flash) and is_valid_password(inputed_password, do_flash):
        return True
    
    return False

def is_valid_username(inputed_username, do_flash=False):

    # Tratando os dados
    inputed_username = str(inputed_username)

    # Usuários cadastrados no banco de dados
    repeated_user = users_collection.find_one({"username": inputed_username})

    if repeated_user:
        if do_flash:
            flash("Usuário já existe!")
        return False

    if not (len(inputed_username) > 2 and len(inputed_username) <= 12):
        if do_flash:
            flash("Seu nome de usuário deve ter de 3 a 12 caracteres!")
        return False
    
    if not inputed_username.isalnum():
        if do_flash:
            flash("Seu nome de usuário deve conter apenas letras e números")
        return False
    
    if inputed_username.isnumeric():
        if do_flash:
            flash("Seu nome de usuário não deve conter apenas números!")
        return False
    
    return True

def is_valid_password(inputed_password, do_flash=False):

    inputed_password = str(inputed_password).strip()

    if len(inputed_password) < 8:
        if do_flash:
            flash("Sua senha deve conter ao menos 8 caracteres!")
        return False
    return True

def is_correct_login(inputed_username, inputed_password):

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

def is_correct_password(inputed_password):

    inputed_password = str(inputed_password).strip()
    logged_password = session["password"]

    if not logged_password:
        return False

    if not inputed_password == logged_password:
        return False
    
    return True

def is_admin():

    session_username = session["username"]
    logged_user = users_collection.find_one({"username": session_username})

    if not logged_user:
        return False

    if not logged_user["is_admin"]:
        return False
    
    return True

def any_empty_value(dict, do_flash=False):

    if any(not str(valor).strip() for valor in dict.values()):

        if do_flash:
            flash("Há valores vazios!") 
        return True

    return False