from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user
import os

app = Flask(__name__)

# Configure for flask forms
app.config['SECRET_KEY'] = 'mysecretkey'

########################## DATABASE SETUP ###########################################
# Configure for SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
# CALL the following commands on the terminal to initialize models and migrate them to the database:
# 1) export FLASK_APP=app.py
# 2) flask db init
# 3) flask db migrate -m "migration message"
# 4) flask db upgrade

#################### LOGIN CONFIGS #################################################
login_manager = LoginManager()
login_manager.init_app(app)

# login view of the flask-login-manager
login_manager.login_view = 'users.login'

################ BLUEPRINT VIEW REGISTRATION #######################################
from core.views import core
from users.views import users
from error_pages.handlers import error_pages
from blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)

