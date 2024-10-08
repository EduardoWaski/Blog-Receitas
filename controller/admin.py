from flask import Blueprint, render_template, request, session, redirect, url_for
from models.db_config import *
from models.models import *
from .auxiliar import *

admin = Blueprint('admin', __name__)

@admin.route("/admin", methods=["GET"])
def admin_get():

    # Verifica se o usuário logado é admin
    if not is_admin():
        return redirect(url_for("index.home_page_get"))
    
    session.pop('_flashes', None)
    
    users = users_collection.find()
    return render_template("admin.html", users=users)
    

@admin.route("/admin", methods=["POST"])
def admin_post():

    # Verifica se o usuário logado é admin
    if not is_admin():
        return redirect(url_for("index.home_page_get"))

    # Pegando o form ao apertar um botão
    form = request.form.to_dict()

    # Recuperando o botão presisonado e a qual usuário se refere
    pressed_btn = list(form.keys())[0]
    pressed_user = form.get(pressed_btn)

    if pressed_btn == "view_btn":
        return redirect(url_for("admin.user_info_get", username=pressed_user))
    
    if pressed_btn == "add_new_user":
        return redirect(url_for("admin.add_new_user_get"))

    if pressed_btn == "delete_btn":

        # Deletando o usuário
        users_collection.delete_one({'username': pressed_user})
        flash(f'Usuário "{pressed_user}" foi deletado')

        # Carregando a página
        users = users_collection.find()
        return render_template("admin.html", users=users)



# ----------------------------- ÁREA DO USER INFO ----------------------------------

@admin.route("/admin/<username>", methods=["GET"])
def user_info_get(username):

    # Verifica se o usuário logado é admin
    if not is_admin():
        return redirect(url_for("index.home_page_get"))
    
    session.pop('_flashes', None)
    
    # Recuperando usuário do banco de dados
    user = users_collection.find_one({"username": username})
    return render_template("admin_user_info.html", user=user)


@admin.route("/admin/<username>", methods=["POST"])
def user_info_post(username):

    # Verifica se o usuário logado é admin
    if not is_admin():
        return redirect(url_for("index.home_page_get"))
    
    
    form = request.form.to_dict()
    
    # Recuperando as informações do formulário
    inputed_username = form.get("username")
    inputed_password = form.get("password")
    inputed_favourite_recipes = form.get("favourite_recipes")
    inputed_is_admin_radio = True if form.get("is_admin_radio") == "true" else False

    # Recuperando o usuário do banco de dados
    filter = {"username": username}
    # Atualizando os dados do usuário
    users_collection.update_one(filter, {"$set": {"username": inputed_username}})
    users_collection.update_one(filter, {"$set": {"password": inputed_password}})
    users_collection.update_one(filter, {"$set": {"favourite_recipes": inputed_favourite_recipes}})
    users_collection.update_one(filter, {"$set": {"is_admin": inputed_is_admin_radio}})

    flash(f"Usuário editado com sucesso!")

    # Recuperando o usuário no banco de dados
    user = users_collection.find_one({"username": username})
    return render_template("admin_user_info.html", user=user)


# ----------------------------- ÁREA DO ADD_NEW_USER ----------------------------------

@admin.route("/admin/add_new_user", methods=["GET"])
def add_new_user_get():

    session.pop('_flashes', None)

    # Verifica se o usuário logado é admin
    if not is_admin():
        return redirect(url_for("index.home_page_get"))
    
    # Recuperando usuário do banco de dados
    return render_template("admin_add_new_user.html")


@admin.route("/admin/add_new_user", methods=["POST"])
def add_new_user_post():

    # Verifica se o usuário logado é admin
    if not is_admin():
        return redirect(url_for("index.home_page_get"))
    
    form = request.form.to_dict()
    
    # Recuperando as informações do formulário
    inputed_username = form.get("username")
    inputed_password = form.get("password")
    inputed_favourite_recipes = form.get("favourite_recipes")
    inputed_is_admin_radio = True if form.get("is_admin_radio") == "true" else False

    # Criando um novo usuário a partir da classe
    new_user = User(inputed_username, inputed_password, inputed_favourite_recipes, inputed_is_admin_radio).__dict__
    users_collection.insert_one(new_user)
    
    flash(f'Usuário "{new_user.get("username")}" criado com sucesso!')
    return render_template("admin_add_new_user.html")