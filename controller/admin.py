from flask import Blueprint, render_template, request, session, redirect, url_for
from models.db_config import *
from models.models import *
from .auxiliar import *

admin = Blueprint('admin', __name__)

@admin.route("/admin", methods=["GET"])
def admin_get():

    session.pop('_flashes', None)

    users = users_collection.find()
    return render_template("admin.html", users=users)


@admin.route("/admin", methods=["POST"])
def admin_post():

    # Pegando o form ao apertar um botão
    form = request.form.to_dict()

    # Recuperando o botão presisonado e a qual usuário se refere
    pressed_btn = list(form.keys())[0]
    pressed_user = form.get(pressed_btn)

    if pressed_btn == "view_btn":
        return redirect(url_for("admin.user_info_get", username=pressed_user))

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
    
    # Recuperando usuário do banco de dados
    user = users_collection.find_one({"username": username})
    return render_template("admin_view.html", user=user)


@admin.route("/admin/<username>", methods=["POST"])
def user_info_post(username):
    
    form = request.form.to_dict()
    
    # Recuperando as informações do formulário
    inputed_username = form.get("username")
    inputed_password = form.get("password")
    inputed_favourite_receipts = form.get("favourite_receipts")
    inputed_is_admin_radio = bool(form.get("is_admin_radio"))

    # Recuperando o usuário do banco de dados
    filter = {"username": username}
    # Atualizando os dados do usuário
    users_collection.update_one(filter, {"$set": {"username": inputed_username}})
    users_collection.update_one(filter, {"$set": {"password": inputed_password}})
    users_collection.update_one(filter, {"$set": {"favourite_receipts": inputed_favourite_receipts}})
    users_collection.update_one(filter, {"$set": {"is_admin": inputed_is_admin_radio}})


    return redirect(url_for("admin.admin_get"))