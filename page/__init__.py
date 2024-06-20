import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://default:NjXqClpM73Kx@ep-curly-dawn-a4hwnczb-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)

import page.models

# Importar vistas y registrar Blueprints
from page.views.admin import admin
app.register_blueprint(admin)

from page.views.blog import blog
app.register_blueprint(blog)

from page.views.auth import auth
app.register_blueprint(auth)
