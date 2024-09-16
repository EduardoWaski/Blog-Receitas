from flask import Blueprint, render_template, session, redirect, url_for, request
from models.db_config import *
from models.models import *
from controller.auxiliar import *

index = Blueprint("index", __name__)

@index.route("/", methods=["GET"])
def home_page_get():
    
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))
    
    recipes = recipes_collection.find().limit(6)
    return render_template("index.html", recipes=recipes)

# --------------------------------------- POST -------------------------------------------------------

@index.route("/", methods=["POST"])
def home_page_post():
    
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))
    
    form = request.get_json()
    recipe_id = form["recipe_id"]

    return 'ok'