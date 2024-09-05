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

    if request.method == "GET":
        return render_template('login_signup.html')

    # Se não for GET, é POST
    # Recuperando os dados do formulário
    inputed_username = request.form['username']
    inputed_password = request.form['password']
    login_option = True if "login_btn" in request.form.to_dict() else False

    # Verificando se o usuário tentou fazer login ou cadastro
    if login_option:

        # Verificação dos dados (Trocando o "in" pelo "==")
        # Essa parte deverá ser trocada depois, pois devemos analisar os usuários dentro do banco de dados
        if (inputed_username == users['username']) and (inputed_password == users['password']):
            session['username'] = inputed_username
            session['password'] = inputed_password
            return redirect(url_for('index.home_page'))
        
        # Retirada do "else", pois o "return" torna o "else" dispensável
        flash('Nome de usuário e/ou senha incorretos!') 


    # Se for cadastro
    else:                   
        print((inputed_username != users['username']))
        print(inputed_password.isalnum())
        if (inputed_username != users['username']) and (inputed_password.isalnum()): # Retirada do inputed_password.isalpha()
            
            # Criando um novo usuário a partir da classe
            new_user = User(inputed_username, inputed_password).__dict__
            users_collection.insert_one(new_user) # Método insert_one corrigido (insertOne -> insert_one)

            # Não inserir dentro da sessão até o usuário fazer login
            # session['username'] = inputed_username
            # session['password'] = inputed_password
            
            flash("Usuário criado com sucesso!")

        flash('Nome de usuário digitado já existe!')
    
    return render_template('login_signup.html')




# Para existir uma outra função signup, deveria ter uma outra rota (@auth.route)
# def sign_up():
#     if request.method == "POST":
#         created_username = request.form['username']
#         created_password = request.form['password']

    





