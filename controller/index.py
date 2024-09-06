from flask import Blueprint, render_template, session, redirect, url_for

index = Blueprint("index", __name__)

@index.route("/", methods=["GET"])
def home_page():
    
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))
    return render_template("index.html")