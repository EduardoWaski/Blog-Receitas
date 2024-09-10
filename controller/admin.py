from flask import Blueprint, render_template, request, session, redirect, url_for
from models.db_config import *
from models.models import *
from .auxiliar import *

admin = Blueprint('admin', __name__)

@admin.route("/admin", methods=["GET"])
def admin_get():

    users = users_collection.find()
    return render_template("admin.html", users=users)


@admin.route("/admin", methods=["POST"])
def admin_post():

    # Pegando o form ao apertar um botão
    form = request.form.to_dict()

    # Recuperando o botão presisonado e a qual usuário se refere
    pressed_btn = list(form.keys())[0]
    pressed_user = form.get(pressed_btn)

    edited_username = ...
    # Implementar a lógica aqui

    if pressed_btn == "view_btn":

        return database.users_collection.find().pretty()

    if pressed_btn == "edit_btn":
        flash(f'O nome de "{pressed_user}" foi mudado para "{edited_username}"')

        return database.users_collection.update_one(
            {'username' : pressed_user},
            {'$set': {'username': edited_username}}
        )

    if pressed_btn == "delete_btn":
        flash(f'Usuário "{pressed_user}" foi deletado ')

        return database.users_collection.delete_one(
            {'username': pressed_user}
        )

    return render_template("admin.html")