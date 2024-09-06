from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify, make_response
from models.db_config import *
from .auxiliar import *
from models.models import * # Importando apenas para criar um usuário teste. Deve ser removido depois

profile = Blueprint("profile", __name__)

@profile.route("/perfil", methods=["GET"])
def profile_page():
    
    # Usuário apenas para teste (deve ser removido depois)
    new_user = User("novo_user", "123456").__dict__
    users_collection.insert_one(new_user)

    # Alimentando a sessão
    session["username"] = new_user.get("username")
    session["password"] = new_user.get("password")

    # Verifica se há um usuário logado, caso contrário é direcionado para a página de login
    if "username" in session:
        return render_template("profile_page.html")
    return redirect(url_for("auth.login_page"))


# ------------------------------------- MÉTODO POST DO PERFIL -----------------------------------------------


@profile.route("/perfil", methods=["POST"])
def profile_page_post():
    
    # Recuperando o formulário e os valores nele colocados
    inputed_form = request.get_json()


    inputed_new_username = inputed_form["inputed_new_username"]
    inputed_new_password = inputed_form["inputed_new_password"]
    inputed_password = inputed_form["inputed_password"]
    pressed_btn = inputed_form["pressed_btn"]

    print(inputed_new_username, inputed_new_password, inputed_password, pressed_btn)

    # Recuperando o usuário logado
    logged_username = session["username"]
    logged_password = session["password"]


    # # Verificando se a senha colocada está correta
    # if not is_valid_password(logged_password, inputed_password):
    #     return make_response(jsonify({"status": "invalid_password"}))
    
    if pressed_btn == "delete_account_btn":
        users_collection.delete_one({"username": logged_username})
        session.clear()

        return make_response(jsonify({"status": "user_deleted"}))

    # Trocando username/senha

    filter = {"username": logged_username}

    if pressed_btn == "edit_username_btn":
        users_collection.update_one(filter, {"$set": {"username": inputed_new_username}})
        session["username"] = inputed_new_username

        return make_response(jsonify({"status": "username_changed"}))
    
    if pressed_btn == "edit_password_btn":
        users_collection.update_one(filter, {"$set": {"password": inputed_new_password}})
        session["password"] = inputed_new_password

        return make_response(jsonify({"status": "password_changed"}))
    
    return make_response(jsonify({"status": "default"}))
    