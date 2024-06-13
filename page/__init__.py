from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# Importar vistas y registrar Blueprints
from page.views.admin import admin
app.register_blueprint(admin)

from page.views.blog import blog
app.register_blueprint(blog)

from page.views.auth import auth
app.register_blueprint(auth)
