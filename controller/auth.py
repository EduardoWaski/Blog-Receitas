from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route("/acesso")
def login_page():
    return render_template("login_signup.html")