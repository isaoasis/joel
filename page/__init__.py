from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# Función para añadir encabezados de control de caché
@app.after_request
def add_header(response):
    # Deshabilitar el almacenamiento en caché
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# Importar vistas y registrar Blueprints
from page.views.admin import admin
app.register_blueprint(admin)

from page.views.blog import blog
app.register_blueprint(blog)

from page.views.auth import auth
app.register_blueprint(auth)
