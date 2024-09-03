from flask import Blueprint, render_template

profile = Blueprint("profile", __name__)

@profile.route("/perfil")
def profile_page():
    return render_template("profile_page.html")