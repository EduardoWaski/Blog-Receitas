from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from models.db_config import *

auth = Blueprint('auth', __name__)

# User fictício
users = {
    'username': 'eduardo', 'password': '1234'
}

@auth.route("/acesso", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Verificação dos dados
        if (username in users['username']) and (users['password'] == password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Nome de usuário e/ou senha incorretos!')

    return render_template('login_signup.html')

def sign_up():
    if request.method == "POST":
        created_username = request.form['username']
        created_password = request.form['password']


        if (created_username not in users['username']) and (created_username.isalnum or created_username.isalpha):
            database.users_collection.insertOne({'username': created_username, 'password': created_password})
            session['username'] = created_username

        else:
            flash('Nome de usuário digitado já existe!')

    





