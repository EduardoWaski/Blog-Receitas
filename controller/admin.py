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

    # Recuperando o usuário do banco de dados
    user = users_collection.find_one({"username": pressed_user})
    print(user)

    if pressed_btn == "view_btn":
        return render_template("admin_view.html", user=user)

    if pressed_btn == "delete_btn":
        pass