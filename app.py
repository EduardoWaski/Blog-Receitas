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

from controller.recipe import recipe
app.register_blueprint(recipe)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)