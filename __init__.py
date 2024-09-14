from flask import Flask
from datetime import timedelta

app = Flask(__name__)
# Definindo a chave secreta para cookies/sessões/formulários
app.config['SECRET_KEY'] = "secreto demais"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=15)

# Registrando as blueprints
from controller.auth import auth
app.register_blueprint(auth)

from controller.index import index
app.register_blueprint(index)

from controller.profile import profile
app.register_blueprint(profile)

from controller.logout import logout
app.register_blueprint(logout)

from controller.admin import admin
app.register_blueprint(admin)

from controller.recipe_page import recipe_page
app.register_blueprint(recipe_page)

if __name__ == "__main__":
    app.run(debug=True)