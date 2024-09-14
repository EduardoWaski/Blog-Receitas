from flask import Blueprint, render_template, request
from models.db_config import *
from models.models import *

recipe_page = Blueprint('recipe_page', __name__)


@recipe_page.route("/receitas", methods = ["GET"])
def recipe_page_get():
    return render_template("recipe_page.html")


@recipe_page.route("/receitas", methods = ["POST"])
def recipe_page_post():
    category_chosen = request.form.get("recipe")
    category_recipes = list(recipes_collection.find({"category": category_chosen}))
    return render_template("recipe_page.html", category_recipes = category_recipes) # A PRIMEIRA VAR É COMO VAI SER CHAMADA NO HTML E A SEGUNDA É A VARIAVEL DA ROTA

