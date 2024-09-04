from flask import Blueprint, render_template, request, session, redirect, url_for
from models.db_config import *
from .auxiliar import is_valid_password
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
    inputed_form = request.form

    new_username = inputed_form.get("new_username")
    new_password = inputed_form.get("new_password")
    inputed_password = inputed_form.get("password")

    # Recuperando o usuário logado
    logged_username = session["username"]
    logged_password = session["password"]

    # Verificando se a senha colocada está correta
    if not is_valid_password(logged_password, inputed_password):
        return "Not valid password"
    
    if "delete_account_bt" in inputed_form:
        users_collection.delete_one({"username": logged_username})
        session.clear()

        return "User deleted"


    # Trocando username/senha

    filter = {"username": logged_username}

    if new_username:
        users_collection.update_one(filter, {"$set": {"username": new_username}})
        session["username"] = new_username

        return "Username updated"
    
    if new_password:
        users_collection.update_one(filter, {"$set": {"password": new_password}})
        session["password"] = new_password

        return "Pass updated"
    