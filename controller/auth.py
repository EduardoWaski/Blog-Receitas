from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from models.db_config import *
from models.models import *
from .auxiliar import *

auth = Blueprint('auth', __name__)

# User fictício
users = {
    'username': 'eduardo', 'password': '1234',
}

@auth.route("/acesso", methods = ["GET", "POST"])
def login_signup():

    session.pop('_flashes', None)

    if request.method == "GET":
        return render_template('login_signup.html')

    # Se não for GET, é POST
    # Recuperando os dados do formulário
    inputed_username = request.form['username']
    inputed_password = request.form['password']
    login_option = True if "login_btn" in request.form.to_dict() else False

    # Verificando se o usuário tentou fazer login ou cadastro
    if login_option:

        # Essa parte deverá ser trocada depois, pois devemos analisar os usuários dentro do banco de dados
        if is_valid_login(inputed_username, inputed_password):

            session['username'] = inputed_username
            session['password'] = inputed_password
            return redirect(url_for('index.home_page'))

    # Se for cadastro
    else:                   
        if is_valid_input(inputed_username):

            session['username'] = inputed_username
            session['password'] = inputed_password
            
            # Criando um novo usuário a partir da classe
            new_user = User(inputed_username, inputed_password).__dict__
            users_collection.insert_one(new_user)
            return redirect(url_for(f'index.home_page'))
        
    return render_template('login_signup.html')

    





