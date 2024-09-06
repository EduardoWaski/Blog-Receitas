from flask import Blueprint, session, redirect, url_for

logout = Blueprint("logout", __name__)

@logout.route("/logout")
def logout_link():
    
    session.clear()
    return redirect(url_for("auth.login_signup"))