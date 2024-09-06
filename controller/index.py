from flask import Blueprint, render_template, session, redirect, url_for, request

index = Blueprint("index", __name__)

@index.route("/", methods=["GET"])
def home_page():
    
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))
    return render_template("index.html")


@index.route("/", methods=["POST"])
def home_page_post():
    
    form = request.form.to_dict()
    logout_option = True if "logout_btn" in form else False

    if logout_option:
        session.clear()
        return redirect(url_for("auth.login_signup"))
    
    return render_template("index.html")

