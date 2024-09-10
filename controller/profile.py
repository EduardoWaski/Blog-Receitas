from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify, make_response
from models.db_config import *
from models.models import *
from .auxiliar import *

profile = Blueprint("profile", __name__)

@profile.route("/perfil", methods=["GET"])
def profile_page():

    if "username" in session:
        return render_template("profile_page.html")
    return redirect(url_for("auth.login_signup"))

# ------------------------------------- MÉTODO POST DO PERFIL -----------------------------------------------

@profile.route("/perfil", methods=["POST"])
def profile_page_post():
    
    # Recuperando o formulário, senha e o botão apertado
    inputed_form = request.get_json()
    inputed_password = inputed_form["inputed_password"]
    pressed_btn = inputed_form["pressed_btn"]



    # Verificando se a senha colocada está correta
    if not is_correct_password(inputed_password):
        return make_response(jsonify({"status": "incorrect_password"}))
    
    # BOTÕES

    # Recuperando o usuário logado
    logged_username = session["username"]

    # Deletando conta
    if pressed_btn == "delete_account_btn":

        users_collection.delete_one({"username": logged_username})
        return redirect(url_for("logout.logout_link"))

    # Filtro para encontrar o usuário no banco de dados
    filter = {"username": logged_username}

    # Editando usuário
    if pressed_btn == "edit_username_btn":

        inputed_new_username = inputed_form["inputed_new_username"]

        # Verificando se o usuário é válido
        if not is_valid_username(inputed_new_username):
            return make_response(jsonify({"status": "invalid_username"}))
        
        session["username"] = inputed_new_username
        users_collection.update_one(filter, {"$set": {"username": inputed_new_username}})
        return make_response(jsonify({"status": "credentials_changed"}))
    
    # Editando senha
    if pressed_btn == "edit_password_btn":

        inputed_new_password = inputed_form["inputed_new_password"]

        if not is_valid_password(inputed_new_password):
            return make_response(jsonify({"status": "invalid_password"}))


        users_collection.update_one(filter, {"$set": {"password": inputed_new_password}})
        session["password"] = inputed_new_password
        return make_response(jsonify({"status": "credentials_changed"}))
    
    return make_response(jsonify({"status": "credentials_changed"}))
    