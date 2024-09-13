from flask import Blueprint, render_template, request, session, redirect, url_for
from models.db_config import *
from models.models import *

receipt_page = Blueprint('receipt_page', __name__)


@receipt_page.route("/receitas", methods = ["GET"])
def receipt_page_get():
    return render_template("receipt_page.html")


@receipt_page.route("/receitas", methods = ["POST"])
def receipt_page_post():
    category_chosen = request.form.get("receipt")
    category_recipes = list(receipt_collection.find({"category": category_chosen}))
    return render_template("receipt_page.html", category_recipes = category_recipes) # A PRIMEIRA VAR É COMO VAI SER CHAMADA NO HTML E A SEGUNDA É A VARIAVEL DA ROTA

