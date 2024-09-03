from flask import Flask

app = Flask(__name__)

# Registrando as blueprints
from controller.auth import auth
app.register_blueprint(auth)

from controller.index import index
app.register_blueprint(index)

from controller.profile import profile
app.register_blueprint(profile)

if __name__ == "__main__":
    app.run(debug=True)